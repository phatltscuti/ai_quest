"""Quickstart: 1 request Decisions API hỏi 3 loại câu hỏi (noul / choice / score) cho 1 tài liệu."""
import base64, json, sys, time
from pathlib import Path
from dotenv import dotenv_values
from google import genai

ROOT = Path(__file__).resolve().parents[3]
key = dotenv_values(ROOT / ".env")["GEMINI_API_KEY"]
print(f"GEMINI_API_KEY: {key[:3]}****{key[-4:]} (loaded from .env)")
client = genai.Client(api_key=key, http_options={"api_version": "v1beta"})

doc = Path(__file__).parent / "dataset" / (sys.argv[1] if len(sys.argv) > 1 else "doc_05.png")
print(f"Document: {doc.name}\n")
t0 = time.perf_counter()
r = client.decisions.create(
    model="gemini-decision-1",
    input=[
        {"type": "text", "text": "Scanned document received by the back office."},
        {"type": "image", "data": base64.b64encode(doc.read_bytes()).decode(), "mime_type": "image/png"},
    ],
    questions={
        "doc_type": {"type": "choice", "instructions": "What kind of business document is this?",
                     "criteria": {"invoice": "requests payment", "quotation": "price offer before an order",
                                  "receipt": "confirms payment received", "contract": "agreement with articles",
                                  "other": "anything else"}},
        "has_signature": {"type": "noul", "instructions": "Is there a handwritten signature on the signature line?"},
        "amount_level": {"type": "score", "instructions": "How large is the total amount?",
                         "criteria": ["no amount", "under 10,000,000 VND", "10–50 million VND", "over 50 million VND"]},
    },
)
ms = (time.perf_counter() - t0) * 1000
print(json.dumps(r.model_dump(exclude_none=True)["answers"], indent=2, ensure_ascii=False))
u = r.usage
print(f"\n⏱  {ms:.0f} ms | input {u.total_input_tokens} tokens | output {u.total_output_tokens} tokens"
      f" | cost ≈ ${u.total_input_tokens * 0.10 / 1e6:.6f}")
