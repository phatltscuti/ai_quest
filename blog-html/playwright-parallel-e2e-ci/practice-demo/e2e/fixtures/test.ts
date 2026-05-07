import { test as base } from "@playwright/test";
import { DocumentPage } from "../pages/DocumentPage";

type DocBundle = {
  title: string;
  track: string[];
  teardown: () => Promise<void>;
};

/**
 * Per-test fixture: each test gets isolated data and must not share state.
 * Mirrors the article's factory + teardown pattern in a simplified local form.
 */
export const test = base.extend<{
  documentPage: DocumentPage;
  docBundle: DocBundle;
}>({
  documentPage: async ({ page }, use) => {
    const documentPage = new DocumentPage(page);
    await documentPage.open();
    await use(documentPage);
  },

  docBundle: async ({ page }, use) => {
    const unique = `${Date.now()}-${Math.floor(Math.random() * 100000)}`;
    const bundle: DocBundle = {
      title: `SOP-${unique}`,
      track: [],
      teardown: async () => {
        // Clear only this browser context's local store after the test.
        await page.evaluate(() => localStorage.clear());
      }
    };

    await use(bundle);
    await bundle.teardown();
  }
});

export { expect } from "@playwright/test";
