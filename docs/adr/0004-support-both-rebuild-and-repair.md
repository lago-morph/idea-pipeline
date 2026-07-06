# ADR 0004: Support both rebuild and repair of implementations

- **Status**: Accepted
- **Date**: 2026-07-06
- **Deciders**: jonathan@manton.com (owner); Claude session

## Context

The authoring process assumes disposable implementations throughout: builder output is
"graded, archived, and abandoned," and a spec is frozen only after rounds of fresh
one-shot builds (ten passing builds across two rounds). The owner's correction:
one-shot specs were studied because they are examples of *complete* specs — evidence,
not the objective. The purpose of this work is to help build software specifically for
implementation by AI agents, not to join the "specs are the new deliverable" camp.
Throwaway builds are fine for flushing out large spec defects and horribly wasteful
for small changes or fixing one isolated part of the spec.

## Decision

The pipeline supports both paths, without assuming either:

- **Repair.** The existing implementation is kept. A spec change produces a matching
  implementation change, and re-running the spec's own acceptance checklist and smoke
  test proves spec and implementation still correspond.
- **Rebuild.** The implementation is discarded and rebuilt from the spec — including
  the several-parallel-builds form, which remains available as a diagnostic for
  finding large spec defects cheaply.

Which path to take is a tactical, per-change decision, not a process constant.

Two assumptions do hold universally: the spec is the source of truth, and an
implementation that does not correspond to the spec has defects. Having defects does
not mean the implementation is discarded.

## Alternatives considered

**Always rebuild (the process as written).** Rejected. The token cost is unjustifiable
for small changes; the owner is not made of tokens.

**Always repair.** Rejected. It gives up the genuinely useful diagnostic — parallel
independent builds are the cheapest known way to expose where a spec lets reasonable
implementers diverge — and sometimes a rebuild is honestly cheaper than a gnarly repair.

## Consequences

- The coming rewrite reworks the process document's build-and-grade stages and the
  freeze/re-verification rules so that repair is a first-class path, with the
  acceptance checklist serving as the standing conformance suite for a living
  implementation.
- The completeness bar is unchanged: a spec complete enough that an agent could build
  it without asking questions is exactly what makes small repairs safe later.
- Documentation gains a natural home: it belongs to the retained implementation and is
  repaired alongside the code rather than regenerated per build.

## References

- [spec-completeness/process.md](../../spec-completeness/process.md) — the build-and-discard stages this decision reworks
- [spec-completeness/README.md](../../spec-completeness/README.md) — the completeness checklist, which is unchanged by this decision
