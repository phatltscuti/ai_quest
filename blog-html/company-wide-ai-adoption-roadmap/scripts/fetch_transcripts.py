# Fetch speakerdeck pages and extract transcript text (slide-by-slide)
import urllib.request, re, html, json, sys
sys.stdout.reconfigure(encoding="utf-8")
URLS = {
 "lmi": "https://speakerdeck.com/lmi/pek2026-link-and-motivation",
 "smarthr": "https://speakerdeck.com/yoshikikonishi_/smarthr-no-zensha-ai-suishin-ha-dou-hajimata-ka",
}
for k, u in URLS.items():
    req = urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0"})
    h = urllib.request.urlopen(req, timeout=30).read().decode("utf-8", "ignore")
    open(f"scripts/{k}.html", "w", encoding="utf-8").write(h)
    t = re.search(r"<title>(.*?)</title>", h, re.S)
    print("=====", k, t.group(1).strip() if t else "")
    m = re.search(r'<div class="deck-transcript.*?</div>\s*</div>', h, re.S) or re.search(r'id="transcript".*', h, re.S)
    body = m.group(0) if m else h
    items = re.findall(r'<li[^>]*>(.*?)</li>', body, re.S)
    out = []
    for i, it in enumerate(items, 1):
        txt = html.unescape(re.sub(r"<[^>]+>", " ", it))
        txt = re.sub(r"\s+", " ", txt).strip()
        if txt: out.append(f"[{i}] {txt}")
    open(f"scripts/{k}_transcript.txt", "w", encoding="utf-8").write("\n".join(out))
    print(len(out), "items")
