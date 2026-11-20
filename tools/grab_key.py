"""Doc Gemini API key tu dialog 'API key details' dang mo tren AI Studio -> ghi .env. Chi in ra dang da che."""
import re
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b = p.chromium.connect_over_cdp("http://127.0.0.1:9222")
    pg = next(pg for c in b.contexts for pg in c.pages if "aistudio.google.com/api-keys" in pg.url)
    t = pg.query_selector(".cdk-overlay-container").inner_text()
    m = re.search(r"\b(AQ\.[A-Za-z0-9_\-\.]{20,}|AIza[0-9A-Za-z_\-]{35})", t)
    pg.get_by_role("button", name="close").first.click()
    if not m: raise SystemExit("NOT_FOUND")
    k = m.group(1)
    open(".env", "w").write(f"GEMINI_API_KEY={k}\n")
    print("saved", k[:3] + "****" + k[-4:], "len", len(k))
