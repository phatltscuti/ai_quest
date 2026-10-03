"""
Ghep video hoan chinh cho blog:
  1) video cu (khao sat nguon chinh thuc) 0 -> 84.5s  (bo doan sign-in wall + blog cu)
  2) video/google-pics-live-session.mp4  (thao tac that trong Pics + Gemini)
  3) quay moi: blog VI hoan chinh cuon tu dau den cuoi
=> video/google-pics-vs-nanobanana-demo.mp4
"""
import os, shutil, subprocess, glob, pathlib
import imageio_ffmpeg
from playwright.sync_api import sync_playwright

HERE = os.path.dirname(os.path.abspath(__file__))
VID = os.path.join(HERE, "video")
TMP = os.path.join(HERE, "video_raw")
FF = imageio_ffmpeg.get_ffmpeg_exe()
W, H = 1440, 900
OLD = os.path.join(VID, "google-pics-vs-nanobanana-demo.mp4")
SOURCES_PART = os.path.join(VID, "google-pics-sources-part.mp4")
LIVE = os.path.join(VID, "google-pics-live-session.mp4")


def run(*args):
    subprocess.run([FF, "-y", "-loglevel", "error", *args], check=True)


def record_blog_scroll():
    os.makedirs(TMP, exist_ok=True)
    url = pathlib.Path(os.path.join(HERE, "google-pics-vs-nanobanana-blog.html")).as_uri()
    with sync_playwright() as p:
        b = p.chromium.launch(channel="chrome", headless=False)
        ctx = b.new_context(viewport={"width": W, "height": H}, record_video_dir=TMP,
                            record_video_size={"width": W, "height": H})
        pg = ctx.new_page()
        pg.goto(url)
        pg.wait_for_timeout(2500)
        total = pg.evaluate("document.body.scrollHeight")
        y = 0
        while y < total - H:
            y += 140
            pg.evaluate(f"window.scrollTo({{top:{y},behavior:'smooth'}})")
            pg.wait_for_timeout(420)
            total = pg.evaluate("document.body.scrollHeight")
        pg.wait_for_timeout(2000)
        path = pg.video.path()
        ctx.close(); b.close()
    return path


def main():
    # 1) phan nguon: chi cat 1 lan tu video cu (giu lai file rieng de chay lai duoc)
    if not os.path.exists(SOURCES_PART):
        run("-i", OLD, "-t", "84.5", "-c:v", "libx264", "-pix_fmt", "yuv420p", "-an", SOURCES_PART)
    blog_webm = record_blog_scroll()
    scale = f"scale={W}:{H}:force_original_aspect_ratio=decrease,pad={W}:{H}:(ow-iw)/2:(oh-ih)/2,setsar=1,fps=25"
    out = os.path.join(VID, "google-pics-vs-nanobanana-demo.tmp.mp4")
    run("-i", SOURCES_PART, "-i", LIVE, "-i", blog_webm,
        "-filter_complex", f"[0:v]{scale}[a];[1:v]{scale}[b];[2:v]{scale}[c];[a][b][c]concat=n=3:v=1:a=0[v]",
        "-map", "[v]", "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "23", "-movflags", "+faststart", out)
    os.replace(out, OLD)
    shutil.rmtree(TMP, ignore_errors=True)
    print("OK", OLD)


if __name__ == "__main__":
    main()
