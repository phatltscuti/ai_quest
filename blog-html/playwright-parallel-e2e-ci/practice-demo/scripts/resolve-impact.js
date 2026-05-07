#!/usr/bin/env node
/**
 * Impact resolver (fail-open):
 * - first matching rule wins when ordered from specific to broad
 * - unknown files fall through to the final fallback-all rule
 */
const fs = require("fs");
const path = require("path");

function matchGlob(pattern, filePath) {
  const normalized = filePath.replace(/\\/g, "/");
  const escaped = pattern
    .replace(/\\/g, "/")
    .replace(/[.+^${}()|[\]\\]/g, "\\$&")
    .replace(/\*\*/g, ":::DOUBLE:::")
    .replace(/\*/g, "[^/]*")
    .replace(/:::DOUBLE:::/g, ".*");
  const re = new RegExp(`^${escaped}$`);
  return re.test(normalized);
}

function resolveImpact(changedFiles, mapPath) {
  const map = JSON.parse(fs.readFileSync(mapPath, "utf8"));
  const selected = new Set();
  const hits = [];

  for (const file of changedFiles) {
    let matched = false;
    for (const rule of map.rules) {
      if (rule.match.some((pattern) => matchGlob(pattern, file))) {
        hits.push({ file, rule: rule.name, specs: rule.specs });
        rule.specs.forEach((spec) => selected.add(spec));
        matched = true;
        break; // first-match
      }
    }
    if (!matched) {
      // fail-open: run all
      map.rules[map.rules.length - 1].specs.forEach((spec) => selected.add(spec));
      hits.push({ file, rule: "fail-open-all", specs: [...selected] });
    }
  }

  return {
    changedFiles,
    selectedSpecs: [...selected],
    hits
  };
}

function main() {
  const args = process.argv.slice(2);
  const files = args.length
    ? args
    : ["app/index.html"]; // default demo input
  const mapPath = path.join(__dirname, "..", "impact-map.json");
  const result = resolveImpact(files, mapPath);
  console.log(JSON.stringify(result, null, 2));
}

if (require.main === module) {
  main();
}

module.exports = { resolveImpact, matchGlob };
