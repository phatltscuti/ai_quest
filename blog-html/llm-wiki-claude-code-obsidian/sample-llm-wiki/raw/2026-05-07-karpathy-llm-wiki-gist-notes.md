# Source note: Karpathy — LLM Wiki (gist)

> Source: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f  
> Main ideas excerpt — not a full copy.

- Typical RAG “finds chunks and answers” on every query; an LLM Wiki is a **compounding artifact**: structured Markdown that is **compiled and maintained**.
- The wiki sits **between** raw sources and the reader; sources are usually **immutable**; the agent owns wiki updates plus schema conventions (`CLAUDE.md` / `AGENTS.md`).
- Flow: **Ingest** (read source → update many pages) → **Query** (read index, drill down; strong answers should be **written back** to the wiki) → periodic **Lint** (contradictions, stale claims, orphans).
- `index.md` is content-oriented navigation; `log.md` is time-oriented history.
- Tooling hints: Obsidian (live reading), graph view; optional qmd/MCP search when the vault grows large.
