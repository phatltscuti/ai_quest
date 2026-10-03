"""Record ONE Playwright session (real Chrome, headed) for the blog:
source article -> key sections (screenshots) -> plugin GitHub page -> render diagrams -> finished blog.
Then convert webm -> mp4 (libx264, yuv420p) and delete video_raw.
"""
import shutil, subprocess, time
from pathlib import Path
from playwright.sync_api import sync_playwright
import imageio_ffmpeg

ROOT = Path(__file__).resolve().parent
IMG = ROOT / "images"
RAW = ROOT / "video_raw"
OUT = ROOT / "video" / "ai-driven-code-modernization-prep-demo.mp4"
ARTICLE = "https://claude.com/blog/how-to-prepare-for-ai-driven-code-modernization-projects"
PLUGIN = "https://github.com/anthropics/claude-plugins-official/tree/main/plugins/code-modernization"
IMG.mkdir(exist_ok=True); OUT.parent.mkdir(exist_ok=True)
if RAW.exists(): shutil.rmtree(RAW)


def smooth_to(page, target_y, step=60, delay=0.025):
    cur = page.evaluate("window.scrollY")
    target_y = max(0, int(target_y))
    direction = 1 if target_y > cur else -1
    while abs(target_y - cur) > step:
        cur += step * direction
        page.evaluate(f"window.scrollTo(0,{cur})")
        time.sleep(delay)
    page.evaluate(f"window.scrollTo(0,{target_y})")
    time.sleep(0.6)


def heading_y(page, text, offset=165):
    loc = page.locator("h1,h2,h3", has_text=text).first
    return page.evaluate("(e)=>e.getBoundingClientRect().top + window.scrollY", loc.element_handle()) - offset


def dismiss_cookies(page):
    for name in ["Reject all", "Reject All", "Accept all", "Accept All", "Accept All Cookies", "Accept"]:
        try:
            btn = page.get_by_role("button", name=name, exact=True)
            if btn.count() and btn.first.is_visible():
                btn.first.click(timeout=2000); time.sleep(0.8); return name
        except Exception:
            pass
    return None


def scroll_through(page, speed=45, delay=0.03, pause_every=None):
    h = page.evaluate("document.body.scrollHeight") - page.viewport_size["height"]
    y = page.evaluate("window.scrollY")
    while y < h:
        y = min(h, y + speed)
        page.evaluate(f"window.scrollTo(0,{y})")
        time.sleep(delay)
        h = page.evaluate("document.body.scrollHeight") - page.viewport_size["height"]


with sync_playwright() as p:
    browser = p.chromium.launch(channel="chrome", headless=False)
    ctx = browser.new_context(viewport={"width": 1440, "height": 900},
                              record_video_dir=str(RAW), record_video_size={"width": 1440, "height": 900})
    page = ctx.new_page()
    t0 = time.time()

    # 1) Source article
    page.goto(ARTICLE, wait_until="networkidle"); time.sleep(2)
    print("cookie:", dismiss_cookies(page))
    time.sleep(1.5)
    page.screenshot(path=str(IMG / "step-01-article-hero.png"))
    time.sleep(1.5)

    sections = [
        ("Step 1: Define the target", "step-02-define-target.png"),
        ("Step 2: Define the certificate", "step-03-certificate.png"),
        ("Step 3: Set the promotion policy", "step-04-promotion-policy.png"),
        ("Step 4: Put the prerequisites in place", "step-05-prerequisites.png"),
        ("Step 5: Build and refine", "step-06-workflow-run.png"),
        ("A note on cost", "step-07-cost.png"),
    ]
    for text, fname in sections:
        smooth_to(page, heading_y(page, text))
        time.sleep(1.2)
        page.screenshot(path=str(IMG / fname))
        time.sleep(1.5)
        # glance a bit further into the section, like a reader
        smooth_to(page, page.evaluate("window.scrollY") + 500, step=40)
        time.sleep(1.0)
    smooth_to(page, heading_y(page, "Beyond the modernization")); time.sleep(2)

    # 2) Plugin page on GitHub (public, no login)
    page.goto(PLUGIN, wait_until="domcontentloaded"); time.sleep(3)
    try:
        y = heading_y(page, "Code Modernization", offset=90)
        smooth_to(page, y, step=40)
    except Exception as e:
        print("plugin heading not found:", e)
    time.sleep(1.2)
    page.screenshot(path=str(IMG / "step-08-plugin-github.png"))
    time.sleep(1.2)
    smooth_to(page, page.evaluate("window.scrollY") + 900, step=35); time.sleep(1.5)

    # 3) Diagrams: render to PNG and show them
    for name in ["diagram-01-six-step-roadmap", "diagram-02-preparation-checklist"]:
        page.goto((ROOT / "diagrams" / f"{name}.html").as_uri(), wait_until="load"); time.sleep(1)
        page.locator("#canvas").screenshot(path=str(IMG / f"{name}.png"))
        time.sleep(1.5)
        smooth_to(page, 400, step=20); time.sleep(1.5)
        smooth_to(page, 0, step=40); time.sleep(0.8)

    # 4) Finished blog, top to bottom
    page.goto((ROOT / "ai-driven-code-modernization-prep-blog.html").as_uri(), wait_until="load")
    time.sleep(2.5)
    scroll_through(page, speed=40, delay=0.03)
    time.sleep(2.5)
    print("session seconds:", round(time.time() - t0, 1))
    ctx.close(); browser.close()

webms = sorted(RAW.glob("*.webm"))
print("raw videos:", webms)
ff = imageio_ffmpeg.get_ffmpeg_exe()
subprocess.run([ff, "-y", "-i", str(webms[-1]), "-c:v", "libx264", "-pix_fmt", "yuv420p",
                "-preset", "medium", "-crf", "23", "-movflags", "+faststart", str(OUT)], check=True,
               stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
shutil.rmtree(RAW)
print("saved", OUT, OUT.stat().st_size)
