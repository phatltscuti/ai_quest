"""Ghép video Quest 2: thẻ tiêu đề + các đoạn terminal thật -> videos/full-demo.mp4"""
import subprocess, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent; Q2 = HERE.parent; ROOT = Q2.parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from cdp_rec import FF
from film import film_cast
VID = Q2 / "videos"
def card(name, title, sub="", secs=3.4):
    t = title.replace(":", r"\:"); s = sub.replace(":", r"\:")
    f1 = "C\:/Windows/Fonts/segoeuib.ttf"; f2 = "C\:/Windows/Fonts/segoeui.ttf"
    vf = (f"drawtext=fontfile='{f1}':text='{t}':fontcolor=white:fontsize=58:x=(w-text_w)/2:y=(h/2)-70,"
          f"drawtext=fontfile='{f2}':text='{s}':fontcolor=0xcfe3ff:fontsize=32:x=(w-text_w)/2:y=(h/2)+30")
    subprocess.run([str(FF), "-y", "-loglevel", "error", "-f", "lavfi", "-i", f"color=c=0x0d47a1:s=1920x1080:d={secs}:r=30",
                    "-vf", vf, "-c:v", "libx264", "-pix_fmt", "yuv420p", str(VID / f"{name}.mp4")], check=True)
CARDS = {"k0": ("One Agent Skill for Claude Code and Codex", "requirement-definition + code-review · same SKILL.md · real runs"),
 "k1": ("Step 1: One skill folder, validated", ".agents/skills (Codex) + .claude/skills junction (Claude Code)"),
 "k2": ("Step 2: Do both agents discover the skills?", "Claude Code, then Codex CLI"),
 "k3": ("Step 3: requirement-definition", "Same Slack message → structured requirements doc"),
 "k4": ("Step 4: code-review", "Same file with 6 seeded issues"),
 "k5": ("Done", "Comparison and the full skills in the blog post")}
ORDER = ["k0", "k1", "s1", "k2", "s2a", "s2c", "k3", "s3", "s4", "k4", "s5", "s6", "k5"]
if __name__ == "__main__":
    for k, (t, s) in CARDS.items(): card(k, t, s)
    film_cast(HERE / "casts" / "s2a.json", VID / "s2a.mp4", max_gap=6000)
    parts = [VID / f"{k}.mp4" for k in ORDER]
    inputs = sum([["-i", str(p)] for p in parts], [])
    fc = "".join(f"[{i}:v]scale=1920:1080,setsar=1,fps=30[v{i}];" for i in range(len(parts)))
    fc += "".join(f"[v{i}]" for i in range(len(parts))) + f"concat=n={len(parts)}:v=1:a=0[out]"
    subprocess.run([str(FF), "-y", "-loglevel", "error", *inputs, "-filter_complex", fc, "-map", "[out]", "-c:v", "libx264",
                    "-crf", "23", "-pix_fmt", "yuv420p", "-movflags", "+faststart", str(VID / "full-demo.mp4")], check=True)
    print("→", VID / "full-demo.mp4")
