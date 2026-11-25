"""Quay buoc 2: dat ten OAuth client, tick 'AI-powered agent', Continue, tai client secret JSON (che secret)."""
import re
import sys
from pathlib import Path
HERE = Path(__file__).resolve().parent; ROOT = HERE.parents[2]
sys.path.insert(0, str(ROOT / "tools"))
from playwright.sync_api import sync_playwright
from cdp_rec import Recorder, show_click, mask_pii
SECRET_JS = r"""(() => { if (window.__m2) return; window.__m2 = true;
 const re = /GOCSPX-[\w-]+|\d{6,}-[\w]+\.apps\.googleusercontent\.com/g;
 const fix = r => { const w = document.createTreeWalker(r, NodeFilter.SHOW_TEXT); let n; while ((n = w.nextNode())) { if (re.test(n.nodeValue)) n.nodeValue = n.nodeValue.replace(re, '••••••••••••'); re.lastIndex = 0; } };
 fix(document.body); setInterval(() => fix(document.body), 100);
 document.querySelectorAll('input').forEach(i => { if (/GOCSPX|googleusercontent/.test(i.value)) i.style.filter = 'blur(8px)'; }); })()"""
SP = Path(sys.argv[1]); SECRET_DIR = ROOT / ".secrets"; SECRET_DIR.mkdir(exist_ok=True)
def m(pg): mask_pii(pg); pg.evaluate(SECRET_JS)
with sync_playwright() as p:
    b = p.chromium.connect_over_cdp("http://127.0.0.1:9222")
    pg = [x for c in b.contexts for x in c.pages if "auth/overview/personal" in x.url and "rapt=" not in x.url][0]
    pg.bring_to_front(); pg.wait_for_timeout(800); m(pg)
    rec = Recorder(pg); rec.start(); rec.pump(1.5)
    try:
        name = pg.get_by_role("textbox", name=re.compile(r"^Name"))
        show_click(pg, name); name.fill(""); name.press_sequentially("gwscli-mcp-agent", delay=60); rec.pump(1)
        for i in (0, 1):
            cb = pg.locator("input[type=checkbox]").nth(i)
            show_click(pg, cb); rec.pump(0.8)
            if not cb.is_checked(): cb.check(force=True); rec.pump(0.5)
        pg.screenshot(path=str(HERE.parent / "images" / "step-02-oauth-client-agent.png"))
        show_click(pg, pg.get_by_role("button", name="Continue")); rec.pump(2)
        rec.fast(6)
        for i in range(120):
            m(pg); t = pg.inner_text("body")
            if re.search(r"Download JSON|Download", t) and ("Client ID" in t or "created" in t.lower()): break
            rec.pump(2)
        rec.normal(); m(pg); rec.pump(2)
        pg.screenshot(path=str(HERE.parent / "images" / "step-03-client-created.png"))
        btn = pg.get_by_role("button", name=re.compile("Download", re.I)).first
        if btn.count():
            with pg.expect_download(timeout=30000) as d:
                show_click(pg, btn)
            d.value.save_as(str(SECRET_DIR / "gwscli_client_secret.json")); print("saved client json")
        rec.pump(2)
    finally:
        m(pg)
        (SP / "c2.txt").write_text(pg.url + "\n" + pg.inner_text("body"), encoding="utf-8")
        pg.screenshot(path=str(SP / "c2.png"))
        rec.stop(str(HERE.parent / "videos" / "s2-client-raw.mp4"), caption="console.cloud.google.com/auth/overview/personal")
