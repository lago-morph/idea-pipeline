# ADR: Traceability mechanization targets one regex-greppable citation-tag grammar

- **ID**: ADR-281c013fb9
- **Status**: Draft (not yet adopted to docs/adr/)
- **Date**: 2026-07-05
- **Source retrospective**: ../2026-07-05-26.md
- **PRs covered**: #26

## Context

The traceability rules T1–T7 are only checkable if citations are machine-
findable. artifact-model.md §5 therefore defines exactly four tag forms —
element declaration `[#C-BC-012]`, realization citation `[realizes: …]`,
freedom pointer `[freedom: …]`, gate citation `[checks: …]` — all matched by
one regular expression
(`\[(#|realizes:|freedom:|checks:)\s*[A-Z]-[A-Z]{2}-[0-9]{3}`), and requires
tags to survive compilation verbatim. The gold specs approximate this with
prose section references ("see Section 6.4 table"), which humans resolve and
checkers cannot. Task-03's tiering (deterministic → constrained-LLM → human)
depends on the deterministic tier being cheap: one grep surface for all four
relationship kinds is what keeps it so.

## Decision

All traceability tags use the four-form bracket grammar of artifact-model.md §5, kept parseable by a single regular expression so task-03's deterministic tier stays cheap.

## Alternatives considered

- **Section-number cross-references (gold-spec practice)** — rejected for
  mechanization: section numbers drift under edits and carry no relationship
  kind (realizes vs. checks vs. freedom).
- **HTML-comment tags (invisible in rendered output)** — rejected: tags must
  survive compilation *visibly* because post-compilation checkability is the
  point; invisible tags also tempt divergence between rendered claims and
  hidden anchors.
- **Richer per-kind grammars (YAML blocks, footnote systems)** — rejected:
  every additional form multiplies checker cost and authoring error surface;
  four forms already cover declaration, realization, freedom, and gate.

## Consequences

- Easier: T1/T2/T5/T6 mechanize as tag-closure checks over one grep; tags
  double as stable anchors for tooling and diffs.
- Harder: authors carry a tagging burden on every normative element;
  documents look denser.
- Accepted trade-off: the grammar is now load-bearing — changing it after
  task-03 ships checkers is a breaking change, so any extension must be
  additive to the regex.

## References

- [`../2026-07-05-26.md`](../2026-07-05-26.md) — the source retrospective.
- `spec-completeness/artifact-model.md` §5 — the tag grammar; §4 — the rules
  it serves.
- PRs the decision was made in: #26.
