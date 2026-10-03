"""One continuous Playwright session (real Chrome, headed) that:
  1. opens the original post on x.com (no login, never types credentials)
  2. opens the public mirror api.fxtwitter.com JSON
  3. reads the article in the local reader view (sources/article-reader.html) and takes screenshots
  4. shows the 2 custom infographics
  5. ends on the finished blog (file://), scrolled slowly top to bottom
The whole session is recorded to video_raw/ and converted to video/<slug>-demo.mp4 (libx264, yuv420p).
"""
import shutil
import subprocess
import time
from pathlib import Path

import imageio_ffmpeg
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).parent.resolve()
IMG = ROOT / "images"
RAW = ROOT / "video_raw"
OUT = ROOT / "video" / "greg-isenberg-x-post-insights-demo.mp4"
POST = "https://x.com/gregisenberg/status/2103927365977928019"
API = "https://api.fxtwitter.com/gregisenberg/status/2103927365977928019"
W, H = 1440, 900


def pause(s):
    time.sleep(s)


def smooth_scroll(page, total, step=120, delay=0.05):
    done = 0
    while done < total:
        page.mouse.wheel(0, step)
        done += step
        time.sleep(delay)


def scroll_to(page, selector, offset=-90):
    """Scroll gradually until selector sits near the top of the viewport."""
    for _ in range(200):
        top = page.evaluate(f"document.querySelector({selector!r}).getBoundingClientRect().top")
        if abs(top + offset) < 60:
            break
        page.mouse.wheel(0, max(min(top + offset, 160), -160))
        time.sleep(0.04)
    pause(0.6)


def shot(page, name):
    page.screenshot(path=str(IMG / name))
    print("screenshot", name)


def main():
    IMG.mkdir(exist_ok=True)
    OUT.parent.mkdir(exist_ok=True)
    if RAW.exists():
        shutil.rmtree(RAW)
    with sync_playwright() as pw:
        browser = pw.chromium.launch(channel="chrome", headless=False, args=["--window-size=1460,1000"])
        ctx = browser.new_context(viewport={"width": W, "height": H}, record_video_dir=str(RAW),
                                  record_video_size={"width": W, "height": H}, locale="en-US")
        page = ctx.new_page()

        # 1. Original post on x.com
        page.goto(POST, wait_until="domcontentloaded")
        pause(9)
        shot(page, "step-01-x-post-login-wall.png")
        smooth_scroll(page, 700)
        pause(2)
        page.evaluate("window.scrollTo({top:0,behavior:'smooth'})")
        pause(2)

        # 2. Public mirror JSON
        page.goto(API, wait_until="domcontentloaded")
        pause(2)
        # Chrome's JSON viewer has a "Pretty-print" checkbox; click it like a user would
        try:
            page.get_by_text("Pretty-print").first.wait_for(timeout=1500)
        except Exception:
            pass
        page.mouse.move(60, 9, steps=15)
        page.mouse.click(95, 9)  # the checkbox lives in a closed shadow root, so click it by position
        pause(2.5)
        shot(page, "step-02-fxtwitter-api-json.png")
        smooth_scroll(page, 900, delay=0.06)
        pause(1.5)

        # 3. Reader view of the article
        page.goto((ROOT / "sources" / "article-reader.html").as_uri())
        page.wait_for_load_state("networkidle")
        pause(2.5)
        shot(page, "step-03-article-intro.png")
        smooth_scroll(page, 900, delay=0.06)
        pause(1.5)

        scroll_to(page, "#img-0", offset=-40)
        pause(1.5)
        shot(page, "step-04-who-is-doing-it.png")

        scroll_to(page, "#img-1", offset=-40)
        pause(1.5)
        shot(page, "step-05-holdco-folder.png")

        scroll_to(page, "#img-2", offset=-40)
        pause(1.5)
        shot(page, "step-06-agents-you-build.png")

        page.evaluate("""() => { const h=[...document.querySelectorAll('h2')].find(e=>e.textContent.startsWith('Step 5')); h.id='step5'; }""")
        scroll_to(page, "#step5", offset=-30)
        pause(1.5)
        shot(page, "step-07-rulebook-prompts.png")

        scroll_to(page, "#img-7", offset=-40)
        pause(1.5)
        shot(page, "step-08-dashboard.png")
        smooth_scroll(page, 1500, delay=0.04)
        pause(1.5)

        # 4. Custom infographics
        for name in ("infographic-01-ai-rollup-playbook-vi.html", "infographic-02-scuti-application-vi.html"):
            page.goto((ROOT / "infographics" / name).as_uri())
            pause(3)
            smooth_scroll(page, 400, delay=0.08)
            pause(2.5)

        # 5. Finished blog, top to bottom
        page.goto((ROOT / "greg-isenberg-x-post-insights-blog.html").as_uri())
        page.wait_for_load_state("load")
        pause(3)
        # read-like pacing: steady scroll, short pause whenever a section heading or image reaches the top area
        stops = page.evaluate("[...document.querySelectorAll('h2, .screenshot-wrap')].map(e => e.getBoundingClientRect().top + window.scrollY)")
        height = page.evaluate("document.body.scrollHeight")
        while page.evaluate("window.scrollY + window.innerHeight") < height - 5:
            y = page.evaluate("window.scrollY")
            page.mouse.wheel(0, 80)
            time.sleep(0.06)
            y2 = page.evaluate("window.scrollY")
            if any(y + 120 < t <= y2 + 120 for t in stops):
                time.sleep(1.2)
            height = page.evaluate("document.body.scrollHeight")
        pause(3)

        video_path = page.video.path()
        ctx.close()
        browser.close()

    ff = imageio_ffmpeg.get_ffmpeg_exe()
    subprocess.run([ff, "-y", "-i", str(video_path), "-c:v", "libx264", "-pix_fmt", "yuv420p",
                    "-preset", "medium", "-crf", "23", "-movflags", "+faststart", str(OUT)], check=True,
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    shutil.rmtree(RAW, ignore_errors=True)
    print("video", OUT)


if __name__ == "__main__":
    main()
