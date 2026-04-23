import json
import os
import time

from playwright.sync_api import sync_playwright


BASE_DIR = os.path.dirname(__file__)
OUT_DIR = os.path.join(BASE_DIR, "screenshots_v3")
REPORT_PATH = os.path.join(BASE_DIR, "trial_report_v3.json")


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


def click_xy(page, x: int, y: int, steps, step_id: str):
    s = now_ms()
    try:
        page.mouse.click(x, y, delay=30)
        page.wait_for_timeout(1500)
        return True, now_ms() - s
    except Exception as e:
        record(steps, step_id, s, f"Click at ({x},{y})", False, str(e))
        return False, 0


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    steps = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()

        page.set_viewport_size({"width": 1280, "height": 720})

        # 1) Open home
        s1 = now_ms()
        try:
            page.goto("https://stitch.withgoogle.com/", wait_until="domcontentloaded")
            page.wait_for_timeout(9000)
            safe_screenshot(page, "16_home.png")
            record(steps, "s1_home", s1, "Open Stitch home", True)
        except Exception as e:
            safe_screenshot(page, "16_home_error.png")
            record(steps, "s1_home", s1, "Open Stitch home", False, str(e))

        # 2) Try clicking the top-right Try now button by coordinates
        s2 = now_ms()
        try:
            # Coordinates are tuned to 1280x720 viewport used above.
            for (x, y) in [(1160, 40), (1130, 40), (1100, 40)]:
                page.mouse.click(x, y, delay=20)
                page.wait_for_timeout(2000)
            safe_screenshot(page, "17_after_try_now_coordinate_click.png")
            record(steps, "s2_try_now_click", s2, "Coordinate-click 'Try now' (multiple attempts)", True)
        except Exception as e:
            safe_screenshot(page, "17_after_try_now_coordinate_click_error.png")
            record(steps, "s2_try_now_click", s2, "Coordinate-click 'Try now'", False, str(e))

        # 3) Click in the prompt card area and attempt typing
        s3 = now_ms()
        try:
            # Click inside the big card (rough center lower half)
            for (x, y) in [(640, 520), (640, 560), (480, 520), (800, 520)]:
                page.mouse.click(x, y, delay=20)
                page.wait_for_timeout(1000)

            prompt_text = (
                "Coffee subscription app landing page with hero, benefits, pricing cards, testimonials, "
                "and a sign-up CTA. Minimal warm style."
            )
            page.keyboard.type(prompt_text, delay=10)
            page.keyboard.press("Enter")
            page.wait_for_timeout(8000)
            safe_screenshot(page, "18_after_click_and_type.png")
            record(steps, "s3_click_type", s3, "Click prompt card and type prompt then Enter", True)
        except Exception as e:
            safe_screenshot(page, "18_after_click_and_type_error.png")
            record(steps, "s3_click_type", s3, "Click prompt card and type prompt then Enter", False, str(e))

        # 4) Attempt to click likely bottom action icons/buttons
        s4 = now_ms()
        try:
            # These are guess positions near the bottom-right of the card in the screenshot.
            for (x, y) in [(930, 640), (1010, 640), (1090, 640), (860, 640)]:
                page.mouse.click(x, y, delay=20)
                page.wait_for_timeout(1500)
            safe_screenshot(page, "19_after_bottom_icon_clicks.png")
            record(steps, "s4_bottom_clicks", s4, "Coordinate-click bottom icons/buttons", True)
        except Exception as e:
            safe_screenshot(page, "19_after_bottom_icon_clicks_error.png")
            record(steps, "s4_bottom_clicks", s4, "Coordinate-click bottom icons/buttons", False, str(e))

        # 5) Attempt prototypes/Play (if any button appears): click near top-right button area
        s5 = now_ms()
        try:
            # Try to click around where a Play button would plausibly be (right side mid).
            for (x, y) in [(1080, 280), (1080, 320), (980, 280)]:
                page.mouse.click(x, y, delay=20)
                page.wait_for_timeout(1500)
            safe_screenshot(page, "20_after_play_click_coords.png")
            record(steps, "s5_play_coords", s5, "Coordinate-click potential Play/prototype controls", True)
        except Exception as e:
            safe_screenshot(page, "20_after_play_click_coords_error.png")
            record(steps, "s5_play_coords", s5, "Coordinate-click potential Play/prototype controls", False, str(e))

        # 6) Attempt voice: click near where a mic might be if visible (right lower corner)
        s6 = now_ms()
        try:
            for (x, y) in [(1120, 650), (1050, 650), (1200, 650)]:
                page.mouse.click(x, y, delay=20)
                page.wait_for_timeout(1000)
            safe_screenshot(page, "21_after_voice_coords.png")
            record(steps, "s6_voice_coords", s6, "Coordinate-click potential voice/mic controls", True)
        except Exception as e:
            safe_screenshot(page, "21_after_voice_coords_error.png")
            record(steps, "s6_voice_coords", s6, "Coordinate-click potential voice/mic controls", False, str(e))

        context.close()
        browser.close()

    report = {"generated_at_ms": now_ms(), "steps": steps, "screenshots_dir": OUT_DIR}
    with open(REPORT_PATH, "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2)

    print(f"Wrote report to: {REPORT_PATH}")


if __name__ == "__main__":
    main()

