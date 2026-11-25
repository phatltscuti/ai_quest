import film_gws as F
from termcast import run_steps
cast = run_steps(F.SEG["s6"], F.CASTS / "s6.json")
(F.RES / "s6-output.txt").write_text("".join(t for st in cast["steps"] for _, t in st["events"]), encoding="utf-8")
print("[s6] seconds:", [s["seconds"] for s in cast["steps"]])
