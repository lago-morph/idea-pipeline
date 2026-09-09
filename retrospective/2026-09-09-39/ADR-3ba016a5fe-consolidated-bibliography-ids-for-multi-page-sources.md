# ADR: Consolidated bibliography ids for multi-page sources

- **ID**: ADR-3ba016a5fe
- **Status**: Draft (not yet adopted to docs/adr/)
- **Date**: 2026-09-09
- **Source retrospective**: ../2026-09-09-39.md
- **PRs covered**: #39

## Context

The agent-patterns build fetched several sources that are single works published as many pages: Simon Willison's *Agentic Engineering Patterns* guide (16 chapters plus index and intro, fetched as 18 cache files), the Claude Code documentation set (5 pages), and the Codex documentation set (3 pages). Triage rated each page individually — the Willison chapters alone produced 18 triage rows, 13 of them high — so a naive "one note per high item" rule would have generated ~24 source notes for what SPEC §10 lists as three bibliography entries (`willison-2026-aep`, `claude-code-docs`, `codex-docs`), and every pattern page citing "the Willison guide" would have had to pick chapter-level ids that fragment the evidence trail.

## Decision

A source published as many pages under one canonical umbrella — a chaptered guide or a documentation set — gets one bibliography id and one source note covering all its pages; independently published items keep per-item ids.

In practice: triage may still rate umbrella pages individually (that costs nothing and preserves granularity in `sources/_triage.md`), but distillation consolidates them into the umbrella note, whose "Candidate patterns / evidence" section may run longer than a normal note's (the Willison note was allowed one bullet per chapter-level pattern). Blog posts, newsletters, and papers remain one id each (`osmani-2026-good-spec`, `every-2026-07-16-case-against-skills`) because each is an independently authored, independently citable work.

## Alternatives considered

- **One note per page** — rejected: ~24 notes for three works, each thin; evidence lines splinter (`[willison-aep-red-green-tdd]` vs `[willison-aep-first-run-tests]`) so a reader can't see at a glance that one guide underwrites a pattern; and the bibliography stops matching SPEC §10's own id scheme.
- **One note per work, no individual triage of pages** — rejected: SPEC §9 Phase 2 explicitly says to triage the Willison chapters individually "for consistency", and per-page triage rows are what let the orchestrator see which chapters carry the weight.
- **Per-page ids with an umbrella alias** — rejected as ceremony: an aliasing layer to reassemble what one id already expresses, violating the 80/20 charter.

## Consequences

- Easier: evidence lines stay legible (`[willison-2026-aep]` appears on 8 pattern pages); the bibliography maps 1:1 to SPEC §10; staleness checks at model releases touch one `verified:` per work.
- Harder: an evidence line citing an umbrella note points at a work, not a chapter — a reader wanting the exact chapter follows the note's per-chapter evidence bullets. The umbrella notes also exceed the normal ≤150-word summary budget (accepted deliberately for `willison-2026-aep`).
- Accepted trade-off: three umbrella ids (`claude-code-docs`, `codex-docs`, `willison-2026-aep`) have no direct rows in `_triage.md` — their component pages do. This is recorded in `log.md` (Phase 3) so lint doesn't flag it as a gap.

## References

- [`../2026-09-09-39.md`](../2026-09-09-39.md) — the source retrospective.
- [`./SKILL-SPEC-6c1c282b73-planned-evidence-synthesis.md`](./SKILL-SPEC-6c1c282b73-planned-evidence-synthesis.md) — the synthesis workflow that consumes these ids.
- `agent-patterns/sources/willison-2026-aep.md`, `agent-patterns/sources/claude-code-docs.md`, `agent-patterns/sources/codex-docs.md` — the three consolidated notes.
- PR the decision was made in: #39.
