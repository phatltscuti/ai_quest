"""Run a real Claude Code session in Windows Terminal, capture the window every few seconds, record the desktop."""
import glob, json, os, subprocess, sys, time
import imageio_ffmpeg
import termcap as tc

HERE = os.path.dirname(os.path.abspath(__file__))
SHOTS = os.path.join(HERE, "shots"); os.makedirs(SHOTS, exist_ok=True)
PROJ_TR = os.path.expanduser(r"~\.claude\projects\D--ai-quest-blog-html-scuti-ai-motion-graphics-video")
LOG = open(os.path.join(HERE, "drive.log"), "a", encoding="utf-8")

PROMPT_A = ("Gauntlet round 3 for our Scuti AI intro video (animation/scuti-intro.html, 18s). "
            "Step 1: grab stills every 1.5s from 0.5s to 17.5s with python animation/render_frames.py --stills ... "
            "Step 2: tile them into ONE timestamped contact sheet at animation/contact-sheet-round3.png. "
            "Step 3: spawn a NEW subagent that has not seen the build, give it only the contact sheet, animation/storyboard.md "
            "and the motion rules in animation/prompts.md, with this brief: You are reviewing a video you did not build. Be honest. "
            "List every problem, biggest first, each with a time in the video and a severity (major or minor): empty frames, "
            "shots that hold too long, text that collides, text visible too early. Do not suggest changing what the video is about. "
            "Step 4: save its answer to animation/critic-notes-v3.md and show me the list. Do not edit the animation yet.")

PROMPT_B = ("Here are the critic notes. Fix the major problems only in animation/scuti-intro.html (keep it 18s, keep the story), "
            "re-grab stills at the listed times to verify, then do the full render with python -u animation/render_frames.py "
            "(about 1-2 minutes, use a long timeout) and check the mp4 with ffmpeg: duration, resolution, fps, audio. "
            "Finish with a short list of what changed.")


def log(*a):
    s = time.strftime("%H:%M:%S ") + " ".join(str(x) for x in a)
    print(s, flush=True); LOG.write(s + "\n"); LOG.flush()


def sendkeys_escape(s):
    return "".join("{%s}" % c if c in "+^%~(){}[]" else c for c in s)


def type_prompt(hwnd, text):
    tc.front(hwnd); time.sleep(0.8)
    esc = sendkeys_escape(text).replace("'", "''")
    ps = ("$w = New-Object -ComObject WScript.Shell; "
          f"$w.SendKeys('{esc}'); Start-Sleep -Milliseconds 800; $w.SendKeys('{{ENTER}}')")
    subprocess.run(["powershell", "-NoProfile", "-Command", ps], check=True)


def newest_transcript(since):
    fs = [f for f in glob.glob(os.path.join(PROJ_TR, "*.jsonl")) if os.path.getmtime(f) >= since]
    return max(fs, key=os.path.getmtime) if fs else None


def turn_done(path, n_user_prompts):
    """True when the transcript has n_user_prompts real prompts and the last assistant message ended its turn."""
    if not path: return False
    lines = []
    with open(path, encoding="utf-8") as f:
        for ln in f:
            try: lines.append(json.loads(ln))
            except Exception: pass
    prompts = 0; last = None
    for e in lines:
        if e.get("isSidechain"): continue
        t = e.get("type")
        if t == "user":
            c = e.get("message", {}).get("content")
            if isinstance(c, str) or (isinstance(c, list) and any(x.get("type") == "text" for x in c if isinstance(x, dict))):
                if not e.get("isMeta"): prompts += 1
            last = e
        elif t == "assistant":
            last = e
    if prompts < n_user_prompts or not last or last.get("type") != "assistant": return False
    return last.get("message", {}).get("stop_reason") == "end_turn" and time.time() - os.path.getmtime(path) > 12


def main():
    cmdfile = os.path.join(HERE, "session.cmd")
    clear = " ".join(["CLAUDECODE", "CLAUDE_CODE_CHILD_SESSION", "CLAUDE_CODE_SESSION_ID", "CLAUDE_PID", "CLAUDE_CODE_ENTRYPOINT",
                      "CLAUDE_CODE_EXECPATH", "CLAUDE_CODE_MESSAGING_TOKEN", "CLAUDE_CODE_MESSAGING_SOCKET",
                      "CLAUDE_CODE_SESSION_ATTENDED", "CLAUDE_EFFORT"])
    with open(cmdfile, "w", encoding="ascii") as f:
        f.write("@echo off\r\n")
        f.write(f"for %%v in ({clear}) do set %%v=\r\n")
        f.write("cd /d D:\\ai_quest\\blog-html\\scuti-ai-motion-graphics-video\r\n")
        f.write(f'claude --permission-mode auto "{PROMPT_A}"\r\n')

    rec = os.path.join(HERE, "terminal-session-raw.mkv")
    ff = subprocess.Popen([imageio_ffmpeg.get_ffmpeg_exe(), "-y", "-v", "error", "-f", "gdigrab", "-framerate", "10",
                           "-draw_mouse", "1", "-i", "desktop", "-c:v", "libx264", "-preset", "ultrafast", "-crf", "26",
                           "-pix_fmt", "yuv420p", rec], stdin=subprocess.PIPE)
    t_start = time.time()
    time.sleep(2)
    hwnd = tc.launch(cmdfile)
    tc.place(hwnd, 0, 0, 1920, 1030); tc.front(hwnd)
    log("launched", hwnd)
    i = 0; phase = "A"; deadline = time.time() + 75 * 60
    try:
        while time.time() < deadline:
            time.sleep(3); i += 1
            tc.capture(hwnd, os.path.join(SHOTS, f"{phase}_{i:04d}.png"))
            tr = newest_transcript(t_start)
            if os.path.exists(os.path.join(HERE, "stop.flag")): log("stop flag"); break
            if phase == "A" and (turn_done(tr, 1) or os.path.exists(os.path.join(HERE, "next.flag"))):
                log("turn A done", tr); time.sleep(5)
                tc.capture(hwnd, os.path.join(SHOTS, f"A_{i:04d}_end.png"))
                type_prompt(hwnd, PROMPT_B); phase = "B"; log("prompt B sent")
                time.sleep(20)
            elif phase == "B" and turn_done(tr, 2):
                log("turn B done"); time.sleep(6)
                tc.front(hwnd); time.sleep(2)
                tc.capture(hwnd, os.path.join(SHOTS, f"B_{i:04d}_end.png"))
                time.sleep(4)
                break
    finally:
        ff.stdin.write(b"q"); ff.stdin.flush(); ff.wait(timeout=60)
        log("recording stopped; elapsed", round(time.time() - t_start))
        log("window left open, pid", tc.pid_of(hwnd))


if __name__ == "__main__":
    main()
