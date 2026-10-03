"""Record ONE Playwright session (real Chrome, 1440x900) for the blog:
note.com article -> YouTube webinar -> diagrams -> finished blog (file://).
Takes step-XX screenshots on the way, then converts the recorded webm to mp4.

Run:  python record_demo.py
"""
import shutil, subprocess, time
from pathlib import Path
from playwright.sync_api import sync_playwright
import imageio_ffmpeg

ROOT = Path(__file__).parent
IMG = ROOT / "images"
RAW = ROOT / "video_raw"
OUT = ROOT / "video" / "ai-hr-performance-evaluation-demo.mp4"
NOTE = "https://note.com/hashiyaman/n/na03108694c97"
YT_ID = "X52tm3MsSjA"
BLOG = ROOT / "ai-hr-performance-evaluation-blog.html"

CAPTION_JS = """(t) => {
  let d = document.getElementById('__cap');
  if (!d) { d = document.createElement('div'); d.id='__cap';
    d.style.cssText='position:fixed;left:50%;bottom:28px;transform:translateX(-50%);z-index:2147483647;'+
      'background:rgba(13,71,161,.92);color:#fff;font:600 18px Segoe UI,Arial,sans-serif;padding:10px 22px;'+
      'border-radius:24px;box-shadow:0 4px 14px rgba(0,0,0,.3);max-width:80%;text-align:center;pointer-events:none';
    document.body.appendChild(d); }
  d.textContent = t; d.style.display = t ? 'block' : 'none';
}"""


def caption(page, text):
    try:
        page.evaluate(CAPTION_JS, text)
    except Exception:
        pass


def shot(page, name, locator=None):
    caption(page, "")
    time.sleep(1.0)
    path = str(IMG / name)
    if locator is not None:
        locator.screenshot(path=path)
    else:
        page.screenshot(path=path)
    print("screenshot", name)


def smooth_to(page, y, step=18, delay=0.016):
    cur = page.evaluate("() => window.scrollY")
    n = max(1, int(abs(y - cur) / step))
    for i in range(1, n + 1):
        page.evaluate("(v) => window.scrollTo(0, v)", cur + (y - cur) * i / n)
        time.sleep(delay)


def scroll_to_text(page, text, offset=90, selector="h2, h3, strong, p, figure"):
    y = page.evaluate("""([t, sel, off]) => {
        const el = Array.from(document.querySelectorAll(sel)).find(e => e.innerText && e.innerText.trim().startsWith(t));
        return el ? el.getBoundingClientRect().top + window.scrollY - off : null; }""", [text, selector, offset])
    if y is None:
        print("  ! text not found:", text)
        return False
    smooth_to(page, y)
    return True


def main():
    IMG.mkdir(exist_ok=True)
    OUT.parent.mkdir(exist_ok=True)
    if RAW.exists():
        shutil.rmtree(RAW)
    with sync_playwright() as p:
        # hide the automation banner/flag, otherwise the YouTube player refuses to play ("エラーが発生しました")
        browser = p.chromium.launch(channel="chrome", headless=False,
                                    ignore_default_args=["--enable-automation"],
                                    args=["--disable-blink-features=AutomationControlled"])
        ctx = browser.new_context(viewport={"width": 1440, "height": 900}, locale="ja-JP",
                                  record_video_dir=str(RAW), record_video_size={"width": 1440, "height": 900})
        page = ctx.new_page()

        # ---------- 1. note.com article ----------
        page.goto(NOTE, wait_until="domcontentloaded")
        time.sleep(5)
        caption(page, "Nguồn 1: bài note của hashiyaman (Ubie) – AI đánh giá nhân sự")
        time.sleep(3)
        shot(page, "step-01-note-article-top.png")
        caption(page, "Mục lục: vì sao giao đánh giá cho AI và cách triển khai")
        scroll_to_text(page, "目次", selector="h2, h3, p, div, span")
        time.sleep(2.5)
        scroll_to_text(page, "なぜAIに評価をやらせるのか", selector="h2")
        caption(page, "4 mục đích: tập trung vào việc, bỏ thiên kiến, hợp cách làm việc mới, dữ liệu hóa mọi hoạt động")
        time.sleep(3)
        shot(page, "step-02-note-why-ai.png")
        for sub in ["評価の過程からバイアスを外す", "すべての活動がデータ化される力学を作る"]:
            scroll_to_text(page, sub, selector="h3, h2")
            time.sleep(2.5)
        scroll_to_text(page, "評価の最終決定は代表のみが行う", selector="h3")
        caption(page, "5 bước: dữ liệu → AI nháp → nhân viên bổ sung → AI kiểm chứng → CEO duyệt")
        time.sleep(3)
        shot(page, "step-03-note-five-steps.png")
        scroll_to_text(page, "成果と能力を別々に測り、掛け合わせる", selector="h3")
        caption(page, "Thành quả (7 dạng) × Năng lực (Ubieness + U-map)")
        time.sleep(3)
        shot(page, "step-04-note-achievement-ability.png")
        scroll_to_text(page, "評価システムの全体像", selector="h2")
        caption(page, "Toàn cảnh: Activity Report → Evaluation AI agent → Companion AI agent")
        time.sleep(3)
        shot(page, "step-05-note-system-overview.png")
        scroll_to_text(page, "アクティビティレポート", selector="h3")
        caption(page, "Activity Report: log từ Slack, biên bản họp, GitHub, Jira, Notion… sinh mỗi ngày (NDJSON)")
        time.sleep(2)
        smooth_to(page, page.evaluate("() => window.scrollY") + 250)
        time.sleep(2.5)
        shot(page, "step-06-note-activity-report.png")
        scroll_to_text(page, "データ処理にコードと生成AIを使い分ける", selector="h3, h2")
        caption(page, "Mẹo triển khai: code/SQL cho phần chính xác, GenAI cho phần diễn giải; rubric 3 tầng")
        time.sleep(3)
        shot(page, "step-07-note-rubric.png")
        scroll_to_text(page, "精度を上げる工程もAIに回させる", selector="h3")
        caption(page, "Human-on-the-loop: AI tự chấm 8–12 giờ/người, con người sửa rubric")
        time.sleep(3)
        shot(page, "step-08-note-human-on-the-loop.png")
        scroll_to_text(page, "何を学んだか", selector="h2")
        caption(page, "Bài học: làm rõ triết lý, định nghĩa phần việc của con người, dữ liệu dùng được ngoài đánh giá")
        time.sleep(3)
        shot(page, "step-09-note-learnings.png")
        scroll_to_text(page, "評価においてマネジメントに何が残るのか", selector="h2, h3")
        time.sleep(3)

        # ---------- 2. YouTube webinar ----------
        caption(page, "Nguồn 2: webinar YouTube của Ubie × Offers")
        time.sleep(1.5)
        page.goto(f"https://www.youtube.com/watch?v={YT_ID}", wait_until="domcontentloaded")
        time.sleep(6)
        for sel in ["button:has-text('Reject all')", "button:has-text('すべて拒否')"]:
            try:
                page.locator(sel).first.click(timeout=1200)
                time.sleep(2)
            except Exception:
                pass
        page.evaluate("() => { const v=document.querySelector('video'); if (v) { v.muted=true; v.pause(); } }")
        caption(page, "Webinar ~65 phút: Ubieが実践するAI時代の人事評価")
        time.sleep(3)
        shot(page, "step-10-youtube-video-page.png")
        try:
            page.locator("#description-inline-expander, #expand").first.click(timeout=4000)
        except Exception:
            pass
        time.sleep(1.5)
        smooth_to(page, 420)
        caption(page, "Mô tả video: diễn giả Hashiyama (Ubie), host Suzuki (Offers)")
        time.sleep(3)
        shot(page, "step-11-youtube-description.png")
        try:
            page.locator("ytd-video-description-transcript-section-renderer button").first.click(timeout=4000)
        except Exception as e:
            print("transcript button:", e)
        smooth_to(page, 0)
        caption(page, "Bảng 'Hiện bản chép lời' – trong phiên này chỉ quay vòng tải, nên transcript được lấy từ phụ đề tự động")
        time.sleep(6)
        shot(page, "step-12-youtube-transcript-panel.png")

        # Play the webinar and jump to the demo / slide parts
        player = page.locator("#movie_player")
        page.evaluate("() => { const v=document.querySelector('video'); if (v) v.muted=true; }")
        try:
            player.click(timeout=3000)
        except Exception:
            page.evaluate("() => document.querySelector('video') && document.querySelector('video').play()")
        time.sleep(3)
        for t, name, cap in [
            (1630, "step-13-youtube-demo-activity-report.png", "27:10 – Demo Activity Report: tổng hợp hoạt động mỗi ngày (dữ liệu demo)"),
            (1715, "step-14-youtube-demo-fact-sheet.png", "28:35 – Evaluation AI agent gom hoạt động 1 tháng thành Fact Sheet"),
            (1770, "step-15-youtube-demo-evaluation-report.png", "29:30 – Bản nháp Evaluation Report: bậc thành quả × năng lực + lý do"),
            (1835, "step-16-youtube-demo-companion-agent.png", "30:35 – Companion agent phản hồi và gợi ý hướng phát triển"),
            (2075, "step-17-youtube-rubric-slide.png", "34:35 – Rubric 3 tầng để AI biết thế nào là 'đúng'"),
            (2160, "step-18-youtube-human-on-the-loop.png", "36:00 – Human-on-the-loop: AI tự review AI, người sửa rubric"),
        ]:
            page.evaluate("(s) => { const v=document.querySelector('video'); if (v) { v.muted=true; v.currentTime=s; v.play(); } }", t)
            caption(page, cap)
            page.mouse.move(1430, 880)
            time.sleep(7)
            shot(page, name, player)
            caption(page, cap)
            time.sleep(1.5)
        page.evaluate("() => { const v=document.querySelector('video'); if (v) v.pause(); }")

        # ---------- 3. Diagrams ----------
        for d, cap in [("diagram-01-data-flow", "Sơ đồ tự vẽ 1: dữ liệu hằng ngày → AI phân tích → đánh giá"),
                       ("diagram-02-scuti-rollout", "Sơ đồ tự vẽ 2: đề xuất áp dụng tại Scuti AI + rào chắn quyền riêng tư")]:
            page.goto((ROOT / "diagrams" / f"{d}.html").as_uri() + "?lang=vi")
            time.sleep(1)
            caption(page, cap)
            time.sleep(3)
            smooth_to(page, 500, step=8)
            time.sleep(3)
            smooth_to(page, 0, step=12)
            time.sleep(1)

        # ---------- 4. Finished blog ----------
        if BLOG.exists():
            page.goto(BLOG.as_uri())
            time.sleep(1)
            caption(page, "Blog hoàn chỉnh (tiếng Việt) – cuộn từ đầu đến cuối")
            time.sleep(3)
            caption(page, "")
            total = page.evaluate("() => document.body.scrollHeight - window.innerHeight")
            y = 0
            while y < total:
                y = min(total, y + 9)
                page.evaluate("(v) => window.scrollTo(0, v)", y)
                time.sleep(0.018)
            time.sleep(2)
            caption(page, "Hết – cảm ơn đã xem!")
            time.sleep(3)

        video = page.video
        ctx.close()
        browser.close()
        webm = Path(video.path())

    ffmpeg = imageio_ffmpeg.get_ffmpeg_exe()
    subprocess.run([ffmpeg, "-y", "-i", str(webm), "-c:v", "libx264", "-pix_fmt", "yuv420p", "-preset", "medium",
                    "-crf", "23", "-r", "25", "-movflags", "+faststart", "-an", str(OUT)], check=True,
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    shutil.rmtree(RAW, ignore_errors=True)
    print("video:", OUT)


if __name__ == "__main__":
    main()
