# Critic round 2 (a NEW fresh agent) – review of v2 (18.0s) – score 6/10 vs a studio launch video

1. 12.50–13.10s – major – stats exit unevenly, then ~0.5s nearly empty frame. Fix: exit together, bring the dragon in ~0.3s earlier.
2. 4.25–4.60s – major – words collide while scaling in ("bythe"). Fix: reveal with a mask/offset instead of scale.
3. 4.25–5.90s – major – carrier network only faint ghost dots in shot 2. Fix: keep it visible.
4. 6.00s – minor – "What we build" fades in while the old line is still leaving. Fix: delay ~0.2s.
5. 7.25–9.25s – minor – static hold of the service grid. Fix: pulses running along connector lines.
6. 6.75–9.25s – minor – cards close to the frame edges. Fix: safe margin >= 96px.
7. 13.25–17.75s – minor – dragon cropped by frame edges. Fix: move it ~10% into frame.
8. 15.0–17.75s – minor – end card holds with little motion. Fix: network pulse on the end card.
(Also noted: small labels – partly a thumbnail artefact; real sizes are 28–32px at 1080p.)

## What was changed for v3
- #1 stats leave together at S5-0.55, network settles while the dragon starts 0.2s earlier.
- #2 words of line 2 rise from below with blur (no scale) – no more overlap.
- #3 network stays at 85% opacity above the line in shot 2.
- #4 title delayed 0.2s. #5 dashes flow along the connector lines for the whole shot.
- #6 card columns moved to 150px safe margin. #7 dragon path moved +70px into frame.
- #8 node pulse on the end card (on top of the 3.5% push-in).
Loop stopped after v3: remaining notes are small (the article's stop rule: "until each round only makes small changes").
