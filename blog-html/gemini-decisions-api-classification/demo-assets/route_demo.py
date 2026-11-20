"""Demo pipeline thực tế: tự động phân loại khi confidence cao, đẩy sang người duyệt khi thấp.

  python route_demo.py --threshold 0.9 [--files doc_01.png doc_07.png ...]
"""
import argparse, base64, csv, time
from pathlib import Path
from dotenv import dotenv_values
from google import genai
from run_benchmark import CLASSES, Q_TYPE, ROOT, DATA, mime

ap = argparse.ArgumentParser(); ap.add_argument("--threshold", type=float, default=0.9); ap.add_argument("--files", nargs="*")
a = ap.parse_args()
client = genai.Client(api_key=dotenv_values(ROOT / ".env")["GEMINI_API_KEY"], http_options={"api_version": "v1beta"})
labels = {r["file"]: r for r in csv.DictReader(open(DATA / "labels.csv", encoding="utf-8"))}
files = a.files or [f for f, r in labels.items() if r["difficulty"] != "normal"][:12]

auto = review = wrong_auto = 0
print(f"Confidence threshold: {a.threshold}\n")
for f in files:
    p = DATA / f
    t0 = time.perf_counter()
    r = client.decisions.create(model="gemini-decision-1", input=[{
        "type": "document" if p.suffix == ".pdf" else "image", "data": base64.b64encode(p.read_bytes()).decode(), "mime_type": mime(p)}],
        questions={"doc_type": {"type": "choice", "instructions": Q_TYPE, "criteria": CLASSES}})
    ans = r.answers["doc_type"]; ms = (time.perf_counter() - t0) * 1000
    top2 = sorted(ans.probabilities.items(), key=lambda kv: -kv[1])[:2]
    truth = labels[f]["doc_type"]
    if ans.confidence >= a.threshold:
        auto += 1; wrong_auto += ans.choice != truth
        route = f"🤖 AUTO → folder /{ans.choice}/" + ("   (⚠ wrong!)" if ans.choice != truth else "")
    else:
        review += 1
        route = f"👤 REVIEW (unsure: {top2[0][0]} {top2[0][1]:.2f} / {top2[1][0]} {top2[1][1]:.2f})"
    print(f"{f:<11}[{labels[f]['difficulty']:<7}] conf {ans.confidence:.2f}  {ms:5.0f} ms  {route}")
print(f"\nAutomated: {auto}/{len(files)} (wrong {wrong_auto}) | Needs human review: {review}/{len(files)}")
