# ADR: Deprecate with the successor named, never delete

- **ID**: ADR-9f82550e42
- **Status**: Draft (not yet adopted to docs/adr/)
- **Date**: 2026-09-13
- **Source retrospective**: ../2026-09-13-50.md
- **PRs covered**: #50

## Context

The corpus owner judged that two of its pages no longer describe 2026 practice: an anti-pattern against shipping unreviewed agent code, and the positive pattern telling you to review every agent diff yourself. Both had multiple external sources, all of which predate the judgement, and the owner's own first-hand evidence contradicted them — a captured session covering six merged pull requests contains no instance of him reading a diff.

Removing them outright would have destroyed the record of why they were ever believed, and would have left dangling references from other pages, from source notes, and from the router. Leaving them adopted would have left the injectable checklist telling agents to do something the owner had explicitly rejected.

There was also a subtler risk, raised by a reader of the first-hand source: both pages were doing real work, and the defects that actually surfaced in that session — an agent claiming an artifact it had never produced, and a validator pinned to the wrong release — were not the kind a diff read catches. Deprecating the pages without saying what now catches those defects would remove a function from the corpus while leaving nothing in its place.

## Decision

A pattern page that no longer applies is marked deprecated and kept, and its deprecation note names where each surviving part of its function went.

Concretely: set `status: deprecated`; re-rate durability where the reason is that a model weakness has eased; leave existing sources and evidence lines unedited, since they still record what those sources said; add a dated note at the top of the body stating the judgement and listing, part by part, which pages absorbed which function; remove the page from the injectable checklist; reroute any task-router rows that pointed at it; and keep its row in the router with the deprecation stated in place of its trigger, so an agent meeting a stale reference elsewhere learns the status from the index rather than from the page it may never open.

## Alternatives considered

- **Delete the pages.** Rejected: it erases the reasoning, breaks inbound references, and leaves a future reader unable to tell whether the idea was considered and rejected or never considered.
- **Re-rate only, keeping them adopted.** Rejected as the weaker half of the change: the injectable checklist would still have carried "review every diff, always", the exact claim being rejected.
- **Rewrite both pages into narrower surviving forms.** Considered and offered; the owner chose deprecation instead. Distributing the surviving parts into pages that already existed achieved the same coverage without inventing two new hedged pages.
- **Drop the pages silently from the router.** Rejected: that is how a stale reference becomes undiagnosable. A router row that says "deprecated, see X instead" is the cheapest place for that information to live.

## Consequences

The corpus keeps its history and its inbound links stay valid, at the cost of carrying pages an agent must be told not to apply — which is why the router row and the body banner both exist. Deprecation also becomes a multi-file operation rather than a one-line status change: this session's two deprecations touched the page, the checklist, the category list, four task-router rows, the router file, and two absorbing pages.

The requirement to name the successor is the load-bearing part. It forces the question "what catches this now?" at the moment of deprecation, when the answer is still known.

## References

- [`../2026-09-13-50.md`](../2026-09-13-50.md) — the source retrospective.
- [`./SKILL-SPEC-b43c0c77d9-corpus-source-ingest.md`](./SKILL-SPEC-b43c0c77d9-corpus-source-ingest.md) — the ingest that produced the contradicting first-hand evidence.
- `agent-patterns/patterns/unreviewed-code.md` and `agent-patterns/patterns/review-agent-diffs.md` — the two deprecations.
- PR #50.
