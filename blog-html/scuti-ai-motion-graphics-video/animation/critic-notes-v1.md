# Critic round 1 (fresh agent, did not see the build) – review of v1 (19.0s)

Input: timestamped contact sheets critic-v1-01.png / critic-v1-02.png (4 fps) + brief + motion rules.

1. 14.25–15.75s – dead air and the carrier object disappears; tiny dragon crawls in from the corner. Fix: keep the network on screen as stats leave, overlap the dragon entry, gap <= 0.25s.
2. 4.5–6.25s – "by the power of Gen AI." frozen ~1.75s. Fix: trim hold to ~1s or add a slow push-in.
3. 6.5–6.75s – near-empty frame; "What we build" jammed against the top edge. Fix: start cards as the line exits, title top margin >= 80px.
4. 7.0–7.5s – card text visible while cards slide out over the network lines. Fix: hide card content until each card lands.
5. 7.75–10.5s – service grid holds too long, descriptions too small, bottom card near the frame edge. Fix: hold ~1.5–2s, text >= 28px, even spacing with safe margins.
6. 10.75–11.0s – messy exit, leftover "Software Outsourcing" chip. Fix: pull all cards in together, cut on the network scale-up.
7. 11.25–11.75s – "Founded" counts up 1991->2015 (wrong for a year); counters start at different times. Fix: show the year fixed; stagger evenly ~80ms.
8. 0.75–1.75s – network draws over "We make"; words split vertically. (Also found by the builder: line-1 wrap bug.)
9. 4.0s – fly-through lines cut across "by the". Fix: bring the text in after the lines clear.
10. 16.0–16.5s – stray red dots at the top, network crowds the whiskers, wordmark appears grey/split, lockup pushed left. Fix: dots join cleanly, more space, full-colour reveal, rebalance the lockup.

## What was changed for v2
- Timeline restructured with shot-start variables (S2..S5); total 18.0s.
- #1: network shrinks into its logo position while the stats leave and stays visible; the dragon starts 0.25s after.
- #2/#9: line 2 starts after the fly-through (4.15s), hold trimmed, slow push-in added.
- #3/#4/#5/#6: title top 100px; cards fly out as solid chips, content fades in on landing; text 28px+; new even layout; cards collapse together.
- #7: year is fixed "2015" (drops in); 3 counters staggered 80ms.
- #10: wordmark revealed from a mask in full colour; i-dots drop only after letters land; lockup shifted right 60px for breathing room.
