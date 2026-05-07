#!/usr/bin/env node
const { spawnSync } = require("child_process");
const { resolveImpact } = require("./resolve-impact");
const path = require("path");

const changed = process.argv.slice(2);
const files = changed.length ? changed : ["app/app.js"];
const mapPath = path.join(__dirname, "..", "impact-map.json");
const result = resolveImpact(files, mapPath);

console.log("Impact resolution:");
console.log(JSON.stringify(result, null, 2));

if (!result.selectedSpecs.length) {
  console.error("No specs selected.");
  process.exit(1);
}

const args = ["playwright", "test", ...result.selectedSpecs];
const run = spawnSync("npx", args, { stdio: "inherit", shell: true });
process.exit(run.status || 0);
