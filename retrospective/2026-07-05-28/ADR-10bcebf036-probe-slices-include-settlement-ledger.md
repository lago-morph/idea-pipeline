# ADR: Probe context slices include the settlement ledger

- **ID**: ADR-10bcebf036
- **Status**: Draft (not yet adopted to docs/adr/)
- **Date**: 2026-07-05
- **Source retrospective**: ../2026-07-05-28.md
- **PRs covered**: #28

## Context

The task-02 design sketch specified that the S3 question-count probe reads "Layer 0–1 drafts only". Executed literally, every settled deferral is invisible to the probe: it re-raises resolved questions on every iteration, the new-question count never reaches zero, and the loop-until-dry exit (two consecutive clean probes) becomes unreachable — the burn-down metric ends up measuring probe blindness rather than spec completeness. The same failure appears one stage earlier: an S1 re-probe that cannot see the A-VS draft re-lists every assumption the owner already dispositioned.

## Decision

Every probe's context slice includes the artifacts that record already-settled decisions at its layer — R-FR for the S3 question-count probe, the A-VS draft for S1 re-probes — so settled questions are not re-raised as noise.

## Alternatives considered

- **Layer 0–1 only, with triage-side dedup against R-FR** — rejected: dedup happens after the count is taken, so either the recorded metric is polluted or triage silently rewrites it; and probe attention is finite — spending it re-deriving settled questions crowds out fresh ones.
- **Full-workspace probes** — rejected: destroys the measurement (P4, ignorance is the instrument). The probe must not see drafts of the layers it is meant to question; it sees only the ledger of what is already decided at its own layer.

## Consequences

Easier: the dry condition is reachable and means what it claims; declared freedoms get tested for bound quality (a probe that still asks despite seeing the register entry is evidence the entry's bound is too vague — a T7 signal for free). Harder: probe packets are assembled per stage rather than "the workspace"; accepted as the price of a meaningful instrument. Binding on task-03: its hardened probe definitions must preserve slice discipline, including the settlement-ledger inclusion, or the S3 gate it feeds stops converging.

## References

- [`../2026-07-05-28.md`](../2026-07-05-28.md) — the source retrospective.
- `spec-completeness/process.md` — §4.7 probe charters (the deviation is stated inline), S1 and S3 stage cards.
- `spec-completeness/artifact-model.md` — §4 rules T2 and T7.
- PR the decision was made in: #28.
