# ADR: Transcriptions capture author intent; the agent's contribution is mechanical only

- **ID**: ADR-b051a79e17
- **Status**: Draft (not yet adopted to docs/adr/)
- **Date**: 2026-09-13
- **Source retrospective**: ../2026-09-13-48.md
- **PRs covered**: #44, #45, #46, #48

## Context

The first version of the `handwritten-notes-transcription` skill treated the raw transcription as strictly verbatim: the ink was the record, and the only permitted edit was a correction against the page. Applied to the scoped-sandbox notes, that rule produced bracketed provenance notes stapled to the author's own words — "[the page has a single short word where this phrase now stands; the author supplied the full wording]" — because the author had resolved an unreadable word by expanding it into a sentence and moved a margin note to the bullet it belonged to.

The author rejected the brackets: "My intention was to rearrange and add sentence when transcribing." The transcription's job is to capture what the author *meant to write*, and the author is the only party entitled to say what that was. The same principle then governed the session capture (Appendix A) and was written into the second skill, `preserve-context`, from the start. It is architectural because it fixes the meaning of "raw transcription" across every idea document and both transcription skills.

## Decision

In transcription-type work — handwritten notes and session captures — the record is the author's intent: the author may correct a reading, rearrange lines, or expand shorthand into full sentences, and those edits are the transcription written clean, while the agent contributes only mechanical reading, structure preservation, and marking of what it cannot read; enhancement and reorganization are fenced to a separate later step.

## Alternatives considered

- **Strict verbatim with provenance brackets** — tried in PR #44's first commits. Rejected by the author: it annotates the author's own intent as if it were an agent's guess, and clutters the record with process detail the author does not want.
- **Agent-tidied transcription** (expand `w/`, fix spelling, merge fragments) — never attempted; rejected on principle. It is agent invention, and a confident tidy-up does not look like it needs checking.
- **Ask the author, per edit, whether it is transcription or enhancement** — rejected as ceremony. The author's stated frustration trigger is "tedious ceremony"; the distinction is theirs to draw implicitly by making the edit.

## Consequences

*Easier:* author corrections fold in with no annotation and no round-trip; the transcription reads as the author's document, not a forensic record. The boundary the agent must hold is simple and mechanical: read the marks, keep the structure, mark what you can't read, never infer.

*Harder / accepted:* ink-level fidelity is given up. The committed transcription is the intent-level record; the page itself lives only in the session upload, which is not committed. If ink-level fidelity is ever needed for a document, the source scan must be kept alongside it — that is an open question, not decided here. The "author intent in, agent invention out" line also demands the attribution-drift re-read (see the agents-file rule of that name), because the only way the agent can break the rule is silently.

*Applies to:* `handwritten-notes-transcription`, `preserve-context`, and any future skill that speaks for the author.

## References

- [`../2026-09-13-48.md`](../2026-09-13-48.md) — the source retrospective.
- [`../../.claude/skills/handwritten-notes-transcription/SKILL.md`](../../.claude/skills/handwritten-notes-transcription/SKILL.md)
- [`../../.claude/skills/preserve-context/SKILL.md`](../../.claude/skills/preserve-context/SKILL.md)
- [`../../13-scoped-sandbox.md`](../../13-scoped-sandbox.md)
- PRs the decision was made in: #44, #45, #46, #48.
