# Concept: LLM Wiki (Karpathy pattern)

**Short definition:** Markdown pages authored and maintained by an LLM/agent, with an index and cross-links, expressing a **compiled synthesis** from raw sources — not merely a retrieval store for each question.

## Compared to “upload then ask” RAG

| Aspect | Typical upload RAG | LLM Wiki |
|--------|--------------------|----------|
| Accumulation | Rediscover fragments every time | Artifact updated via ingest |
| Cross-references | Mostly implicit via embeddings | Explicit in Markdown |
| Source conflicts | Rarely surfaced | Surfaced via lint / editing |

## Human vs agent

- **Human:** picks sources, asks questions, sets priorities, approves larger edits when needed.
- **Agent:** summarises, edits many pages, maintains log and index, suggests lint passes.

## Source reference

- Raw note: `raw/2026-05-07-karpathy-llm-wiki-gist-notes.md`
