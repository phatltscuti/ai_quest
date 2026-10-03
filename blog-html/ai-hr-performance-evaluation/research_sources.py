"""Research script: extract full text of the note.com article and the YouTube transcript
(via the "Show transcript" panel) into sources/. Not recorded."""
import json, time
from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).parent
SRC = ROOT / "sources"
SRC.mkdir(exist_ok=True)
NOTE = "https://note.com/hashiyaman/n/na03108694c97"
YT = "https://www.youtube.com/watch?v=X52tm3MsSjA"

with sync_playwright() as p:
    b = p.chromium.launch(channel="chrome", headless=False)
    ctx = b.new_context(viewport={"width": 1440, "height": 900}, locale="ja-JP")
    page = ctx.new_page()

    page.goto(NOTE, wait_until="domcontentloaded")
    time.sleep(5)
    txt = page.evaluate("() => (document.querySelector('.note-common-styles__textnote-body') || document.querySelector('article') || document.body).innerText")
    (SRC / "note-article.txt").write_text(page.title() + "\n\n" + txt, encoding="utf-8")
    print("note chars", len(txt))

    page.goto(YT, wait_until="domcontentloaded")
    time.sleep(6)
    for sel in ["button:has-text('Reject all')", "button:has-text('すべて拒否')", "button:has-text('Accept all')"]:
        try:
            page.locator(sel).first.click(timeout=1500); time.sleep(2); break
        except Exception:
            pass
    try:
        page.locator("#description-inline-expander, #expand").first.click(timeout=4000)
        time.sleep(1.5)
    except Exception as e:
        print("expand fail", e)
    clicked = False
    for sel in ["ytd-video-description-transcript-section-renderer button",
                "button[aria-label*='transcript' i]", "button:has-text('文字起こし')", "button:has-text('Show transcript')"]:
        try:
            page.locator(sel).first.click(timeout=4000); clicked = True; break
        except Exception:
            pass
    print("transcript clicked", clicked)
    time.sleep(6)
    segs = page.evaluate("""() => Array.from(document.querySelectorAll('ytd-transcript-segment-renderer')).map(e => {
        const t = e.querySelector('.segment-timestamp'); const s = e.querySelector('.segment-text');
        return (t?t.innerText.trim():'') + '\\t' + (s?s.innerText.trim():''); })""")
    if not segs:
        segs = page.evaluate("""() => Array.from(document.querySelectorAll('transcript-segment-view-model, [class*=transcript] [class*=segment]')).map(e => e.innerText.replace(/\\n/g,' ').trim())""")
    (SRC / "yt-transcript.txt").write_text("\n".join(segs), encoding="utf-8")
    print("segments", len(segs))
    desc = page.evaluate("() => (document.querySelector('#description-inline-expander')||{}).innerText || ''")
    (SRC / "yt-description.txt").write_text(page.title() + "\n\n" + desc, encoding="utf-8")
    b.close()
