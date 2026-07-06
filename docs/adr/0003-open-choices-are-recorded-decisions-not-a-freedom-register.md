# ADR 0003: Open choices are recorded decisions, not a freedom register

- **Status**: Accepted
- **Date**: 2026-07-06
- **Deciders**: jonathan@manton.com (owner); Claude session

## Context

The artifact model includes a "freedom register": a first-class artifact cataloguing
choices the spec deliberately leaves to the implementer, each with a bounding
contract and a documentation obligation. The owner's objection: these are degrees of
freedom observed in the gold specs, and elevating them to a curated artifact treats
gaps as features. An implementation cannot be generated without these decisions being
made by someone; an open choice is therefore an unresolved spec defect, not a thing
to enshrine.

## Decision

The freedom register is removed as a first-class artifact. An open choice is a defect
in the question queue until it is resolved. Two resolutions are legal:

1. **The spec decides.** The answer lands in the spec like any other decision.
2. **The owner explicitly decides not to decide.** The implementer makes the call and
   documents what it picked. This ruling is recorded as an ordinary decision record —
   "left open on purpose" — not as an entry in a special register.

The point of recording the explicit "not chosen" is traceability of feedback: when the
owner later says "that's not what I want," the trail leads back to "this decision was
left open and ambiguous, and it had this effect."

## Alternatives considered

**Keep the freedom register as designed.** Rejected. It gives unresolved decisions a
respectable home and invites parking hard calls there instead of resolving them.

**Pin everything in the spec, no open choices at all.** Rejected. It forces the owner
to personally decide choices that genuinely do not matter to them and that the
acceptance tests cannot distinguish. Deciding-not-to-decide, made explicit, keeps the
owner in control without that ceremony.

## Consequences

- The coming rewrite removes the freedom-register artifact and reroutes its checks:
  hedge-word detection and "referenced but never defined" checks now report defects
  into the question queue instead of validating register entries.
- The decision log gains the "left open on purpose" form, giving feedback a place to
  land when an open choice turns out to matter after all.
- Nothing in a spec is silently open: every open choice is either a tracked defect or
  an explicit owner ruling.

## References

- [spec-completeness/artifact-model.md](../../spec-completeness/artifact-model.md) — defines the freedom register this decision removes
- [spec-completeness/process.md](../../spec-completeness/process.md) — the question queue and decision log that absorb its role
