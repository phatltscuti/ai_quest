"""Quest 2: chạy thật 2 skill trên Claude Code và Codex CLI, ghi cast + quay video, lưu output để chấm điểm."""
import shutil, subprocess, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent; Q2 = HERE.parent; ROOT = Q2.parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from termcast import run_steps
from film import film_cast
PROJ = Q2 / "demo-project"; VID = Q2 / "videos"; CASTS = HERE / "casts"; RES = HERE / "results"
for d in (VID, CASTS, RES): d.mkdir(exist_ok=True)
CODEX = str(ROOT / "tools" / "codex.cmd")
P = r"PS D:\ai_quest\agent-skill-claude-codex\demo-project>"

def step(comment, show, run):
    disp = run.replace(CODEX, "codex").replace(str(ROOT / ".venv" / "Scripts" / "agentskills.exe"), "agentskills")
    return {"comment": comment, "show": disp, "run": run, "cwd": str(PROJ), "prompt": P}

def move_req(tag):
    src = PROJ / "docs" / "requirements"
    for f in src.glob("*.md"): shutil.copy(f, RES / f"requirements-{tag}.md"); f.unlink()

SEG = {
 "s1": [step("One skill folder, two tools: .claude/skills is a junction to .agents/skills", "tree /F .agents", "tree /F /A .agents"),
        step("Validate against the Agent Skills spec", "agentskills validate .agents/skills/code-review", rf'{ROOT}\.venv\Scripts\agentskills.exe validate .agents\skills\code-review && {ROOT}\.venv\Scripts\agentskills.exe validate .agents\skills\requirement-definition')],
 "s2": [step("Claude Code: which skills are loaded?", 'claude -p "List the project skills you can use (name: one-line purpose)"', 'claude -p "List the project skills you can use (name: one-line purpose). Only project skills from .claude/skills. Answer in English."'),
        step("Codex CLI: which skills are loaded?", 'codex exec "List the skills you can use (name: one-line purpose)"', f'{CODEX} exec --skip-git-repo-check "List the skills available to you from .agents/skills (name: one-line purpose). Do not run commands. Answer in English."')],
 "s2c": [step("Codex CLI: which skills are loaded?", 'codex exec "..."', f'{CODEX} exec --skip-git-repo-check "List the skills available to you from .agents/skills (name: one-line purpose). Do not run commands. Answer in English."')],
 "s3": [step("Claude Code + requirement-definition skill", 'claude -p "/requirement-definition feature-request.txt (answer in English)" --permission-mode acceptEdits', 'claude -p "/requirement-definition feature-request.txt (answer in English)" --permission-mode acceptEdits')],
 "s4": [step("Codex CLI + the SAME requirement-definition skill", 'codex exec --sandbox workspace-write "$requirement-definition feature-request.txt (answer in English)"', f'{CODEX} exec --skip-git-repo-check --dangerously-bypass-approvals-and-sandbox "$requirement-definition feature-request.txt (answer in English)"')],
 "s5": [step("Claude Code + code-review skill", 'claude -p "/code-review leave_service.py (answer in English)"', 'claude -p "/code-review leave_service.py (answer in English)" --allowedTools Read,Grep,Glob')],
 "s6": [step("Codex CLI + the SAME code-review skill", 'codex exec "$code-review leave_service.py (answer in English)"', f'{CODEX} exec --skip-git-repo-check --dangerously-bypass-approvals-and-sandbox "$code-review leave_service.py (answer in English)"')],
}
if __name__ == "__main__":
    for k in sys.argv[1:]:
        cast = run_steps(SEG[k], CASTS / f"{k}.json")
        out = "".join(t for st in cast["steps"] for _, t in st["events"])
        (RES / f"{k}-output.txt").write_text(out, encoding="utf-8")
        if k == "s3": move_req("claude")
        if k == "s4": move_req("codex")
        print(f"[{k}] seconds:", [s["seconds"] for s in cast["steps"]])
        film_cast(CASTS / f"{k}.json", VID / f"{k}.mp4", max_gap=6000)
