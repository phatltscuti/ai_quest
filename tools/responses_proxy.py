"""Local OpenAI Responses API -> Gemini bridge (via litellm), so Codex CLI can run with a Gemini model.

  python tools/responses_proxy.py            # listens on http://127.0.0.1:4141/v1
Codex config: base_url = "http://127.0.0.1:4141/v1", wire_api = "responses".
GEMINI_API_KEY is read from the repo .env and never printed.
"""
import json, os
from pathlib import Path
import truststore; truststore.inject_into_ssl()
os.environ.setdefault("LITELLM_LOCAL_MODEL_COST_MAP", "True")
from dotenv import dotenv_values
os.environ["GEMINI_API_KEY"] = dotenv_values(Path(__file__).resolve().parents[1] / ".env")["GEMINI_API_KEY"]
import litellm
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, StreamingResponse
import uvicorn

MODEL = os.environ.get("PROXY_MODEL", "gemini/gemini-3.5-flash")
DROP = {"model", "stream", "store", "include", "prompt_cache_key", "client_metadata", "service_tier", "safety_identifier"}
app = FastAPI()
LOG = Path(__file__).with_name("responses_proxy.log")

def dump(o):
    if hasattr(o, "model_dump"): return o.model_dump(exclude_none=True)
    return o

@app.post("/v1/responses")
async def responses(req: Request):
    body = await req.json()
    stream = body.get("stream", False)
    kw = {k: v for k, v in body.items() if k not in DROP}
    with LOG.open("a", encoding="utf-8") as f: f.write(json.dumps({"keys": list(body.keys()), "tools": len(body.get("tools") or [])}) + "\n")
    if stream:
        resp = await litellm.aresponses(model=MODEL, stream=True, drop_params=True, **kw)
        async def gen():
            try:
                async for ev in resp:
                    d = dump(ev); t = d.get("type", "message")
                    yield f"event: {t}\ndata: {json.dumps(d, default=str)}\n\n"
            except Exception as e:
                with LOG.open("a", encoding="utf-8") as f: f.write("STREAM ERROR " + repr(e)[:500] + "\n")
                err = {"type": "response.failed", "response": {"id": "err", "status": "failed", "error": {"code": "proxy_error", "message": str(e)[:300]}}}
                yield f"event: response.failed\ndata: {json.dumps(err)}\n\n"
        return StreamingResponse(gen(), media_type="text/event-stream")
    resp = await litellm.aresponses(model=MODEL, drop_params=True, **kw)
    return JSONResponse(dump(resp))

@app.get("/v1/models")
async def models():
    return {"object": "list", "data": [{"id": MODEL.split("/")[-1], "object": "model"}]}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=4141, log_level="warning")
