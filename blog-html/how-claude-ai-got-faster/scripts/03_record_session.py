"""Buoc 3: quay TOAN BO phien Playwright (Chrome that, headless=False, 1440x900):
mo bai goc -> cuon qua cac phan chinh + chup step-XX -> mo cac so do tu ve -> mo blog (file://) cuon tu tren xuong duoi.
Sau do chuyen webm -> mp4 (libx264, yuv420p) va xoa video_raw."""
import pathlib, random, shutil, subprocess
import imageio_ffmpeg
from playwright.sync_api import sync_playwright

ROOT = pathlib.Path(__file__).resolve().parent.parent
IMG, RAW, OUT = ROOT / "images", ROOT / "video_raw", ROOT / "video"
URL = "https://claude.dev/blog/how-we-made-claude-ai-faster/"
SLUG = "how-claude-ai-got-faster"

# (ten file, doan text de tim, do lech px so voi dinh viewport, y toi thieu de bo qua muc luc)
SHOTS = [
    ("step-02-core-journeys-chart", "Core user journeys, p75", -40, 800),
    ("step-03-the-brief", "The brief", -30, 1500),
    ("step-04-instruction-vs-wallclock", "Does the count track the clock?", -40, 1500),
    ("step-05-loop-figure", "One thread in the loop", -40, 1500),
    ("step-06-sidebar-jank-fig-a", "FIG A", -430, 1500),
    ("step-07-em-dash-chart", "Highlighting the first code block on a page", -40, 1500),
    ("step-08-guardrails-static-composer", "FIG B", -330, 1500),
    ("step-09-chrome-prerender-thread", "Occasionally, I", -160, 1500),
    ("step-10-steering", "Steering", -30, 1500),
    ("step-11-8ms-budget", "An 8-millisecond budget", -30, 1500),
    ("step-12-whats-next", "What’s next", -30, 1500),
]

FIND_Y = """([needle, minY]) => {
  const w = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
  const n = needle.toLowerCase();
  while (w.nextNode()) {
    const t = w.currentNode;
    let sticky = false;
    for (let e = t.parentElement; e; e = e.parentElement) {
      const pos = getComputedStyle(e).position;
      if (pos === 'sticky' || pos === 'fixed') { sticky = true; break; }
    }
    if (!sticky && t.textContent.trim().toLowerCase().startsWith(n) && t.parentElement) {
      const r = t.parentElement.getBoundingClientRect();
      const y = r.top + window.scrollY;
      if (y >= minY && r.height > 0) return Math.round(y);
    }
  }
  return null;
}"""

def smooth_scroll_to(page, target_y, step=110, delay=(55, 95)):
    cur = page.evaluate("window.scrollY")
    while abs(target_y - cur) > 4:
        d = max(-step, min(step, target_y - cur))
        page.mouse.wheel(0, d)
        page.wait_for_timeout(random.randint(*delay))
        new = page.evaluate("window.scrollY")
        if new == cur:  # het trang / khong cuon duoc nua
            break
        cur = new

def scroll_through(page, step=100, delay=(110, 160), pauses=()):
    h = page.evaluate("document.documentElement.scrollHeight") - page.viewport_size["height"]
    y = 0
    while y < h:
        page.mouse.wheel(0, step)
        page.wait_for_timeout(random.randint(*delay))
        y = page.evaluate("window.scrollY")
        if any(abs(y - p) < step for p in pauses):
            page.wait_for_timeout(1500)
        if page.evaluate("window.scrollY + innerHeight >= document.documentElement.scrollHeight - 2"):
            break

def main():
    if RAW.exists():
        shutil.rmtree(RAW)
    with sync_playwright() as p:
        browser = p.chromium.launch(channel="chrome", headless=False, args=["--start-maximized"])
        ctx = browser.new_context(viewport={"width": 1440, "height": 900},
                                  record_video_dir=str(RAW), record_video_size={"width": 1440, "height": 900})
        page = ctx.new_page()
        page.goto(URL, wait_until="networkidle", timeout=60000)
        page.mouse.move(720, 450)
        page.wait_for_timeout(2500)
        print("final url:", page.url, "| title:", page.title())
        page.screenshot(path=str(IMG / "step-01-article-header.png"))
        page.wait_for_timeout(1500)

        for name, needle, off, min_y in SHOTS:
            y = page.evaluate(FIND_Y, [needle, min_y])
            if y is None:
                print("NOT FOUND:", needle); continue
            smooth_scroll_to(page, max(0, y + off))
            page.wait_for_timeout(2600)
            page.screenshot(path=str(IMG / f"{name}.png"))
            print("shot", name, "at", y)
            page.wait_for_timeout(1200)

        # Xem cac so do tu ve (HTML/SVG da render ra PNG o buoc 2)
        for d in ["diagram-01-optimization-map", "diagram-02-before-after-p75",
                  "diagram-03-static-shell-concept", "diagram-04-scuti-perf-loop"]:
            page.goto((ROOT / "diagrams" / f"{d}.html").as_uri())
            page.mouse.move(720, 450)
            page.wait_for_timeout(3000)
            scroll_through(page, step=80, delay=(120, 170))
            page.wait_for_timeout(1500)

        # Ket thuc tren blog hoan chinh, cuon tu tren xuong duoi
        page.goto((ROOT / f"{SLUG}-blog.html").as_uri())
        page.mouse.move(720, 450)
        page.wait_for_timeout(3000)
        scroll_through(page, step=100, delay=(120, 170))
        page.wait_for_timeout(3000)

        video_path = page.video.path()
        ctx.close(); browser.close()

    OUT.mkdir(exist_ok=True)
    mp4 = OUT / f"{SLUG}-demo.mp4"
    ff = imageio_ffmpeg.get_ffmpeg_exe()
    subprocess.run([ff, "-y", "-i", str(video_path), "-c:v", "libx264", "-pix_fmt", "yuv420p",
                    "-preset", "medium", "-crf", "23", "-movflags", "+faststart", str(mp4)], check=True,
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    shutil.rmtree(RAW, ignore_errors=True)
    print("video:", mp4)

if __name__ == "__main__":
    main()
