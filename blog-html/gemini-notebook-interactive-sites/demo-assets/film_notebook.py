"""Quay video Quest 5 trên Gemini Notebook (quay ngầm qua CDP screencast).

  python film_notebook.py n1      # tạo notebook mới, upload 4 PDF, gửi 2 prompt, chờ generate (tua nhanh)
  python film_notebook.py n2      # dùng site A (tra mã lỗi, calculator)
  python film_notebook.py n3      # dùng dashboard B
  python film_notebook.py n4      # hỏi notebook chat 2 câu so sánh với RAG
"""
import json, sys, time
from pathlib import Path
from playwright.sync_api import sync_playwright

HERE = Path(__file__).resolve().parent
Q5 = HERE.parent
ROOT = Q5.parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from cdp_rec import open_window, Recorder, show_click, mask_pii

VID = Q5 / "videos"; VID.mkdir(exist_ok=True)
STATE = HERE / "film_state.json"
SHOT = Q5 / "images"
BLUR_HOME = "project-button{filter:blur(9px)!important}"
NAME = "AQ-200 Demo – Interactive Site (video)"

def state(): return json.loads(STATE.read_text()) if STATE.exists() else {}
def save(**kw): s = state(); s.update(kw); STATE.write_text(json.dumps(s, indent=1))

def typing(page, rec, text, delay=12):
    page.keyboard.type(text, delay=delay)

def n1(page, rec):
    if state().get("notebook"):
        page.goto(state()["notebook"]); page.wait_for_timeout(4000); mask_pii(page); rec.pump(1)
    else:
        page.add_style_tag(content=BLUR_HOME); mask_pii(page); rec.pump(2)
        show_click(page, page.get_by_role("button", name="New notebook").first); rec.pump(5)
        save(notebook=page.url)
    # đóng banner nếu có
    for lbl in ["Close", "Dismiss"]:
        b = page.get_by_role("button", name=lbl)
        if b.count() and b.first.is_visible(): show_click(page, b.first); rec.pump(1); break
    # đổi tên
    try:
        t = page.get_by_text("Untitled notebook").first
        show_click(page, t); rec.pump(1)
        ed = page.locator("input:visible, [contenteditable=true]:visible").first
        ed.fill(NAME, timeout=3000); page.keyboard.press("Enter"); rec.pump(1.5)
    except Exception as e:
        print("rename skipped:", str(e)[:80]); page.keyboard.press("Escape")
    # upload nguồn
    show_click(page, page.locator("button:visible", has_text="Add sources").first); rec.pump(1.5)
    pdfs = sorted(str(p) for p in (Q5 / "sources").glob("*.pdf"))
    with page.expect_file_chooser() as fc:
        show_click(page, page.locator(":is(button,[role=button],a):visible", has_text="Upload files").first)
    fc.value.set_files(pdfs); rec.pump(12)
    page.screenshot(path=str(SHOT / "video-01-sources.png"))
    # 2 prompt
    for i, f in enumerate(["prompt-a-site.txt", "prompt-b-dashboard.txt"]):
        box = page.get_by_placeholder("Ask a question or create something")
        if not box.count(): box = page.locator("textarea").last
        show_click(page, box.first)
        typing(page, rec, (HERE / "prompts" / f).read_text(encoding="utf-8").strip(), 4)
        rec.pump(1); page.keyboard.press("Enter"); rec.pump(12)
        nn = page.get_by_role("button", name="Not now")
        if nn.count() and nn.first.is_visible(): show_click(page, nn.first)
        rec.pump(6)
    page.screenshot(path=str(SHOT / "video-02-generating.png"))
    # chờ generate (tua nhanh x12)
    rec.fast(12); t0 = time.time()
    while time.time() - t0 < 420:
        rec.pump(5)
        if page.get_by_text("Generating", exact=False).count() == 0 and time.time() - t0 > 30: break
    rec.normal(); save(gen_seconds=round(time.time() - t0)); rec.pump(3)
    page.screenshot(path=str(SHOT / "video-03-studio-done.png"))

def open_artifact(page, rec, title_part):
    card = page.locator(f"text={title_part} >> visible=true").first
    show_click(page, card); rec.pump(4)
    print("artifact url:", page.url)

def n2(page, rec):
    s = state(); page.goto(s["notebook"]); page.wait_for_timeout(4000); mask_pii(page); rec.pump(2)
    open_artifact(page, rec, "Series Guide & Troubleshooting")
    rec.pump(6)
    fr = page.frame_locator("iframe").first
    try:
        inp = fr.locator("input[type=search], input[type=text]").first
        show_click(page, inp); page.keyboard.type("E03", delay=180); rec.pump(4)
        page.keyboard.press("Control+A"); page.keyboard.type("E02", delay=180); rec.pump(4)
    except Exception as e: print("lookup:", str(e)[:100])
    for _ in range(12): page.mouse.move(900, 700); page.mouse.wheel(0, 250); rec.pump(0.5)
    try:
        show_click(page, fr.get_by_text("Pets, smoking", exact=False).first); rec.pump(3)
    except Exception as e: print("calc:", str(e)[:100])
    rec.pump(2)
    page.screenshot(path=str(SHOT / "video-04-site-a.png"))

def n3(page, rec):
    s = state(); page.goto(s["notebook"]); page.wait_for_timeout(4000); mask_pii(page); rec.pump(2)
    open_artifact(page, rec, "Sales & Support Dashboard")
    rec.pump(8)
    fr = page.frame_locator("iframe").first
    try:
        sel = fr.locator("select").first
        show_click(page, sel, click=False); sel.select_option(index=1, timeout=5000); rec.pump(3)
    except Exception as e: print("filter:", str(e)[:100])
    for _ in range(14): page.mouse.move(900, 700); page.mouse.wheel(0, 250); rec.pump(0.5)
    rec.pump(2)
    page.screenshot(path=str(SHOT / "video-05-dashboard.png"))

SEG = {"n1": ("https://notebook.google.com/", n1), "n2": (None, n2), "n3": (None, n3)}

if __name__ == "__main__":
    for k in sys.argv[1:]:
        url, fn = SEG[k]
        with sync_playwright() as p:
            b = p.chromium.connect_over_cdp("http://127.0.0.1:9222")
            page = open_window(b, url or "about:blank")
            page.wait_for_timeout(4000)
            rec = Recorder(page); rec.start(); rec.pump(1)
            try:
                fn(page, rec)
            except Exception as e:
                print("ERROR", k, e); page.screenshot(path=str(VID / f"{k}-error.png"))
            rec.pump(1.5)
            rec.stop(VID / f"{k}.mp4", caption=page.url.split("?")[0])
            page.close()
