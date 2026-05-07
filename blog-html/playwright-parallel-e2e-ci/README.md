# Playwright Parallel E2E + CI Tuning Practice

Practice folder for the Berry Zenn article:

https://zenn.dev/berry_blog/articles/39392e1da7ca71

## Contents
- `index.html` — English blog
- `index-vi.html` — Vietnamese blog
- `HUONG-DAN-DEMO.md` — how to run the practice
- `practice-demo/` — local mini Playwright project
- `demo-assets/` — execution logs and run summary

## Quick start
```bash
cd practice-demo
npm install
npx playwright install chromium
npx playwright test
```

Observed local result: **3 passed in ~10s**.
