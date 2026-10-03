"""
Quay lai phien demo trong blog: Motion Studio -> xem truoc -> keo thanh thoi gian -> contact sheet
-> nhan xet critic -> render MP4 -> phat thanh pham.
Moi buoc chup 1 anh (images/step-XX-*.png), ca phien quay thanh 1 video
(video/scuti-ai-motion-graphics-video-demo.mp4). Render lai that video/scuti-ai-motion-graphics.mp4.

Chay:  python run_demo.py      (tu khoi dong studio/studio_server.py)
"""
import os, shutil, subprocess, sys, time, json, urllib.request
import imageio_ffmpeg
from playwright.sync_api import sync_playwright

ROOT = os.path.dirname(os.path.abspath(__file__))
IMG = os.path.join(ROOT, "images")
VID = os.path.join(ROOT, "video")
RAW = os.path.join(ROOT, "video_raw")
BASE = "http://localhost:8766"
W, H = 1440, 900

OVERLAY_JS = """
(() => { if (window.__ov) return; window.__ov = 1;
  const add = () => {
    const d = document.createElement('div'); d.id = '__cursor';
    d.style.cssText = 'position:fixed;z-index:2147483647;width:20px;height:20px;border-radius:50%;background:rgba(227,18,27,.55);' +
      'border:2px solid #fff;pointer-events:none;left:-40px;top:-40px;transform:translate(-50%,-50%);box-shadow:0 0 6px rgba(0,0,0,.5)';
    const c = document.createElement('div'); c.id = '__caption';
    c.style.cssText = 'position:fixed;z-index:2147483646;left:50%;bottom:70px;transform:translateX(-50%);background:rgba(20,8,10,.9);' +
      'color:#fff;font:600 18px Segoe UI,sans-serif;padding:9px 20px;border-radius:10px;pointer-events:none;display:none;max-width:80%;text-align:center';
    document.documentElement.append(d, c);
    addEventListener('mousemove', e => { d.style.left = e.clientX + 'px'; d.style.top = e.clientY + 'px'; }, true);
  };
  if (document.body) add(); else addEventListener('DOMContentLoaded', add);
})();
"""


def caption(pg, text):
    pg.evaluate("t => { const c = document.getElementById('__caption'); if (c) { c.textContent = t; c.style.display = t ? 'block' : 'none'; } }", text)


def shot(pg, name):
    pg.evaluate("() => ['__caption','__cursor'].forEach(id => { const e = document.getElementById(id); if (e) e.style.visibility = 'hidden'; })")
    pg.screenshot(path=os.path.join(IMG, name))
    pg.evaluate("() => ['__caption','__cursor'].forEach(id => { const e = document.getElementById(id); if (e) e.style.visibility = 'visible'; })")
    print("  chup", name, flush=True)


def click(pg, selector):
    loc = pg.locator(selector).first
    b = loc.bounding_box()
    pg.mouse.move(b["x"] + b["width"] / 2, b["y"] + b["height"] / 2, steps=18)
    pg.wait_for_timeout(350)
    loc.click()


def wait_server():
    for _ in range(50):
        try:
            urllib.request.urlopen(BASE + "/studio/", timeout=1); return
        except Exception:
            time.sleep(0.3)
    raise SystemExit("studio_server khong chay")


def main():
    for d in (IMG, VID, RAW):
        os.makedirs(d, exist_ok=True)
    server = subprocess.Popen([sys.executable, os.path.join(ROOT, "studio", "studio_server.py")],
                              stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    try:
        wait_server()
        with sync_playwright() as p:
            browser = p.chromium.launch(channel="chrome", headless=False, ignore_default_args=["--enable-automation"],
                                        args=["--mute-audio"])
            ctx = browser.new_context(viewport={"width": W, "height": H}, record_video_dir=RAW,
                                      record_video_size={"width": W, "height": H})
            ctx.add_init_script(OVERLAY_JS)
            pg = ctx.new_page()

            # 1. Mo Motion Studio
            pg.goto(BASE + "/studio/"); pg.wait_for_timeout(1500)
            caption(pg, "Bước 1 – Mở Motion Studio: storyboard 5 shot")
            pg.mouse.move(450, 300, steps=20); pg.wait_for_timeout(1200)
            pg.mouse.move(450, 520, steps=25); pg.wait_for_timeout(1200)
            shot(pg, "step-01-mo-studio.png")

            # 2. Xem truoc
            caption(pg, "Bước 2 – Mở bản xem trước: animation chạy ngay trong Chrome")
            click(pg, "#previewBtn")
            pg.wait_for_function("window.renderReady === true || document.querySelector('#ctrl')", timeout=30000)
            pg.evaluate("() => { window.seekTo(0); }")
            pg.wait_for_timeout(300)
            caption(pg, "Bước 2 – Mở bản xem trước: animation chạy ngay trong Chrome")
            pg.wait_for_timeout(2600)
            shot(pg, "step-02-xem-truoc.png")
            pg.wait_for_timeout(4000)

            # 3. Keo thanh thoi gian toi shot dich vu
            caption(pg, "Bước 3 – Kéo thanh thời gian để soi từng shot")
            sb = pg.locator("#scrub").bounding_box()
            y = sb["y"] + sb["height"] / 2
            pg.mouse.move(sb["x"] + 5, y, steps=15); pg.mouse.down()
            for frac in (0.2, 0.35, 0.47, 0.42):
                pg.mouse.move(sb["x"] + sb["width"] * frac, y, steps=25); pg.wait_for_timeout(500)
            pg.mouse.up(); pg.wait_for_timeout(1500)
            shot(pg, "step-03-keo-thanh-thoi-gian.png")

            # 4. Contact sheet
            caption(pg, "Bước 4 – Quay lại Studio, tạo contact sheet cho critic")
            click(pg, "#ctrl a")
            pg.wait_for_selector("#sheetBtn"); pg.wait_for_timeout(800)
            caption(pg, "Bước 4 – Bấm “Tạo contact sheet”")
            click(pg, "#sheetBtn")
            pg.wait_for_function("document.getElementById('sheetStatus').textContent.includes('✅')", timeout=120000)
            pg.wait_for_timeout(1500)
            shot(pg, "step-04-contact-sheet.png")

            # 5. Nhan xet critic
            caption(pg, "Bước 5 – Đọc nhận xét của critic độc lập")
            click(pg, "#notesBtn"); pg.wait_for_timeout(1500)
            pg.locator("#notes").scroll_into_view_if_needed(); pg.wait_for_timeout(1500)
            shot(pg, "step-05-nhan-xet-critic.png")
            pg.wait_for_timeout(1500)

            # 6. Render MP4
            caption(pg, "Bước 6 – Bấm “Render MP4”: tua và chụp từng frame 1920×1080")
            click(pg, "#notesBtn"); pg.wait_for_timeout(600)
            click(pg, "#renderBtn")
            pg.wait_for_function("(() => { const m = document.getElementById('renderStatus').textContent.match(/frame (\\d+)/); return m && +m[1] >= 240; })()",
                                 timeout=600000, polling=1000)
            shot(pg, "step-06-dang-render.png")

            # 7. Render xong
            pg.wait_for_function("window.RENDER_DONE", timeout=900000, polling=1000)
            res = pg.evaluate("window.RENDER_DONE")
            print("  render:", json.dumps(res, ensure_ascii=False), flush=True)
            caption(pg, "Bước 7 – Render xong: MP4 18 giây, 1920×1080, có nhạc nền")
            pg.wait_for_timeout(2000)
            shot(pg, "step-07-render-xong.png")
            pg.wait_for_timeout(1500)

            # 8. Phat thanh pham
            caption(pg, "")
            click(pg, "#openBtn")
            pg.wait_for_selector("video"); pg.wait_for_timeout(500)
            pg.evaluate("document.querySelector('video').play()")
            pg.wait_for_timeout(15500)
            shot(pg, "step-08-phat-video.png")
            pg.wait_for_timeout(3000)

            raw = pg.video.path()
            ctx.close(); browser.close()

        out = os.path.join(VID, "scuti-ai-motion-graphics-video-demo.mp4")
        subprocess.run([imageio_ffmpeg.get_ffmpeg_exe(), "-y", "-v", "error", "-i", raw, "-c:v", "libx264",
                        "-pix_fmt", "yuv420p", "-crf", "23", "-movflags", "+faststart", out], check=True)
        shutil.rmtree(RAW, ignore_errors=True)
        print("video qua trinh:", out)
    finally:
        server.terminate()


if __name__ == "__main__":
    main()
