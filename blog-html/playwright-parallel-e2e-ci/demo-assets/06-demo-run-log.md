# Practice run log — Playwright parallel E2E patterns (Berry Zenn article)

## Environment
- Date: 2026-07-24
- OS: Windows 10
- Node.js: v16.14.0
- Playwright: @playwright/test@1.40.1 (pinned for Node 16 compatibility)
- Browser: Chromium (Playwright build)

## What was practiced
1. Per-test fixtures with isolated document titles + teardown
2. Page Object Model (no locators in specs)
3. Light vs heavy Playwright projects with different worker strategies
4. Iron Law waits (no waitForTimeout; web-first assertions)
5. Impact-map first-match resolver + fail-open fallback
6. Sample GitHub Actions matrix workflow file

## Commands run
```bash
npm install
npx playwright install chromium
npx playwright test
node scripts/resolve-impact.js app/index.html
node scripts/resolve-impact.js e2e/document/approve-heavy.spec.ts
npx playwright test --project=light-r1-document
npx playwright test --project=heavy-r1-document
```

## Results
| Run | Result | Wall-clock | Notes |
|---|---|---|---|
| Full suite (light + heavy projects) | 3 passed | ~10.0s | 3 workers |
| Light project only | 2 passed | ~4.6s | fullyParallel |
| Heavy project only | 1 passed | ~7.3s | slower path (~1.2s simulated edge work) |
| Impact resolve `app/index.html` | document-ui rule | - | selected both specs |
| Impact resolve heavy spec | document-heavy-only | - | selected one spec |

## Observations
- Parallel-safe tests required unique per-test data; shared drafts would collide under workers.
- Separating `@heavy` kept the slow path from blocking light CRUD checks.
- State-based waits (`toHaveText`, `toBeVisible`) were enough for this mini app; no fixed sleeps were used.
- This practice intentionally simplifies Berry's full Supabase/Kong/8-core matrix stack into a local reproducible core.

## Limits of this practice vs the article
- No real Supabase, Kong 502 keep-alive race, or PSI CPU instrumentation was reproduced.
- No 8-core Larger Runner matrix was executed on GitHub Actions in this local session.
- The demo validates architecture and config patterns, not Berry's production wall-clock of 6–8 minutes for ~140 cases.
