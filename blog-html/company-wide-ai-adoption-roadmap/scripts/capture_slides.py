"""Open both Speaker Deck decks in real Chrome, flip slide by slide with ArrowRight
and screenshot the key slides into ../images/step-XX-*.png.
Usable standalone (no video) or imported by record_demo.py (with video)."""
import sys, os
sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
IMG = os.path.join(HERE, "..", "images")

DECKS = [
  ("https://speakerdeck.com/lmi/pek2026-link-and-motivation", 45, "lmi", {
      1: "cover", 4: "results", 9: "two-walls", 12: "narrow-deep", 13: "adoption-wall-reasons",
      14: "ax-structure", 17: "66-days", 20: "outcome-map", 27: "guardrail-levels",
      32: "security-team", 42: "fit-journey", 44: "platform-engineering"}),
  ("https://speakerdeck.com/yoshikikonishi_/smarthr-no-zensha-ai-suishin-ha-dou-hajimata-ka", 20, "smarthr", {
      1: "cover", 8: "ai-ops-background", 9: "mission", 10: "5as", 12: "enabler-roles",
      13: "operating-model", 14: "monitoring", 18: "three-walls", 20: "summary"}),
]

def flip_deck(pg, url, last, prefix, keys, counter, step_ms=380, hold_ms=1600):
    pg.goto(url, wait_until="domcontentloaded")
    pg.wait_for_timeout(4000)
    player = pg.locator("iframe.speakerdeck-iframe")
    player.scroll_into_view_if_needed()
    box = player.bounding_box()
    # focus the player by clicking its "previous" arrow area (no-op on slide 1)
    pg.mouse.move(box["x"] + 35, box["y"] + box["height"] - 40)
    pg.wait_for_timeout(600)
    pg.mouse.click(box["x"] + 35, box["y"] + box["height"] - 40)
    pg.mouse.move(box["x"] + box["width"] + 60, box["y"] + 40)   # move away, hide controls
    slide = 1
    while True:
        if slide in keys:
            pg.wait_for_timeout(hold_ms)
            counter[0] += 1
            name = f"step-{counter[0]:02d}-{prefix}-s{slide:02d}-{keys[slide]}.png"
            player.screenshot(path=os.path.join(IMG, name))
            print("saved", name)
            pg.wait_for_timeout(hold_ms // 2)
        if slide >= max(keys) or slide >= last:
            break
        pg.keyboard.press("ArrowRight")
        slide += 1
        pg.wait_for_timeout(step_ms)
    pg.wait_for_timeout(800)

def run_decks(pg, counter):
    for url, last, prefix, keys in DECKS:
        flip_deck(pg, url, last, prefix, keys, counter)

if __name__ == "__main__":
    from playwright.sync_api import sync_playwright
    os.makedirs(IMG, exist_ok=True)
    with sync_playwright() as p:
        b = p.chromium.launch(channel="chrome", headless=False)
        pg = b.new_page(viewport={"width": 1440, "height": 900})
        run_decks(pg, [0])
        b.close()
