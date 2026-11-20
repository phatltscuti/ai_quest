"""Quay nội dung 1 tab Chrome qua CDP screencast (không bị cửa sổ khác đè lên).

Dùng trong code:
    from cdp_rec import open_window, Recorder, show_click
    page = open_window(browser, url)          # mở cửa sổ Chrome riêng 1920x1080
    rec = Recorder(page); rec.start()
    ... thao tác (show_click(page, locator) để hiện con trỏ + hiệu ứng click) ...
    rec.stop("out.mp4", caption="https://...")   # ghép frame theo timestamp thật -> mp4
"""
import base64, os, shutil, subprocess, tempfile, time
from pathlib import Path

FF = Path(os.environ["LOCALAPPDATA"]) / "Microsoft/WinGet/Packages/Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe/ffmpeg-9.1-full_build/bin/ffmpeg.exe"
W, H = 1920, 1080

def open_window(browser, url="about:blank"):
    """Tạo cửa sổ Chrome mới (không đụng tab của người dùng) và trả về Page."""
    ctx = browser.contexts[0]
    s = browser.new_browser_cdp_session()
    with ctx.expect_page() as pi:
        s.send("Target.createTarget", {"url": "about:blank", "newWindow": True, "width": W, "height": H + 140})
    page = pi.value
    page.set_viewport_size({"width": W, "height": H})
    if url != "about:blank": page.goto(url)
    return page

CURSOR_JS = """
(() => { if (window.__cur) return;
  const c = document.createElement('div'); window.__cur = c;
  c.style.cssText = 'position:fixed;z-index:2147483647;width:22px;height:22px;left:-50px;top:-50px;pointer-events:none;transition:left .45s ease,top .45s ease';
  const NS = 'http://www.w3.org/2000/svg', svg = document.createElementNS(NS, 'svg'), path = document.createElementNS(NS, 'path');
  svg.setAttribute('width', '22'); svg.setAttribute('height', '22'); svg.setAttribute('viewBox', '0 0 22 22');
  path.setAttribute('d', 'M2 2 L2 18 L7 13 L11 21 L14 20 L10 12 L17 12 Z'); path.setAttribute('fill', '#111');
  path.setAttribute('stroke', '#fff'); path.setAttribute('stroke-width', '1.5'); svg.appendChild(path); c.appendChild(svg);
  document.documentElement.appendChild(c);
  window.__ripple = (x, y) => { const r = document.createElement('div');
    r.style.cssText = `position:fixed;z-index:2147483646;left:${x-18}px;top:${y-18}px;width:36px;height:36px;border-radius:50%;background:rgba(255,109,0,.45);pointer-events:none;transition:transform .5s,opacity .5s`;
    document.documentElement.appendChild(r); requestAnimationFrame(() => { r.style.transform = 'scale(2.2)'; r.style.opacity = '0'; });
    setTimeout(() => r.remove(), 600); };
})()"""

def show_click(page, locator, click=True, pause=0.6):
    """Di chuyển con trỏ giả tới phần tử, hiện hiệu ứng click, rồi click thật."""
    locator.scroll_into_view_if_needed()
    b = locator.bounding_box()
    x, y = b["x"] + b["width"] / 2, b["y"] + b["height"] / 2
    page.evaluate(CURSOR_JS)
    page.evaluate(f"window.__cur.style.left='{x}px';window.__cur.style.top='{y}px'")
    time.sleep(pause)
    if click:
        page.evaluate(f"window.__ripple({x},{y})")
        page.mouse.click(x, y)
        time.sleep(0.3)

MASK_JS = r"""
(() => { if (window.__masked) return; window.__masked = true;
  const re = /[\w.+-]+@[\w-]+(\.[\w-]+)+|AIza[\w-]{20,}|AQ\.[\w.-]{20,}/g;
  const fix = root => { const w = document.createTreeWalker(root, NodeFilter.SHOW_TEXT); let n;
    while ((n = w.nextNode())) if (re.test(n.nodeValue)) { re.lastIndex = 0; n.nodeValue = n.nodeValue.replace(re, '••••••••'); } re.lastIndex = 0; };
  fix(document.body);
  new MutationObserver(ms => ms.forEach(m => m.addedNodes.forEach(x => x.nodeType === 3 ? fix(x.parentNode || document.body) : x.nodeType === 1 && fix(x)))
  ).observe(document.body, {childList: true, subtree: true, characterData: true});
  document.querySelectorAll('img[src*="googleusercontent"]').forEach(i => i.style.filter = 'blur(6px)');
})()"""

def mask_pii(page):
    """Che email / API key / avatar trong trang trước khi quay."""
    try: page.evaluate(MASK_JS)
    except Exception: pass

class Recorder:
    def __init__(self, page, fps=30, quality=82):
        self.page, self.fps, self.q = page, fps, quality
        self.dir = Path(tempfile.mkdtemp(prefix="cdprec_"))
        self.frames = []
        self.speeds = [(0, 1.0)]  # (thời điểm, hệ số tua) - dùng fast()/normal()

    def fast(self, factor=10.0): self.speeds.append((time.time(), factor))
    def normal(self): self.speeds.append((time.time(), 1.0))
    def _factor(self, t): return [f for ts, f in self.speeds if ts <= t][-1]

    def _on_frame(self, ev):
        t = time.time()
        f = self.dir / f"{len(self.frames):06d}.jpg"
        f.write_bytes(base64.b64decode(ev["data"]))
        self.frames.append((t, f))
        try: self.cdp.send("Page.screencastFrameAck", {"sessionId": ev["sessionId"]})
        except Exception: pass

    def start(self):
        mask_pii(self.page)
        self.cdp = self.page.context.new_cdp_session(self.page)
        self.cdp.on("Page.screencastFrame", self._on_frame)
        self.cdp.send("Page.startScreencast", {"format": "jpeg", "quality": self.q, "maxWidth": W, "maxHeight": H, "everyNthFrame": 1})
        self.t0 = time.time()

    def pump(self, seconds):
        """Chờ nhưng vẫn nhận frame (Playwright sync cần event loop chạy)."""
        self.page.wait_for_timeout(int(seconds * 1000))

    def stop(self, out, caption=None, tail=1.0):
        self.page.wait_for_timeout(300)
        self.cdp.send("Page.stopScreencast")
        t_end = time.time()
        out = Path(out); out.parent.mkdir(parents=True, exist_ok=True)
        lst = self.dir / "list.txt"
        with open(lst, "w") as fh:
            for i, (t, f) in enumerate(self.frames):
                nxt = self.frames[i + 1][0] if i + 1 < len(self.frames) else t_end + tail
                fh.write(f"file '{f.as_posix()}'\nduration {max((nxt - t) / self._factor(t), 1 / self.fps):.4f}\n")
            fh.write(f"file '{self.frames[-1][1].as_posix()}'\n")
        vf = f"scale={W}:{H}:force_original_aspect_ratio=decrease,pad={W}:{H}:(ow-iw)/2:(oh-ih)/2:white"
        if caption:  # thanh địa chỉ giả phía trên để người xem biết đang ở trang nào
            cap = caption.replace(":", r"\:").replace("'", "")
            vf = (f"scale={W}:{H - 44},pad={W}:{H}:0:44:0xdee1e6,"
                  f"drawbox=x=12:y=7:w={W - 24}:h=30:color=white:t=fill,"
                  f"drawtext=fontfile='C\\:/Windows/Fonts/segoeui.ttf':text='{cap}':x=28:y=12:fontsize=18:fontcolor=0x202124")
        subprocess.run([str(FF), "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", str(lst), "-vf", vf,
                        "-r", str(self.fps), "-c:v", "libx264", "-crf", "21", "-pix_fmt", "yuv420p", "-movflags", "+faststart", str(out)], check=True)
        shutil.rmtree(self.dir, ignore_errors=True)
        print(f"saved {out} ({len(self.frames)} frames, {t_end - self.t0:.0f}s)")
        return out
