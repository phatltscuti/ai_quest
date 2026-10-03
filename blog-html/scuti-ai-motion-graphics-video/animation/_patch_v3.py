# one-off patch: applies critic round-2 fixes (v2 -> v3) to scuti-intro.html
from pathlib import Path
f = Path(__file__).with_name("scuti-intro.html")
c = f.read_text(encoding="utf-8")
rep = [
    # 2: mask-like rise instead of scale
    (".from('#h2 .w', {scale:2.4, opacity:0, filter:'blur(18px)', duration:.55, ease:'expo.out', stagger:.11}, S2)",
     ".from('#h2 .w', {yPercent:70, opacity:0, filter:'blur(14px)', duration:.55, ease:'expo.out', stagger:.11}, S2)"),
    # 3: network visible in shot 2
    ("{scale:.35, rotation:0, opacity:.35, y:-300, duration:1.4,", "{scale:.4, rotation:0, opacity:.85, y:-270, duration:1.4,"),
    # 4: title delay
    ("{opacity:1, y:0, duration:.5, ease:'power3.out', immediateRender:false}, S3)", "{opacity:1, y:0, duration:.5, ease:'power3.out', immediateRender:false}, S3+.2)"),
    # 5: flowing dashes on connectors
    ("tl.to('#net', {rotation:24, duration:3.6, ease:'sine.inOut'}, S3)",
     "tl.to('#net', {rotation:24, duration:3.6, ease:'sine.inOut'}, S3)\n  .to(linkEls, {strokeDashoffset:-160, duration:3.6, ease:'none'}, S3)"),
    # 6: safe margins
    ("x:110,  y:220", "x:150,  y:220"), ("x:1310, y:220", "x:1270, y:220"),
    ("x:110,  y:540", "x:150,  y:540"), ("x:1310, y:540", "x:1270, y:540"),
    # 1: stats leave together, network earlier
    ("tl.to('.stat', {y:80, opacity:0, duration:.35, ease:'power3.in', stagger:.05}, S5-.35)",
     "tl.to('.stat', {y:80, opacity:0, duration:.35, ease:'power3.in'}, S5-.55)"),
    ("  .to('#src', {opacity:0, duration:.25}, S5-.35)", "  .to('#src', {opacity:0, duration:.25}, S5-.55)"),
    ("rotation:360, duration:.8, ease:'expo.inOut'}, S5-.3)", "rotation:360, duration:.8, ease:'expo.inOut'}, S5-.5)"),
    ("tl.set('#dragonHead', {opacity:1}, S5)\n  .to(headPos, {p:1, duration:1.5, ease:'power2.inOut', onUpdate:placeHead}, S5)\n  .to(trail, {strokeDashoffset:0, duration:1.5, ease:'power2.inOut'}, S5)",
     "tl.set('#dragonHead', {opacity:1}, S5-.2)\n  .to(headPos, {p:1, duration:1.7, ease:'power2.inOut', onUpdate:placeHead}, S5-.2)\n  .to(trail, {strokeDashoffset:0, duration:1.7, ease:'power2.inOut'}, S5-.2)"),
    # 8: end-card node pulse
    ("  .to('#fade', {opacity:1, duration:.4, ease:'power1.in'}, D-0.4);",
     "  .to(nodes, {scale:1.3, duration:.35, yoyo:true, repeat:1, ease:'sine.inOut', stagger:.08}, S5+3.0)\n  .to('#fade', {opacity:1, duration:.4, ease:'power1.in'}, D-0.4);"),
]
for a, b in rep:
    assert a in c, a
    c = c.replace(a, b)
# 7: dragon further into frame (both trail paths)
old = 'd="M -150 1150 C 150 950, 420 1000, 330 820 S 60 640, 150 560 S 220 520, 250 520"'
assert c.count(old) == 2
c = c.replace(old, 'd="M -80 1150 C 220 950, 490 1000, 400 820 S 130 640, 220 560 S 290 520, 320 520"')
f.write_text(c, encoding="utf-8")
print("patched v3")
