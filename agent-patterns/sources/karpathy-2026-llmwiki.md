---
id: karpathy-2026-llmwiki
title: LLM Wiki
author: Andrej Karpathy
date: 2026-04-04
url: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
access: direct
accessed: 2026-08-29
scope: meta
relevance: high
pass: distilled
patterns: [wiki-as-memory, ingest-query-lint-loop, index-plus-log, human-curates-agent-writes, review-agent-diffs]
---

## Summary

A short design document (deliberately abstract, meant to be pasted into your own
agent) describing a pattern for one human plus one agent building a persistent
markdown knowledge base. The contrast is with RAG: instead of re-deriving
answers from raw documents on every query, the agent compiles knowledge once
into interlinked markdown pages and then keeps them current, so cross-references
and flagged contradictions already exist when a question arrives — Karpathy's
phrase is that the wiki is "a persistent, compounding artifact." Three layers:
immutable **raw sources** the agent only reads; the **wiki**, agent-written
markdown the human only reads; and the **schema** (CLAUDE.md / AGENTS.md), the
config that turns the agent into a disciplined maintainer and that the human and
agent co-evolve. Three operations — ingest, query, lint — plus two navigation
files, index.md and log.md. The stated reason it works: the barrier to a
human-maintained wiki is bookkeeping, and bookkeeping is exactly what an agent
does cheaply.

## Takeaways for our use case

- Three layers with strict ownership: raw sources are immutable and agent-read
  only; the wiki is agent-written and human-read; the schema file is the one
  layer both parties edit. This repo's `.cache/` → `sources/`+`patterns/` →
  `AGENTS.md` split is the same shape.
- Ingest is a full pass, not an index step: read the source, discuss takeaways
  with the human, write a summary page, update the index, update every affected
  concept page, append to the log. One source may touch 10–15 pages.
- Karpathy prefers ingesting one source at a time and staying involved (reading
  summaries, steering emphasis) over unsupervised batch ingest — and says to
  write whichever workflow you settle on into the schema for future sessions.
- Query answers worth keeping get **filed back into the wiki as new pages**, so
  exploration compounds the same way ingestion does instead of dying in chat
  history.
- Lint is a periodic health check with a concrete checklist: contradictions
  between pages, stale claims newer sources supersede, orphan pages with no
  inbound links, concepts mentioned but lacking a page, missing cross-refs, and
  gaps a search could fill.
- Two files do the navigating: `index.md` is content-oriented (every page, a
  link, a one-line summary, by category, updated on every ingest, read first
  when answering); `log.md` is chronological and append-only. A consistent log
  prefix like `## [2026-04-02] ingest | Title` makes it greppable.
- Index-based navigation is reported to work to roughly 100 sources / a few
  hundred pages without any embedding infrastructure; build search only when you
  outgrow that. Plain markdown in git gives version history for free.
- Commenter reports (third-party, not Karpathy — treat as weaker evidence):
  huachen-wang and others independently converged on **reviewing the generated
  artifact rather than the plan**, saying plan review catches far fewer problems
  than reviewing what the agent actually wrote; huachen-wang also records human
  corrections as *pins* storing the claim rather than a diff, so a fix survives
  the next regeneration of the page; kriss-b reports the agent navigating with
  grep/ls rather than embeddings because plain text in git doesn't go stale the
  way a vector index does.

## Candidate patterns / evidence

- → `wiki-as-memory`: knowledge is compiled once into a persistent interlinked
  markdown artifact and kept current, rather than re-derived per query from raw
  sources.
- → `ingest-query-lint-loop`: names three operations as the whole maintenance
  cycle, with lint given an explicit checklist (contradictions, stale claims,
  orphans, missing pages, missing cross-refs, gaps).
- → `index-plus-log`: a content-oriented index.md read first on every query plus
  an append-only chronological log.md with a greppable line prefix, updated on
  every ingest.
- → `human-curates-agent-writes`: the human curates sources, directs analysis
  and asks questions; the agent does all summarizing, cross-referencing, filing
  and bookkeeping — "you never (or rarely) write the wiki yourself."
- → `review-agent-diffs`: gist commenters converged on approving the actual
  generated pages instead of the agent's stated plan, because plan review misses
  most problems (commenter evidence, not the gist body).
- → `file-answers-back`: a good query answer becomes a new wiki page so
  exploration compounds instead of being lost to chat history.

## Other-use-case material

- The team/multi-audience material in the comments is a different use case:
  concurrent ingests forking the wiki (fixed with placeholder page reservations
  and atomic conditional writes), and compiling a *second* wiki from
  external-safe sources rather than filtering pages by an `audience` label,
  because a label is one derivation bug away from a leak. Both only matter with
  parallel ingest or multiple readers.
- Several commenters advertise implementations (MindBase, Cortexes, IWE,
  project-wiki, doc.html and others) and a deterministic fact-store alternative;
  vendor/tool territory, noted here only so we don't re-triage them.
