"""Upload video và chèn vào post (thay đoạn placeholder nhắc tới full-demo.mp4, hoặc sau heading 'Demo video'). Usage: wp_video.py <post_id> <video.mp4>"""
import re, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from wp_post import wp_session, upload, blk, SITE
pid, vid = sys.argv[1], sys.argv[2]
s = wp_session()
mid, url = upload(s, Path(vid).resolve(), {})
vb = blk("video", f'<figure class="wp-block-video"><video controls src="{url}"></video></figure>', {"id": mid})
raw = s.get(f"{SITE}/wp-json/wp/v2/posts/{pid}?context=edit").json()["content"]["raw"]
pat = re.compile(r"<!-- wp:paragraph -->\s*<p>[^\n]*full-demo\.mp4[\s\S]*?<!-- /wp:paragraph -->")
if pat.search(raw): new = pat.sub(lambda m: vb, raw, count=1); how = "replaced placeholder"
else:
    m = re.search(r"(<!-- wp:heading[^>]*-->\s*<h\d[^>]*>[^<]*(?:Demo video|Video)[^<]*</h\d>\s*<!-- /wp:heading -->)", raw)
    new = raw.replace(m.group(1), m.group(1) + "\n\n" + vb, 1) if m else vb + "\n\n" + raw; how = "inserted"
r = s.post(f"{SITE}/wp-json/wp/v2/posts/{pid}", json={"content": new}); r.raise_for_status()
print(how, "->", url)
