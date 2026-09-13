# ADR: One artifact per pull request for idea documents and skills

- **ID**: ADR-524c3dd121
- **Status**: Draft (not yet adopted to docs/adr/)
- **Date**: 2026-09-13
- **Source retrospective**: ../2026-09-13-48.md
- **PRs covered**: #44, #45, #46, #47, #48

## Context

The session's designated branch began carrying two things: the scoped-sandbox transcription and, later, the secrets transcription that had been added to the same branch for convenience. The author asked for "an isolated pr for this transcription." The secrets file was carved onto a fresh branch from `origin/main`, merged as #47, and `main` merged back so #44's diff returned to one file. The two skills and the skill revision each got their own branch and PR (#45, #46, #48) as a matter of course.

Every isolated PR merged with a single call — including the last one, requested because "the GitHub interface is being strange." A PR carrying two documents would have forced the author to merge both or neither. The convention outlives the session because the retrospective skill mines merged PRs by number and treats each as a unit of work; one artifact per PR keeps that record legible.

## Decision

Each idea document and each skill change is delivered in its own pull request branched from origin/main, and a long-running working branch re-syncs by merging main so its diff stays at one artifact.

## Alternatives considered

- **One session branch carrying everything** — how the session started; rejected by the author the first time it mattered.
- **Stacked PRs** (each branched from the previous) — rejected: the tooling here has no stack-aware merge, so a stack becomes a merge-order puzzle, and a squash merge of the base rewrites the history the stack depends on.
- **Commit skills into the same PR as the document they helped produce** — rejected: the skill is reused across documents and should merge on its own schedule; the first skill (#45) had to be merged before it could be applied to verify the document it was written for.

## Consequences

*Easier:* any artifact can be merged the moment it is ready, independently; PR bodies describe one thing; the retrospective's commit-by-PR table is one artifact per section.

*Harder / accepted:* more branches and more PRs per session (five here), and a carve-out procedure when a file lands in the wrong place — two git commands, recorded in the agents-file rule of the same name. After a squash merge the working branch must not be reset in place (destructive git operations are denied in this environment); follow-up work starts from a fresh branch instead.

## References

- [`../2026-09-13-48.md`](../2026-09-13-48.md) — the source retrospective.
- [`./AGENTS-MD-3fade0ecfb-one-artifact-per-pull-request-for-idea-documents-and-skills.md`](./AGENTS-MD-3fade0ecfb-one-artifact-per-pull-request-for-idea-documents-and-skills.md)
- [`./AGENTS-MD-64fed5f8d3-start-follow-up-work-from-a-fresh-branch-off-originmain-after-a-merge.md`](./AGENTS-MD-64fed5f8d3-start-follow-up-work-from-a-fresh-branch-off-originmain-after-a-merge.md)
- PRs the decision was made in: #44, #45, #46, #47, #48.
