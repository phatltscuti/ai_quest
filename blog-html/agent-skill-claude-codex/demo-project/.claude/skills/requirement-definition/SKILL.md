---
name: requirement-definition
description: Turn an informal feature request (Slack message, email, meeting note) into a structured requirements document with user stories, numbered functional and non-functional requirements, Given/When/Then acceptance criteria, assumptions and open questions. Use when the user asks to define, clarify, write or review requirements, a spec, or acceptance criteria for a feature.
license: MIT
compatibility: Agent Skills standard (agentskills.io). Tested with Claude Code and OpenAI Codex CLI. Needs read/write access to the repository.
metadata:
  author: phatlt
  version: "1.0"
---

# Requirement definition

Produce a requirements document that a developer, a tester and the requester can all agree on.

## Procedure

1. **Read the request and the code it touches.** Find the related modules (search for nouns from the request) so requirements match the real data model. Never invent tables or fields that do not exist without marking them as *new*.
2. **Separate facts from guesses.** Anything the requester did not state explicitly goes to *Assumptions* (A-xx). Anything that blocks implementation goes to *Open questions* (Q-xx) addressed to a named role.
3. **Write the document** using exactly the template in [references/template.md](references/template.md). Keep every heading, in the same order, even if a section is "None".
4. **Number everything**: FR-01, NFR-01, AC-01, A-01, Q-01. Each acceptance criterion references the FR it verifies.
5. **Acceptance criteria** use Given / When / Then and must be testable (concrete values, no "should work well").
6. **Save** the document to `docs/requirements/<kebab-case-feature-name>.md` and print a 3-line summary: number of FRs, NFRs, ACs and open questions.

## Rules

- Write in the language of the request unless the user asks otherwise.
- Prefer short sentences; one requirement per line.
- Flag security, privacy and audit needs explicitly as NFRs.
- Do not write implementation code in this skill.
