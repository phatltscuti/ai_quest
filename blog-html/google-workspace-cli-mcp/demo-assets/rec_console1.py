"""Quay buoc 1: Personal mode onboarding -> tao project + OAuth client (Desktop, agent)."""
import sys, time
from pathlib import Path
HERE = Path(__file__).resolve().parent; ROOT = HERE.parents[2]
sys.path.insert(0, str(ROOT / "tools"))
from playwright.sync_api import sync_playwright
from cdp_rec import open_window, Recorder, show_click, mask_pii
URL = "https://console.cloud.google.com/auth/overview/personal?apis=ws,wsmcp,tasksmcp&clientType=desktop&isAgent=true"
SP = Path(sys.argv[1])
with sync_playwright() as p:
    b = p.chromium.connect_over_cdp("http://127.0.0.1:9222")
    pg = open_window(b, URL)
    pg.wait_for_selector("text=Personal mode onboarding", timeout=60000); pg.wait_for_timeout(3000)
    rec = Recorder(pg); rec.start(); rec.pump(2)
    try:
        name = pg.get_by_label("Project name")
        show_click(pg, name); name.fill(""); name.press_sequentially("ai-quest-gwscli-demo", delay=60); rec.pump(1.5)
        pg.screenshot(path=str(HERE.parent / "images" / "step-01-personal-mode-project.png"))
        show_click(pg, pg.get_by_role("button", name="Create", exact=True)); rec.pump(3)
        rec.fast(8)
        for i in range(90):
            mask_pii(pg)
            t = pg.inner_text("body")
            if "Download" in t or "Client ID" in t or "client secret" in t.lower(): break
            rec.pump(2)
        rec.normal(); rec.pump(3)
    finally:
        (SP / "c1.txt").write_text(pg.url + "\n" + pg.inner_text("body"), encoding="utf-8")
        pg.screenshot(path=str(SP / "c1.png"))
        rec.stop(str(HERE.parent / "videos" / "s1-console-raw.mp4"), caption="console.cloud.google.com/auth/overview/personal")
