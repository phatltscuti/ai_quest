"""Quay màn hình bằng ffmpeg (gdigrab).

  python tools/rec.py start <out.mp4>   # bắt đầu quay toàn màn hình (ghi tạm .mkv)
  python tools/rec.py stop              # dừng, chuyển .mkv -> .mp4 (H.264, faststart)
  python tools/rec.py blur <in.mp4> <out.mp4> x:y:w:h[@t0-t1] ...   # làm mờ vùng (che key)
"""
import json, os, subprocess, sys, time
from pathlib import Path

FF = Path(os.environ["LOCALAPPDATA"]) / "Microsoft/WinGet/Packages/Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe/ffmpeg-9.1-full_build/bin/ffmpeg.exe"
STATE = Path(__file__).with_name(".rec_state.json")

def start(out):
    out = Path(out).resolve(); out.parent.mkdir(parents=True, exist_ok=True)
    mkv = out.with_suffix(".mkv")
    p = subprocess.Popen([str(FF), "-y", "-loglevel", "error", "-f", "gdigrab", "-framerate", "30", "-draw_mouse", "1",
                          "-i", "desktop", "-c:v", "libx264", "-preset", "ultrafast", "-crf", "23", "-pix_fmt", "yuv420p", str(mkv)],
                         stdin=subprocess.DEVNULL, creationflags=subprocess.CREATE_NEW_PROCESS_GROUP | subprocess.DETACHED_PROCESS)
    STATE.write_text(json.dumps({"pid": p.pid, "mkv": str(mkv), "out": str(out), "t0": time.time()}))
    print("recording pid", p.pid, "->", out)

def stop():
    s = json.loads(STATE.read_text())
    subprocess.run(["taskkill", "/PID", str(s["pid"]), "/F"], capture_output=True)
    time.sleep(1.5)
    subprocess.run([str(FF), "-y", "-loglevel", "error", "-i", s["mkv"], "-c:v", "libx264", "-preset", "medium", "-crf", "22",
                    "-vf", "scale=1920:-2", "-movflags", "+faststart", s["out"]], check=True)
    os.remove(s["mkv"]); STATE.unlink()
    print(f"saved {s['out']} ({time.time() - s['t0']:.0f}s)")

def blur(src, dst, *regions):
    f, last = [], "0:v"
    for i, r in enumerate(regions):
        box, _, tr = r.partition("@")
        x, y, w, h = box.split(":")
        en = f":enable='between(t,{tr.replace('-', ',')})'" if tr else ""
        f.append(f"[{last}]split[b{i}][c{i}];[c{i}]crop={w}:{h}:{x}:{y},boxblur=20:5[k{i}];[b{i}][k{i}]overlay={x}:{y}{en}[v{i}]")
        last = f"v{i}"
    subprocess.run([str(FF), "-y", "-loglevel", "error", "-i", src, "-filter_complex", ";".join(f), "-map", f"[{last}]",
                    "-map", "0:a?", "-c:v", "libx264", "-crf", "22", "-movflags", "+faststart", dst], check=True)
    print("blurred ->", dst)

if __name__ == "__main__":
    {"start": start, "stop": stop, "blur": blur}[sys.argv[1]](*sys.argv[2:])
