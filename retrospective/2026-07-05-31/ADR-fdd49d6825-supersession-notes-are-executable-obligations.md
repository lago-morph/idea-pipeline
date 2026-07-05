# ADR: Supersession notes are executable obligations discharged by a dedicated reconciliation pass

- **ID**: ADR-fdd49d6825
- **Status**: Draft (not yet adopted to docs/adr/)
- **Date**: 2026-07-05
- **Source retrospective**: ../2026-07-05-31.md
- **PRs covered**: #30, #31

## Context

The spec-completeness documents were authored in dependency order across sessions, so earlier deliverables carry forward-references: process.md §4.7 said "when task-03's hardened probe definitions merge, its templates supersede these and this document keeps only the ingestion/routing rules"; its preamble and S5-X2/S6 cards carried "until hardening merges" placeholders. When PR #30 merged the hardening suite, all of those became latently false — two normative copies of the probe templates existed at once. Task-03 was barred from editing the task-01/02 deliverables, so the tension could not be resolved in-place; the session recorded every affected site in `tasks/task-04-refactor.md` and, on the owner's instruction, discharged the whole queue as PR #31 the same day.

## Decision

When a document declares that a future deliverable supersedes part of it, merging that deliverable creates an obligation to execute the supersession — recorded as an exact-edit-site queue in tasks/ and discharged as its own reviewed PR that trims the superseded text to a pointer, never leaving both copies normative.

The trim keeps what the superseded document uniquely owns (dispatch rationale, ingestion rules, the module-selection rule a downstream check cites) and replaces the migrated content with named pointers (P-ASSUME = check L-04, P-QCOUNT = L-01, P-IMPL = L-07).

## Alternatives considered

- **Leave both copies and rely on the supersession sentence** — rejected: two live normative copies drift independently; the repo's own artifact model treats exactly this as a defect class (T4 conflicts, attractor's hand-maintained Appendix A rotting against its body).
- **Edit the superseded document in the same PR that merges the superseding one** — rejected for this repo's workflow: it entangles a new deliverable's review with edits to already-ratified documents, and task-03 was explicitly constrained from touching them; a separate pass keeps each review about one thing.
- **Third-document indirection (a registry mapping topics to owners) instead of trimming** — rejected: adds a permanent artifact to maintain when a one-time trim plus pointers achieves single-source-of-truth with less machinery.

## Consequences

Easier: exactly one normative home per template/procedure (checks.md §3), with process.md retaining routing and rationale — the division both documents now state in matching words; future supersessions have a worked pattern (queue file → ratification → reconciliation PR → resolution log). Harder: supersession costs a second PR and a queue file rather than being free at merge time — accepted, because the queue survives session loss (the nine items were executed hours later with zero re-analysis) and the separate PR keeps per-item veto cheap. Residual risk: a supersession note nobody queues; the mitigation used here is writing the queue in the same session that creates the obligation.

## References

- [`../2026-07-05-31.md`](../2026-07-05-31.md) — the source retrospective.
- `spec-completeness/tasks/task-04-refactor.md` — the queue with its per-item resolution log (the pattern's worked example).
- `spec-completeness/process.md` §4.7 — the trimmed section, post-reconciliation.
- [`./SKILL-SPEC-b047218881-refactor-queue-execute.md`](./SKILL-SPEC-b047218881-refactor-queue-execute.md) — the executable form of the pattern.
- PRs the decision was made in: #30 (obligation created), #31 (obligation discharged).
