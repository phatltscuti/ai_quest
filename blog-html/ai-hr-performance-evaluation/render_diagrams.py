"""Render the HTML/SVG diagrams in diagrams/ to PNG (VI + EN) into images/."""
import time
from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).parent
DIAGRAMS = ["diagram-01-data-flow", "diagram-02-scuti-rollout"]

with sync_playwright() as p:
    b = p.chromium.launch(channel="chrome", headless=False)
    pg = b.new_context(viewport={"width": 1440, "height": 900}, device_scale_factor=1.5).new_page()
    for name in DIAGRAMS:
        src = ROOT / "diagrams" / f"{name}.html"
        if not src.exists():
            continue
        for lang in ("vi", "en"):
            pg.goto(src.as_uri() + f"?lang={lang}")
            time.sleep(0.8)
            out = ROOT / "images" / (f"{name}.png" if lang == "vi" else f"{name}-en.png")
            pg.locator("#canvas").screenshot(path=str(out))
            print("saved", out.name)
    b.close()
