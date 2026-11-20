"""Tổng hợp results/*.jsonl -> bảng terminal + biểu đồ PNG (../images) + results/summary.json + results/report.html"""
import json, statistics as st
from collections import defaultdict
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = Path(__file__).parent
RES = HERE / "results"; IMG = HERE.parent / "images"; IMG.mkdir(exist_ok=True)
ORDER = ["decision", "decision-low", "flash-lite", "flash"]
NAME = {"decision": "Decisions API", "decision-low": "Decisions API (low res)",
        "flash-lite": "3.5 Flash-Lite (JSON)", "flash": "3.8 Flash (JSON)"}
COLOR = {"decision": "#2a78d6", "decision-low": "#eb6834", "flash-lite": "#1baf7a", "flash": "#eda100"}  # categorical slot 1-4
INK, INK2, GRID = "#0b0b0b", "#52514e", "#e4e3df"

rows = defaultdict(list)
for f in sorted(RES.glob("*_run[1-9].jsonl")):
    for ln in open(f, encoding="utf-8"):
        r = json.loads(ln); r["run"] = int(f.stem.split("_run")[1]); rows[r["method"]].append(r)
methods = [m for m in ORDER if rows[m]]

def pct(xs, q):
    xs = sorted(xs); return xs[min(len(xs) - 1, int(round(q * (len(xs) - 1))))]

S = {}
for m in methods:
    R = rows[m]; runs = sorted({r["run"] for r in R})
    acc_runs = [st.mean(r["pred_type"] == r["doc_type"] for r in R if r["run"] == k) for k in runs]
    by_diff = {d: st.mean(r["pred_type"] == r["doc_type"] for r in R if r["difficulty"] == d)
               for d in ["normal", "notitle", "photo", "lowres"]}
    # ổn định: tỉ lệ tài liệu có cùng dự đoán ở mọi lần chạy
    per_doc = defaultdict(set)
    for r in R: per_doc[r["file"]].add(r["pred_type"])
    errs = sorted({(r["file"], r["doc_type"], r["pred_type"], r["difficulty"]) for r in R if r["pred_type"] != r["doc_type"]})
    S[m] = dict(name=NAME[m], model=R[0]["model"], n=len(R), runs=len(runs),
                acc=st.mean(acc_runs), acc_min=min(acc_runs), acc_max=max(acc_runs),
                sign_acc=st.mean(r["pred_sign"] == int(r["has_signature"]) for r in R),
                by_diff=by_diff, consistency=st.mean(len(v) == 1 for v in per_doc.values()),
                p50=pct([r["ms"] for r in R], .5), p95=pct([r["ms"] for r in R], .95),
                in_tok=st.mean(r["in_tok"] for r in R), out_tok=st.mean(r["out_tok"] + r["think_tok"] for r in R),
                cost_1k=st.mean(r["cost_usd"] for r in R) * 1000, errors=errs)
    # routing theo confidence: ngưỡng -> % tự động, accuracy phần tự động
    conf = [(r["conf_type"], r["pred_type"] == r["doc_type"]) for r in R if r["conf_type"] is not None]
    S[m]["routing"] = []
    for th in [0.5, 0.7, 0.8, 0.9, 0.95, 0.99]:
        auto = [ok for c, ok in conf if c >= th]
        S[m]["routing"].append(dict(th=th, auto=len(auto) / len(conf), acc_auto=(st.mean(auto) if auto else None)))

json.dump(S, open(RES / "summary.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1, default=str)

# ---------- terminal ----------
print(f"\n{'Method':<26}{'Accuracy':>10}{'(min–max)':>13}{'Sign.':>8}{'Stable':>9}{'p50 ms':>8}{'p95 ms':>8}{'tok in':>8}{'tok out':>8}{'USD/1k':>8}")
for m in methods:
    s = S[m]
    print(f"{s['name']:<26}{s['acc']:>10.1%}{f'{s['acc_min']:.0%}–{s['acc_max']:.0%}':>13}{s['sign_acc']:>8.0%}{s['consistency']:>9.0%}"
          f"{s['p50']:>8}{s['p95']:>8}{s['in_tok']:>8.0f}{s['out_tok']:>8.0f}{s['cost_1k']:>8.3f}")
print("\nAccuracy by difficulty:")
for m in methods:
    print(f"  {S[m]['name']:<26}" + "  ".join(f"{d}: {v:.0%}" for d, v in S[m]["by_diff"].items()))
for m in methods:
    if S[m]["errors"]:
        print(f"\nErrors of {S[m]['name']}: " + "; ".join(f"{f} {t}→{p} ({d})" for f, t, p, d in S[m]["errors"]))

# ---------- charts ----------
plt.rcParams.update({"font.family": "Segoe UI", "font.size": 11, "axes.edgecolor": GRID, "axes.labelcolor": INK2,
                     "xtick.color": INK2, "ytick.color": INK2, "axes.spines.top": False, "axes.spines.right": False})

def bars(key, title, fname, fmt, scale=1):
    fig, ax = plt.subplots(figsize=(8, 3.6), dpi=150)
    vals = [S[m][key] * scale for m in methods]
    b = ax.barh([NAME[m] for m in methods], vals, color=[COLOR[m] for m in methods], height=0.6, edgecolor="white", linewidth=2)
    for rect, v in zip(b, vals):
        ax.text(rect.get_width(), rect.get_y() + rect.get_height() / 2, " " + fmt(v), va="center", color=INK, fontsize=10)
    ax.invert_yaxis(); ax.grid(axis="x", color=GRID); ax.set_axisbelow(True)
    ax.set_title(title, loc="left", color=INK, fontsize=12, fontweight="bold")
    ax.set_xlim(0, max(vals) * 1.22)
    fig.tight_layout(); fig.savefig(IMG / fname); plt.close(fig)

bars("acc", "Classification accuracy (mean of 3 runs)", "chart-accuracy.png", lambda v: f"{v:.1f}%", 100)
bars("p50", "p50 latency per document (ms, lower is better)", "chart-latency.png", lambda v: f"{v:,.0f} ms")
bars("cost_1k", "Estimated cost per 1,000 documents (USD)", "chart-cost.png", lambda v: f"${v:.3f}")

fig, ax = plt.subplots(figsize=(8, 3.8), dpi=150)
for m in methods:
    pts = [(r["auto"] * 100, r["acc_auto"] * 100) for r in S[m]["routing"] if r["acc_auto"] is not None]
    ax.plot(*zip(*pts), marker="o", markersize=6, linewidth=2, color=COLOR[m], label=NAME[m])
ax.set_xlabel("% of documents automated (confidence ≥ threshold)"); ax.set_ylabel("Accuracy of automated part (%)")
ax.grid(color=GRID); ax.legend(frameon=False, fontsize=9, loc="lower left")
ax.set_title("Confidence routing: how much can be automated safely?", loc="left", color=INK, fontsize=12, fontweight="bold")
fig.tight_layout(); fig.savefig(IMG / "chart-routing.png"); plt.close(fig)

# ---------- html ----------
tr = "".join(f"<tr><td>{S[m]['name']}<br><small>{S[m]['model']}</small></td><td>{S[m]['acc']:.1%}</td><td>{S[m]['sign_acc']:.0%}</td>"
             f"<td>{S[m]['consistency']:.0%}</td><td>{S[m]['p50']:,}</td><td>{S[m]['p95']:,}</td><td>{S[m]['in_tok']:.0f} / {S[m]['out_tok']:.0f}</td>"
             f"<td>${S[m]['cost_1k']:.3f}</td></tr>" for m in methods)
html = f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Benchmark Decisions API</title>
<style>body{{font-family:Segoe UI,sans-serif;max-width:980px;margin:32px auto;padding:0 16px;color:#0b0b0b;background:#fcfcfb}}
table{{border-collapse:collapse;width:100%}}td,th{{border:1px solid #e4e3df;padding:8px 10px;text-align:right}}td:first-child,th:first-child{{text-align:left}}
th{{background:#0d47a1;color:#fff}}img{{max-width:100%;margin:12px 0}}</style></head><body>
<h1>Classification benchmark: 40 documents × {S[methods[0]]['runs']} runs</h1>
<table><tr><th>Method</th><th>Type accuracy</th><th>Signature accuracy</th><th>Stability</th><th>p50 ms</th><th>p95 ms</th><th>Token in/out</th><th>USD / 1,000 docs</th></tr>{tr}</table>
<img src="../../images/chart-accuracy.png"><img src="../../images/chart-latency.png"><img src="../../images/chart-cost.png"><img src="../../images/chart-routing.png">
</body></html>"""
(RES / "report.html").write_text(html, encoding="utf-8")
print(f"\n→ {RES / 'report.html'}")
