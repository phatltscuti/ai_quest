"""Chuyển blog HTML (bản EN) -> Gutenberg blocks, upload ảnh/video, tạo bài DRAFT trên scuti.asia.

Dùng phiên đăng nhập WordPress đang có trong Chrome demo (CDP 9222): lấy cookie + REST nonce, gọi /wp-json/wp/v2.

  python tools/wp_post.py <blog-en.html> --cats 31,136,50 --tags 33,75,51 [--video videos/full-demo.mp4] [--featured images/x.png] [--post-id N]
"""
import argparse, html, json, mimetypes, re, sys
from pathlib import Path
import truststore; truststore.inject_into_ssl()
import requests
from bs4 import BeautifulSoup, Comment, NavigableString, Tag
from playwright.sync_api import sync_playwright

SITE = "https://scuti.asia"

def wp_session():
    p = sync_playwright().start()
    b = p.chromium.connect_over_cdp("http://127.0.0.1:9222")
    s = requests.Session()
    for c in b.contexts[0].cookies(SITE): s.cookies.set(c["name"], c["value"], domain=c["domain"], path=c["path"])
    p.stop()
    s.headers.update({"User-Agent": "Mozilla/5.0"})
    nonce = s.get(f"{SITE}/wp-admin/admin-ajax.php?action=rest-nonce", timeout=30).text.strip()
    if not nonce or nonce == "0": sys.exit("Chưa đăng nhập WordPress trong Chrome demo")
    s.headers["X-WP-Nonce"] = nonce
    return s

def upload(s, path, cache):
    path = Path(path)
    if str(path) in cache: return cache[str(path)]
    mime = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
    r = s.post(f"{SITE}/wp-json/wp/v2/media", data=path.read_bytes(),
               headers={"Content-Type": mime, "Content-Disposition": f'attachment; filename="{path.name}"'}, timeout=600)
    r.raise_for_status(); j = r.json()
    cache[str(path)] = (j["id"], j["source_url"]); print("  uploaded", path.name, "->", j["source_url"])
    return cache[str(path)]

def inner(el):
    return "".join(str(c) for c in el.contents).strip()

def blk(name, body, attrs=None):
    a = (" " + json.dumps(attrs, ensure_ascii=False)) if attrs else ""
    return f"<!-- wp:{name}{a} -->\n{body}\n<!-- /wp:{name} -->"

def convert(el, base, s, cache, out):
    if isinstance(el, Comment):
        if "VIDEO" in el: out.append("<!-- VIDEO -->")
        return
    if isinstance(el, NavigableString):
        t = str(el).strip()
        if t: out.append(blk("paragraph", f"<p>{html.escape(t)}</p>"))
        return
    if not isinstance(el, Tag) or el.name in ("script", "style", "nav"): return
    cls = el.get("class", [])
    if el.name in ("h2", "h3", "h4"):
        lvl = int(el.name[1]); a = {"level": lvl} if lvl != 2 else None
        out.append(blk("heading", f'<{el.name} class="wp-block-heading">{inner(el)}</{el.name}>', a))
    elif el.name == "p":
        if el.get_text(strip=True) or el.find("img"):
            if el.find("img") and not el.get_text(strip=True):
                for im in el.find_all("img"): convert(im, base, s, cache, out)
            else:
                out.append(blk("paragraph", f"<p>{inner(el)}</p>"))
    elif el.name in ("ul", "ol"):
        items = "".join(blk("list-item", f"<li>{inner(li)}</li>") for li in el.find_all("li", recursive=False))
        a = {"ordered": True} if el.name == "ol" else None
        out.append(blk("list", f'<{el.name} class="wp-block-list">{items}</{el.name}>', a))
    elif el.name == "table":
        for x in el.find_all(True):
            for k in list(x.attrs):
                if k not in ("colspan", "rowspan"): del x[k]
        out.append(blk("table", f'<figure class="wp-block-table"><table class="has-fixed-layout">{inner(el)}</table></figure>'))
    elif el.name == "img":
        src = el.get("src", "")
        if src.startswith("http"): url, mid = src, None
        else: mid, url = upload(s, (base / src).resolve(), cache)
        alt = html.escape(el.get("alt", ""))
        a = {"sizeSlug": "full", "linkDestination": "none", "align": "center"}
        if mid: a["id"] = mid
        cap = ""
        fig = el.find_parent("figure") or el.find_parent(class_="screenshot-wrap")
        if fig and fig.find(["figcaption", "p", "div"], class_=re.compile("caption")):
            cap = f'<figcaption class="wp-element-caption">{inner(fig.find(["figcaption","p","div"], class_=re.compile("caption")))}</figcaption>'
        elif fig and fig.find("figcaption"):
            cap = f'<figcaption class="wp-element-caption">{inner(fig.find("figcaption"))}</figcaption>'
        out.append(blk("image", f'<figure class="wp-block-image aligncenter size-full"><img src="{url}" alt="{alt}"'
                       + (f' class="wp-image-{mid}"' if mid else "") + f"/>{cap}</figure>", a))
    elif el.name == "video" or (el.name == "source" and el.parent.name != "video"):
        src = el.get("src") or (el.find("source") or {}).get("src")
        if src:
            mid, url = upload(s, (base / src).resolve(), cache)
            out.append(blk("video", f'<figure class="wp-block-video"><video controls src="{url}"></video></figure>', {"id": mid}))
    elif el.name == "pre" or "prompt-box" in cls or "code-block" in cls:
        for lab in el.select(".label"): lab.decompose()
        out.append(blk("preformatted", f'<pre class="wp-block-preformatted">{html.escape(el.get_text())}</pre>'))
    elif el.name in ("figure",) or "screenshot-wrap" in cls:
        for im in el.find_all("img"): convert(im, base, s, cache, out)
        if el.find("video"): convert(el.find("video"), base, s, cache, out)
    elif el.name == "blockquote":
        out.append(blk("quote", f'<blockquote class="wp-block-quote">{blk("paragraph", "<p>" + el.get_text(" ", strip=True) + "</p>")}</blockquote>'))
    elif el.name in ("strong", "em", "a", "span", "code", "b", "i"):
        out.append(blk("paragraph", f"<p>{str(el)}</p>"))
    else:  # div/section/card...: duyệt con
        for c in el.children: convert(c, base, s, cache, out)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("html"); ap.add_argument("--cats", default=""); ap.add_argument("--tags", default="")
    ap.add_argument("--video"); ap.add_argument("--featured"); ap.add_argument("--post-id", type=int); ap.add_argument("--title")
    a = ap.parse_args()
    src = Path(a.html).resolve(); base = src.parent
    soup = BeautifulSoup(src.read_text(encoding="utf-8"), "html.parser")
    title = a.title or (soup.select_one(".hero h1") or soup.title).get_text(strip=True)
    sub = soup.select_one(".hero .subtitle")
    s = wp_session(); cache = {}
    out = []
    if sub: out.append(blk("paragraph", f"<p><em>{inner(sub)}</em></p>"))
    container = soup.select_one(".container") or soup.body
    for c in container.children:
        if isinstance(c, Tag) and (c.name == "nav" or "toc" in c.get("class", [])): continue
        convert(c, base, s, cache, out)
    content = "\n\n".join(out)
    if a.video:  # thay placeholder <!-- VIDEO --> hoặc chèn sau đoạn mở đầu
        mid, url = upload(s, (Path(a.video)).resolve(), cache)
        vb = blk("video", f'<figure class="wp-block-video"><video controls src="{url}"></video></figure>', {"id": mid})
        if "<!-- VIDEO -->" in content: content = content.replace("<!-- VIDEO -->", vb)
        else: content = content.replace("\n\n", "\n\n" + vb + "\n\n", 2) if len(out) > 2 else vb + "\n\n" + content
    content = content.replace("<!-- VIDEO -->", "")
    data = {"title": title, "content": content, "status": "draft"}
    if a.cats: data["categories"] = [int(x) for x in a.cats.split(",")]
    if a.tags: data["tags"] = [int(x) for x in a.tags.split(",")]
    if a.featured: data["featured_media"] = upload(s, Path(a.featured).resolve(), cache)[0]
    url = f"{SITE}/wp-json/wp/v2/posts" + (f"/{a.post_id}" if a.post_id else "")
    r = s.post(url, json=data, timeout=120); r.raise_for_status(); j = r.json()
    print(f"DRAFT id={j['id']} status={j['status']}\n  edit: {SITE}/wp-admin/post.php?post={j['id']}&action=edit\n  preview: {j['link']}")

if __name__ == "__main__":
    main()
