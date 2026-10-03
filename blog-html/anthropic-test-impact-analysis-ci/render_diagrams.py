"""Render diagram HTML/SVG files to PNG (images/diagram-*.png).
Also runs tia_demo.py and renders its real console output as a terminal-style card.
Usage: python render_diagrams.py
"""
import html
import subprocess
import sys
from pathlib import Path
from playwright.sync_api import sync_playwright

HERE = Path(__file__).parent
DIAG = HERE / "diagrams"
IMG = HERE / "images"
IMG.mkdir(exist_ok=True)

# 1) build terminal card from REAL output of tia_demo.py
out = subprocess.run([sys.executable, str(HERE / "tia_demo.py")], capture_output=True,
                     text=True, check=True).stdout
term = f"""<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><title>tia_demo.py output</title>
<style>body{{margin:0;background:#fafafa;font-family:'Segoe UI',Arial,sans-serif}}
#canvas{{width:1200px;padding:24px;box-sizing:border-box}}
.win{{background:#263238;border-radius:12px;overflow:hidden;box-shadow:0 4px 18px rgba(0,0,0,.2)}}
.bar{{background:#37474f;padding:10px 16px;color:#cfd8dc;font-size:14px}}
.bar span{{display:inline-block;width:12px;height:12px;border-radius:50%;margin-right:6px;vertical-align:middle}}
pre{{margin:0;padding:22px 26px;color:#e0f2f1;font:15px/1.6 Consolas,'Cascadia Code',monospace;white-space:pre-wrap}}
.note{{margin-top:12px;color:#c62828;font-size:14px;font-weight:600}}</style></head><body><div id="canvas">
<div class="win"><div class="bar"><span style="background:#ef5350"></span><span style="background:#ffca28"></span>
<span style="background:#66bb6a"></span>&nbsp; PS&gt; python tia_demo.py</div><pre>{html.escape(out)}</pre></div>
<div class="note">Author's own illustration (toy data) &mdash; NOT Anthropic's code.</div></div></body></html>"""
(DIAG / "diagram-03-tia-demo-output.html").write_text(term, encoding="utf-8")

with sync_playwright() as p:
    b = p.chromium.launch(channel="chrome", headless=True)
    pg = b.new_page(viewport={"width": 1440, "height": 900}, device_scale_factor=1.5)
    for f in sorted(DIAG.glob("diagram-*.html")):
        pg.goto(f.resolve().as_uri())
        pg.wait_for_timeout(500)
        pg.locator("#canvas").screenshot(path=str(IMG / (f.stem + ".png")))
        print("rendered", f.stem + ".png")
    b.close()
