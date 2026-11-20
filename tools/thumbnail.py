"""Tạo thumbnail 1200x630 theo tiêu đề bài viết (render HTML trong Chrome demo qua CDP, chụp PNG).

  python tools/thumbnail.py "<title>" "<subtitle/kicker>" <out.png> [--bg screenshot.png] [--tags "A,B,C"]
"""
import argparse, html, base64
from pathlib import Path
from playwright.sync_api import sync_playwright

TPL = """<!doctype html><html><head><meta charset="utf-8"><style>
*{margin:0;box-sizing:border-box}body{width:1200px;height:630px;overflow:hidden;font-family:'Segoe UI',sans-serif;
background:linear-gradient(135deg,#0b3d91 0%,#1565c0 55%,#00838f 100%);color:#fff;position:relative}
.bg{position:absolute;right:-60px;top:70px;width:640px;border-radius:18px;box-shadow:0 30px 60px rgba(0,0,0,.45);transform:rotate(-4deg);opacity:.95}
.shade{position:absolute;inset:0;background:linear-gradient(90deg,rgba(9,42,110,.97) 0%,rgba(9,42,110,.9) 52%,rgba(9,42,110,0) 78%)}
.c{position:absolute;left:64px;top:56px;width:660px}
.k{display:inline-block;background:#ff6d00;padding:7px 18px;border-radius:20px;font-weight:700;font-size:20px;letter-spacing:.3px}
h1{font-size:{fs}px;line-height:1.12;font-weight:800;margin:26px 0 22px;text-shadow:0 2px 12px rgba(0,0,0,.25)}
.t{display:flex;gap:10px;flex-wrap:wrap}.t span{background:rgba(255,255,255,.16);border:1px solid rgba(255,255,255,.35);padding:6px 14px;border-radius:14px;font-size:19px}
.f{position:absolute;left:64px;bottom:40px;font-size:20px;opacity:.85;font-weight:600}
</style></head><body>{bg}<div class="shade"></div><div class="c"><span class="k">{kicker}</span><h1>{title}</h1><div class="t">{tags}</div></div>
<div class="f">Scuti AI - PhatLT</div></body></html>"""

def make(title, kicker, out, bg=None, tags="", art=None):
    bgtag = ""
    if art:
        bgtag = Path(art).read_text(encoding="utf-8")
    if bg:
        b64 = base64.b64encode(Path(bg).read_bytes()).decode()
        bgtag = f'<img class="bg" src="data:image/png;base64,{b64}">'
    fs = 50 if len(title) <= 60 else (44 if len(title) <= 90 else 40)
    page_html = (TPL.replace("{fs}", str(fs)).replace("{bg}", bgtag).replace("{kicker}", html.escape(kicker)).replace("{title}", html.escape(title))
                 .replace("{tags}", "".join(f"<span>{html.escape(t.strip())}</span>" for t in tags.split(",") if t.strip())))
    with sync_playwright() as p:
        b = p.chromium.connect_over_cdp("http://127.0.0.1:9222")
        pg = b.contexts[0].new_page()
        pg.set_viewport_size({"width": 1200, "height": 630})
        pg.set_content(page_html); pg.wait_for_timeout(500)
        pg.screenshot(path=out); pg.close()
    print("→", out)

if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("title"); ap.add_argument("kicker"); ap.add_argument("out")
    ap.add_argument("--bg"); ap.add_argument("--tags", default=""); ap.add_argument("--art")
    a = ap.parse_args(); make(a.title, a.kicker, a.out, a.bg, a.tags, a.art)
