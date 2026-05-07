import { test } from "../fixtures/test";

test.describe("document approval heavy flow", () => {
  test("approve after review simulates slow edge function @heavy", async ({ documentPage, docBundle }) => {
    await test.step("S0: create draft", async () => {
      await documentPage.createDraft(docBundle.title);
    });

    await test.step("S1: request review", async () => {
      await documentPage.requestReview();
      await documentPage.expectStatus("Review requested");
    });

    await test.step("S2: approve (heavy path)", async () => {
      await documentPage.approveHeavy();
    });

    await test.step("E1: status becomes Approved", async () => {
      await documentPage.expectStatus("Approved");
      await documentPage.expectAuditContains("approved:");
    });
  });
});
