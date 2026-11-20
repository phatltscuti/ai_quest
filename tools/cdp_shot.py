"""Chup man hinh tab Chrome (qua CDP 9222) co URL chua tu khoa. Usage: cdp_shot.py <url-substring> <out.png>"""
import sys
from playwright.sync_api import sync_playwright
key, out = sys.argv[1], sys.argv[2]
with sync_playwright() as p:
    b = p.chromium.connect_over_cdp("http://127.0.0.1:9222")
    pages = [pg for c in b.contexts for pg in c.pages]
    pg = next(pg for pg in pages if key in pg.url)
    pg.bring_to_front()
    pg.wait_for_timeout(1500)
    pg.screenshot(path=out)
    print(pg.url, "|", pg.title())
