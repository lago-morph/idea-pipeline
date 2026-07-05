# ADR: Observable numeric behavior is contract, not algorithm

- **ID**: ADR-0f28b1a371
- **Status**: Draft (not yet adopted to docs/adr/)
- **Date**: 2026-07-05
- **Source retrospective**: ../2026-07-05-26.md
- **PRs covered**: #26

## Context

The planning hypothesis filed "exact formulas" under R-RA (reference
algorithms). The symphony decomposition refuted that placement with direct
textual evidence: its backoff formula
(`delay = min(10000 * 2^(attempt-1), …)`, symphony L766–768) lives in the
behavior *prose*, and the §16 pseudocode deliberately invokes it abstractly
(`schedule_retry` without delay math). The formula is not a witness of a
commitment — it *is* the commitment: any conforming implementation must
produce exactly those delays. Filing it as realization would have made an
observable obligation deletable with the HOW, violating the rewrite test.

## Decision

Formulas whose outputs are externally observable (backoff delays, limits, thresholds) are stated as exact formulas in C-BC; R-RA pseudocode invokes them by reference and keeps only internal computation steps.

## Alternatives considered

- **All formulas in R-RA (the planning hypothesis)** — rejected on the
  symphony evidence above; it also collides with README §3.B, which lists
  "numeric behavior is an exact formula" under *Behavior*, not algorithms.
- **All formulas in C-BC** — rejected: some formulas are genuinely internal
  (a hash-window scan step inside loop detection) and hoisting them would
  stuff the contract with mechanism, breaching C-BC's "semantics, not
  mechanism" boundary.

## Consequences

- Easier: the rewrite test passes for numeric behavior — rewriting all
  pseudocode cannot change contracted delays/limits; gate items can cite a
  contract element for every numeric assertion.
- Harder: authors must decide per formula whether its output is observable;
  the boundary question ("would a black-box test see it?") becomes part of
  authoring.
- Accepted trade-off: a formula in the contract layer references config
  knobs (e.g. `max_backoff`) whose *values* live in R-CD — the split is
  intentional (field and formula are WHAT; the default value is tuning).

## References

- [`../2026-07-05-26.md`](../2026-07-05-26.md) — the source retrospective.
- `spec-completeness/artifact-model.md` §2.1 delta 4 — the recorded
  refinement with its forcing evidence.
- PRs the decision was made in: #26.
