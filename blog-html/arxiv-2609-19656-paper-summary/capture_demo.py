"""
capture_demo.py - Reproducible capture session for the blog
"Self-Evolving Search Index (arXiv:2609.19656) - paper summary".

One Playwright session (real Chrome, headful, 1440x900, video recorded):
  1. arXiv abstract page  -> HTML (experimental) version of the paper
  2. scroll through key sections / figures / tables, screenshot each
  3. GitHub code repository (public page, no login)
  4. open the 3 local illustration pages (diagrams/*.html) and render them to PNG
  5. open the finished Vietnamese blog via file:// and scroll top -> bottom
Then convert video_raw/*.webm -> video/<slug>-demo.mp4 (libx264, yuv420p)
and delete video_raw.

Run:  python capture_demo.py
"""
import shutil
import subprocess
import time
from pathlib import Path

import imageio_ffmpeg
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent
SLUG = "arxiv-2609-19656-paper-summary"
IMG = ROOT / "images"
RAW = ROOT / "video_raw"
VID = ROOT / "video"
ABS_URL = "https://arxiv.org/abs/2609.19656"
HTML_URL = "https://arxiv.org/html/2609.19656v1"
REPO_URL = "https://github.com/augustinLib/Self-Index"

IMG.mkdir(exist_ok=True)
VID.mkdir(exist_ok=True)
if RAW.exists():
    shutil.rmtree(RAW)


def pause(sec=1.5):
    time.sleep(sec)


def smooth_scroll(page, total_px, step=120, delay=0.06):
    """Scroll gradually so the video looks human."""
    done = 0
    while done < total_px:
        page.mouse.wheel(0, step)
        done += step
        time.sleep(delay)


def scroll_to(page, selector, offset=-80):
    """Smoothly scroll until the element is near the top of the viewport."""
    el = page.locator(selector).first
    target = page.evaluate(
        "([s, o]) => { const e = document.querySelector(s); if (!e) return null;"
        " return e.getBoundingClientRect().top + window.scrollY + o; }",
        [selector, offset],
    )
    if target is None:
        print("  ! selector not found:", selector)
        return False
    cur = page.evaluate("window.scrollY")
    dist = target - cur
    steps = max(8, int(abs(dist) / 150))
    for i in range(1, steps + 1):
        page.evaluate("y => window.scrollTo(0, y)", cur + dist * i / steps)
        time.sleep(0.04)
    try:
        el.hover(timeout=2000)
    except Exception:
        pass
    return True


def shot(page, name):
    path = IMG / name
    page.screenshot(path=str(path))
    print("  saved", path.name)


with sync_playwright() as p:
    browser = p.chromium.launch(channel="chrome", headless=False, slow_mo=150)
    context = browser.new_context(
        viewport={"width": 1440, "height": 900},
        record_video_dir=str(RAW),
        record_video_size={"width": 1440, "height": 900},
        locale="en-US",
    )
    page = context.new_page()

    # 1. arXiv abstract page
    print("[1] arXiv abstract")
    page.goto(ABS_URL, wait_until="domcontentloaded")
    pause(2.5)
    shot(page, "step-01-arxiv-abstract.png")
    smooth_scroll(page, 360)
    pause(1.5)

    # 2. open the HTML (experimental) version by clicking the link
    print("[2] HTML version")
    link = page.locator("a#latexml-download-link, a:has-text('HTML (experimental)')").first
    try:
        link.scroll_into_view_if_needed(timeout=3000)
        link.hover()
        pause(1)
        link.click()
        page.wait_for_load_state("domcontentloaded")
    except Exception as e:
        print("  click failed, goto directly:", e)
        page.goto(HTML_URL, wait_until="domcontentloaded")
    page.wait_for_load_state("load")
    pause(2.5)
    shot(page, "step-02-html-paper-title.png")

    sections = [
        ("#S1", "step-03-introduction.png", 260),
        ("#S3\\.F1", "step-04-figure1-overview.png", 0),
        ("#S3\\.2","step-05-optimizer-section.png", 0),
        ("#S4\\.T1", "step-06-table1-bright.png", 0),
        ("#S4\\.T3", "step-07-table3-browsecomp.png", 0),
        ("#S4\\.F2", "step-08-figure2-online-cost.png", 0),
        ("#S4\\.T4", "step-09-table4-agent-memory.png", 0),
        ("#S5\\.T5", "step-10-table5-ablation.png", 0),
        ("#S5\\.F4", "step-11-figure4-case-study.png", 0),
        ("#S5\\.F6", "step-12-figure6-evolution.png", 0),
    ]
    for sel, name, extra in sections:
        print("[3] section", sel)
        if not scroll_to(page, sel):
            # fallback for subsection ids that differ
            alt = sel.replace("\\.SS2", "\\.2")
            scroll_to(page, alt)
        if extra:
            smooth_scroll(page, extra)
        pause(2)
        shot(page, name)
        pause(1)

    # 3. GitHub repository (public, no login)
    print("[4] GitHub repo")
    page.goto(REPO_URL, wait_until="domcontentloaded")
    pause(2.5)
    smooth_scroll(page, 600)
    pause(1.5)
    shot(page, "step-13-github-repo-readme.png")
    pause(1)

    # 4. illustration pages -> PNG
    print("[5] diagrams")
    for name in ["diagram-01-self-index-loop", "diagram-02-key-evolution", "diagram-03-scuti-apply"]:
        page.goto((ROOT / "diagrams" / f"{name}.html").as_uri(), wait_until="load")
        pause(2)
        page.locator("#card").screenshot(path=str(IMG / f"{name}.png"))
        print("  saved", name + ".png")
        smooth_scroll(page, 300)
        pause(1.5)

    # 5. finished blog, scrolled top -> bottom
    blog = ROOT / f"{SLUG}-blog.html"
    if blog.exists():
        print("[6] finished blog")
        page.goto(blog.as_uri(), wait_until="load")
        pause(2.5)
        shot(page, "step-14-finished-blog.png")
        height = page.evaluate("document.body.scrollHeight")
        y = 0
        while y < height - 900:
            page.mouse.wheel(0, 220)
            y += 220
            time.sleep(0.18)
            height = page.evaluate("document.body.scrollHeight")
        pause(2.5)
    else:
        print("  blog not found yet, skipping final step")

    video_path = page.video.path()
    context.close()
    browser.close()

# convert webm -> mp4
ffmpeg = imageio_ffmpeg.get_ffmpeg_exe()
out = VID / f"{SLUG}-demo.mp4"
cmd = [ffmpeg, "-y", "-i", str(video_path), "-c:v", "libx264", "-pix_fmt", "yuv420p",
       "-preset", "medium", "-crf", "23", "-movflags", "+faststart", str(out)]
print(" ".join(cmd))
subprocess.run(cmd, check=True, capture_output=True)
shutil.rmtree(RAW, ignore_errors=True)
print("video:", out)
