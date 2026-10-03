"""
trial_playwright.py - Google Pics vs NanoBanana (AI Quest Type 2)

Phien thu nghiem tu dong bang Playwright + Chrome that (channel="chrome"):
  1. Mo video YouTube chinh thuc "Say hello to Google Pics" -> chup trang + cac khung hinh tinh nang
  2. Mo bai Workspace Updates (GA 01/09/2026)          -> chup
  3. Mo trang san pham workspace.google.com/products/pics -> chup
  4. Mo Help Center "Get started with Google Pics"     -> chup
  5. Mo pics.new                                        -> neu bi chan dang nhap: chup man hinh sign-in va DUNG
     (KHONG BAO GIO go email / mat khau)
  6. Mo blog da viet (file://) va cuon tu tren xuong duoi (de ket thuc video)

Toan bo phien duoc ghi video (record_video_dir) -> sau do convert webm -> mp4 (libx264, yuv420p).

Chay:
    python trial_playwright.py                      # profile tam trong thu muc .trial-profile
    python trial_playwright.py --profile D:/tmp/p   # chi dinh profile rieng
    python trial_playwright.py --no-video           # chi chup anh
"""
import argparse
import json
import os
import shutil
import subprocess
import sys
import time

from playwright.sync_api import sync_playwright

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMG_DIR = os.path.join(BASE_DIR, "images")
VIDEO_DIR = os.path.join(BASE_DIR, "video")
RAW_VIDEO_DIR = os.path.join(VIDEO_DIR, "raw")
REPORT_PATH = os.path.join(BASE_DIR, "trial_report.json")
SLUG = "google-pics-vs-nanobanana"
BLOG_PATH = os.path.join(BASE_DIR, f"{SLUG}-blog.html")

YOUTUBE_URL = "https://www.youtube.com/watch?v=S18L1NFTda8&hl=en"
BLOG_POST_URL = ("https://workspaceupdates.googleblog.com/2026/09/"
                 "google-pics-brings-pro-level-ai-image-creation-and-editing-to-Google-Workspace.html")
PRODUCT_URL = "https://workspace.google.com/intl/en/products/pics/"
HELP_URL = "https://support.google.com/docs/answer/17170048?hl=en"
PICS_URL = "https://pics.new"

# Khung hinh trong video YouTube (giay) -> ten file anh
VIDEO_FRAMES = [
    (18, "step-02-yt-generate-variations.png"),
    (34, "step-03-yt-add-element.png"),
    (39, "step-04-yt-edit-text.png"),
    (50, "step-05-yt-translate-result.png"),
    (60, "step-06-yt-edit-in-slides.png"),
]

steps = []


def now_ms():
    return int(time.time() * 1000)


def record(step_id, started, action, ok, details=""):
    steps.append({"id": step_id, "started_ms": started, "ended_ms": now_ms(),
                  "action": action, "ok": ok, "details": details})
    print(f"[{'OK' if ok else 'FAIL'}] {step_id}: {action} {details}")


def pause(page, ms):
    page.wait_for_timeout(ms)


def human_scroll(page, total_px, step_px=120, delay_ms=60):
    """Cuon muot nhu nguoi that."""
    done = 0
    while done < total_px:
        page.mouse.wheel(0, step_px)
        done += step_px
        page.wait_for_timeout(delay_ms)


def scroll_to_bottom(page, step_px=110, delay_ms=55, max_ms=90000):
    start = time.time()
    while True:
        at_bottom = page.evaluate(
            "() => (window.innerHeight + window.scrollY) >= document.body.scrollHeight - 4")
        if at_bottom or (time.time() - start) * 1000 > max_ms:
            break
        page.mouse.wheel(0, step_px)
        page.wait_for_timeout(delay_ms)


def move_mouse_around(page, points, delay=350):
    for (x, y) in points:
        page.mouse.move(x, y, steps=18)
        page.wait_for_timeout(delay)


def shot(page, name, full_page=False):
    path = os.path.join(IMG_DIR, name)
    page.screenshot(path=path, full_page=full_page)
    return name


def dismiss_banners(page):
    for label in ["Accept all", "I agree", "Reject all", "No thanks", "Got it", "OK"]:
        try:
            btn = page.get_by_role("button", name=label)
            if btn.count() > 0 and btn.first.is_visible():
                btn.first.click(timeout=1500)
                page.wait_for_timeout(600)
                return
        except Exception:
            pass


def step_youtube(page):
    s = now_ms()
    try:
        page.goto(YOUTUBE_URL, wait_until="domcontentloaded")
        pause(page, 7000)
        dismiss_banners(page)
        # Bo qua quang cao neu co
        for _ in range(6):
            skip = page.locator(".ytp-skip-ad-button, .ytp-ad-skip-button-modern")
            if skip.count() > 0 and skip.first.is_visible():
                skip.first.click()
                pause(page, 1500)
                break
            if page.locator(".ad-showing").count() == 0:
                break
            pause(page, 2500)
        # Mo rong mo ta video
        try:
            page.click("#description-inline-expander #expand", timeout=4000)
        except Exception:
            pass
        pause(page, 4000)  # de video chay tu nhien vai giay
        shot(page, "step-01-youtube-video.png")
        info = page.evaluate("""() => {
            const v = document.querySelector('video');
            return {title: document.querySelector('h1.ytd-watch-metadata')?.innerText,
                    channel: document.querySelector('#owner #channel-name')?.innerText,
                    duration_s: v ? v.duration : null};
        }""")
        record("s1_youtube", s, "Open official YouTube video", True, json.dumps(info, ensure_ascii=False))
    except Exception as e:
        record("s1_youtube", s, "Open official YouTube video", False, str(e))
        return

    # Chup khung hinh tinh nang: tua toi tung moc, cho buffer, chup player
    page.evaluate("() => window.scrollTo({top: 0, behavior: 'smooth'})")
    for sec, name in VIDEO_FRAMES:
        s = now_ms()
        try:
            page.evaluate(f"""() => {{ const v = document.querySelector('video');
                v.currentTime = {sec - 2}; v.play(); }}""")
            pause(page, 2600)  # xem 2 giay nhu nguoi that
            page.evaluate("() => document.querySelector('video').pause()")
            # cho frame on dinh (readyState >= 2)
            for _ in range(20):
                if page.evaluate("() => document.querySelector('video').readyState") >= 2:
                    break
                pause(page, 400)
            pause(page, 900)
            page.mouse.move(1270, 700)  # an thanh dieu khien
            pause(page, 2600)
            page.locator("#movie_player").screenshot(path=os.path.join(IMG_DIR, name))
            record(f"s1_frame_{sec}", s, f"Video frame at {sec}s", True, name)
        except Exception as e:
            record(f"s1_frame_{sec}", s, f"Video frame at {sec}s", False, str(e))


def step_page(page, step_id, url, name, scroll_px=0, label=""):
    s = now_ms()
    try:
        page.goto(url, wait_until="domcontentloaded")
        pause(page, 5000)
        dismiss_banners(page)
        move_mouse_around(page, [(300, 250), (640, 380), (900, 300)])
        if scroll_px:
            human_scroll(page, scroll_px)
            pause(page, 1500)
        shot(page, name)
        record(step_id, s, label or f"Open {url}", True, f"{name} | final url={page.url}")
        return True
    except Exception as e:
        record(step_id, s, label or f"Open {url}", False, str(e))
        return False


def step_product_page(page):
    step_page(page, "s3_product", PRODUCT_URL, "step-08-product-page-hero.png", 0,
              "Open product page (hero)")
    # cuon xem cac muc tinh nang
    s = now_ms()
    try:
        human_scroll(page, 1500)
        pause(page, 2000)
        shot(page, "step-09-product-page-features.png")
        human_scroll(page, 1800)
        pause(page, 1500)
        record("s3_product_features", s, "Scroll product page features", True)
    except Exception as e:
        record("s3_product_features", s, "Scroll product page features", False, str(e))


def step_pics_signin(page):
    s = now_ms()
    try:
        page.goto(PICS_URL, wait_until="domcontentloaded")
        pause(page, 7000)
        url = page.url
        needs_login = "accounts.google.com" in url or page.locator("input[type=email]").count() > 0
        shot(page, "step-11-pics-signin-wall.png")
        record("s5_pics", s, "Open pics.new", True,
               f"final url={url} | sign-in required={needs_login} -> STOP (khong nhap thong tin dang nhap)")
        pause(page, 2500)
    except Exception as e:
        record("s5_pics", s, "Open pics.new", False, str(e))


def step_blog(page):
    s = now_ms()
    if not os.path.exists(BLOG_PATH):
        record("s6_blog", s, "Open finished blog", False, "blog chua ton tai - bo qua")
        return
    try:
        page.goto("file:///" + BLOG_PATH.replace("\\", "/"), wait_until="load")
        pause(page, 3500)
        # tam dung video nhung trong blog (neu co) de khong tu phat
        scroll_to_bottom(page, step_px=70, delay_ms=120, max_ms=150000)
        pause(page, 3000)
        page.evaluate("() => window.scrollTo({top: 0, behavior: 'smooth'})")
        pause(page, 2500)
        record("s6_blog", s, "Scroll finished blog top -> bottom", True)
    except Exception as e:
        record("s6_blog", s, "Scroll finished blog", False, str(e))


def convert_video(webm_path, mp4_path):
    import imageio_ffmpeg
    ffmpeg = imageio_ffmpeg.get_ffmpeg_exe()
    cmd = [ffmpeg, "-y", "-i", webm_path, "-c:v", "libx264", "-pix_fmt", "yuv420p",
           "-preset", "medium", "-crf", "23", "-movflags", "+faststart", "-an", mp4_path]
    subprocess.run(cmd, check=True, capture_output=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--profile", default=os.path.join(BASE_DIR, ".trial-profile"),
                    help="Thu muc profile Chrome rieng (KHONG dung profile chinh)")
    ap.add_argument("--no-video", action="store_true")
    ap.add_argument("--skip-frames", action="store_true")
    args = ap.parse_args()

    os.makedirs(IMG_DIR, exist_ok=True)
    os.makedirs(RAW_VIDEO_DIR, exist_ok=True)

    with sync_playwright() as p:
        kwargs = dict(user_data_dir=args.profile, channel="chrome", headless=False,
                      viewport={"width": 1280, "height": 720}, locale="en-US",
                      args=["--mute-audio", "--window-size=1296,820"])
        if not args.no_video:
            kwargs.update(record_video_dir=RAW_VIDEO_DIR,
                          record_video_size={"width": 1280, "height": 720})
        ctx = p.chromium.launch_persistent_context(**kwargs)
        page = ctx.pages[0] if ctx.pages else ctx.new_page()

        if not args.skip_frames:
            step_youtube(page)
        step_page(page, "s2_blogpost", BLOG_POST_URL, "step-07-workspace-updates-post.png", 0,
                  "Open Workspace Updates post")
        human_scroll(page, 900)
        pause(page, 1500)
        step_product_page(page)
        step_page(page, "s4_help", HELP_URL, "step-10-help-center-get-started.png", 250,
                  "Open Help Center: Get started with Google Pics")
        step_pics_signin(page)
        step_blog(page)

        video = page.video
        ctx.close()
        if video and not args.no_video:
            webm = video.path()
            mp4 = os.path.join(VIDEO_DIR, f"{SLUG}-demo.mp4")
            convert_video(webm, mp4)
            shutil.rmtree(RAW_VIDEO_DIR, ignore_errors=True)
            print("Video:", mp4)

    with open(REPORT_PATH, "w", encoding="utf-8") as f:
        json.dump({"generated_at_ms": now_ms(), "steps": steps}, f, ensure_ascii=False, indent=2)
    print("Report:", REPORT_PATH)


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    main()
