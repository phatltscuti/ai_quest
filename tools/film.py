"""Phát lại file cast (termcast) trong cửa sổ Chrome riêng và quay thành mp4.

  python tools/film.py <cast.json> <out.mp4> [typeMs] [maxGapMs]
"""
import json, sys, time
from pathlib import Path
from playwright.sync_api import sync_playwright
sys.path.insert(0, str(Path(__file__).parent))
from cdp_rec import open_window, Recorder

PLAYER = (Path(__file__).parent / "term_player.html").resolve().as_uri()

def film_cast(cast_path, out, type_ms=32, max_gap=2500):
    cast = json.loads(Path(cast_path).read_text(encoding="utf-8"))
    with sync_playwright() as p:
        b = p.chromium.connect_over_cdp("http://127.0.0.1:9222")
        page = open_window(b, PLAYER)
        page.wait_for_function("typeof window.play === 'function'")
        page.wait_for_timeout(800)
        rec = Recorder(page); rec.start()
        rec.pump(0.8)
        page.evaluate("([c, o]) => { window.play(c, o); }", [cast, {"typeMs": type_ms, "maxGap": max_gap}])
        while not page.evaluate("window.__done"):
            rec.pump(0.5)
        rec.stop(out)
        page.close()

if __name__ == "__main__":
    a = sys.argv
    film_cast(a[1], a[2], int(a[3]) if len(a) > 3 else 32, int(a[4]) if len(a) > 4 else 2500)
