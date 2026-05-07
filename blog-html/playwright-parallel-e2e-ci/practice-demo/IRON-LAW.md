# Iron Law checklist (adapted from Berry Zenn article)

1. No `waitForTimeout`. Wait for state (hidden button, URL, text, response).
2. Specs describe S/E steps only. Locators and waits live in Page Objects.
3. Prefer Playwright web-first assertions (`toHaveText`, `toBeVisible`) over sync DOM reads + static expect.
4. Before absence checks (`toHaveCount(0)`), wait for a positive landmark.
5. For refetch/sort/filter actions, wait for the network/RPC before asserting final UI.
6. Silent-success actions should assert busy appear then disappear when an indicator exists.
7. Precheck fixture/factory data before UI actions when possible.
8. Keep retries at 0 in CI so flaky tests are fixed instead of hidden.
9. Record video/trace evidence for failures and investigations.
10. Keep tests data-independent so workers can run in parallel safely.
