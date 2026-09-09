# ADR: Two-source threshold for adopted patterns

- **ID**: ADR-ce4eb52bb1
- **Status**: Draft (not yet adopted to docs/adr/)
- **Date**: 2026-09-09
- **Source retrospective**: ../2026-09-09-39.md
- **PRs covered**: #39

## Context

SPEC §8's lint workflow says to "promote candidates with ≥ 2 evidence lines to `adopted` (ask if unsure)", but at synthesis time this was ambiguous in a way that mattered: a single consolidated source note (the 18-chapter Willison guide) can easily supply two or more evidence lines for one pattern all by itself. Reading the rule as "≥ 2 evidence lines" would have promoted `run-tests-first`, `red-green-tdd`, and `hoard-working-code` — patterns attested by exactly one author — into `quickref.md`, the artifact injected into every future session. The status decision had to be made for all 36 pages at once during Phase 4, before Checkpoint B review.

## Decision

A pattern page is promoted to status: adopted only when its evidence lines cite at least two distinct source notes; single-source pages stay candidate and are excluded from quickref.md.

The reviewer (Jonathan, at a checkpoint or via lint) can promote any candidate deliberately; the threshold governs only what gets promoted *automatically*. Applied in PR #39 this yielded 31 adopted and 5 candidate pages (`run-tests-first`, `hoard-working-code`, `red-green-tdd`, `jig-for-tuning`, `over-compressed-context`).

## Alternatives considered

- **Count evidence lines, not sources** (the literal SPEC reading) — rejected: one prolific author generates many lines; corroboration is what the count is supposed to measure, and a consolidated umbrella note (ADR-3ba016a5fe) makes line-counting trivially gameable.
- **Promote everything, let review demote** — rejected: quickref is the injected artifact; shipping single-source advice into every session by default inverts the burden of proof, and Checkpoint B review of 36 pages is exactly when a reviewer is least likely to catch five over-promotions.
- **Hold everything at candidate until human review** — rejected: an empty quickref fails the MVP's own done-condition ("quickref.md exists… every line traces to a pattern page"), and the ≥2-distinct-sources cases are precisely the ones the SPEC's rule intended to auto-promote.

## Consequences

- Easier: `quickref.md` carries only corroborated guidance; the candidate marker honestly signals thin evidence in `index.md`; promotion is a one-field edit once a second source (including `[own]` experience with a date, per SPEC §2) lands.
- Harder: some genuinely good single-author practices (Willison's `run-tests-first`) sit outside the quickref until corroborated — dogfooding (Phase 5) is the intended second source.
- Accepted trade-off: "distinct source notes" inherits the consolidation decision — the whole Willison guide counts as one source. That is intentional: it measures independent authorship, not page count.

## References

- [`../2026-09-09-39.md`](../2026-09-09-39.md) — the source retrospective.
- [`./ADR-3ba016a5fe-consolidated-bibliography-ids-for-multi-page-sources.md`](./ADR-3ba016a5fe-consolidated-bibliography-ids-for-multi-page-sources.md) — the id-consolidation decision this threshold interacts with.
- `agent-patterns/SPEC.md` §8 (lint promotion rule), §5.7 (quickref = adopted only); `agent-patterns/log.md` Phase 4 entry recording the applied split.
- PR the decision was made in: #39.
