"""
Rong Do Studio - server nho chay local cho trang studio/index.html.

  python studio/studio_server.py      -> mo http://localhost:8765/studio/

API:
  POST /api/tts     {"text": "...", "voice": "vi-VN-NamMinhNeural"}
                    -> ghi scripts/narration-vi.txt, chay scripts/make_tts.py (edge-tts)
                    -> tra ve thoi luong, so tu, so cau
  POST /api/export?x=&y=&w=&h=   body = file WebM do Chrome ghi lai tab (MediaRecorder)
                    -> cat dung khung 1280x720 cua san khau, chuyen sang MP4 (H.264 + AAC)
                    -> video/scuti-ai-red-dragon.mp4
"""
import json, os, re, subprocess, sys
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from urllib.parse import urlparse, parse_qs

import imageio_ffmpeg

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FF = imageio_ffmpeg.get_ffmpeg_exe()
PORT = 8765


def probe(path):
    err = subprocess.run([FF, "-i", path], capture_output=True, text=True).stderr
    m = re.search(r"Duration: (\d+):(\d+):([\d.]+)", err)
    dur = int(m.group(1)) * 3600 + int(m.group(2)) * 60 + float(m.group(3)) if m else 0
    return {"duration": round(dur, 2), "audio": "Audio:" in err,
            "video": (re.search(r"Video: (\w+)", err) or [None, "?"])[1]}


class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *a, **kw):
        super().__init__(*a, directory=ROOT, **kw)

    def end_headers(self):
        self.send_header("Cache-Control", "no-store")
        super().end_headers()

    def log_message(self, fmt, *args):
        sys.stderr.write("[studio] " + fmt % args + "\n")

    def _json(self, obj, code=200):
        body = json.dumps(obj, ensure_ascii=False).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_POST(self):
        url = urlparse(self.path)
        data = self.rfile.read(int(self.headers.get("Content-Length", 0)))
        if url.path == "/api/tts":
            req = json.loads(data)
            with open(os.path.join(ROOT, "scripts", "narration-vi.txt"), "w", encoding="utf-8") as f:
                f.write(req["text"].strip() + "\n")
            r = subprocess.run([sys.executable, os.path.join(ROOT, "scripts", "make_tts.py"),
                                "--voice", req.get("voice", "vi-VN-NamMinhNeural")],
                               capture_output=True, text=True, encoding="utf-8")
            if r.returncode:
                return self._json({"ok": False, "error": r.stderr[-800:]}, 500)
            b = json.load(open(os.path.join(ROOT, "assets", "boundaries.json"), encoding="utf-8"))
            return self._json({"ok": True, "duration": b["duration"], "words": len(b["words"]),
                               "sentences": len(b["sentences"]), "voice": b["voice"]})
        if url.path == "/api/export":
            q = {k: int(float(v[0])) for k, v in parse_qs(url.query).items()}
            raw = os.path.join(ROOT, "video", "_tab-capture.webm")
            out = os.path.join(ROOT, "video", "scuti-ai-red-dragon.mp4")
            os.makedirs(os.path.dirname(raw), exist_ok=True)
            open(raw, "wb").write(data)
            crop = f"crop={q['w']}:{q['h']}:{q['x']}:{q['y']},scale=1280:720,fps=30,format=yuv420p"
            r = subprocess.run([FF, "-y", "-v", "error", "-i", raw, "-vf", crop,
                                "-c:v", "libx264", "-preset", "medium", "-crf", "20",
                                "-c:a", "aac", "-b:a", "160k", "-movflags", "+faststart", out],
                               capture_output=True, text=True)
            if r.returncode:
                return self._json({"ok": False, "error": r.stderr[-800:]}, 500)
            if not os.environ.get("KEEP_RAW"): os.remove(raw)
            info = probe(out)
            info.update(ok=True, file="video/scuti-ai-red-dragon.mp4",
                        size_mb=round(os.path.getsize(out) / 1e6, 1))
            return self._json(info)
        self._json({"ok": False, "error": "not found"}, 404)


if __name__ == "__main__":
    print(f"Rong Do Studio: http://localhost:{PORT}/studio/")
    ThreadingHTTPServer(("127.0.0.1", PORT), Handler).serve_forever()
