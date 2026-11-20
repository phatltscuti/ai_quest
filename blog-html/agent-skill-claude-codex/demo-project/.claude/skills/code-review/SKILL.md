---
name: code-review
description: Review source code or a diff for security, correctness, error handling, maintainability and test coverage, and report findings in a fixed severity-ranked format with file:line references and concrete fixes. Use when the user asks for a code review, PR review, bug hunt, security check or "look over this code".
license: MIT
compatibility: Agent Skills standard (agentskills.io). Tested with Claude Code and OpenAI Codex CLI. Read-only; does not modify code.
metadata:
  author: phatlt
  version: "1.0"
---

# Code review

Review like a senior engineer who must sign off the change. Be specific, cite lines, propose fixes. Do not edit the code.

## Procedure

1. **Scope**: review the files or diff the user names. If none are named, review files changed in the working tree (`git diff --name-only`), otherwise all source files in the current directory.
2. **Read every line** of the in-scope files. Check each item of [references/checklist.md](references/checklist.md).
3. **Classify** every finding with exactly one severity:
   - **Critical**: security hole, data loss, secret exposure. Must fix before merge.
   - **Major**: wrong behaviour, broken business rule, crash risk.
   - **Minor**: error handling, robustness, maintainability.
   - **Nit**: style, naming, comments.
4. **Report** using the output format below, sorted Critical → Nit. One finding per row. Merge duplicates.
5. Finish with a one-line **verdict**: `APPROVE`, `APPROVE WITH COMMENTS` or `REQUEST CHANGES` (any Critical or Major → REQUEST CHANGES).

## Output format

```
## Code review: <scope>

| # | Severity | Location | Finding | Suggested fix |
|---|----------|----------|---------|---------------|
| 1 | Critical | file.py:12 | ... | ... |

**Summary:** <n> Critical, <n> Major, <n> Minor, <n> Nit
**Verdict:** REQUEST CHANGES
```

## Rules

- Location must be `path:line` (or `path:start-end`).
- Never report something you did not verify in the code.
- If tests are missing for changed logic, report it as Minor.
