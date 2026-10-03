from pathlib import Path
from playwright.sync_api import sync_playwright
ROOT = Path(r"D:\ai_quest\blog-html\arxiv-2609-19656-paper-summary")
URL = "https://arxiv.org/html/2609.19656v1"
OUT = {"Table 1": "step-06-table1-full.png", "Table 3": "step-07-table3-full.png"}
with sync_playwright() as p:
    b = p.chromium.launch(channel="chrome", headless=True)
    pg = b.new_page(viewport={"width": 1600, "height": 2400}, device_scale_factor=2)
    pg.goto(URL, wait_until="networkidle", timeout=90000)
    # hide fixed/sticky overlays (arXiv header, nav buttons)
    pg.evaluate("""() => { for (const e of document.querySelectorAll('body *')) {
        const s = getComputedStyle(e);
        if (s.position === 'fixed' || s.position === 'sticky') e.style.display = 'none'; } }""")
    for label, fn in OUT.items():
        fig = pg.locator("figure.ltx_table").filter(
            has=pg.locator("figcaption", has_text=label + ":")).first
        fig.evaluate("""f => { f.style.width = 'max-content'; f.style.maxWidth = 'none';
            f.style.overflow = 'visible'; f.style.background = '#fff'; f.style.padding = '12px 16px';
            for (const e of f.querySelectorAll('*')) { e.style.overflow = 'visible'; e.style.maxWidth = 'none'; }
            const cap = f.querySelector('figcaption'); const t = f.querySelector('table');
            if (cap && t) cap.style.maxWidth = t.getBoundingClientRect().width + 'px'; }""")
        fig.scroll_into_view_if_needed()
        print(label, fig.bounding_box(), fig.evaluate("e => [e.scrollWidth, e.clientWidth]"))
        fig.screenshot(path=str(ROOT / "images" / fn))
    b.close()
