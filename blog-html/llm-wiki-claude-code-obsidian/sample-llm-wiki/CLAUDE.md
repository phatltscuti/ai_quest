# LLM Wiki — Claude Code schema

You maintain an **LLM Wiki** following the [Karpathy gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) pattern: a middle layer of structured, cross-linked Markdown updated by the agent; the user curates raw sources and steers analysis.

## Three layers

1. **`raw/`** — primary sources (articles, notes, transcripts…). **Do not edit** originals unless the user explicitly asks.
2. **`wiki/`** — maintained by you: concept pages, entities, syntheses, comparisons.
3. **This schema file (`CLAUDE.md`)** — conventions and workflows; update when you and the user agree on changes.

## File conventions

- Internal links (Obsidian/Git): `[[Page-name]]` or `wiki/relative-path.md`.
- `wiki/index.md` — catalogue: one short line per page + link.
- `wiki/log.md` — append-only log with date prefix: `## [YYYY-MM-DD] action_type | short summary`.
- Each **ingest** of a new source: summarise, refresh `index.md`, touch related entity/concept pages, and append **one** `log.md` entry.
- **Query**: answer with citations (`[[…]]`/paths). If an answer should be reused, propose (or create) a wiki page and log it.

## Layout

```
sample-llm-wiki/
  CLAUDE.md
  raw/           # sources (immutable by convention)
  wiki/
    index.md
    log.md
    overview.md
    concepts/
```

## Lint (when the user asks)

Check for: contradictions across pages, stale claims, orphan pages, concepts without a dedicated page, missing cross-links.
