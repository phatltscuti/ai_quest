import json
import os
import re
import time

from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeoutError


OUT_DIR = os.path.join(os.path.dirname(__file__), "screenshots")
REPORT_PATH = os.path.join(os.path.dirname(__file__), "trial_report.json")


def now_ms() -> int:
    return int(time.time() * 1000)


def safe_screenshot(page, filename: str) -> str:
    path = os.path.join(OUT_DIR, filename)
    page.screenshot(path=path, full_page=True)
    return filename


def try_click_by_button_name(page, names, timeout_ms=2500) -> str | None:
    for name in names:
        try:
            locator = page.get_by_role("button", name=re.compile(name, re.I))
            if locator.count() > 0:
                locator.first.click(timeout=timeout_ms)
                return name
        except Exception:
            continue
    return None


def try_fill_first_textbox(page, text: str, timeout_ms=2500) -> bool:
    # Prefer textarea first (common in design tools), then generic input/role textbox.
    try:
        ta = page.locator("textarea").first
        if ta.count() > 0:
            ta.wait_for(state="visible", timeout=timeout_ms)
            ta.fill(text)
            return True
    except Exception:
        pass

    try:
        tb = page.get_by_role("textbox").first
        if tb.count() > 0:
            tb.wait_for(state="visible", timeout=timeout_ms)
            tb.fill(text)
            return True
    except Exception:
        pass
    return False


def try_press_enter(page) -> None:
    # If an input is focused, Enter often triggers generation.
    try:
        page.keyboard.press("Enter")
    except Exception:
        pass


def main():
    os.makedirs(OUT_DIR, exist_ok=True)

    steps = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()

        # Reduce flakiness: consistent viewport for screenshot comparisons.
        page.set_viewport_size({"width": 1280, "height": 720})

        def record(step_id: str, started_ms: int, action: str, ok: bool, details: str = ""):
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

        # Step 1: Tweet content
        s1 = now_ms()
        try:
            page.goto("https://x.com/stitchbygoogle/status/2034332847893574080", wait_until="domcontentloaded")
            page.wait_for_timeout(8000)
            safe_screenshot(page, "01_x_tweet_loaded.png")
            record(
                "s1_tweet_loaded",
                s1,
                "Open X tweet and capture loaded state screenshot",
                True,
                "Page loaded; screenshot captured.",
            )
        except Exception as e:
            safe_screenshot(page, "01_x_tweet_loaded_error.png")
            record("s1_tweet_loaded", s1, "Open X tweet and capture loaded state screenshot", False, str(e))

        # Step 2: Stitch home
        s2 = now_ms()
        try:
            page.goto("https://stitch.withgoogle.com/", wait_until="domcontentloaded")
            page.wait_for_timeout(8000)
            safe_screenshot(page, "02_stitch_home.png")
            record("s2_stitch_home", s2, "Open Stitch web app home", True, "Home loaded; screenshot captured.")
        except Exception as e:
            safe_screenshot(page, "02_stitch_home_error.png")
            record("s2_stitch_home", s2, "Open Stitch web app home", False, str(e))

        # Step 3: Start new project / canvas
        s3 = now_ms()
        clicked = None
        try:
            clicked = try_click_by_button_name(
                page,
                names=[
                    "new",
                    "new project",
                    "create",
                    "start",
                    "get started",
                    "try",
                    "launch",
                ],
                timeout_ms=2500,
            )
            page.wait_for_timeout(4000)
            safe_screenshot(page, "03_stitch_after_start_attempt.png")
            record(
                "s3_start_project",
                s3,
                f"Attempt to start a new project by clicking a likely button (clicked={clicked})",
                True,
                f"Clicked button match: {clicked!r}",
            )
        except Exception as e:
            safe_screenshot(page, "03_stitch_after_start_attempt_error.png")
            record("s3_start_project", s3, "Attempt to start a new project", False, str(e))

        # Step 4: Use design agent by sending a natural-language prompt
        s4 = now_ms()
        prompt_text = (
            "Design a modern landing page for a coffee subscription app: add a hero section, three benefit cards, "
            "pricing cards, testimonials, and a sign-up CTA. Use a warm, minimalist style."
        )
        try:
            filled = try_fill_first_textbox(page, prompt_text, timeout_ms=3500)
            action_details = f"filled={filled}"

            if filled:
                # Try common generate buttons.
                gen_clicked = try_click_by_button_name(
                    page,
                    names=["generate", "create", "run", "generate ui", "make", "send"],
                    timeout_ms=2500,
                )
                if not gen_clicked:
                    try_press_enter(page)
                page.wait_for_timeout(8000)
                safe_screenshot(page, "04_stitch_after_prompt.png")
                record("s4_send_prompt", s4, f"Fill prompt textbox and trigger generation ({action_details})", True, f"gen_clicked={gen_clicked!r}")
            else:
                safe_screenshot(page, "04_stitch_prompt_box_not_found.png")
                record("s4_send_prompt", s4, "Attempt to fill prompt textbox and generate UI", False, "No visible textbox/textarea found.")
        except Exception as e:
            safe_screenshot(page, "04_stitch_after_prompt_error.png")
            record("s4_send_prompt", s4, "Attempt prompt+generation", False, str(e))

        # Step 5: Prototypes / Play
        s5 = now_ms()
        try:
            play_clicked = try_click_by_button_name(
                page,
                names=["play", "prototype", "prototypes"],
                timeout_ms=2500,
            )
            page.wait_for_timeout(6000)
            safe_screenshot(page, "05_stitch_after_play_attempt.png")
            record("s5_play_attempt", s5, f"Attempt to start prototype play mode (clicked={play_clicked})", True, f"play_clicked={play_clicked!r}")
        except Exception as e:
            safe_screenshot(page, "05_stitch_after_play_attempt_error.png")
            record("s5_play_attempt", s5, "Attempt prototype Play", False, str(e))

        # Step 6: DESIGN.md
        s6 = now_ms()
        try:
            designmd_clicked = try_click_by_button_name(
                page,
                names=["design\\.md", "design.md", "design system", "export", "import", "DESIGN\\.md", "DESIGN\\.MD"],
                timeout_ms=2500,
            )
            page.wait_for_timeout(4000)
            safe_screenshot(page, "06_stitch_after_designmd_attempt.png")
            record(
                "s6_designmd_attempt",
                s6,
                f"Attempt to access DESIGN.md/export UI (clicked={designmd_clicked})",
                True,
                f"designmd_clicked={designmd_clicked!r}",
            )
        except Exception as e:
            safe_screenshot(page, "06_stitch_after_designmd_attempt_error.png")
            record("s6_designmd_attempt", s6, "Attempt DESIGN.md access", False, str(e))

        # Step 7: Voice / vibe design
        s7 = now_ms()
        try:
            voice_clicked = try_click_by_button_name(
                page,
                names=["voice", "vibe", "microphone", "mic"],
                timeout_ms=2500,
            )
            page.wait_for_timeout(6000)
            safe_screenshot(page, "07_stitch_after_voice_attempt.png")
            record("s7_voice_attempt", s7, f"Attempt to access voice/vibe design (clicked={voice_clicked})", True, f"voice_clicked={voice_clicked!r}")
        except Exception as e:
            safe_screenshot(page, "07_stitch_after_voice_attempt_error.png")
            record("s7_voice_attempt", s7, "Attempt voice/vibe design", False, str(e))

        context.close()
        browser.close()

    report = {
        "generated_at_ms": now_ms(),
        "steps": steps,
        "screenshots_dir": OUT_DIR,
    }
    with open(REPORT_PATH, "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2)

    print(f"Wrote report to: {REPORT_PATH}")


if __name__ == "__main__":
    main()

