"""Chay 'gwscli auth login ...', mo URL dang nhap trong Chrome demo (CDP), quay man hinh consent, bam Allow."""
import re, subprocess, sys, threading, time, os
from pathlib import Path
HERE = Path(__file__).resolve().parent; ROOT = HERE.parents[2]
sys.path.insert(0, str(ROOT / "tools"))
GW = str(Path.home() / "bin" / "gwscli.exe")
p = subprocess.Popen([GW, "auth", "login", *sys.argv[1:]], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.DEVNULL)
url = None; buf = []
def rd():
    global url
    for line in iter(p.stdout.readline, b""):
        s = line.decode("utf-8", "replace"); buf.append(s)
        m = re.search(r"https://accounts\.google\.com/\S+", s)
        if m and not url: url = m.group(0); print("[Open this URL in your browser to sign in]", flush=True)
        else: print(s, end="", flush=True)
threading.Thread(target=rd, daemon=True).start()
while url is None and p.poll() is None: time.sleep(0.2)
if url:
    from playwright.sync_api import sync_playwright
    from cdp_rec import open_window, Recorder, show_click, mask_pii
    with sync_playwright() as pw:
        b = pw.chromium.connect_over_cdp("http://127.0.0.1:9222")
        pg = open_window(b, "about:blank"); pg.bring_to_front()
        pg.goto(url); pg.wait_for_timeout(2500)
        rec = Recorder(pg); rec.start(); rec.pump(1.5)
        try:
            for i in range(25):
                if pg.url.split("/")[2].split(":")[0] in ("127.0.0.1", "localhost"): break
                mask_pii(pg)
                acc = pg.locator("[data-identifier]").first
                if acc.count() and acc.is_visible(): show_click(pg, acc); rec.pump(3); continue
                sel = pg.get_by_role("checkbox", name=re.compile("Select all", re.I)).first
                if sel.count() and sel.is_visible() and not sel.is_checked(): show_click(pg, sel); rec.pump(1)
                btn = pg.get_by_role("button", name=re.compile(r"^(Continue|Allow|Tiếp tục|Cho phép)$", re.I)).last
                if btn.count() and btn.is_visible() and btn.is_enabled():
                    pg.screenshot(path=str(HERE.parent / "images" / f"step-04-consent-{i}.png")); show_click(pg, btn); rec.pump(3)
                else: rec.pump(2)
            rec.pump(2)
            pg.screenshot(path=str(HERE.parent / "images" / "step-05-login-done.png"))
        finally:
            rec.stop(str(HERE.parent / "videos" / f"s3-consent-{int(time.time())}-raw.mp4"), caption="accounts.google.com - gwscli sign-in")
            pg.close()
p.wait(timeout=120); time.sleep(0.5)
sys.exit(p.returncode)
