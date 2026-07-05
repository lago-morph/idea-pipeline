# ADR: Freeze requires a replication round on byte-identical text

- **ID**: ADR-b1b74062d9
- **Status**: Draft (not yet adopted to docs/adr/)
- **Date**: 2026-07-05
- **Source retrospective**: ../2026-07-05-28.md
- **PRs covered**: #28

## Context

One-shot build outcomes are high-variance — README §4.2 mandates k ≥ 5 builds per variant for exactly this reason — so a single all-pass round can be luck. Worse, in the naive loop every round is followed by fixes, so consecutive rounds never grade the same document, and a "two clean rounds" criterion would quietly conflate spec quality with churn between rounds. process.md needed a freeze criterion that is statistically defensible, cheap to state, and immune to that conflation.

## Decision

A spec freezes only after two consecutive clean rounds of five one-shot builds each, where the second round runs against the byte-identical compiled text of the first.

## Alternatives considered

- **Freeze on one clean k=5 round** — rejected: at a true per-build pass rate of 0.7, a clean quintet occurs ≈17% of the time; freezing on it ships a coin flip.
- **One larger round (k=10)** — rejected: same build budget as 2×5 but loses the replication property (it never demonstrates that a clean round reproduces), and it cannot exercise the no-deltas-after-clean-round invariant that makes byte-identical replication possible.
- **Two clean rounds at k=3** — rejected: six builds bound the true pass rate too weakly (≈0.61 at 95%); k=3 is the improvement-round economy setting, not freeze evidence.

## Consequences

Ten consecutive passing builds bound the true per-build pass rate at ≥ ~0.74 with 95% confidence (0.05^(1/10)) — stated in process.md §9.1 so a pressure test can re-derive and retune it. Freeze cost is bounded at ten builds, paid only when the spec is plausibly done. Harder: a flaky smoke test (G-ST) can force repeated near-freezes; accepted, because that flakiness is itself a GATE_GAP the rounds exist to surface. The replication round is possible precisely because a clean round applies no deltas — the criterion and the change-control rule reinforce each other.

## References

- [`../2026-07-05-28.md`](../2026-07-05-28.md) — the source retrospective.
- `spec-completeness/process.md` — S7 stage card, §9.1 R_freeze row, §10 freeze semantics.
- `spec-completeness/README.md` — §4.2 ablation protocol (the k ≥ 5 floor).
- PR the decision was made in: #28.
