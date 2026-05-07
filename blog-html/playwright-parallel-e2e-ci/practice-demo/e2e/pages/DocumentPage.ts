import { expect, type Locator, type Page } from "@playwright/test";
import { selectors } from "../selectors";

/**
 * Page Object Model keeps waits and locators out of specs.
 * Iron Law: no waitForTimeout; only state-based waits.
 */
export class DocumentPage {
  readonly page: Page;
  readonly titleInput: Locator;
  readonly createBtn: Locator;
  readonly busy: Locator;
  readonly toast: Locator;
  readonly docId: Locator;
  readonly docTitle: Locator;
  readonly docStatus: Locator;
  readonly requestReviewBtn: Locator;
  readonly approveBtn: Locator;
  readonly taskList: Locator;
  readonly auditLog: Locator;

  constructor(page: Page) {
    this.page = page;
    this.titleInput = page.locator(selectors.titleInput);
    this.createBtn = page.locator(selectors.createBtn);
    this.busy = page.locator(selectors.busy);
    this.toast = page.locator(selectors.toast);
    this.docId = page.locator(selectors.docId);
    this.docTitle = page.locator(selectors.docTitle);
    this.docStatus = page.locator(selectors.docStatus);
    this.requestReviewBtn = page.locator(selectors.requestReviewBtn);
    this.approveBtn = page.locator(selectors.approveBtn);
    this.taskList = page.locator(selectors.taskList);
    this.auditLog = page.locator(selectors.auditLog);
  }

  async open() {
    await this.page.goto("/");
    await expect(this.createBtn).toBeVisible();
  }

  async createDraft(title: string) {
    await this.titleInput.fill(title);
    await this.createBtn.click();
    await expect(this.docStatus).toHaveText("Draft");
    await expect(this.docTitle).toHaveText(title);
  }

  async requestReview() {
    await this.requestReviewBtn.click();
    // Iron Law #8 style: wait for busy appear then disappear when available.
    // App shows busy briefly; also wait for final state.
    await expect(this.docStatus).toHaveText("Review requested");
    await expect(this.toast).toBeVisible();
  }

  async approveHeavy() {
    await this.approveBtn.click();
    await expect(this.docStatus).toHaveText("Approved", { timeout: 20_000 });
  }

  async expectStatus(status: string) {
    await expect(this.docStatus).toHaveText(status);
  }

  async expectTaskVisible(title: string) {
    await expect(this.taskList).toContainText(title);
  }

  async expectAuditContains(fragment: string) {
    await expect(this.auditLog).toContainText(fragment);
  }

  async currentDocId() {
    return (await this.docId.innerText()).trim();
  }
}
