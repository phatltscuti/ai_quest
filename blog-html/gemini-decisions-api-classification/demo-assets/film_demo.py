"""Quay toàn bộ video demo Quest 3 (quay ngầm: Chrome qua CDP screencast, terminal = lệnh thật được phát lại).

  python film_demo.py            # quay tất cả các đoạn rồi ghép full-demo.mp4
  python film_demo.py t3 c2      # chỉ quay lại vài đoạn, rồi ghép lại
"""
import subprocess, sys, time
from pathlib import Path
from playwright.sync_api import sync_playwright

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path.insert(0, str(ROOT / "tools"))
from cdp_rec import open_window, Recorder, show_click, FF
from termcast import run_steps
from film import film_cast

VID = HERE.parent / "videos"; VID.mkdir(exist_ok=True)
CASTS = HERE / "casts"; CASTS.mkdir(exist_ok=True)
PY = str(ROOT / ".venv" / "Scripts" / "python.exe")
PROMPT = r"(.venv) PS D:\ai_quest\gemini-decisions-api-classification\demo-assets>"

def term(name, steps, max_gap=2500):
    for s in steps:
        s.setdefault("cwd", str(HERE)); s.setdefault("prompt", PROMPT)
        if s.get("run"): s["run"] = s["run"].replace("python ", f'"{PY}" ', 1)
    run_steps(steps, CASTS / f"{name}.json")
    film_cast(CASTS / f"{name}.json", VID / f"{name}.mp4", max_gap=max_gap)

def scroll(page, rec, total, step=120, dt=0.08, x=900, y=600):
    page.mouse.move(x, y)
    for _ in range(int(total / step)):
        page.mouse.wheel(0, step); rec.pump(dt)

def chrome(name, url, actions, caption=None):
    with sync_playwright() as p:
        b = p.chromium.connect_over_cdp("http://127.0.0.1:9222")
        page = open_window(b, url)
        page.wait_for_load_state("networkidle"); page.wait_for_timeout(1500)
        rec = Recorder(page); rec.start(); rec.pump(1.5)
        actions(page, rec)
        rec.pump(1.5); rec.stop(VID / f"{name}.mp4", caption=caption or url)
        page.close()

def card(name, title, sub="", secs=3.2):
    t = title.replace(":", r"\:"); s = sub.replace(":", r"\:")
    font = "C\\:/Windows/Fonts/segoeuib.ttf"; font2 = "C\\:/Windows/Fonts/segoeui.ttf"
    vf = (f"drawtext=fontfile='{font}':text='{t}':fontcolor=white:fontsize=64:x=(w-text_w)/2:y=(h/2)-70,"
          f"drawtext=fontfile='{font2}':text='{s}':fontcolor=0xcfe3ff:fontsize=34:x=(w-text_w)/2:y=(h/2)+30")
    subprocess.run([str(FF), "-y", "-loglevel", "error", "-f", "lavfi", "-i", f"color=c=0x0d47a1:s=1920x1080:d={secs}:r=30",
                    "-vf", vf, "-c:v", "libx264", "-pix_fmt", "yuv420p", str(VID / f"{name}.mp4")], check=True)

# ---------------- các đoạn ----------------
def c1(page, rec):  # docs Decisions API
    scroll(page, rec, 5200, dt=0.22)
def c2(page, rec):  # pricing
    page.evaluate("document.querySelector('#gemini-decision, [id*=decision]')?.scrollIntoView({behavior:'smooth'})")
    rec.pump(5)
    scroll(page, rec, 600, dt=0.15); rec.pump(3)
def c3(page, rec):  # gallery dataset
    rec.pump(2); scroll(page, rec, 1800, dt=0.1); rec.pump(1.5)
    show_click(page, page.locator("img").nth(12), click=False); rec.pump(1.5)
def c4(page, rec):  # report.html
    rec.pump(4); scroll(page, rec, 2600, dt=0.15); rec.pump(2)

SEGMENTS = {
  "k0": lambda: card("k0", "Gemini Decisions API vs Text-gen", "Classifying 40 documents – accuracy, speed, cost"),
  "k1": lambda: card("k1", "Step 1: Read the API docs & pricing", "aistudio.google.com/docs/decisions-api"),
  "c1": lambda: chrome("c1", "https://aistudio.google.com/docs/decisions-api", c1),
  "c2": lambda: chrome("c2", "https://aistudio.google.com/docs/pricing", c2),
  "k2": lambda: card("k2", "Step 2: Python environment", "venv + google-genai SDK · API key loaded from .env (never shown)"),
  "t1": lambda: term("t1", [
      {"comment": "Create a virtualenv and install the SDK", "show": "python -m venv .venv; .\\.venv\\Scripts\\Activate.ps1",
       "run": None, "prompt": r"PS D:\ai_quest\gemini-decisions-api-classification\demo-assets>"},
      {"show": "pip install google-genai pillow matplotlib python-dotenv", "run": "python -m pip install google-genai pillow matplotlib python-dotenv"},
      {"show": "pip show google-genai", "run": "python -m pip show google-genai"},
  ]),
  "k3": lambda: card("k3", "Step 3: Build a synthetic dataset", "8 document types × 5 · Vietnamese / English / Japanese · 24 hard samples"),
  "t2": lambda: term("t2", [
      {"comment": "Generate 40 fictional documents + ground-truth labels", "show": "python make_dataset.py", "run": "python make_dataset.py"},
      {"show": "python gallery.py", "run": "python gallery.py"},
      {"show": "Get-Content dataset\\labels.csv -TotalCount 8", "run": "python -c \"print(''.join(open('dataset/labels.csv',encoding='utf-8').readlines()[:8]))\""},
  ]),
  "c3": lambda: chrome("c3", (HERE / "dataset" / "gallery.html").as_uri(), c3, caption="dataset/gallery.html"),
  "k4": lambda: card("k4", "Step 4: First Decisions API call", "1 request · 3 questions: choice + noul + score"),
  "t3": lambda: term("t3", [
      {"comment": "Quickstart: document type, signature?, amount level", "show": "python quickstart_decision.py doc_05.png", "run": "python quickstart_decision.py doc_05.png"},
  ], max_gap=8000),
  "k5": lambda: card("k5", "Step 5: Decisions API vs text generation", "Same first 10 documents · timings are real (not sped up)"),
  "t4": lambda: term("t4", [
      {"comment": "A. Decisions API (gemini-decision-1)", "show": "python run_benchmark.py --method decision --limit 10 --run 0", "run": "python run_benchmark.py --method decision --limit 10 --run 0"},
      {"comment": "B. Decisions API, resolution=low (fewer tokens)", "show": "python run_benchmark.py --method decision-low --limit 10 --run 0", "run": "python run_benchmark.py --method decision-low --limit 10 --run 0"},
      {"comment": "C. Traditional text generation: 3.5 Flash-Lite + JSON schema", "show": "python run_benchmark.py --method flash-lite --limit 10 --run 0", "run": "python run_benchmark.py --method flash-lite --limit 10 --run 0"},
  ], max_gap=15000),
  "k6": lambda: card("k6", "Step 6: Full results", "40 documents × 3 runs × 3 methods = 360 requests"),
  "t5": lambda: term("t5", [
      {"comment": "Aggregate results → tables, charts, report.html", "show": "python report.py", "run": "python report.py"},
  ]),
  "c4": lambda: chrome("c4", (HERE / "results" / "report.html").as_uri(), c4, caption="results/report.html"),
  "k7": lambda: card("k7", "Step 7: Confidence-based routing", "Automate when confident, send to a human when unsure"),
  "t6": lambda: term("t6", [
      {"comment": "12 hard documents · threshold 0.9", "show": "python route_demo.py --threshold 0.9", "run": "python route_demo.py --threshold 0.9"},
  ], max_gap=8000),
  "k8": lambda: card("k8", "Done", "Full analysis in the blog post"),
}

def concat():
    parts = [VID / f"{k}.mp4" for k in SEGMENTS if (VID / f"{k}.mp4").exists()]
    inputs = sum([["-i", str(p)] for p in parts], [])
    fc = "".join(f"[{i}:v]scale=1920:1080,setsar=1,fps=30[v{i}];" for i in range(len(parts)))
    fc += "".join(f"[v{i}]" for i in range(len(parts))) + f"concat=n={len(parts)}:v=1:a=0[out]"
    subprocess.run([str(FF), "-y", "-loglevel", "error", *inputs, "-filter_complex", fc, "-map", "[out]",
                    "-c:v", "libx264", "-crf", "22", "-preset", "medium", "-pix_fmt", "yuv420p", "-movflags", "+faststart",
                    str(VID / "full-demo.mp4")], check=True)
    print("→", VID / "full-demo.mp4")

if __name__ == "__main__":
    for k in (sys.argv[1:] or SEGMENTS):
        print(f"=== {k} ==="); SEGMENTS[k]()
    concat()
