# ADR: Spec quality is governed by WHAT/HOW layering with traceability rules T1–T7

- **ID**: ADR-add4c46d32
- **Status**: Draft (not yet adopted to docs/adr/)
- **Date**: 2026-07-05
- **Source retrospective**: ../2026-07-05-26.md
- **PRs covered**: #26

## Context

Task-01's central requirement was strict WHAT/HOW separation: contract
artifacts that survive a total rewrite of the realization, with every
realization element citing the contract it realizes. Decomposing the four
gold specs showed both that the discipline is *achievable* (the specs'
content re-sorts into the layers without residue) and that its absence is
*costly*: the zones where behavioral contract existed only inside pseudocode
(attractor's handlers, coding-agent-loop's core loop) are precisely where the
audited defects clustered — undefined helpers, phantom fields, internal
contradictions. The seven traceability rules (T1 realization grounding, T2
contract closure, T3 layer-1 self-sufficiency, T4 precedence and conflict,
T5 gate coverage and checkability, T6 reference closure, T7 freedom hygiene)
re-expressed all 14 audited defects and surfaced 11 more the audits missed.

## Decision

Specs authored in this repo separate contract (WHAT) from realization (HOW) per artifact-model.md, with conformance to traceability rules T1–T7 as the definition of a well-formed spec.

## Alternatives considered

- **Checklist-only quality control (README §3 as-is)** — rejected as the
  *sole* regime: the checklist audits a finished document but cannot
  localize defects to artifacts or make layering checkable; six gate-vs-body
  conflicts in gold specs were invisible to checklist-style review.
- **Aspirational layering without rules** — rejected: the gold specs
  themselves demonstrate that unenforced layering leaks (README §2.3), and
  "checkable, not aspirational" was the task's explicit requirement.

## Consequences

- Easier: defects become greppable rule violations; task-03 gets a concrete
  target (mechanize T1–T7); authoring order clarifies (contract before
  witness).
- Harder: authoring cost rises — C-BC must be written out even where
  pseudocode feels sufficient; that is the deliberate price, paid exactly
  where gold specs rotted.
- Accepted trade-off: T1–T7 depend on the citation-tag scheme; specs written
  without tags can only be checked approximately.

## References

- [`../2026-07-05-26.md`](../2026-07-05-26.md) — the source retrospective.
- [`./SKILL-SPEC-5203d49c36-known-defect-reexpression.md`](./SKILL-SPEC-5203d49c36-known-defect-reexpression.md) — the validation method that earned the rules their place.
- `spec-completeness/artifact-model.md` §1, §4, §9.
- PRs the decision was made in: #26.
