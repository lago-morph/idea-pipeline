# ADR: Ideas reach agent-method only at named events with one relationship kind each

- **ID**: ADR-da90a66c30
- **Status**: Draft (not yet adopted to docs/adr/)
- **Date**: 2026-09-06
- **Source retrospective**: ../2026-09-06-41.md
- **PRs covered**: #41

## Context

Fourteen ideas were written for eventual inclusion in agent-method, each with a free-text trigger. The owner found the conditions and trigger points confusing and ambiguous. On inspection the triggers mixed four kinds of condition: work items already on agent-method's plan, thresholds on a judgment, symptoms of a run, and external events that might never happen. Some fired continuously rather than once. Some joined conditions with "or". The plan's sync table named the same events in different words. Nothing said what "pulled" meant.

Agent-method's own rule is that process is added only where real friction has been observed, and its lessons say a merge is never ratification. Any interface between this repository and agent-method has to respect both.

## Decision

Each idea in architecture-ideas/ideas carries one relationship kind, rule, rider, or conditional, and one event from a fixed named list shared with the plan, and its content lands in agent-method only as part of the work item that event names.

Every idea has exactly one relationship kind and one event. A rule applies every time its recurring event happens and is never pulled once. A rider is carried into one specific agent-method work item as extra columns or sections of that item's proposal, never as a standalone change. A conditional waits on an event that may never happen for the workbench. Events are a short fixed list, written out by name, identical in the README, the plan, and every idea's front matter. Each idea names the friction in agent-method that justifies it; "none yet" is what makes it conditional. An idea is pulled when its content appears in a ratified agent-method artifact, ratified meaning the owner said so in conversation.

## Alternatives considered

- **Free-text triggers per idea**: rejected by the owner as confusing and ambiguous; they cannot be lined up against agent-method's plan and mix incompatible kinds of condition.
- **Standalone pull requests to agent-method per idea**: rejected because agent-method adds process only on observed friction and one artifact at a time; a standalone change arrives without the work item that justifies it.
- **Short event codes shared between files**: tried and rejected by the owner: codes are confusing for things he must review or follow; names are used instead.

## Consequences

Easier: a reader can line up any idea against agent-method's next steps in one table, and the plan and the ideas cannot drift because they share names. Harder: an idea that fits two events has to be split, and the event list has to be maintained as agent-method's sequence changes. The trade-off accepted is that a slightly rigid list is better than a flexible one nobody can follow.

## References

- [`../2026-09-06-41.md`](../2026-09-06-41.md): the source retrospective.
- [`../../architecture-ideas/spine/overview.md`](../../architecture-ideas/spine/overview.md): the spine overview this decision governs.
- [`../../architecture-ideas/plan.md`](../../architecture-ideas/plan.md): the plan that applies it.
- [`./SKILL-SPEC-6c79deb0a5-repo-orientation-report.md`](./SKILL-SPEC-6c79deb0a5-repo-orientation-report.md): how agent-method's conventions were learned before the shadow-first rule was set.
- PRs the decision was made in: #41.
