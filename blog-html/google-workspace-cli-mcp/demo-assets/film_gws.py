"""Quest: Google Workspace CLI + MCP. Chay lenh THAT, ghi cast (che secret tu .env), quay video."""
import sys
from pathlib import Path
HERE = Path(__file__).resolve().parent; Q = HERE.parent; ROOT = Q.parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from termcast import run_steps
from film import film_cast
VID = Q / "videos"; CASTS = HERE / "casts"; RES = HERE / "results"
GW = str(Path.home() / "bin" / "gwscli.exe"); PY = str(ROOT / ".venv" / "Scripts" / "python.exe")
P = r"PS D:\ai_quest\google-workspace-cli-mcp>"
def step(comment, show, run=None):
    return {"comment": comment, "show": show, "run": run or show.replace("gwscli ", GW + " ", 1), "cwd": str(HERE), "prompt": P}
SECRET = str(ROOT / ".secrets" / "gwscli_client_secret.json")
SEG = {
 "s3": [step("Installed binary (manual download from dl.google.com)", "gwscli version"),
        step("Services exposed by the CLI", "gwscli --help"),
        step("Register my agent-flagged Desktop OAuth client", r"echo Y | gwscli auth setup --oauth_client_file=client_secret.json",
             f'echo Y | {GW} auth setup --oauth_client_file="{SECRET}"'),
        step("Incremental sign-in: only the scopes the demo needs", 'gwscli auth login drive calendar tasks "gmail create_draft"',
             f'{PY} login_helper.py drive calendar tasks "gmail create_draft"'),
        step("Check the cached login", "gwscli auth status")],
 "s4": [step("Which scopes does create_file need?", "gwscli drive create_file --show-scopes | Select-String scope",
             f'{GW} drive create_file --help --show-scopes | findstr /i "scope googleapis"'),
        step("Task 1: upload a (fictional) weekly report to Drive", 'gwscli drive create_file --title "AIQuest gwscli demo - weekly report" --filePath data/aiquest-gwscli-demo-report.md --contentMimeType text/markdown',
             f'{GW} drive create_file --title "AIQuest gwscli demo - weekly report" --filePath data/aiquest-gwscli-demo-report.md --contentMimeType text/markdown'),
        step("Find it again with a structured Drive query", "gwscli drive search_files --query \"title contains 'AIQuest gwscli demo'\" --excludeContentSnippets",
             f'{GW} drive search_files --query "title contains \'AIQuest gwscli demo\'" --excludeContentSnippets'),
        step("Task 2: book a review meeting on my calendar", 'gwscli calendar create_event --summary "AIQuest demo: review gwscli report" --startTime 2026-11-26T10:00:00 --endTime 2026-11-26T10:30:00',
             f'{GW} calendar create_event --summary "AIQuest demo: review gwscli report" --startTime 2026-11-26T10:00:00 --endTime 2026-11-26T10:30:00'),
        step("Read the calendar back (only demo events)", 'gwscli calendar list_events --fullText "AIQuest demo"',
             f'{GW} calendar list_events --fullText "AIQuest demo" --startTime 2026-11-25T00:00:00 --endTime 2026-11-27T00:00:00'),
        step("Task 3: create a follow-up task", 'gwscli tasks create_task --title "AIQuest demo: send weekly report" --scheduledDate 2026-11-26',
             f'{GW} tasks create_task --title "AIQuest demo: send weekly report" --scheduledDate 2026-11-26'),
        step("Task 4: draft (not send) the status e-mail", 'gwscli gmail create_draft --to demo@example.com --subject "AIQuest demo: weekly report" --body "..."',
             f'{GW} gmail create_draft --to demo@example.com --subject "AIQuest demo: weekly report" --body "Hi, the weekly report for the fictional Sample Leave App is in Drive: AIQuest gwscli demo - weekly report. This is a demo draft created by gwscli."')],
}

SEG["s5"] = [
  step("Same backend, raw MCP: handshake + tools/list on the Drive MCP server", "python mcp_probe.py drive", f"{PY} mcp_probe.py drive"),
  step("tools/call through MCP (read-only search)", "python mcp_probe.py drive search_files \"query=title contains 'AIQuest'\"",
       PY + """ mcp_probe.py drive search_files "query=title contains 'AIQuest'\""""),
  step("Calendar and Tasks MCP servers", "python mcp_probe.py calendar list_calendars", f"{PY} mcp_probe.py calendar list_calendars"),
  step("Tasks MCP server", "python mcp_probe.py tasks list_task_lists", f"{PY} mcp_probe.py tasks list_task_lists"),
  step("Register the remote MCP server in Claude Code (agent-flagged OAuth client)",
       "claude mcp add --transport http gws-drive https://drivemcp.googleapis.com/mcp/v1 --client-id **** --client-secret --callback-port 8765",
       f'claude mcp add --transport http gws-drive https://drivemcp.googleapis.com/mcp/v1 --client-id %GWS_CLIENT_ID% --client-secret --callback-port 8765'),
  step("Claude Code sees the server", "claude mcp list", "claude mcp list"),
  step("Install the gwscli agent skills for Claude Code", "gwscli skills install --dir .claude/skills", f"{GW} skills install --dir .claude/skills"),
  step("What was installed", "tree /F .claude", "tree /F /A .claude"),
]

import os
for ln in (ROOT / ".env").read_text().splitlines():
    if ln.startswith("GWS_CLIENT_ID="): os.environ["GWS_CLIENT_ID"] = ln.split("=", 1)[1].strip()
    if ln.startswith("GWS_CLIENT_SECRET="): os.environ["MCP_CLIENT_SECRET"] = ln.split("=", 1)[1].strip()
if __name__ == "__main__":
    for k in [a for a in sys.argv[1:] if not a.startswith("--")]:
        if k == "s5": pass
        cast = run_steps(SEG[k], CASTS / f"{k}.json")
        (RES / f"{k}-output.txt").write_text("".join(t for st in cast["steps"] for _, t in st["events"]), encoding="utf-8")
        print(f"[{k}] seconds:", [s["seconds"] for s in cast["steps"]])
        if "--nofilm" not in sys.argv: film_cast(CASTS / f"{k}.json", VID / f"{k}.mp4", max_gap=5000)

SEG["s6"] = [step("Claude Code + the installed gwscli skill: a natural-language task",
  'claude -p "Use the gwscli skill: find my Drive files whose title contains AIQuest, then list my Google Tasks lists. Report exactly what happened."',
  'claude -p "Use the gwscli skill: find my Drive files whose title contains AIQuest, then list my Google Tasks lists. Report exactly what happened, including any error text. Do not try to change any settings." --allowedTools "Bash(gwscli:*)" "Bash(%USERPROFILE%\bin\gwscli.exe:*)" Read Skill')]
