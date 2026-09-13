# ADR: Idea documents record stated positions, not decisions

- **ID**: ADR-81144f763e
- **Status**: Draft (not yet adopted to docs/adr/)
- **Date**: 2026-09-13
- **Source retrospective**: ../2026-09-13-48.md
- **PRs covered**: #44, #48

## Context

Appendix A of `13-scoped-sandbox.md` was written to capture a long design conversation by topic. Its first draft marked seven of the author's firmer statements as *explicit decision* — no stubs, Beads as carrier, snapshot as file list plus commit hash, and so on. The author corrected the framing in one sentence: "the only decisions made have been how we handled the original transcription and how we handle this idea transcription. Anything I stated as a decision was a statement of my opinion at a specific point in time. I don't want decisions solid until later."

This is a repo-wide convention, not a one-document fix. The idea pipeline exists to let ideas be captured early and chewed on later; a document that records decisions forecloses exactly the later thinking it is meant to enable. The `preserve-context` skill encodes the rule; this ADR records it as the convention for every idea document.

## Decision

In idea-pipeline documents and session captures, statements about an idea are recorded as positions at a point in time — the firmest marked *stated position* — and the only decisions recorded are process decisions about how the document itself was made, until a separate, explicit decision step occurs.

## Alternatives considered

- **Mark explicit decisions inline where the author spoke firmly** — tried; corrected by the author within the same session. Firmness is not the same as decision, and only the author can tell them apart.
- **No markers at all** — rejected because it loses real information: a future reader should be able to see which positions the author held firmly and which were exploratory.
- **A status field per statement** (open / leaning / decided) — rejected; it is organizing, which is the processing step these documents defer. It also invites the agent to assign status, which is the failure mode.

## Consequences

*Easier:* idea documents stay open by construction. A later synthesis step is required to turn positions into decisions, and that step is visible as its own act — an ADR, a spec, an organized section above the raw material. Readers can still see firmness through the *stated position* marker.

*Harder / accepted:* the phrasing is slightly more verbose, and process decisions must be distinguished from content decisions explicitly in each capture's introduction. Agents must resist a strong default: when a human says "X, explicit," the natural record is "decided X." Here it is "J placed X firmly, as stated at the time."

*Applies to:* `NN-name.md` idea documents, their appendices, and captures produced by `preserve-context`.

## References

- [`../2026-09-13-48.md`](../2026-09-13-48.md) — the source retrospective.
- [`../../13-scoped-sandbox.md`](../../13-scoped-sandbox.md)
- [`../../.claude/skills/preserve-context/SKILL.md`](../../.claude/skills/preserve-context/SKILL.md)
- PRs the decision was made in: #44, #48.
