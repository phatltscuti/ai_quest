"""Record the Windows Terminal window where you run Claude Code.

- Finds the newest Windows Terminal window, maximizes it
- Records the whole screen -> claude-terminal/terminal-session-raw.mkv
- Captures the terminal window every 3 seconds -> claude-terminal/shots/
Stop with Ctrl+C when Claude Code has finished.

Usage:  python claude-terminal/record_terminal.py
"""
import ctypes, ctypes.wintypes as wt, os, subprocess, time
import imageio_ffmpeg
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
SHOTS = os.path.join(HERE, "shots")
user32, gdi32 = ctypes.windll.user32, ctypes.windll.gdi32
try:
    ctypes.windll.shcore.SetProcessDpiAwareness(2)
except Exception:
    user32.SetProcessDPIAware()


def find_terminal():
    found = []
    cb_t = ctypes.WINFUNCTYPE(ctypes.c_bool, wt.HWND, wt.LPARAM)
    def cb(h, _):
        buf = ctypes.create_unicode_buffer(256); user32.GetClassNameW(h, buf, 256)
        if buf.value == "CASCADIA_HOSTING_WINDOW_CLASS" and user32.IsWindowVisible(h):
            found.append(h)
        return True
    user32.EnumWindows(cb_t(cb), 0)
    return found[0] if found else None  # EnumWindows is top-most first


class BIH(ctypes.Structure):
    _fields_ = [("biSize", wt.DWORD), ("biWidth", wt.LONG), ("biHeight", wt.LONG), ("biPlanes", wt.WORD),
                ("biBitCount", wt.WORD), ("biCompression", wt.DWORD), ("biSizeImage", wt.DWORD),
                ("biXPelsPerMeter", wt.LONG), ("biYPelsPerMeter", wt.LONG), ("biClrUsed", wt.DWORD), ("biClrImportant", wt.DWORD)]


def capture(hwnd, path):
    """PrintWindow: works even if another window (e.g. the render Chrome) covers the terminal."""
    r = wt.RECT(); user32.GetWindowRect(hwnd, ctypes.byref(r))
    w, h = r.right - r.left, r.bottom - r.top
    hdc = user32.GetWindowDC(hwnd); mdc = gdi32.CreateCompatibleDC(hdc)
    bmp = gdi32.CreateCompatibleBitmap(hdc, w, h); gdi32.SelectObject(mdc, bmp)
    user32.PrintWindow(hwnd, mdc, 2)
    bi = BIH(); bi.biSize = ctypes.sizeof(BIH); bi.biWidth = w; bi.biHeight = -h; bi.biPlanes = 1; bi.biBitCount = 32
    buf = ctypes.create_string_buffer(w * h * 4)
    gdi32.GetDIBits(mdc, bmp, 0, h, buf, ctypes.byref(bi), 0)
    gdi32.DeleteObject(bmp); gdi32.DeleteDC(mdc); user32.ReleaseDC(hwnd, hdc)
    Image.frombuffer("RGB", (w, h), buf, "raw", "BGRX", 0, 1).crop((1, 1, w - 1, h - 1)).save(path)


def main():
    os.makedirs(SHOTS, exist_ok=True)
    hwnd = find_terminal()
    if not hwnd:
        raise SystemExit("Open Windows Terminal first.")
    user32.ShowWindow(hwnd, 3)  # maximize
    ff = subprocess.Popen([imageio_ffmpeg.get_ffmpeg_exe(), "-y", "-v", "error", "-f", "gdigrab", "-framerate", "10",
                           "-i", "desktop", "-c:v", "libx264", "-preset", "ultrafast", "-crf", "26", "-pix_fmt", "yuv420p",
                           os.path.join(HERE, "terminal-session-raw.mkv")], stdin=subprocess.PIPE)
    print("Recording... switch to the terminal and run claude. Press Ctrl+C here when done.", flush=True)
    i = 0
    try:
        while True:
            time.sleep(3); i += 1
            capture(hwnd, os.path.join(SHOTS, f"t_{i:04d}.png"))
    except KeyboardInterrupt:
        pass
    finally:
        ff.stdin.write(b"q"); ff.stdin.flush(); ff.wait(timeout=60)
        print(f"Stopped. {i} screenshots in {SHOTS}")


if __name__ == "__main__":
    main()
