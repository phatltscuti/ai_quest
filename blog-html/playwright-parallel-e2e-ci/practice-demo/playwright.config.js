const { defineConfig, devices } = require("@playwright/test");

function lightProject(release, feature, testMatch, options = {}) {
  return {
    name: `light-${release}-${feature}`,
    testMatch,
    grepInvert: /@heavy/,
    fullyParallel: true,
    workers: process.env.CI ? options.ciWorkers || 4 : 3,
    timeout: 30_000,
    use: { ...devices["Desktop Chrome"] }
  };
}

function heavyProject(release, feature, testMatch, options = {}) {
  return {
    name: `heavy-${release}-${feature}`,
    testMatch,
    grep: /@heavy/,
    fullyParallel: false,
    workers: options.ciWorkers || 2,
    timeout: 60_000,
    use: { ...devices["Desktop Chrome"] }
  };
}

module.exports = defineConfig({
  testDir: "./e2e",
  fullyParallel: true,
  forbidOnly: !!process.env.CI,
  retries: 0,
  reporter: [["list"], ["html", { open: "never" }]],
  use: {
    baseURL: "http://127.0.0.1:4173",
    trace: "on-first-retry",
    video: "on",
    screenshot: "only-on-failure"
  },
  webServer: {
    command: "npx --yes serve@14 app -l 4173",
    url: "http://127.0.0.1:4173",
    reuseExistingServer: !process.env.CI,
    timeout: 120_000
  },
  projects: [
    lightProject("r1", "document", /document\/.*\.spec\.ts/),
    heavyProject("r1", "document", /document\/.*\.spec\.ts/)
  ]
});
