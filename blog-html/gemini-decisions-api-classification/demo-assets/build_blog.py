"""Ghép blog Quest 3: <head>/CSS lấy từ blog Quest 5 + body-<lang>.html, điền số liệu từ results/summary.json.
  python build_blog.py en   -> ../gemini-decisions-api-classification-blog-en.html
  python build_blog.py vi   -> ../gemini-decisions-api-classification-blog.html
"""
import json, re, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent; Q3 = HERE.parent
lang = sys.argv[1] if len(sys.argv) > 1 else "en"
S = json.loads((HERE / "results" / "summary.json").read_text(encoding="utf-8"))
ref = (Q3.parent / "gemini-notebook-interactive-sites" / "gemini-notebook-interactive-sites-blog-en.html").read_text(encoding="utf-8")
head = ref[: ref.index("<body>") + len("<body>")]
title = "Gemini Decisions API vs Traditional Text Generation" if lang == "en" else "Gemini Decisions API vs Text-gen truyền thống"
head = re.sub(r"<title>.*?</title>", f"<title>{title}</title>", head, flags=re.S).replace('lang="en"', f'lang="{lang}"')
body = (Q3 / f"body-{lang}.html").read_text(encoding="utf-8")

def fmt_ms(v): return f"{v / 1000:.2f} s" if v >= 1000 else f"{v:.0f} ms"
vals = {}
for m, s in S.items():
    vals[f"{m}.acc"] = f"{s['acc']:.1%}"
    vals[f"{m}.sign"] = f"{s['sign_acc']:.1%}"
    vals[f"{m}.stab"] = f"{s['consistency']:.0%}"
    vals[f"{m}.p50"] = fmt_ms(s["p50"]); vals[f"{m}.p95"] = fmt_ms(s["p95"])
    vals[f"{m}.tok"] = f"{s['in_tok']:,.0f} / {s['out_tok']:.0f}"
    vals[f"{m}.cost"] = f"${s['cost_1k']:.3f}"
vals["speedup"] = f"{S['flash-lite']['p50'] / S['decision']['p50']:.0f}"
vals["costx"] = f"{S['flash-lite']['cost_1k'] / S['decision']['cost_1k']:.1f}"
vals["costx_low"] = f"{S['flash-lite']['cost_1k'] / S['decision-low']['cost_1k']:.1f}"
body = re.sub(r"%%([\w.-]+)%%", lambda m: vals[m.group(1)], body)
out = Q3 / ("gemini-decisions-api-classification-blog-en.html" if lang == "en" else "gemini-decisions-api-classification-blog.html")
out.write_text(head + "\n" + body + "\n</body>\n</html>\n", encoding="utf-8")
print("→", out); print({k: v for k, v in vals.items() if "." not in k or k.endswith((".acc", ".sign", ".p50", ".cost"))})
