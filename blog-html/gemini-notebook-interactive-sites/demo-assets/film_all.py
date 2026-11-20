"""Ghép video đầy đủ Quest 5: thẻ tiêu đề + Notebook (n1,n2,n3) + RAG terminal (r1) -> videos/full-demo.mp4"""
import subprocess, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
Q5 = HERE.parent; ROOT = Q5.parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from cdp_rec import FF
from termcast import run_steps
from film import film_cast

VID = Q5 / "videos"; CASTS = HERE / "casts"; CASTS.mkdir(exist_ok=True)
PY = str(ROOT / ".venv" / "Scripts" / "python.exe")
PROMPT = r"(.venv) PS D:\ai_quest\gemini-notebook-interactive-sites\demo-assets\rag>"

def card(name, title, sub="", secs=3.2):
    t = title.replace(":", r"\:"); s = sub.replace(":", r"\:")
    f1 = "C\\:/Windows/Fonts/segoeuib.ttf"; f2 = "C\\:/Windows/Fonts/segoeui.ttf"
    vf = (f"drawtext=fontfile='{f1}':text='{t}':fontcolor=white:fontsize=60:x=(w-text_w)/2:y=(h/2)-70,"
          f"drawtext=fontfile='{f2}':text='{s}':fontcolor=0xcfe3ff:fontsize=32:x=(w-text_w)/2:y=(h/2)+30")
    subprocess.run([str(FF), "-y", "-loglevel", "error", "-f", "lavfi", "-i", f"color=c=0x0d47a1:s=1920x1080:d={secs}:r=30",
                    "-vf", vf, "-c:v", "libx264", "-pix_fmt", "yuv420p", str(VID / f"{name}.mp4")], check=True)

def rag():
    q = ['ask "What does error code E03 mean on the AeroPure AQ-200 and how do I fix it?"',
         'ask "Which month had the most Wi-Fi/App support tickets, how many, and what was the reason?"',
         'ask "What is the price and launch date of the AeroPure AQ-300?"']
    steps = [{"comment": "Traditional RAG: extract → chunk → embed (gemini-embedding-2) → index.json", "show": "python rag.py build", "run": f'"{PY}" rag.py build'}]
    steps += [{"comment": c, "show": f"python rag.py {x}", "run": f'"{PY}" rag.py {x}'} for c, x in zip(
        ["Retrieve top-5 (cosine) → answer with gemini-3.5-flash-lite, cite [S#]", "Aggregation question over the monthly table", "Trap question: AQ-300 is NOT in the documents"], q)]
    for s in steps: s["cwd"] = str(HERE / "rag"); s["prompt"] = PROMPT
    run_steps(steps, CASTS / "r1.json")
    film_cast(CASTS / "r1.json", VID / "r1.mp4", max_gap=9000)

ORDER = ["k0", "k1", "n1", "k2", "n2", "k3", "n3", "k4", "r1", "k5"]
CARDS = {"k0": ("Gemini Notebook – Interactive Sites", "Product manual → interactive site & dashboard, compared with traditional RAG"),
         "k1": ("Step 1–3: Notebook, sources, prompts", "4 fictional PDFs · 2 × “Make me a site” · generation fast-forwarded"),
         "k2": ("Step 4: Interactive troubleshooting site", "Error-code lookup · maintenance checklist · filter cost calculator"),
         "k3": ("Step 5: Sales & support dashboard", "KPI cards · filters · charts computed by JavaScript"),
         "k4": ("Step 6: Traditional RAG baseline", "Same 4 PDFs · real commands · API key never shown"),
         "k5": ("Done", "Full comparison & opinions in the blog post")}

if __name__ == "__main__":
    todo = sys.argv[1:] or ["cards", "r1"]
    if "cards" in todo:
        for k, (t, s) in CARDS.items(): card(k, t, s)
    if "r1" in todo: rag()
    parts = [VID / f"{k}.mp4" for k in ORDER if (VID / f"{k}.mp4").exists()]
    inputs = sum([["-i", str(p)] for p in parts], [])
    fc = "".join(f"[{i}:v]scale=1920:1080,setsar=1,fps=30[v{i}];" for i in range(len(parts)))
    fc += "".join(f"[v{i}]" for i in range(len(parts))) + f"concat=n={len(parts)}:v=1:a=0[out]"
    subprocess.run([str(FF), "-y", "-loglevel", "error", *inputs, "-filter_complex", fc, "-map", "[out]", "-c:v", "libx264",
                    "-crf", "24", "-preset", "medium", "-pix_fmt", "yuv420p", "-movflags", "+faststart", str(VID / "full-demo.mp4")], check=True)
    print("→", VID / "full-demo.mp4", [p.name for p in parts])
