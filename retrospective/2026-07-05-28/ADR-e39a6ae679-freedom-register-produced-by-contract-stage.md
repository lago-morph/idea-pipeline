# ADR: The Freedom Register is produced by the contract stage

- **ID**: ADR-e39a6ae679
- **Status**: Draft (not yet adopted to docs/adr/)
- **Date**: 2026-07-05
- **Source retrospective**: ../2026-07-05-28.md
- **PRs covered**: #28

## Context

process.md had to assign every artifact-model artifact exactly one producing stage (task-02 acceptance requirement). The Freedom Register (R-FR) is a Layer-2 realization artifact in the artifact model, which naively places it in S4 with the other R-artifacts. But the question taxonomy makes deferral (DEFERRABLE) a triage outcome of the WHAT loop: the moment a question is classified deferrable, a register entry with a bounding contract must exist or the deferral is unbounded ambiguity (T7). And traceability rule T2 counts an R-FR entry as contract closure — a Layer-1 element may legally lack a realization only if the register covers it. If the register were produced in S4, S3's exit criterion "no dangling Layer-1 obligations" could never be evaluated at S3 exit.

## Decision

R-FR is produced and owned by the contract loop (S3): deferrals mint register entries at triage time, and every later addition arrives as a scoped S3 re-entry.

## Alternatives considered

- **Produce R-FR in S4 with the other R-artifacts** — rejected: S3 cannot close (T2 needs the register to evaluate contract closure), and freedoms discovered at contract time would be parked informally until S4 — precisely the "freedom leaked, not declared" failure that principle P3 exists to prevent.
- **Split production (S3 declares, S4 formalizes)** — rejected: two homes for one artifact breaks "produced by exactly one stage", and every entry field (choice, bounding contract, documentation obligation) is already writable at triage time, so the split buys nothing except a synchronization defect class.

## Consequences

Easier: the WHAT loop closes cleanly against T2; freedom declaration is owner-visible, because deferrals ride the same ratification batches as arbitrary answers. Harder: deferrals discovered after S3 (P-IMPL inventions, gate construction, probe builds) must route as scoped S3 re-entries rather than being written into R-FR directly — one extra routing hop, accepted because it keeps every freedom on the decision-record trail. Downstream, task-03's checks can treat R-FR as available from S3 exit onward.

## References

- [`../2026-07-05-28.md`](../2026-07-05-28.md) — the source retrospective.
- `spec-completeness/process.md` — §7 production map (boundary note), §4.2 DEFERRABLE class, S3/S4 stage cards.
- `spec-completeness/artifact-model.md` — §2.2 R-FR definition, §4 rules T2 and T7.
- PR the decision was made in: #28.
