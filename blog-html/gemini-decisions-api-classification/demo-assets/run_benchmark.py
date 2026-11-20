"""Benchmark phân loại tài liệu: Gemini Decisions API vs text-gen (JSON) truyền thống.

Usage:
  python run_benchmark.py --method decision        # gemini-decision-1
  python run_benchmark.py --method decision-low    # gemini-decision-1, resolution="low"
  python run_benchmark.py --method flash-lite      # gemini-3.5-flash-lite + JSON schema
  python run_benchmark.py --method flash           # gemini-3.8-flash + JSON schema
  thêm --limit 5 để chạy thử, --run 2 để đánh số lần chạy.

Mỗi tài liệu hỏi 2 câu: doc_type (8 lựa chọn) + has_signature (Yes/No).
Kết quả: results/<method>_run<k>.jsonl
API key đọc từ file .env ở thư mục gốc repo (không in ra màn hình).
"""
import argparse, base64, csv, json, sys, time
from pathlib import Path

from dotenv import dotenv_values
from google import genai
from google.genai import types

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).parent
DATA = HERE / "dataset"
OUT = HERE / "results"; OUT.mkdir(exist_ok=True)

# Giá USD / 1M token (aistudio.google.com/docs/pricing, tra ngày 2026-11-20, Standard tier)
PRICE = {"gemini-decision-1": (0.10, 0.0), "gemini-3.5-flash-lite": (0.30, 2.50), "gemini-3.8-flash": (0.75, 3.75)}

CLASSES = {
    "invoice": "Invoice / bill requesting payment (has due date, bank account, amount to pay)",
    "quotation": "Quotation / price estimate offered before an order (has validity period)",
    "receipt": "Receipt confirming a payment was already received",
    "contract": "Contract / service agreement with numbered articles between parties",
    "leave_request": "Employee leave / time-off request form",
    "resume": "Resume / CV of a job candidate",
    "meeting_minutes": "Meeting minutes with attendees, agenda and action items",
    "delivery_note": "Delivery note listing goods and quantities delivered (no prices)",
}
Q_TYPE = "Classify the business document in the attachment. It may be in Vietnamese, English or Japanese, may be a skewed photo or low resolution, and the title may be missing."
Q_SIGN = "Is there a handwritten signature (ink scribble) on the signature line of the document?"

def load_key():
    k = dotenv_values(ROOT / ".env").get("GEMINI_API_KEY")
    if not k: sys.exit("Missing GEMINI_API_KEY in .env")
    return k

def mime(p): return "application/pdf" if p.suffix == ".pdf" else "image/png"

def call_decision(client, path, resolution=None):
    blk = {"type": "document" if path.suffix == ".pdf" else "image",
           "data": base64.b64encode(path.read_bytes()).decode(), "mime_type": mime(path)}
    if resolution and blk["type"] == "image": blk["resolution"] = resolution
    r = client.decisions.create(model="gemini-decision-1", input=[blk], questions={
        "doc_type": {"type": "choice", "instructions": Q_TYPE, "criteria": CLASSES},
        "has_signature": {"type": "noul", "instructions": Q_SIGN},
    })
    a = r.answers
    return dict(pred_type=a["doc_type"].choice, conf_type=a["doc_type"].confidence,
                pred_sign=int(a["has_signature"].noul >= 0.5), conf_sign=a["has_signature"].confidence,
                in_tok=r.usage.total_input_tokens, out_tok=0, think_tok=0)

SCHEMA = types.Schema(type="OBJECT", required=["doc_type", "has_signature", "confidence"], properties={
    "doc_type": types.Schema(type="STRING", enum=list(CLASSES)),
    "has_signature": types.Schema(type="BOOLEAN"),
    "confidence": types.Schema(type="NUMBER", description="your confidence 0..1 for doc_type"),
})
PROMPT = (Q_TYPE + "\nCategories:\n" + "\n".join(f"- {k}: {v}" for k, v in CLASSES.items())
          + "\n" + Q_SIGN + "\nReturn JSON only.")

def call_textgen(client, path, model):
    r = client.models.generate_content(
        model=model,
        contents=[types.Part.from_bytes(data=path.read_bytes(), mime_type=mime(path)), PROMPT],
        config=types.GenerateContentConfig(response_mime_type="application/json", response_schema=SCHEMA, temperature=0),
    )
    j = json.loads(r.text)
    u = r.usage_metadata
    return dict(pred_type=j["doc_type"], conf_type=j.get("confidence"), pred_sign=int(bool(j["has_signature"])), conf_sign=None,
                in_tok=u.prompt_token_count or 0, out_tok=u.candidates_token_count or 0, think_tok=u.thoughts_token_count or 0)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--method", required=True, choices=["decision", "decision-low", "flash-lite", "flash"])
    ap.add_argument("--limit", type=int); ap.add_argument("--run", type=int, default=1)
    a = ap.parse_args()
    key = load_key()
    if a.method.startswith("decision"):
        client, model = genai.Client(api_key=key, http_options={"api_version": "v1beta"}), "gemini-decision-1"
        fn = lambda p: call_decision(client, p, "low" if a.method == "decision-low" else None)
    else:
        model = {"flash-lite": "gemini-3.5-flash-lite", "flash": "gemini-3.8-flash"}[a.method]
        client = genai.Client(api_key=key)
        fn = lambda p: call_textgen(client, p, model)
    labels = list(csv.DictReader(open(DATA / "labels.csv", encoding="utf-8")))[: a.limit]
    pin, pout = PRICE[model]
    out = OUT / f"{a.method}_run{a.run}.jsonl"
    ok = n = 0; lat = []; cost = 0.0
    print(f"\n▶ {a.method}  ({model})  — {len(labels)} documents\n")
    print(f"{'file':<11}{'truth':<16}{'predicted':<16}{'conf':>6}{'sig':>5}{'ms':>7}{'tok in/out':>12}")
    with open(out, "w", encoding="utf-8") as f:
        for row in labels:
            p = DATA / row["file"]
            for attempt in range(6):
                try:
                    t0 = time.perf_counter(); res = fn(p); ms = (time.perf_counter() - t0) * 1000; break
                except Exception as e:  # 429 / 5xx: chờ rồi thử lại (thời gian chờ không tính vào latency)
                    msg = str(e)[:90]; wait = 5 * (attempt + 1)
                    print(f"   ! {row['file']}: {msg} → retry in {wait}s"); time.sleep(wait)
            else:
                continue
            c = (res["in_tok"] * pin + (res["out_tok"] + res["think_tok"]) * pout) / 1e6
            rec = dict(row, method=a.method, model=model, ms=round(ms), cost_usd=c, **res)
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")
            n += 1; ok += rec["pred_type"] == row["doc_type"]; lat.append(ms); cost += c
            mark = "✅" if rec["pred_type"] == row["doc_type"] else "❌"
            conf = f"{res['conf_type']:.2f}" if res["conf_type"] is not None else "  - "
            print(f"{row['file']:<11}{row['doc_type']:<16}{mark} {res['pred_type']:<13}{conf:>6}{res['pred_sign']:>5}{ms:>7.0f}"
                  f"{res['in_tok']:>7}/{res['out_tok'] + res['think_tok']:<4}")
    lat.sort()
    print(f"\nAccuracy doc_type: {ok}/{n} = {ok / max(n,1):.1%} | p50 {lat[len(lat)//2]:.0f} ms | "
          f"cost {cost:.5f} USD → {cost / max(n,1) * 1000:.3f} USD per 1,000 docs\n→ {out}")

if __name__ == "__main__":
    main()
