# Hướng dẫn demo — Playwright parallel E2E (theo bài Berry trên Zenn)

Nguồn: https://zenn.dev/berry_blog/articles/39392e1da7ca71

## Mục tiêu
Thực hành các ý chính của bài viết trên một mini app local:
- fixture dữ liệu độc lập theo test
- Page Object Model
- tách project light / heavy + workers
- Iron Law (không `waitForTimeout`)
- impact map chọn spec theo file đổi

## Chuẩn bị
```bash
cd blog-html/playwright-parallel-e2e-ci/practice-demo
npm install
npx playwright install chromium
```

Yêu cầu Node.js:
- Bài demo đã pin Playwright 1.40.1 để chạy được trên Node 16.
- Nếu máy có Node 18+, có thể nâng Playwright lên bản mới hơn.

## Các lệnh cần chạy
1. Full suite:
```bash
npx playwright test
```
Kỳ vọng: 3 passed (2 light + 1 heavy).

2. Chỉ light:
```bash
npx playwright test --project=light-r1-document
```

3. Chỉ heavy:
```bash
npx playwright test --project=heavy-r1-document
```

4. Impact resolve:
```bash
node scripts/resolve-impact.js app/index.html
node scripts/resolve-impact.js e2e/document/approve-heavy.spec.ts
```

5. Impact run:
```bash
npm run test:impact
```

## File quan trọng
- `playwright.config.js` — light/heavy workers
- `e2e/fixtures/test.ts` — per-test fixture + teardown
- `e2e/pages/DocumentPage.ts` — POM + state waits
- `IRON-LAW.md` — checklist chống flaky
- `impact-map.json` + `scripts/resolve-impact.js`
- `.github/workflows/e2e-practice.yml` — mẫu matrix CI

## Ghi kết quả
Điền/đối chiếu `../demo-assets/06-demo-run-log.md`.
