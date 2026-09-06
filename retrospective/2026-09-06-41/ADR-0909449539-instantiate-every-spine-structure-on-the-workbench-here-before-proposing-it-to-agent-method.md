# ADR: Instantiate every spine structure on the workbench here before proposing it to agent-method

- **ID**: ADR-0909449539
- **Status**: Draft (not yet adopted to docs/adr/)
- **Date**: 2026-09-06
- **Source retrospective**: ../2026-09-06-41.md
- **PRs covered**: #41

## Context

Agent-method's history is two abandoned attempts that designed structure in the abstract, followed by a restart that grows only from real content. The spine drafted in this session is structure, and the risk that it repeats the abstract failure is the main risk the plan names. At the same time agent-method's workbench must stay self-contained so it can move to its own repository, and nothing may land there ahead of its trigger. So the spine cannot be validated by editing agent-method, and cannot be trusted without validation.

The session's drafts already showed the value of instantiation: filling in the workbench's profile exposed that its statefulness is "local" not "none", because the vision commits to durable storage, which is the profile-versus-maturity distinction on real content. The maturity ladder's gap analysis reproduced agent-method's own list of guides to write, which is the evidence that the ladder adds nothing to agent-method's rule.

## Decision

Every spine structure is instantiated for idea-workbench under architecture-ideas/testbed in this repository, and validated there, before any piece derived from it is proposed to agent-method.

Each spine structure gets a shadow instance for the workbench under `architecture-ideas/testbed/workbench/`, regenerated from agent-method's current state at the start of each plan phase and never edited independently of it. Only after a structure fits the workbench's real content without forcing is any piece derived from it proposed to agent-method, through agent-method's own process. Where the workbench does not fit, the spine definition changes and the change is recorded in the decisions log.

## Alternatives considered

- **Propose spine pieces directly to agent-method as they are drafted**: rejected because it violates agent-method's friction-first rule and puts unvalidated structure in front of the owner as if it were ready.
- **Validate on a hypothetical system instead of the workbench**: rejected because hypothetical content is exactly the abstraction that killed the archived attempts; the workbench is small, real, and already has decisions notes to rewrite as records.
- **Edit the workbench inside agent-method to add spine fields**: rejected because the workbench must stay self-contained and unaware of anything outside agent-method's conventions.

## Consequences

Easier: the spine is tested on real content before anyone else sees it, and the artifact-count test has a concrete subject. Harder: the shadow and the real workbench can diverge, so the shadow must be disposable and regenerated rather than maintained, and a phase cannot start until the regeneration is done. The trade-off accepted is duplicated content in exchange for a structure that has earned its way into agent-method.

## References

- [`../2026-09-06-41.md`](../2026-09-06-41.md): the source retrospective.
- [`../../architecture-ideas/spine/overview.md`](../../architecture-ideas/spine/overview.md): the spine overview this decision governs.
- [`../../architecture-ideas/plan.md`](../../architecture-ideas/plan.md): the plan that applies it.
- [`./SKILL-SPEC-6c79deb0a5-repo-orientation-report.md`](./SKILL-SPEC-6c79deb0a5-repo-orientation-report.md): how agent-method's conventions were learned before the shadow-first rule was set.
- PRs the decision was made in: #41.
