# ADR: The architecture framework's data model is six named structures

- **ID**: ADR-ba464ab8f3
- **Status**: Draft (not yet adopted to docs/adr/)
- **Date**: 2026-09-06
- **Source retrospective**: ../2026-09-06-41.md
- **PRs covered**: #41

## Context

The session set out to structure every decision needed to go from an idea to a running system, for use by agents and humans. The owner's first instinct was to start with a data model. Reading agent-method showed that its artifact graph with typed two-way links already served as a data model for functional artifacts, and that its two archived attempts had collapsed under abstract structure designed ahead of content. The owner then pushed back on the nuggets-only approach, saying free-form notes work for a while and then collapse under their own weight, and asked for the structure that pulls artifacts, concerns, and subjects together for a whole system.

The tension is between two failure modes: too little structure, which agent-method's note pile will eventually hit, and too much, which killed its predecessors. The decision fixes the amount of structure at six things that can each be validated against the workbench, and makes growth beyond six expensive by rule.

## Decision

The architecture framework's data model is exactly six structures, system profile, maturity ladder, subject catalog, artifact type registry, decision records, and derivation graph, and any proposed seventh must first be attempted as a field on one of the six and recorded either way.

The six structures are the whole data model. Everything discussed in the session, status vocabulary, binding time, binding level, provenance, five kinds of guidance, concern tags, refinement stages, dependency kinds, is a field, a status, or a link type on one of the six. The three things that ride on the spine, modes of entry, verification at three levels, and the harvest loop, are operations over the six and add no structure. A proposal for a new structure is first written up as a field on an existing one; if that fails, the failure is recorded in the decisions log before a seventh is admitted.

## Alternatives considered

- **A separate data model authored first, as the owner initially proposed**: rejected because agent-method's graph already is a data model for the functional layer, and a second model would duplicate it; the six structures extend that graph rather than replacing it.
- **Nuggets only, pulled into agent-method one at a time with no spine**: rejected by the owner: it reproduces the free-form-notes collapse more slowly, and gives a real application no way to say which artifacts are required, who decided what, or what to change when a prototype is wrong.
- **An open-ended framework that adds structures as needs appear**: rejected because that is how every traditional architecture framework grew past usability, and how agent-method's archived attempts died; the seventh-structure rule is the guard.

## Consequences

Easier: every idea has a home, and the question "where does this go" has a mechanical answer. The owner can review a prototype by walking decision records by subject and revising at the root cause. Harder: some things will fit awkwardly as fields, and the pressure to add a seventh structure will be constant. The trade-off accepted is that awkward fields are cheaper than an eighth and twelfth structure. The plan's standing checks include the seventh-structure check so the pressure is visible rather than silent.

## References

- [`../2026-09-06-41.md`](../2026-09-06-41.md): the source retrospective.
- [`../../architecture-ideas/spine/overview.md`](../../architecture-ideas/spine/overview.md): the spine overview this decision governs.
- [`../../architecture-ideas/plan.md`](../../architecture-ideas/plan.md): the plan that applies it.
- [`./SKILL-SPEC-54447908e8-design-discussion-capture.md`](./SKILL-SPEC-54447908e8-design-discussion-capture.md): the capture skill whose interface rules this decision fixes.
- PRs the decision was made in: #41.
