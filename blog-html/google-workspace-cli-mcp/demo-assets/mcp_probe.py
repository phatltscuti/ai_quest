"""MCP client toi gian (Streamable HTTP, JSON-RPC) goi thang remote Workspace MCP server.
Dung access token ma gwscli da cap (agent-flagged OAuth client); khong in token ra man hinh.
  python mcp_probe.py <server> [tool json-args]
"""
import json, os, sys, time, requests
from pathlib import Path
import truststore; truststore.inject_into_ssl()
URLS = {"drive": "https://drivemcp.googleapis.com/mcp/v1", "calendar": "https://calendarmcp.googleapis.com/mcp/v1",
        "tasks": "https://tasksmcp.googleapis.com/mcp/v1", "gmail": "https://gmailmcp.googleapis.com/mcp/v1"}
tok = json.loads((Path(os.environ["APPDATA"]) / "gwscli" / "token.json").read_text())
tok = tok.get("access_token") or tok.get("token", {}).get("access_token")
srv = sys.argv[1]; url = URLS[srv]
H = {"Authorization": f"Bearer {tok}", "Content-Type": "application/json", "Accept": "application/json, text/event-stream"}
def rpc(method, params=None, i=[0]):
    i[0] += 1; t = time.time()
    r = requests.post(url, headers=H, json={"jsonrpc": "2.0", "id": i[0], "method": method, "params": params or {}}, timeout=60)
    if "mcp-session-id" in r.headers: H["Mcp-Session-Id"] = r.headers["mcp-session-id"]
    body = r.text
    if body.lstrip().startswith("event:") or "data:" in body[:20]:
        body = "\n".join(l[5:] for l in body.splitlines() if l.startswith("data:"))
    try: j = json.loads(body)
    except Exception: j = {"raw": body[:400]}
    return r.status_code, round((time.time() - t) * 1000), j
print(f"> POST {url}  initialize")
st, ms, j = rpc("initialize", {"protocolVersion": "2025-06-18", "capabilities": {}, "clientInfo": {"name": "aiquest-probe", "version": "0.1"}})
print(f"  HTTP {st} in {ms} ms  server={json.dumps(j.get('result', {}).get('serverInfo'))}  protocol={j.get('result', {}).get('protocolVersion')}")
if st >= 400: print(json.dumps(j, indent=1)[:600])
requests.post(url, headers=H, json={"jsonrpc": "2.0", "method": "notifications/initialized"}, timeout=30)
print("> tools/list")
st, ms, j = rpc("tools/list")
tools = j.get("result", {}).get("tools", [])
print(f"  HTTP {st} in {ms} ms  {len(tools)} tools:")
for t in tools: 
    ann = t.get("annotations", {}); ro = "read-only" if ann.get("readOnlyHint") else ("DESTRUCTIVE" if ann.get("destructiveHint") else "write")
    print(f"   - {t['name']:<28} [{ro}]")
if len(sys.argv) > 2:
    name, args = sys.argv[2], dict(a.split('=', 1) for a in sys.argv[3:])
    print(f"> tools/call {name} {json.dumps(args)}")
    st, ms, j = rpc("tools/call", {"name": name, "arguments": args})
    print(f"  HTTP {st} in {ms} ms")
    print("  " + json.dumps(j.get("result", j.get("error", j)), ensure_ascii=False, indent=1)[:900].replace("\n", "\n  "))
