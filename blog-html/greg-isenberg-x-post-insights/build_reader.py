"""Build a local, readable HTML view of Greg Isenberg's X Article.

Input : sources/fxtwitter-api.json  (downloaded from https://api.fxtwitter.com/gregisenberg/status/2103927365977928019)
Output: sources/article-reader.html  (text + original article images, rendered verbatim from the API JSON)

Purpose: X shows a login wall for Articles, so this page lets the Playwright session
show the real article content (unchanged) for screenshots and the demo video.
"""
import html
import json
from pathlib import Path

ROOT = Path(__file__).parent
data = json.loads((ROOT / "sources" / "fxtwitter-api.json").read_text(encoding="utf-8"))
tw = data["tweet"]
art = tw["article"]

parts = []
img_i = 0
list_open = None
for b in art["content"]["blocks"]:
    t, txt = b["type"], html.escape(b["text"])
    # bold ranges (only offset 0 used in this article) -> keep simple
    for r in b.get("inlineStyleRanges", []):
        if r.get("style") == "Bold" and r["offset"] == 0:
            raw = b["text"]
            txt = "<b>" + html.escape(raw[: r["length"]]) + "</b>" + html.escape(raw[r["length"]:])
    if t == "atomic":
        parts.append(
            f'<figure id="img-{img_i}"><img src="article-img-{img_i}.jpg" alt="Article image {img_i}">'
            f"<figcaption>Original article image #{img_i} (pbs.twimg.com)</figcaption></figure>"
        )
        img_i += 1
    elif t == "header-two":
        parts.append(f"<h2>{txt}</h2>")
    elif t == "blockquote":
        parts.append(f"<blockquote>{txt}</blockquote>")
    elif txt.strip():
        parts.append(f"<p>{txt}</p>")

a = tw["author"]
page = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<title>Reader view – {html.escape(art['title'])}</title>
<style>
body{{margin:0;background:#f4f6f8;font-family:'Segoe UI',Arial,sans-serif;color:#0f1419}}
.bar{{background:#0f1419;color:#e7e9ea;padding:10px 24px;font-size:13px}}
.bar code{{color:#1d9bf0}}
.wrap{{max-width:760px;margin:24px auto;background:#fff;border:1px solid #e1e8ed;border-radius:16px;padding:28px 36px}}
.author{{display:flex;gap:12px;align-items:center}}
.author img{{width:48px;height:48px;border-radius:50%}}
.meta{{color:#536471;font-size:14px}}
.cover{{width:100%;border-radius:12px;margin:16px 0}}
h1{{font-size:30px;margin:10px 0}}
h2{{font-size:22px;margin-top:30px}}
p{{font-size:17px;line-height:1.6;white-space:pre-line}}
blockquote{{background:#f7f9f9;border-left:4px solid #1d9bf0;margin:14px 0;padding:12px 16px;font-family:Consolas,monospace;font-size:14px;line-height:1.55}}
figure{{margin:18px 0;text-align:center}} figure img{{max-width:100%;border-radius:10px;border:1px solid #e1e8ed}}
figcaption{{font-size:12px;color:#536471}}
.stats{{display:flex;gap:18px;flex-wrap:wrap;color:#536471;font-size:14px;border-top:1px solid #eff3f4;border-bottom:1px solid #eff3f4;padding:10px 0;margin:12px 0}}
</style></head><body>
<div class="bar">Reader view generated locally from <code>api.fxtwitter.com/gregisenberg/status/{tw['id']}</code> (public mirror) &middot; original: <code>{html.escape(tw['url'])}</code> &middot; text unchanged</div>
<div class="wrap">
<div class="author"><img src="{html.escape(a['avatar_url'])}" alt=""><div><b>{html.escape(a['name'])}</b> &#10004;<br><span class="meta">@{a['screen_name']} &middot; {html.escape(tw['created_at'])}</span></div></div>
<img class="cover" src="article-cover.jpg" alt="cover">
<h1>{html.escape(art['title'])}</h1>
<div class="stats"><span>{tw['views']:,} views</span><span>{tw['likes']:,} likes</span><span>{tw['retweets']:,} reposts</span><span>{tw['replies']:,} replies</span><span>{tw['bookmarks']:,} bookmarks</span></div>
{''.join(parts)}
</div></body></html>"""
(ROOT / "sources" / "article-reader.html").write_text(page, encoding="utf-8")
print("written", img_i, "images")
