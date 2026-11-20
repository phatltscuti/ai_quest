"""Sửa nội dung post: <code>/<kbd> inline -> <strong> (theme làm chữ code bị ẩn). Usage: wp_fix.py <post_id>"""
import re, sys
sys.path.insert(0, __file__.rsplit("\\", 1)[0] if "\\" in __file__ else ".")
from wp_post import wp_session, SITE
pid = sys.argv[1]; s = wp_session()
raw = s.get(f"{SITE}/wp-json/wp/v2/posts/{pid}?context=edit").json()["content"]["raw"]
parts = re.split(r"(<pre[\s\S]*?</pre>)", raw)
for i in range(0, len(parts), 2):
    parts[i] = re.sub(r"<(code|kbd)>([\s\S]*?)</\1>", r"<strong>\2</strong>", parts[i])
new = "".join(parts)
r = s.post(f"{SITE}/wp-json/wp/v2/posts/{pid}", json={"content": new}); r.raise_for_status()
print("updated", pid, "changes:", raw.count("<code>") + raw.count("<kbd>"), "->", new.count("<code>") + new.count("<kbd>"))
