import { expect, test } from "../fixtures/test";

test.describe("document review light flow", () => {
  test("S1-S3: create draft and request review @light", async ({ documentPage, docBundle }) => {
    await test.step("S1: open app and create draft", async () => {
      await documentPage.createDraft(docBundle.title);
      await documentPage.expectStatus("Draft");
    });

    await test.step("S2-S3: request review", async () => {
      await documentPage.requestReview();
    });

    await test.step("E1: status becomes Review requested", async () => {
      await documentPage.expectStatus("Review requested");
    });

    await test.step("E2: reviewer task list includes the document", async () => {
      await documentPage.expectTaskVisible(docBundle.title);
    });

    await test.step("E3: audit log records the request", async () => {
      await documentPage.expectAuditContains("review-requested:");
    });
  });

  test("create multiple isolated drafts in parallel-safe way @light", async ({ documentPage, docBundle }) => {
    await documentPage.createDraft(docBundle.title);
    const id = await documentPage.currentDocId();
    expect(id.startsWith("doc-")).toBeTruthy();
    await documentPage.expectStatus("Draft");
    await expect(documentPage.requestReviewBtn).toBeEnabled();
  });
});
