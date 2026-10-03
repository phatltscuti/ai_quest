"""Buoc 2: render cac so do HTML/SVG trong diagrams/ thanh PNG (VI + EN) vao images/."""
import pathlib
from playwright.sync_api import sync_playwright
ROOT = pathlib.Path(__file__).resolve().parent.parent
NAMES = ["diagram-01-optimization-map", "diagram-02-before-after-p75",
         "diagram-03-static-shell-concept", "diagram-04-scuti-perf-loop"]
with sync_playwright() as p:
    b = p.chromium.launch(channel="chrome", headless=True)
    pg = b.new_page(viewport={"width": 1480, "height": 900}, device_scale_factor=1.5)
    for n in NAMES:
        for lang in ("vi", "en"):
            url = (ROOT / "diagrams" / f"{n}.html").as_uri() + ("#en" if lang == "en" else "")
            pg.goto("about:blank"); pg.goto(url); pg.wait_for_timeout(400)
            out = ROOT / "images" / f"{n}{'-en' if lang == 'en' else ''}.png"
            pg.locator("#canvas").screenshot(path=str(out))
            print("saved", out.name)
    b.close()
