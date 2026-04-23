import json
import os
import time

from playwright.sync_api import sync_playwright


BASE_DIR = os.path.dirname(__file__)
OUT_DIR = os.path.join(BASE_DIR, "screenshots_v4")
REPORT_PATH = os.path.join(BASE_DIR, "trial_report_v4_guest.json")


def now_ms() -> int:
    return int(time.time() * 1000)


def safe_screenshot(page, filename: str) -> str:
    path = os.path.join(OUT_DIR, filename)
    page.screenshot(path=path, full_page=True)
    return filename


def record(steps, step_id: str, started_ms: int, action: str, ok: bool, details: str = ""):
    steps.append(
        {
            "id": step_id,
            "started_ms": started_ms,
            "ended_ms": now_ms(),
            "action": action,
            "ok": ok,
            "details": details,
        }
    )


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    steps = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()

        page.set_viewport_size({"width": 1280, "height": 720})

        s1 = now_ms()
        try:
            page.goto("https://stitch.withgoogle.com/", wait_until="domcontentloaded")
            page.wait_for_timeout(9000)
            safe_screenshot(page, "22_home.png")
            record(steps, "s1_home", s1, "Open Stitch home", True)
        except Exception as e:
            safe_screenshot(page, "22_home_error.png")
            record(steps, "s1_home", s1, "Open Stitch home", False, str(e))

        # Trigger sign-in
        s2 = now_ms()
        try:
            for (x, y) in [(1160, 40), (1130, 40), (1100, 40)]:
                page.mouse.click(x, y, delay=20)
                page.wait_for_timeout(2000)
            page.wait_for_timeout(3000)
            safe_screenshot(page, "23_after_try_now.png")
            record(steps, "s2_try_now", s2, "Coordinate-click 'Try now' to reach sign-in", True)
        except Exception as e:
            safe_screenshot(page, "23_after_try_now_error.png")
            record(steps, "s2_try_now", s2, "Coordinate-click 'Try now'", False, str(e))

        # Try to click 'Guest mode' help link
        s3 = now_ms()
        clicked = False
        try:
            # Look for visible text that contains "Guest mode".
            guest_text = page.get_by_text("Guest mode", exact=False)
            if guest_text.count() > 0:
                guest_text.first.click(timeout=2000)
                clicked = True
                page.wait_for_timeout(6000)
            safe_screenshot(page, "24_after_guest_mode_link_attempt.png")
            record(
                steps,
                "s3_guest_mode_link",
                s3,
                "Click 'Guest mode' link if present",
                True,
                f"clicked={clicked}",
            )
        except Exception as e:
            safe_screenshot(page, "24_after_guest_mode_link_attempt_error.png")
            record(steps, "s3_guest_mode_link", s3, "Click 'Guest mode' link if present", False, str(e))

        context.close()
        browser.close()

    report = {"generated_at_ms": now_ms(), "steps": steps, "screenshots_dir": OUT_DIR}
    with open(REPORT_PATH, "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2)

    print(f"Wrote report to: {REPORT_PATH}")


if __name__ == "__main__":
    main()

