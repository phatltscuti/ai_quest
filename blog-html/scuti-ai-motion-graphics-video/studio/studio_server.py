"""
Motion Studio - server nho chay local cho trang studio/index.html.

  python studio/studio_server.py      -> mo http://localhost:8766/studio/

API:
  POST /api/stills   {"times": [0.8, 2.6, ...]}  -> chup khung hinh tai cac moc, ghep contact sheet
                                                    -> studio/contact-sheet-live.png
  POST /api/render                                -> render tung frame 1920x1080 @30fps + nhac nen -> MP4
  GET  /api/render/status                         -> tien do render (frame hien tai / tong so frame)
"""
import json, os, re, subprocess, sys, threading
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler

import imageio_ffmpeg
from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ANIM = os.path.join(ROOT, "animation")
FF = imageio_ffmpeg.get_ffmpeg_exe()
PORT = 8766
STATE = {"running": False, "frame": 0, "total": 540, "done": False, "result": None, "log": []}


def probe(path):
    err = subprocess.run([FF, "-i", path], capture_output=True, text=True).stderr
    m = re.search(r"Duration: (\d+):(\d+):([\d.]+)", err)
    dur = int(m.group(1)) * 3600 + int(m.group(2)) * 60 + float(m.group(3)) if m else 0
    size = re.search(r"Video: .*?(\d{3,4})x(\d{3,4})", err)
    return {"duration": round(dur, 2), "audio": "Audio:" in err,
            "size": f"{size.group(1)}x{size.group(2)}" if size else "?",
            "fps": (re.search(r"([\d.]+) fps", err) or [None, "?"])[1]}


def run_render():
    STATE.update(running=True, frame=0, done=False, result=None, log=[])
    p = subprocess.Popen([sys.executable, "-u", os.path.join(ANIM, "render_frames.py")],
                         stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    for line in p.stdout:
        line = line.strip()
        m = re.match(r"frame\s+(\d+)/(\d+)", line)
        if m:
            STATE["frame"], STATE["total"] = int(m.group(1)), int(m.group(2))
        if line:
            STATE["log"] = (STATE["log"] + [line])[-6:]
    p.wait()
    out = os.path.join(ROOT, "video", "scuti-ai-motion-graphics.mp4")
    info = probe(out)
    info.update(ok=p.returncode == 0, file="video/scuti-ai-motion-graphics.mp4",
                size_mb=round(os.path.getsize(out) / 1e6, 1))
    STATE.update(running=False, done=True, frame=STATE["total"], result=info)


def contact_sheet(times):
    r = subprocess.run([sys.executable, os.path.join(ANIM, "render_frames.py"),
                        "--stills", ",".join(str(t) for t in times)], capture_output=True, text=True)
    if r.returncode:
        raise RuntimeError(r.stdout[-400:] + r.stderr[-400:])
    cols, w, h = 4, 480, 270
    rows = (len(times) + cols - 1) // cols
    sheet = Image.new("RGB", (cols * w, rows * (h + 34)), "#111")
    d = ImageDraw.Draw(sheet)
    try:
        font = ImageFont.truetype("segoeui.ttf", 20)
    except OSError:
        font = ImageFont.load_default()
    for i, t in enumerate(times):
        im = Image.open(os.path.join(ANIM, "stills", f"still-{t:05.2f}s.png")).convert("RGB").resize((w, h))
        x, y = (i % cols) * w, (i // cols) * (h + 34)
        sheet.paste(im, (x, y + 34))
        d.text((x + 10, y + 6), f"{t:.1f}s", fill="#ffb3b3", font=font)
    out = os.path.join(ROOT, "studio", "contact-sheet-live.png")
    sheet.save(out)
    return "studio/contact-sheet-live.png"


class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *a, **kw):
        super().__init__(*a, directory=ROOT, **kw)

    def end_headers(self):
        self.send_header("Cache-Control", "no-store")
        super().end_headers()

    def log_message(self, fmt, *args):
        pass

    def _json(self, obj, code=200):
        body = json.dumps(obj, ensure_ascii=False).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        if self.path.startswith("/api/render/status"):
            return self._json(STATE)
        return super().do_GET()

    def do_POST(self):
        data = self.rfile.read(int(self.headers.get("Content-Length", 0)) or 0)
        if self.path == "/api/stills":
            times = json.loads(data or b"{}").get("times", [1.0, 4.6, 8.0, 11.0, 13.5, 16.5])
            try:
                return self._json({"ok": True, "file": contact_sheet(times)})
            except Exception as e:
                return self._json({"ok": False, "error": str(e)}, 500)
        if self.path == "/api/render":
            if not STATE["running"]:
                threading.Thread(target=run_render, daemon=True).start()
            return self._json({"ok": True})
        self._json({"ok": False, "error": "not found"}, 404)


if __name__ == "__main__":
    print(f"Motion Studio: http://localhost:{PORT}/studio/")
    ThreadingHTTPServer(("127.0.0.1", PORT), Handler).serve_forever()
