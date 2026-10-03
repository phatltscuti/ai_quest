"""Helpers: launch a console window running a .cmd, find its hwnd, capture it with PrintWindow."""
import ctypes, ctypes.wintypes as wt, subprocess, time, os
from PIL import Image

user32 = ctypes.windll.user32
gdi32 = ctypes.windll.gdi32
try:
    ctypes.windll.shcore.SetProcessDpiAwareness(2)
except Exception:
    user32.SetProcessDPIAware()

EnumProc = ctypes.WINFUNCTYPE(ctypes.c_bool, wt.HWND, wt.LPARAM)


def console_windows(cls="CASCADIA_HOSTING_WINDOW_CLASS"):
    res = []
    def cb(h, _):
        buf = ctypes.create_unicode_buffer(256)
        user32.GetClassNameW(h, buf, 256)
        if buf.value == cls and user32.IsWindowVisible(h):
            res.append(h)
        return True
    user32.EnumWindows(EnumProc(cb), 0)
    return set(res)


WT = r"D:\ai_quest\tools\windows-terminal\WindowsTerminal.exe"


def launch(cmdfile, timeout=20):
    before = console_windows()
    subprocess.Popen([WT, "cmd", "/c", os.path.abspath(cmdfile)])
    t = time.time()
    while time.time() - t < timeout:
        new = console_windows() - before
        if new:
            return new.pop()
        time.sleep(0.2)
    raise RuntimeError("no console window")


def screen_size():
    return user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)


def place(hwnd, x, y, w, h):
    user32.ShowWindow(hwnd, 9)
    user32.MoveWindow(hwnd, x, y, w, h, True)


def front(hwnd):
    user32.keybd_event(0x12, 0, 0, 0); user32.keybd_event(0x12, 0, 2, 0)  # alt trick
    user32.ShowWindow(hwnd, 9)
    user32.SetForegroundWindow(hwnd)


def capture(hwnd, path):
    r = wt.RECT(); user32.GetWindowRect(hwnd, ctypes.byref(r))
    w, h = r.right - r.left, r.bottom - r.top
    hdc = user32.GetWindowDC(hwnd)
    mdc = gdi32.CreateCompatibleDC(hdc)
    bmp = gdi32.CreateCompatibleBitmap(hdc, w, h)
    gdi32.SelectObject(mdc, bmp)
    user32.PrintWindow(hwnd, mdc, 2)  # PW_RENDERFULLCONTENT
    class BIH(ctypes.Structure):
        _fields_ = [("biSize", wt.DWORD), ("biWidth", wt.LONG), ("biHeight", wt.LONG), ("biPlanes", wt.WORD),
                    ("biBitCount", wt.WORD), ("biCompression", wt.DWORD), ("biSizeImage", wt.DWORD),
                    ("biXPelsPerMeter", wt.LONG), ("biYPelsPerMeter", wt.LONG), ("biClrUsed", wt.DWORD), ("biClrImportant", wt.DWORD)]
    bi = BIH(); bi.biSize = ctypes.sizeof(BIH); bi.biWidth = w; bi.biHeight = -h; bi.biPlanes = 1; bi.biBitCount = 32
    buf = ctypes.create_string_buffer(w * h * 4)
    gdi32.GetDIBits(mdc, bmp, 0, h, buf, ctypes.byref(bi), 0)
    img = Image.frombuffer("RGB", (w, h), buf, "raw", "BGRX", 0, 1)
    gdi32.DeleteObject(bmp); gdi32.DeleteDC(mdc); user32.ReleaseDC(hwnd, hdc)
    # trim the invisible resize border Windows 10 adds (7px left/right/bottom)
    img = img.crop((1, 1, w - 1, h - 1))
    img.save(path)
    return img


def pid_of(hwnd):
    pid = wt.DWORD(); user32.GetWindowThreadProcessId(hwnd, ctypes.byref(pid)); return pid.value
