import json
import os
import re
import time

from playwright.sync_api import sync_playwright


BASE_DIR = os.path.dirname(__file__)
OUT_DIR = os.path.join(BASE_DIR, "screenshots_v2")
REPORT_PATH = os.path.join(BASE_DIR, "trial_report_v2.json")


def now_ms() -> int:
    return int(time.time() * 1000)


def safe_screenshot(page, filename: str) -> str:
    path = os.path.join(OUT_DIR, filename)
    page.screenshot(path=path, full_page=True)
    return filename


def try_click_by_button_name(page, names, timeout_ms=3000) -> str | None:
    for name in names:
        try:
            locator = page.get_by_role("button", name=re.compile(name, re.I))
            if locator.count() > 0:
                locator.first.click(timeout=timeout_ms)
                return name
        except Exception:
            continue
    return None


def try_click_by_text_container(page, text: str, timeout_ms=2500) -> bool:
    try:
        loc = page.locator(f"text={text}").first
        if loc.count() > 0:
            loc.click(timeout=timeout_ms)
            return True
    except Exception:
        pass
    return False


def try_fill_first_textbox(page, text: str, timeout_ms=3500) -> bool:
    # Prefer textarea, then textbox.
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


def main():
    os.makedirs(OUT_DIR, exist_ok=True)

    steps = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()

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

        # Step A: Open Stitch home
        sA = now_ms()
        try:
            page.goto("https://stitch.withgoogle.com/", wait_until="domcontentloaded")
            page.wait_for_timeout(8000)
            safe_screenshot(page, "08_stitch_home.png")
            record("sA_stitch_home", sA, "Open Stitch home", True)
        except Exception as e:
            safe_screenshot(page, "08_stitch_home_error.png")
            record("sA_stitch_home", sA, "Open Stitch home", False, str(e))

        # Step B: Click the visible Try now button
        sB = now_ms()
        try:
            clicked = try_click_by_button_name(page, names=["try now", "try"])
            page.wait_for_timeout(8000)
            safe_screenshot(page, "09_after_try_now_click.png")
            record(
                "sB_try_now",
                sB,
                "Click 'Try now' then wait",
                True,
                f"clicked={clicked!r}",
            )
        except Exception as e:
            safe_screenshot(page, "09_after_try_now_click_error.png")
            record("sB_try_now", sB, "Click 'Try now' then wait", False, str(e))

        # Step C: Attempt to reveal/activate the prompt area by clicking the card question text
        sC = now_ms()
        prompt_question = "What native mobile app shall we design?"
        try:
            activated = try_click_by_text_container(page, prompt_question)
            page.wait_for_timeout(5000)
            safe_screenshot(page, "10_after_click_prompt_question.png")
            # Try to find a textbox/textarea after clicking.
            filled = try_fill_first_textbox(
                page,
                "Design a landing page for a coffee subscription app with hero, benefits, pricing cards, testimonials, and a sign-up CTA.",
            )
            safe_screenshot(page, "11_after_prompt_fill_attempt.png")
            record(
                "sC_prompt_activate_and_fill",
                sC,
                "Click prompt card question and attempt fill textbox/textarea",
                True,
                f"activated={activated}, filled={filled}",
            )
        except Exception as e:
            safe_screenshot(page, "10_after_click_prompt_question_error.png")
            record("sC_prompt_activate_and_fill", sC, "Click prompt card question and attempt fill", False, str(e))

        # Step D: Attempt to click a generate/run button
        sD = now_ms()
        try:
            gen_clicked = try_click_by_button_name(
                page,
                names=["generate", "create", "run", "make", "send"],
            )
            page.wait_for_timeout(8000)
            safe_screenshot(page, "12_after_generate_attempt.png")
            record("sD_generate_click", sD, "Attempt generation via button", True, f"gen_clicked={gen_clicked!r}")
        except Exception as e:
            safe_screenshot(page, "12_after_generate_attempt_error.png")
            record("sD_generate_click", sD, "Attempt generation via button", False, str(e))

        # Step E: Attempt to click Play / Prototypes if visible
        sE = now_ms()
        try:
            play_clicked = try_click_by_button_name(page, names=["play", "prototype", "prototypes", "prototyping"])
            page.wait_for_timeout(8000)
            safe_screenshot(page, "13_after_play_attempt.png")
            record("sE_play_click", sE, "Attempt prototypes/Play", True, f"play_clicked={play_clicked!r}")
        except Exception as e:
            safe_screenshot(page, "13_after_play_attempt_error.png")
            record("sE_play_click", sE, "Attempt prototypes/Play", False, str(e))

        # Step F: Attempt to locate DESIGN.md export entry
        sF = now_ms()
        try:
            designmd_clicked = try_click_by_button_name(
                page,
                names=["design.md", "DESIGN.md", "DESIGN\\.md", "design system", "export", "import"],
            )
            page.wait_for_timeout(5000)
            safe_screenshot(page, "14_after_designmd_attempt.png")
            record("sF_designmd_click", sF, "Attempt access DESIGN.md / export UI", True, f"designmd_clicked={designmd_clicked!r}")
        except Exception as e:
            safe_screenshot(page, "14_after_designmd_attempt_error.png")
            record("sF_designmd_click", sF, "Attempt access DESIGN.md / export UI", False, str(e))

        # Step G: Attempt voice/vibe button
        sG = now_ms()
        try:
            voice_clicked = try_click_by_button_name(page, names=["voice", "vibe", "microphone", "mic"])
            page.wait_for_timeout(5000)
            safe_screenshot(page, "15_after_voice_attempt.png")
            record("sG_voice_click", sG, "Attempt voice/vibe UI", True, f"voice_clicked={voice_clicked!r}")
        except Exception as e:
            safe_screenshot(page, "15_after_voice_attempt_error.png")
            record("sG_voice_click", sG, "Attempt voice/vibe UI", False, str(e))

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

