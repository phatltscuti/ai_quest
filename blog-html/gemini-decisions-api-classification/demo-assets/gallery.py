"""Tạo dataset/gallery.html để xem nhanh 40 tài liệu mẫu + nhãn (dùng khi quay video)."""
import csv, subprocess
from pathlib import Path
D = Path(__file__).parent / "dataset"
rows = list(csv.DictReader(open(D / "labels.csv", encoding="utf-8")))
cards = []
for r in rows:
    f = r["file"]
    if f.endswith(".pdf"):
        thumb = f'<embed src="{f}#toolbar=0&view=FitH" type="application/pdf">'
    else:
        thumb = f'<img src="{f}" loading="lazy">'
    cards.append(f'<div class="c">{thumb}<div class="m"><b>{f}</b><span>{r["doc_type"]}</span>'
                 f'<span class="d {r["difficulty"]}">{r["difficulty"]}</span><span>{r["lang"]}</span>'
                 f'<span>{"✍ signed" if r["has_signature"] == "1" else "unsigned"}</span></div></div>')
html = """<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Dataset – 40 sample documents</title><style>
body{font-family:Segoe UI,sans-serif;background:#f4f5f7;margin:0;padding:24px;color:#0b0b0b}
h1{margin:0 0 4px;font-size:26px} p{margin:0 0 18px;color:#52514e}
.g{display:grid;grid-template-columns:repeat(8,1fr);gap:14px}
.c{background:#fff;border:1px solid #e4e3df;border-radius:10px;overflow:hidden}
.c img,.c embed{width:100%;aspect-ratio:900/1273;object-fit:cover;display:block;border-bottom:1px solid #eee}
.m{padding:6px 8px;font-size:12px;display:flex;flex-wrap:wrap;gap:4px}.m b{width:100%}
.m span{background:#eef2f8;border-radius:8px;padding:1px 7px}.d.photo,.d.lowres,.d.notitle{background:#fff1e6;color:#b34700}
</style></head><body><h1>Dataset: 40 synthetic documents (8 types × 5)</h1>
<p>Vietnamese / English / Japanese · 24 hard samples (missing title, skewed blurry photo, low resolution) · 8 PDFs · fictional data</p>
<div class="g">""" + "".join(cards) + "</div></body></html>"
(D / "gallery.html").write_text(html, encoding="utf-8")
print("→", D / "gallery.html")
