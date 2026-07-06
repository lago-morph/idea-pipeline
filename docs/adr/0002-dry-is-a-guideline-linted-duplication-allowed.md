# ADR 0002: DRY is a guideline; linted duplication is allowed

- **Status**: Accepted
- **Date**: 2026-07-06
- **Deciders**: jonathan@manton.com (owner); Claude session

## Context

The artifact model treats single-source-of-truth as close to absolute: consolidated
views must be derived, never hand-maintained, because one gold spec's hand-maintained
"complete reference" appendix silently rotted (it omitted six knobs the body defined).
That rule pushes all information toward exactly one normalized home, which directly
conflicts with keeping information co-located where a human needs it — the use case
problem in ADR-0001.

The owner's position: DRY is a guideline, not a no-exceptions rule. Treating it as
absolute is silly when linters can verify that duplicated statements agree.

## Decision

Duplication of load-bearing information across documents is permitted when a
deterministic linter verifies the copies stay consistent. Where normalization costs
the human reader nothing, prefer it; where human reviewability and co-location are at
stake, duplicate and lint.

The observed failure mode (the rotted appendix) is reclassified: the defect was not
duplication — it was duplication *without a covering check*. Duplicated content with
no covering consistency check remains a defect.

## Alternatives considered

**Strict single source of truth with derived views only.** Rejected. It makes every
human-friendly presentation a generated artifact, which puts the primary review
surface downstream of a compiler and makes commenting on it a round trip.

**Unchecked duplication.** Rejected. The gold-spec corpus demonstrates exactly how it
fails: hand-maintained copies drift silently and read as authoritative while wrong.

## Consequences

- The linter suite grows consistency checks between co-located use-case content and
  shared spec sections; authoring these checks is part of the coming rewrite.
- Documentation-specific deliverables that restate spec content are acceptable —
  they need a covering check, not an exemption argument.
- The "derived, never hand-maintained" rule survives only for content nobody needs to
  review in place (e.g., generated tables of contents and cheat-sheets).

## References

- [ADR-0001: Use cases are the driving artifact](./0001-use-cases-are-the-driving-artifact.md)
- [spec-completeness/artifact-model.md](../../spec-completeness/artifact-model.md) — the derivation-only redundancy rule this decision relaxes
- [spec-completeness/hardening/checks.md](../../spec-completeness/hardening/checks.md) — the check suite that gains the consistency checks
