"""capture_demo.py - one recorded Playwright session (real Chrome, headful, 1440x900).

Flow: open the Anthropic article -> scroll & screenshot key parts (images/step-XX-*.png)
      -> show own diagrams -> show tia_demo.py output -> open finished VI blog via file://
      and scroll top to bottom. The webm recording is converted to
      video/anthropic-test-impact-analysis-ci-demo.mp4 with the ffmpeg bundled in imageio-ffmpeg,
      then video_raw/ is deleted.

Prereq: python render_diagrams.py (creates images/diagram-*.png and diagrams/diagram-03-*.html)
Usage : python capture_demo.py
"""
import shutil
import subprocess
from pathlib import Path

import imageio_ffmpeg
from playwright.sync_api import sync_playwright

HERE = Path(__file__).parent.resolve()
IMG = HERE / "images"
RAW = HERE / "video_raw"
OUT = HERE / "video"
SLUG = "anthropic-test-impact-analysis-ci"
URL = ("https://claude.com/blog/agentic-coding-is-straining-ci-heres-how-we-scaled-"
       "test-impact-analysis-at-anthropic")

HIDE_JS = """(hide) => {
  if (hide) {
    window.__hidden = [];
    for (const el of document.querySelectorAll('body *')) {
      const cs = getComputedStyle(el);
      if ((cs.position === 'fixed' || cs.position === 'sticky') && el.getBoundingClientRect().top < 220
          && el.offsetHeight < 300) { window.__hidden.push([el, el.style.visibility]); el.style.visibility = 'hidden'; }
    }
  } else { (window.__hidden || []).forEach(([el, v]) => el.style.visibility = v); }
}"""


def smooth_scroll(page, distance, step=110, delay=70):
    moved = 0
    while moved < distance:
        page.mouse.wheel(0, step)
        page.wait_for_timeout(delay)
        moved += step


def scroll_to_y(page, target_y, step=110, delay=60):
    """Human-like wheel scroll until window.scrollY reaches target_y."""
    for _ in range(400):
        y = page.evaluate("scrollY")
        if abs(y - target_y) < step:
            break
        page.mouse.wheel(0, step if target_y > y else -step)
        page.wait_for_timeout(delay)
    page.evaluate(f"window.scrollTo(0, {target_y})")
    page.wait_for_timeout(600)


def abs_top(page, locator):
    return page.evaluate("el => el.getBoundingClientRect().top + scrollY", locator.element_handle())


def shot_figure(page, src_part, name):
    img = page.locator(f"img[src*='{src_part}']").first
    top = abs_top(page, img)
    scroll_to_y(page, max(0, int(top) - 40))
    page.wait_for_timeout(1200)
    page.evaluate(HIDE_JS, True)
    box = img.bounding_box()
    pad = 16
    page.screenshot(path=str(IMG / name), clip={
        "x": max(0, box["x"] - pad), "y": max(0, box["y"] - pad),
        "width": box["width"] + 2 * pad, "height": min(900 - max(0, box["y"] - pad), box["height"] + 2 * pad)})
    page.evaluate(HIDE_JS, False)
    print("saved", name)
    page.wait_for_timeout(1500)


def shot_section(page, heading_text, name):
    h = page.locator("h2", has_text=heading_text).first
    scroll_to_y(page, max(0, int(abs_top(page, h)) - 150))
    page.wait_for_timeout(1500)
    page.screenshot(path=str(IMG / name))
    print("saved", name)
    page.wait_for_timeout(1200)


def show_local(page, path, pause=2500, scroll=0):
    page.goto(path.as_uri())
    page.wait_for_timeout(pause)
    if scroll:
        smooth_scroll(page, scroll, step=90, delay=90)
        page.wait_for_timeout(1500)


def main():
    IMG.mkdir(exist_ok=True)
    if RAW.exists():
        shutil.rmtree(RAW)
    with sync_playwright() as p:
        browser = p.chromium.launch(channel="chrome", headless=False)
        ctx = browser.new_context(viewport={"width": 1440, "height": 900},
                                  record_video_dir=str(RAW),
                                  record_video_size={"width": 1440, "height": 900})
        page = ctx.new_page()

        # 1) Source article
        page.goto(URL, wait_until="networkidle", timeout=90000)
        page.wait_for_timeout(2500)
        page.screenshot(path=str(IMG / "step-01-article-hero.png"))
        print("saved step-01-article-hero.png")
        page.wait_for_timeout(1500)

        shot_figure(page, "da466791", "step-02-bottleneck-moves-downstream.png")
        shot_figure(page, "e0fd4bf1", "step-03-ci-job-volume-runway.png")
        shot_section(page, "The test impact analysis architecture", "step-04-tia-architecture-text.png")
        smooth_scroll(page, 700)
        shot_figure(page, "33889734", "step-05-slack-thread-prediction.png")
        shot_figure(page, "c1d3dc74", "step-06-claude-tag-oncall-conversation.png")
        shot_figure(page, "c816aae3", "step-07-listener-memory-limit.png")
        shot_figure(page, "958f4a9d", "step-08-selection-service-before-after.png")
        shot_figure(page, "4deaf7d0", "step-09-listener-backlog-after-redesign.png")
        shot_section(page, "What I would do differently", "step-10-what-i-would-do-differently.png")
        smooth_scroll(page, 500)
        page.wait_for_timeout(1500)

        # 2) Own diagrams + illustrative script output
        show_local(page, HERE / "diagrams" / "diagram-01-tia-pipeline.html", pause=4000, scroll=300)
        show_local(page, HERE / "diagrams" / "diagram-02-patch-timeline.html", pause=4000)
        show_local(page, HERE / "diagrams" / "diagram-03-tia-demo-output.html", pause=3500)

        # 3) Finished blog, top to bottom
        page.goto((HERE / f"{SLUG}-blog.html").as_uri())
        page.wait_for_timeout(2500)
        total = page.evaluate("document.documentElement.scrollHeight") - 900
        smooth_scroll(page, total + 200, step=140, delay=55)
        page.wait_for_timeout(2500)

        ctx.close()
        browser.close()

    # 4) webm -> mp4
    webm = next(RAW.glob("*.webm"))
    OUT.mkdir(exist_ok=True)
    mp4 = OUT / f"{SLUG}-demo.mp4"
    ff = imageio_ffmpeg.get_ffmpeg_exe()
    subprocess.run([ff, "-y", "-i", str(webm), "-c:v", "libx264", "-pix_fmt", "yuv420p",
                    "-preset", "medium", "-crf", "23", "-movflags", "+faststart", str(mp4)],
                   check=True, capture_output=True)
    shutil.rmtree(RAW)
    print("video:", mp4)


if __name__ == "__main__":
    main()
