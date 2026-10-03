# Prompts – Scuti AI motion graphics (Claude Code + HTML/GSAP)

Adapted from the prompt structure in Chris (@everestchris6) "how to run an ai video agency (FULL GUIDE)" on X.
Run them in order inside Claude Code, in an empty folder.

## Prompt 1 – Storyboard first (do not build yet)

```text
plan a 19 second brand intro video for Scuti AI.

- what they do: Vietnam-based system development company specializing in generative AI
  (Gen AI consulting, generative AI OCR, secure RAG, Dify support, software outsourcing)
- who the viewer is: prospective clients and new team members
- what we want people to do at the end: remember the brand and visit scuti.asia
- facts: ONLY use what is on https://scuti.asia (open it and read it). brand = red on dark, mascot = red dragon
- write a storyboard, shot by shot, with what's on screen, what moves, how long it holds, and how it gets to the next shot
- pick ONE object that carries the story across all shots (use the 5-node network from the logo)
- no empty frames and nothing that just sits there. every shot should be moving into the next one
- don't invent testimonials, ratings, prices, savings or results
save it as animation/storyboard.md
```

## Prompt 2 – Build the video as one HTML page

```text
build the storyboard as a single HTML page: animation/scuti-intro.html

- 1920x1080 stage, GSAP 3 from cdnjs, Google font "Be Vietnam Pro"
- ONE paused master timeline (window.__tl) and window.seekTo(t) so it can be rendered frame by frame
- apply these motion rules:
  * the thing in front becomes the transition (title/logo flies toward the camera into the next shot)
  * one main movement with smaller overlapping ones (particles, grid drift, glows)
  * speed changes: hold to read -> leave fast (power3.in) -> arrive slow (expo.out / back.out)
- rebuild the logo in SVG (red network + white "Scuti Ai") so it reads on dark
- draw a stylised red dragon in SVG that flies in along a curve before the logo lockup
- add a preview bar (play/pause/scrub) that is hidden when ?render=1
```

## Prompt 3 – Render (HyperFrames idea, done with Playwright)

```text
write animation/render_frames.py:
- open scuti-intro.html?render=1 in Chrome via Playwright at 1920x1080
- for every frame at 30fps: seekTo(t), screenshot jpeg
- ffmpeg: frames -> H.264 yuv420p mp4, add a calm generated ambient pad (no hype music), fade in/out
- also export a contact sheet so a reviewer can see the whole video at once
- a --stills option to grab single frames for quick checks
```

## Prompt 4 – Fresh critic (gauntlet loop) – verbatim prompt used

```text
You're reviewing a video you did not build. Be honest.
- here are timestamped contact sheets of the rendered video, the brief, and the motion patterns we aim for
- watch the whole thing and list every problem, biggest first
- look hard for empty frames, shots that hold too long, uneven spacing, text that collides or flies
  through other text, text visible before it should be, and anything that looks physically wrong
- give each problem a time in the video so it can be found
- don't suggest fixes that change what the video is about
```

## Prompt 5 – Fix loop

```text
here are the critic's notes. fix the biggest problems only, re-render stills at the listed times to verify,
then do a full render and run a NEW critic. stop when the remaining notes are small.
```
