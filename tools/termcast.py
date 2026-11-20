"""Chạy lệnh THẬT, ghi lại output + thời gian thật vào file cast (JSON) để phát lại & quay video.

Mỗi bước: {"comment", "show" (lệnh hiển thị), "run" (lệnh thực thi thật), "cwd"}.
Mọi chuỗi trùng với giá trị trong .env (API key) đều bị thay bằng ****.
"""
import json, os, subprocess, threading, time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def _secrets():
    s = []
    env = ROOT / ".env"
    if env.exists():
        for ln in env.read_text().splitlines():
            if "=" in ln and len(ln.split("=", 1)[1].strip()) > 8: s.append(ln.split("=", 1)[1].strip())
    return s

def run_steps(steps, cast_path, title="Windows PowerShell", prompt_cwd=None):
    secrets = _secrets()
    env = dict(os.environ, PYTHONUNBUFFERED="1", PYTHONUTF8="1", PYTHONIOENCODING="utf-8", FORCE_COLOR="1")
    out = {"title": title, "steps": []}
    for st in steps:
        events, t0 = [], time.time()
        if st.get("run"):
            p = subprocess.Popen(st["run"], shell=True, cwd=st.get("cwd", ROOT), env=env,
                                 stdin=subprocess.DEVNULL, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            def reader():
                while True:
                    b = p.stdout.read1(4096) if hasattr(p.stdout, "read1") else p.stdout.read(1)
                    if not b: break
                    txt = b.decode("utf-8", "replace")
                    for s in secrets: txt = txt.replace(s, "****")
                    events.append([round(time.time() - t0, 3), txt])
                    print(txt, end="", flush=True)
            th = threading.Thread(target=reader); th.start(); p.wait(); th.join()
            code = p.returncode
        else:
            code = 0
        out["steps"].append({"comment": st.get("comment"), "show": st.get("show", st.get("run")),
                             "prompt": st.get("prompt", prompt_cwd or "PS D:\\code\\work\\ai_quest>"),
                             "events": events, "exit": code, "seconds": round(time.time() - t0, 2)})
        print(f"\n[step done: {st.get('show') or st.get('run')} exit={code} {time.time() - t0:.1f}s]")
    Path(cast_path).parent.mkdir(parents=True, exist_ok=True)
    Path(cast_path).write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    return out
