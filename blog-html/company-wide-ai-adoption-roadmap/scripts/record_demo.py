"""ONE recorded Playwright session (real Chrome, 1440x900, record_video_dir=video_raw):
  1. open the LMI deck, flip slide by slide with ArrowRight, pause + screenshot key slides
  2. same for the SmartHR deck
  3. show the 3 custom diagrams (PNG)
  4. open the finished Vietnamese blog via file:// and scroll top -> bottom
Then convert webm -> mp4 (libx264, yuv420p) and delete video_raw."""
import os, sys, glob, shutil, subprocess
sys.stdout.reconfigure(encoding="utf-8")
from playwright.sync_api import sync_playwright
import imageio_ffmpeg
from capture_slides import run_decks

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, ".."))
RAW = os.path.join(ROOT, "video_raw")
OUT = os.path.join(ROOT, "video", "company-wide-ai-adoption-roadmap-demo.mp4")
SLUG = "company-wide-ai-adoption-roadmap"

def file_url(p): return "file:///" + os.path.abspath(p).replace("\\", "/")

def slow_scroll(pg, step=110, delay=170, pause_every=0):
    total = pg.evaluate("document.body.scrollHeight")
    y = 0; n = 0
    while y < total - 900:
        pg.mouse.wheel(0, step)
        y += step; n += 1
        pg.wait_for_timeout(delay)
        total = pg.evaluate("document.body.scrollHeight")
    pg.wait_for_timeout(1500)

def main():
    os.makedirs(RAW, exist_ok=True); os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with sync_playwright() as p:
        b = p.chromium.launch(channel="chrome", headless=False)
        ctx = b.new_context(viewport={"width": 1440, "height": 900},
                            record_video_dir=RAW, record_video_size={"width": 1440, "height": 900})
        pg = ctx.new_page()
        # 1-2. both decks, slide by slide
        run_decks(pg, [0])
        # 3. custom diagrams
        for name in ("roadmap", "org-structure", "bottlenecks"):
            pg.goto(file_url(os.path.join(ROOT, "images", f"diagram-{name}.png")))
            pg.wait_for_timeout(3500)
        # 4. finished blog, top to bottom
        pg.goto(file_url(os.path.join(ROOT, f"{SLUG}-blog.html")))
        pg.wait_for_timeout(2500)
        slow_scroll(pg)
        pg.mouse.wheel(0, -100000)
        pg.wait_for_timeout(1500)
        video = pg.video
        ctx.close(); b.close()
        webm = video.path()
    ff = imageio_ffmpeg.get_ffmpeg_exe()
    subprocess.run([ff, "-y", "-i", webm, "-c:v", "libx264", "-pix_fmt", "yuv420p", "-preset", "medium",
                    "-crf", "23", "-movflags", "+faststart", OUT], check=True, capture_output=True)
    shutil.rmtree(RAW, ignore_errors=True)
    print("video:", OUT, os.path.getsize(OUT) // 1024, "KB")

if __name__ == "__main__":
    main()
