# ADR: Concrete syntax lives in R-IS and classification is by role

- **ID**: ADR-3226b5ccdc
- **Status**: Draft (not yet adopted to docs/adr/)
- **Date**: 2026-07-05
- **Source retrospective**: ../2026-07-05-26.md
- **PRs covered**: #26

## Context

Task-01 flagged one classification tension the model was required to resolve:
where concrete input syntax (attractor's DOT BNF, coding-agent-loop's v4a
patch grammar) belongs. The decompositions settled it: attractor natively
splits expression *syntax* (§10.2) from evaluation *semantics* (§10.3),
proving the seam is real; and the v4a case showed the abstract twin is
sometimes operation semantics (C-BC) rather than an entity (C-DM) — no
abstract PatchOperation record exists. Two corpus facts made the corollary
mandatory: attractor writes an *abstract* enum in BNF notation (L1141–47),
and normative wire contracts live in *appendices* (attractor App C,
coding-agent-loop App B) while rationale sits in normative bodies — so any
classifier keyed on notation or document position misfiles real gold-spec
content.

## Decision

Concrete input syntax (grammars, wire formats) belongs to R-IS with its abstract twin in C-DM or C-BC, and all artifact classification keys on content role, never notation or document position.

## Alternatives considered

- **Grammars in C-DM (syntax as part of the domain)** — rejected by the
  rewrite test: swapping DOT for YAML must not change the domain truth "a
  workflow is one directed graph of typed-attributed nodes and edges".
- **Notation-keyed classification (BNF ⇒ interface, table ⇒ data, appendix
  ⇒ annex)** — rejected on direct counterexamples in the corpus (abstract
  enum in BNF; normative appendix content; body-resident rationale).

## Consequences

- Easier: the four decomposition tables apply one consistent test; task-03
  checkers know that surface form is never sufficient evidence for artifact
  membership.
- Harder: classification requires reading for role, which resists full
  automation — the deterministic tier can flag candidates but the call is
  semantic.
- Accepted trade-off: some grammars will lack a written abstract twin
  (attractor's core Graph/Node/Edge entity had to be reconstructed);
  the model treats the missing twin as the defect, not the grammar's
  placement.

## References

- [`../2026-07-05-26.md`](../2026-07-05-26.md) — the source retrospective.
- `spec-completeness/artifact-model.md` §2.1 (position statement) and §8
  (its consistent application).
- PRs the decision was made in: #26.
