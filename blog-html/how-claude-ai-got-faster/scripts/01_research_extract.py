"""Buoc 1: mo bai goc bang Chrome that, lay URL cuoi, tieu de, heading, full text de doi chieu (khong quay video)."""
import json, pathlib
from playwright.sync_api import sync_playwright
ROOT = pathlib.Path(__file__).resolve().parent.parent
URL = "https://claude.dev/blog/how-we-made-claude-ai-faster/"
with sync_playwright() as p:
    b = p.chromium.launch(channel="chrome", headless=False)
    pg = b.new_page(viewport={"width": 1440, "height": 900})
    resp = pg.goto(URL, wait_until="networkidle", timeout=60000)
    info = {"requested": URL, "final_url": pg.url, "status": resp.status if resp else None, "title": pg.title()}
    heads = pg.eval_on_selector_all("h1,h2,h3", "els=>els.map(e=>({tag:e.tagName,text:e.innerText.trim(),y:Math.round(e.getBoundingClientRect().top+scrollY)}))")
    imgs = pg.eval_on_selector_all("main img, article img", "els=>els.map(e=>({alt:e.alt,src:e.currentSrc,y:Math.round(e.getBoundingClientRect().top+scrollY)}))")
    info["page_height"] = pg.evaluate("document.body.scrollHeight")
    text = pg.inner_text("main") if pg.query_selector("main") else pg.inner_text("body")
    (ROOT/"sources"/"article-text.txt").write_text(text, encoding="utf-8")
    (ROOT/"sources"/"article-meta.json").write_text(json.dumps({"info":info,"headings":heads,"images":imgs}, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(info, ensure_ascii=False))
    b.close()
