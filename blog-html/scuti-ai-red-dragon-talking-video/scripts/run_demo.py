"""
Quay lai toan bo phien demo trong blog: mo Rong Do Studio -> go kich ban -> tao giong
-> nghe thu -> xem truoc rong -> ghi video -> mo MP4.
Moi buoc chup 1 anh (images/step-XX-*.png), ca phien quay thanh 1 video
(video/scuti-ai-red-dragon-talking-video-demo.mp4). San pham cuoi: video/scuti-ai-red-dragon.mp4.

Chay:  python scripts/run_demo.py
(tu khoi dong studio/studio_server.py; trinh duyet duoc tat tieng loa nhung video xuat ra van co tieng)
"""
import os, shutil, subprocess, sys, time, json, urllib.request
import imageio_ffmpeg
from playwright.sync_api import sync_playwright

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMG = os.path.join(ROOT, "images")
VID = os.path.join(ROOT, "video")
RAW = os.path.join(ROOT, "video_raw")
BASE = "http://localhost:8765"
W, H = 1440, 900
NARRATION = open(os.path.join(ROOT, "scripts", "narration-vi.txt"), encoding="utf-8").read().strip()

# con tro chuot + chu thich cho nguoi xem video (an khi chup anh)
OVERLAY_JS = """
(() => { if (window.__ov) return; window.__ov = 1;
  const add = () => {
    const d = document.createElement('div'); d.id = '__cursor';
    d.style.cssText = 'position:fixed;z-index:2147483647;width:20px;height:20px;border-radius:50%;background:rgba(229,57,53,.55);' +
      'border:2px solid #fff;pointer-events:none;left:-40px;top:-40px;transform:translate(-50%,-50%);box-shadow:0 0 6px rgba(0,0,0,.5)';
    const c = document.createElement('div'); c.id = '__caption';
    c.style.cssText = 'position:fixed;z-index:2147483646;left:50%;bottom:76px;transform:translateX(-50%);background:rgba(10,20,50,.9);' +
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
            urllib.request.urlopen(BASE + "/studio/", timeout=1)
            return
        except Exception:
            time.sleep(0.3)
    raise SystemExit("studio_server khong chay")


def main():
    os.makedirs(IMG, exist_ok=True); os.makedirs(VID, exist_ok=True); os.makedirs(RAW, exist_ok=True)
    server = subprocess.Popen([sys.executable, os.path.join(ROOT, "studio", "studio_server.py")],
                              stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    try:
        wait_server()
        with sync_playwright() as p:
            browser = p.chromium.launch(channel="chrome", headless=False,
                                        ignore_default_args=["--enable-automation"],
                                        args=["--auto-accept-this-tab-capture", "--mute-audio", "--window-size=1456,1050"])
            ctx = browser.new_context(viewport={"width": W, "height": H}, record_video_dir=RAW,
                                      record_video_size={"width": W, "height": H})
            ctx.add_init_script(OVERLAY_JS)
            pg = ctx.new_page()

            # 1. Mo Studio
            pg.goto(BASE + "/studio/"); pg.wait_for_timeout(1500)
            caption(pg, "Bước 1 – Mở Rồng Đỏ Studio (localhost:8765/studio)")
            pg.mouse.move(700, 300, steps=20); pg.wait_for_timeout(1500)
            shot(pg, "step-01-mo-studio.png")

            # 2. Go kich ban + chon giong
            caption(pg, "Bước 2 – Gõ kịch bản 5 câu và chọn giọng Nam Minh")
            click(pg, "#script")
            pg.keyboard.type(NARRATION, delay=22)
            pg.wait_for_timeout(600)
            click(pg, "#voice")
            pg.select_option("#voice", "vi-VN-NamMinhNeural")
            pg.wait_for_timeout(800)
            shot(pg, "step-02-go-kich-ban.png")

            # 3. Tao giong doc
            caption(pg, "Bước 3 – Bấm “Tạo giọng đọc”")
            click(pg, "#ttsBtn")
            pg.wait_for_function("document.getElementById('ttsStatus').textContent.includes('✅')", timeout=120000)
            pg.wait_for_timeout(1500)
            shot(pg, "step-03-tao-giong-doc.png")

            # 4. Nghe thu
            caption(pg, "Bước 4 – Nghe thử giọng đọc")
            b = pg.locator("#aud").bounding_box()
            pg.mouse.move(b["x"] + 22, b["y"] + b["height"] / 2, steps=15); pg.wait_for_timeout(300)
            pg.evaluate("document.getElementById('aud').play()")
            pg.wait_for_timeout(5000)
            shot(pg, "step-04-nghe-thu.png")
            pg.evaluate("document.getElementById('aud').pause()")
            pg.wait_for_timeout(800)

            # 5. Mo trang hoat hinh + xem truoc
            caption(pg, "Bước 5 – Mở trang hoạt hình, bấm “▶ Xem trước”")
            click(pg, "#openBtn")
            pg.wait_for_selector("#playBtn"); pg.wait_for_timeout(1500)
            caption(pg, "Bước 5 – Mở trang hoạt hình, bấm “▶ Xem trước”")
            click(pg, "#playBtn")
            pg.wait_for_timeout(6500)
            shot(pg, "step-05-xem-truoc-rong.png")
            pg.wait_for_timeout(3000)

            # 6. Ghi video (tai lai trang de bat dau tu dau)
            pg.reload(); pg.wait_for_selector("#recBtn"); pg.wait_for_timeout(1200)
            caption(pg, "Bước 6 – Bấm “⏺ Ghi video”: Chrome ghi lại tab kèm âm thanh")
            click(pg, "#recBtn")
            pg.wait_for_timeout(17500)
            shot(pg, "step-06-dang-ghi-video.png")
            pg.wait_for_function("window.EXPORT_RESULT", timeout=180000, polling=500)
            res = pg.evaluate("window.EXPORT_RESULT")
            print("  export:", json.dumps(res, ensure_ascii=False), flush=True)

            # 7. Xuat xong
            caption(pg, "Bước 7 – Video MP4 đã được lưu")
            pg.wait_for_timeout(1500)
            shot(pg, "step-07-xuat-video-xong.png")
            pg.wait_for_timeout(1500)

            # 8. Mo video MP4
            caption(pg, "")
            click(pg, "#resBox a")
            pg.wait_for_selector("video"); pg.wait_for_timeout(500)
            caption(pg, "Bước 8 – Mở video thành phẩm và kiểm tra")
            pg.evaluate("document.querySelector('video').play()")
            pg.wait_for_timeout(13500)
            shot(pg, "step-08-phat-video-mp4.png")
            pg.wait_for_timeout(4000)

            raw = pg.video.path()
            ctx.close(); browser.close()

        out = os.path.join(VID, "scuti-ai-red-dragon-talking-video-demo.mp4")
        subprocess.run([imageio_ffmpeg.get_ffmpeg_exe(), "-y", "-v", "error", "-i", raw, "-c:v", "libx264",
                        "-pix_fmt", "yuv420p", "-crf", "23", "-movflags", "+faststart", out], check=True)
        shutil.rmtree(RAW, ignore_errors=True)
        print("video qua trinh:", out)
    finally:
        server.terminate()


if __name__ == "__main__":
    main()
