# ADR: Idea documents keep raw transcription and session captures verbatim beneath any later organization

- **ID**: ADR-fdde1d0a37
- **Status**: Draft (not yet adopted to docs/adr/)
- **Date**: 2026-09-13
- **Source retrospective**: ../2026-09-13-48.md
- **PRs covered**: #44, #47, #48

## Context

Both idea documents produced this session (`13-scoped-sandbox.md`, `14-scoped-secrets.md`) follow the same shape: `# Title`, a `**Source:**` line, a `## Raw transcription` section holding the notes as transcribed, and — for 13 — `## Appendix A — Session capture` holding the conversation by topic. The author asked that the capture be "pre-emptively" labelled an appendix so that organized content could go above it later, and said of the raw transcription that it "must always be preserved along with any of the other products in the session."

The convention was then written into the `preserve-context` template (an "Appendix X" skeleton) and the `handwritten-notes-transcription` skill ("in a file, it lives under its own `## Raw transcription` heading; everything else goes in other sections"). It is architectural because it fixes the layout every future idea document and both skills assume.

## Decision

An idea document `NN-name.md` opens with a title and source line, keeps the verbatim `## Raw transcription` of its source, and appends each session capture as a lettered appendix; both are preserved unchanged and additively, and any organized or synthesized content produced later is added as its own section rather than replacing them.

## Alternatives considered

- **Replace the raw transcription with an organized version once one exists** — rejected by the author explicitly; the raw material is the artifact of record and organized content is an addition.
- **Keep captures in separate files** (`13-scoped-sandbox-capture.md`) — not chosen; the author wanted the capture "in a section of that 13 document" so the whole context stays together. A separate file was proposed only for the future Later list, and even that was deferred.
- **Put organized content below the raw material** — not chosen; the appendix label signals the raw material sinks to the bottom as organization accrues above it.

## Consequences

*Easier:* every idea document has the same shape, so a reader (or the `preserve-context` skill) knows where the verbatim material is and where to add. Captures are additive; nothing is lost when a document is reorganized.

*Harder / accepted:* documents grow long — `13-scoped-sandbox.md` is ~480 lines with one capture and no organized content yet. The exact placement of organized content relative to the raw transcription (directly under the source line, or with the raw transcription itself demoted to an appendix) was **not decided** in this session; the ADR records only that raw material is kept verbatim and organized content is additive.

## References

- [`../2026-09-13-48.md`](../2026-09-13-48.md) — the source retrospective.
- [`../../13-scoped-sandbox.md`](../../13-scoped-sandbox.md)
- [`../../14-scoped-secrets.md`](../../14-scoped-secrets.md)
- [`../../.claude/skills/preserve-context/templates/capture-template.md`](../../.claude/skills/preserve-context/templates/capture-template.md)
- PRs the decision was made in: #44, #47, #48.
