# ADR: Artifact IDs are a stable, additive-only vocabulary

- **ID**: ADR-8a4c5eccea
- **Status**: Draft (not yet adopted to docs/adr/)
- **Date**: 2026-07-05
- **Source retrospective**: ../2026-07-05-26.md
- **PRs covered**: #26

## Context

The artifact IDs defined in `spec-completeness/artifact-model.md` (`A-VS`,
`C-DM`, `R-FR`, `G-AC`, …) are not private to that document: the task-02 and
task-03 prompt files embed them verbatim as their working vocabulary, and
task-03's planned checkers will grep for them. During the task-01 session the
owner was asked explicitly how much freedom existed to change the hypothesized
IDs; the answer — "stable IDs, additive OK" — was then load-bearing for every
subsequent design decision. Validation pressure produced exactly one addition
(`R-AS`) and four definition-level refinements, zero renames, and the
downstream task files remained accurate without edits.

## Decision

Spec-artifact IDs, once published in artifact-model.md, are never renamed or deleted; evolution is additive (new IDs) or definitional (boundary refinements documented in delta lists).

## Alternatives considered

- **Free restructuring with synchronized downstream edits** — rejected: every
  rename forces same-PR edits to task prompts and future checkers, turning a
  vocabulary tweak into a cross-cutting change with silent-miss risk (a stale
  ID in an unedited file keeps "working" as prose while meaning nothing).
- **Frozen set (no additions either)** — rejected: validation demonstrably
  required a new artifact (all four gold specs carry architecture content the
  hypothesized set could not house); a freeze would have forced misfiling it.

## Consequences

- Easier: downstream documents and checkers can hard-code IDs; grep stays a
  reliable discovery tool; historical documents never go stale on vocabulary.
- Harder: a genuinely wrong name must be lived with (mitigated by IDs being
  short codes whose meaning lives in the definition, not the letters).
- Accepted trade-off: definition drift is possible under a stable ID — which
  is why every definitional refinement must be recorded in a delta list with
  its forcing evidence (artifact-model.md §2.1 is the pattern).

## References

- [`../2026-07-05-26.md`](../2026-07-05-26.md) — the source retrospective.
- `spec-completeness/artifact-model.md` §2.1 and §12 — the delta list and the
  vocabulary note this decision generalizes.
- PRs the decision was made in: #26.
