# ADR 0005: Documentation deliverables are first-class, default-on, and deferrable

- **Status**: Accepted
- **Date**: 2026-07-06
- **Deciders**: jonathan@manton.com (owner); Claude session

## Context

The owner wants documentation in the Diátaxis framework — tutorial, how-to guides,
reference, and explanation — supported as a standard deliverable of the pipeline. The
gold specs never shipped documentation, so the sixteen-artifact model has no homes for
the information documentation needs (who the users are, what tasks they perform, how
to think about the system, what was decided and why). At the same time, mandating all
four document types for every project would be empty ceremony for internal plumbing
that only the owner touches.

## Decision

The pipeline supports all four documentation types as first-class deliverables:
the structure always provides places to put the information they need, so producing
them is always possible. The default for a project is to include them. A project may
explicitly defer any of them — until later, or until never — and that deferral is
recorded with the project's requirements (at the system-vision level or adjacent;
the exact slot gets settled in the coming rewrite). Supported, not mandated.

The information homes, in brief: use cases feed the how-to guides and the tutorial;
the decision log (including alternatives that were rejected and choices explicitly
left open) feeds the explanation docs; the structured spec sections plus the
implementer's documented choices feed the reference docs.

## Alternatives considered

**Mandate all four for every project.** Rejected. A tutorial for a piece of internal
infrastructure with exactly one user is ceremony, not documentation.

**Leave documentation fully optional with no default.** Rejected. With no default and
no recorded deferral, documentation silently never happens.

## Consequences

- The coming rewrite adds the information homes and the checks that go with them
  (e.g., every use case is covered by a how-to guide unless the guide was explicitly
  deferred), and stops discarding the decision-log material that explanation docs
  need.
- Deferral is visible and reviewable: skipping documentation is a recorded decision
  with a reason, never an omission.
- Under ADR-0004, documentation is maintained with the living implementation rather
  than rebuilt per build.

## References

- [ADR-0001: Use cases are the driving artifact](./0001-use-cases-are-the-driving-artifact.md)
- [ADR-0003: Open choices are recorded decisions](./0003-open-choices-are-recorded-decisions-not-a-freedom-register.md)
- [ADR-0004: Support both rebuild and repair](./0004-support-both-rebuild-and-repair.md)
- [Diátaxis framework](https://diataxis.fr/) — the four documentation types
