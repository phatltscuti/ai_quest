"""
Quay demo THAT voi Google Pics + Gemini (NanoBanana) bang Playwright, 1 phien lien tuc.

Yeu cau: profile Chrome D:/chrome-profiles/ai-quest da dang nhap Google Workspace
(dang nhap tay 1 lan bang Chrome thuong, KHONG luu mat khau trong script).

Chay:  python record_pics_live.py
Ket qua:
  images/step-12..19-*.png        anh tung buoc
  images/pics-final-2k.jpg        anh 2K tai ve tu Pics
  images/gemini-nanobanana.png    anh Gemini tao (cung prompt)
  video/google-pics-live-session.mp4  video ca phien
  live_report.json                log thoi gian tung buoc
"""
import json, os, shutil, subprocess, time, glob
import imageio_ffmpeg
from playwright.sync_api import sync_playwright

HERE = os.path.dirname(os.path.abspath(__file__))
IMG = os.path.join(HERE, "images")
VID = os.path.join(HERE, "video")
RAW = os.path.join(HERE, "video_raw")
PROFILE = r"D:\chrome-profiles\ai-quest"
W, H = 1440, 900

PROMPT_MAIN = (
    'A 16:9 tech banner for "SCUTI AI - AI QUEST 2026". Bold headline "SCUTI AI", '
    'subtitle "Build. Learn. Ship with AI.". A cute red dragon mascot beside young Vietnamese '
    "engineers with laptops, glowing AI chat bubbles. Night city skyline, navy and red palette, "
    'flat vector style, footer "scuti.asia".'
)
PROMPT_ELEMENT = "Make the dragon wave its hand and wear a small orange scarf with the text AI"
PROMPT_TRANSLATE = (
    'Translate all text in this banner into Vietnamese. Keep "SCUTI AI" and "scuti.asia" '
    "unchanged. Keep the same fonts, colors and layout."
)

# Con tro chuot + caption chi de nguoi xem video de theo doi (an khi chup anh)
OVERLAY_JS = """
(() => {
  if (window.__ov) return; window.__ov = 1;
  const add = () => {
    const d = document.createElement('div'); d.id = '__cursor';
    d.style.cssText = 'position:fixed;z-index:2147483647;width:18px;height:18px;border-radius:50%;' +
      'background:rgba(229,57,53,.55);border:2px solid #fff;pointer-events:none;left:-40px;top:-40px;' +
      'transform:translate(-50%,-50%);box-shadow:0 0 6px rgba(0,0,0,.5)';
    const c = document.createElement('div'); c.id = '__caption';
    c.style.cssText = 'position:fixed;z-index:2147483646;left:50%;bottom:18px;transform:translateX(-50%);' +
      'background:rgba(10,20,50,.88);color:#fff;font:600 17px Segoe UI,sans-serif;padding:9px 18px;' +
      'border-radius:10px;pointer-events:none;display:none;max-width:80%;text-align:center';
    document.documentElement.append(d, c);
    addEventListener('mousemove', e => { d.style.left = e.clientX + 'px'; d.style.top = e.clientY + 'px'; }, true);
  };
  if (document.documentElement) add(); else addEventListener('DOMContentLoaded', add);
})();
"""

report = []


def log(step, **kw):
    kw.update(step=step, t=round(time.time() - T0, 1))
    report.append(kw)
    print(json.dumps(kw, ensure_ascii=False), flush=True)


def caption(pg, text):
    pg.evaluate("t => { const c = document.getElementById('__caption'); if (c) { c.textContent = t; c.style.display = t ? 'block' : 'none'; } }", text)


def shot(pg, name):
    pg.evaluate("() => { for (const id of ['__caption','__cursor']) { const e = document.getElementById(id); if (e) e.style.visibility = 'hidden'; } }")
    pg.screenshot(path=os.path.join(IMG, name))
    pg.evaluate("() => { for (const id of ['__caption','__cursor']) { const e = document.getElementById(id); if (e) e.style.visibility = 'visible'; } }")
    log(name)


def move_click(pg, loc):
    b = loc.bounding_box()
    pg.mouse.move(b["x"] + b["width"] / 2, b["y"] + b["height"] / 2, steps=15)
    pg.wait_for_timeout(400)
    loc.click()


def wait_generation(pg, timeout=300):
    """Pics hien nut 'Stop generating' khi dang tao anh; tao xong thi nut bien mat."""
    stop = pg.locator("[aria-label='Stop generating']").first
    t = time.time()
    try:
        stop.wait_for(state="visible", timeout=15000)
    except Exception:
        pass
    while time.time() - t < timeout:
        if not stop.is_visible():
            break
        pg.wait_for_timeout(1000)
    pg.wait_for_timeout(2500)
    return round(time.time() - t, 1)


def dismiss_got_it(pg):
    g = pg.get_by_role("button", name="Got it")
    if g.count() and g.first.is_visible():
        g.first.click()
        pg.wait_for_timeout(500)


def red_candidates(pg, box=(150, 80, 1290, 715), cell=40, top=14):
    """Tim cac o co nhieu pixel do (rong do) tren anh dang hien thi, sap xep giam dan."""
    from PIL import Image
    import io
    im = Image.open(io.BytesIO(pg.screenshot())).convert("RGB")
    sx = im.width / W
    px = im.load()
    cells = []
    for y in range(box[1], box[3] - cell, cell // 2):
        for x in range(box[0], box[2] - cell, cell // 2):
            n = red = 0
            for yy in range(y, y + cell, 4):
                for xx in range(x, x + cell, 4):
                    r, g, b = px[int(xx * sx), int(yy * sx)]
                    n += 1
                    red += (r > 170 and g < 90 and b < 100)
            fr = red / n
            # bo cac mang do dong mau (banner/khoi chu): nhan vat co vien + chi tiet
            if 0.3 < fr < 0.85:
                cells.append((fr, x + cell // 2, y + cell // 2))
    cells.sort(reverse=True)
    picked = []
    for sc, x, y in cells:
        if all(abs(x - a) + abs(y - b) > 90 for a, b in picked):
            picked.append((x, y))
        if len(picked) >= top:
            break
    return picked


def select_dragon(pg):
    """Click vao cac vung mau do, chon phan tu ma Pics nhan dien la 'dragon'."""
    for x, y in red_candidates(pg):
        pg.mouse.move(x, y, steps=12)
        pg.wait_for_timeout(500)
        pg.mouse.click(x, y)
        pg.wait_for_timeout(1500)
        tb = pg.locator("[role=textbox][aria-label^='Describe changes for']")
        if tb.count():
            label = tb.first.get_attribute("aria-label")
            log("try-element", x=x, y=y, label=label)
            if "dragon" in label.lower():
                return tb.first, label
            pg.keyboard.press("Escape")
            pg.wait_for_timeout(700)
    return None, None


def main():
    global T0
    os.makedirs(RAW, exist_ok=True)
    os.makedirs(VID, exist_ok=True)
    with sync_playwright() as p:
        ctx = p.chromium.launch_persistent_context(
            PROFILE, channel="chrome", headless=False, viewport={"width": W, "height": H},
            record_video_dir=RAW, record_video_size={"width": W, "height": H},
            ignore_default_args=["--enable-automation"],
            args=["--disable-blink-features=AutomationControlled"], accept_downloads=True)
        ctx.add_init_script(OVERLAY_JS)
        pg = ctx.pages[0] if ctx.pages else ctx.new_page()
        T0 = time.time()

        # 0. Nguon chinh thuc (ngan gon) truoc khi vao Pics
        pg.goto("https://workspace.google.com/products/pics/", wait_until="domcontentloaded")
        pg.wait_for_timeout(2500)
        caption(pg, "Google Pics – trang sản phẩm chính thức (workspace.google.com/products/pics)")
        for _ in range(4):
            pg.mouse.wheel(0, 450); pg.wait_for_timeout(1200)
        log("intro-product-page")

        # 12. Mo pics.new -> canvas trong
        pg.goto("https://pics.new/", wait_until="domcontentloaded")
        box = pg.get_by_role("textbox", name="Bring your ideas to life with Gemini")
        box.wait_for(timeout=60000)
        pg.wait_for_timeout(3000)
        caption(pg, "Bước 12 – Mở pics.new: canvas trống + thanh prompt Gemini")
        pg.wait_for_timeout(2000)
        log("doc-url", url=pg.url)
        shot(pg, "step-12-pics-home.png")

        # 13. Go prompt
        caption(pg, "Bước 13 – Gõ prompt tạo banner Scuti AI (có rồng đỏ)")
        move_click(pg, box)
        box.type(PROMPT_MAIN, delay=18)
        pg.wait_for_timeout(1200)
        shot(pg, "step-13-prompt-entered.png")

        # 14. Tao anh -> 4 phien ban
        caption(pg, "Bước 14 – Submit: Pics tạo 4 phiên bản để chọn")
        move_click(pg, pg.get_by_role("button", name="Submit"))
        secs = wait_generation(pg)
        log("generate-done", seconds=secs)
        for i in (2, 3, 1):
            pv = pg.locator(f"[aria-label='Preview image {i}']")
            bb = pv.first.bounding_box() if pv.count() else None
            if bb and bb["x"] > 0:
                cx, cy = bb["x"] + bb["width"] / 2, bb["y"] + bb["height"] / 2
                pg.mouse.move(cx, cy, steps=15); pg.wait_for_timeout(300)
                pg.mouse.click(cx, cy); pg.wait_for_timeout(1500)
        shot(pg, "step-14-generated-variations.png")
        dismiss_got_it(pg)
        move_click(pg, pg.get_by_role("button", name="Confirm"))
        pg.wait_for_timeout(2500)

        # 15. Chon phan tu con rong -> sua rieng
        caption(pg, "Bước 15 – Click vào con rồng: Pics tự nhận diện đối tượng để sửa riêng")
        tb, label = select_dragon(pg)
        log("select-element", label=label)
        if tb is not None:
            tb.type(PROMPT_ELEMENT, delay=18)
            pg.wait_for_timeout(1000)
            shot(pg, "step-15-select-element-edit.png")
            move_click(pg, pg.get_by_role("button", name="Add", exact=True))
            pg.wait_for_timeout(1500)
            caption(pg, "Bước 15 – Apply 1 edit: chỉ con rồng thay đổi, phần còn lại giữ nguyên")
            move_click(pg, pg.get_by_role("button", name="Apply 1 edit"))
        else:  # du phong: sua bang prompt neu khong chon duoc phan tu
            pg.keyboard.press("Escape")
            ebox = pg.get_by_role("textbox", name="Edit image with Gemini or press ↑ to use past prompts")
            move_click(pg, ebox)
            ebox.type("Only change the red dragon: " + PROMPT_ELEMENT, delay=18)
            shot(pg, "step-15-select-element-edit.png")
            move_click(pg, pg.get_by_role("button", name="Submit"))
        secs = wait_generation(pg)
        log("element-edit-done", seconds=secs)
        pg.wait_for_timeout(1500)
        shot(pg, "step-15b-element-edit-result.png")

        # 16. Dich chu sang tieng Viet
        caption(pg, "Bước 16 – Dịch toàn bộ chữ trong ảnh sang tiếng Việt bằng 1 prompt")
        ebox = pg.get_by_role("textbox", name="Edit image with Gemini or press ↑ to use past prompts")
        move_click(pg, ebox)
        ebox.type(PROMPT_TRANSLATE, delay=18)
        pg.wait_for_timeout(800)
        move_click(pg, pg.get_by_role("button", name="Submit"))
        secs = wait_generation(pg)
        log("translate-done", seconds=secs)
        shot(pg, "step-16-translate-text.png")
        move_click(pg, pg.get_by_role("button", name="Confirm"))
        pg.wait_for_timeout(2500)

        # 17. Transform / ty le khung hinh
        caption(pg, "Bước 17 – Transform: đổi tỉ lệ khung (16:9 → 1:1) và xoay/crop")
        move_click(pg, pg.get_by_role("button", name="Aspect ratio"))
        pg.wait_for_timeout(2000)
        one = pg.get_by_role("button", name="1:1", exact=True)
        if one.count():
            move_click(pg, one.first); pg.wait_for_timeout(2000)
        shot(pg, "step-17-crop-aspect-ratio.png")
        back = pg.get_by_role("button", name="16:9", exact=True)
        if back.count():
            move_click(pg, back.first); pg.wait_for_timeout(1500)
        ex = pg.get_by_role("button", name="Exit")
        if ex.count():
            move_click(pg, ex.first)
        pg.wait_for_timeout(2000)

        # 18. Export -> 2K
        caption(pg, "Bước 18 – Export: Original / 2K / 4K (upscale bằng Gemini)")
        move_click(pg, pg.get_by_role("button", name="Export"))
        pg.wait_for_timeout(2000)
        shot(pg, "step-18-download-menu.png")
        try:
            with pg.expect_download(timeout=240000) as dl:
                move_click(pg, pg.get_by_role("menuitem", name="2K JPEG - Upscale with Gemini"))
            dl.value.save_as(os.path.join(IMG, "pics-final-2k.jpg"))
            log("download-2k", ok=True)
        except Exception as e:
            log("download-2k", ok=False, err=str(e)[:200])
        pg.wait_for_timeout(2000)

        # 19. Cung prompt trong Gemini app (NanoBanana)
        caption(pg, "Bước 19 – So sánh: cùng prompt trong Gemini app (NanoBanana)")
        pg.wait_for_timeout(1500)
        pg.goto("https://gemini.google.com/app", wait_until="domcontentloaded")
        gbox = pg.get_by_role("textbox", name="Enter a prompt for Gemini")
        gbox.wait_for(timeout=60000)
        pg.wait_for_timeout(2500)
        caption(pg, "Bước 19 – Gemini app: gõ cùng prompt, NanoBanana tạo 1 ảnh trong khung chat")
        move_click(pg, gbox)
        gbox.type("Create an image: " + PROMPT_MAIN, delay=12)
        pg.keyboard.press("Enter")
        t = time.time()
        gen_img = None
        while time.time() - t < 240:
            pg.wait_for_timeout(2000)
            imgs = pg.locator("main img")
            for i in range(imgs.count()):
                im = imgs.nth(i)
                try:
                    bb = im.bounding_box()
                    if bb and bb["width"] > 300 and im.evaluate("e => e.complete && e.naturalWidth > 300"):
                        gen_img = im
                        break
                except Exception:
                    pass
            if gen_img:
                break
        log("gemini-done", seconds=round(time.time() - t, 1), found=bool(gen_img))
        pg.wait_for_timeout(3000)
        if gen_img:
            gen_img.scroll_into_view_if_needed(); pg.wait_for_timeout(1500)
            gen_img.screenshot(path=os.path.join(IMG, "gemini-nanobanana.png"))
        shot(pg, "step-19-nanobanana-gemini.png")
        caption(pg, "")
        pg.wait_for_timeout(2000)

        video_path = pg.video.path()
        ctx.close()

    out = os.path.join(VID, "google-pics-live-session.mp4")
    ff = imageio_ffmpeg.get_ffmpeg_exe()
    subprocess.run([ff, "-y", "-i", video_path, "-c:v", "libx264", "-pix_fmt", "yuv420p",
                    "-crf", "23", "-preset", "medium", "-movflags", "+faststart", out], check=True,
                   capture_output=True)
    shutil.rmtree(RAW, ignore_errors=True)
    log("video", path=out)
    with open(os.path.join(HERE, "live_report.json"), "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    main()
