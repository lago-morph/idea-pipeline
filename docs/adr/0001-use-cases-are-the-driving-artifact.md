# ADR 0001: Use cases are the driving artifact of the idea-to-spec pipeline

- **Status**: Accepted
- **Date**: 2026-07-06
- **Deciders**: jonathan@manton.com (owner); Claude session

## Context

The spec-completeness work derived a sixteen-artifact model and an authoring process
from four "gold" specs that AI agents reliably built in one shot. Owner review found
two problems. First, the model has no home for who uses the system and what they are
trying to accomplish — use cases are absent, and only one privileged flow (the smoke
test) survives into the finished spec. Second, the information a human needs in one
place to judge "is this the right thing to build?" is scattered across many normalized
files, which the owner has described as "like reading directly from individual tables
in a SQL database." Humans are the ultimate arbiter and approver of these artifacts;
a review surface they cannot use misses the point. The gold specs are evidence of
what complete looks like — a start, not the finish.

## Decision

One authored use case document per user goal becomes the driving artifact of the
pipeline. Each use case has the traditional, human-reviewable shape: who the user is,
what they are trying to get done, the step-by-step scenario, what can go wrong, and
how you know it worked. A one-page list of all use cases (the kinds of users, one
line per goal) sits in front of them as the index.

Use cases carry an honestly scored maturity level. Freeform text is allowed at L0
and while drafting L1. From L1 on, load-bearing content must be structured so
deterministic linting is possible. Parts of a use case may remain incomplete while
being worked out, with the level score saying so honestly.

The rigor of the prior artifact model's information kinds is retained, not discarded:
typed data definitions, complete enumerations, total state machines, precedence rules
with tie-breaks, failure semantics, and mechanically checkable acceptance criteria all
keep their structured forms. Each kind either moves its home into the use case's
structured sections or stays in a shared section with linters enforcing consistency
between the use case and the shared content.

The AI implementer receives the use cases as part of its input.

## Alternatives considered

**Generate use-case views from the normalized artifacts instead of authoring them.**
Rejected. Review must happen on a real, commentable artifact; a compile-comment-
redistribute round trip is clumsy, and the generated view makes the primary human
review surface a derived afterthought.

**Keep pure normalized authoring with review only on the compiled single file.**
Rejected. Owner review happens during authoring, and scattering highly-relevant
information across many files makes human completeness- and appropriateness-auditing
impractical, whatever the linters can verify mechanically.

**Fully freeform use cases at every maturity level.** Rejected. Freeform text cannot
be linted deterministically, so consistency between use cases and shared spec content
would rest on eyeballs alone. Structure is the price of reliable consistency checking.

## Consequences

- Humans get a first-class early review surface ("is this the right thing?") in
  addition to the compiled spec ("is the full definition right?").
- Per-level validation checklists — the thorough checklists that decide whether a use
  case has genuinely reached a claimed level — must be authored. **Recorded as a TODO;
  future work.**
- Shared cross-cutting content (domain model, shared state machines) needs explicit
  linter rules tying use cases to it; those checks are part of the coming rewrite of
  the spec-completeness documents.
- Noted for later, out of scope now: "scenarios" — concrete instances of a use case
  with specific behavior and data, withheld from the implementer and used to validate
  the finished solution.

## References

- [spec-completeness/README.md](../../spec-completeness/README.md) — the gold-spec findings and completeness checklist
- [spec-completeness/artifact-model.md](../../spec-completeness/artifact-model.md) — the sixteen-artifact model this decision reshapes
- [spec-completeness/process.md](../../spec-completeness/process.md) — the authoring process this decision reshapes
- [ADR-0002: DRY is a guideline; linted duplication is allowed](./0002-dry-is-a-guideline-linted-duplication-allowed.md)
