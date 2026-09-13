# ADR: Generated artifacts carry a format contract and a read-back check

- **ID**: ADR-8612dadc27
- **Status**: Draft (not yet adopted to docs/adr/)
- **Date**: 2026-09-13
- **Source retrospective**: ../2026-09-13-50.md
- **PRs covered**: #50

## Context

The `agent-patterns` wiki generates four artifacts from its pattern pages, one of which — `skill/agent-patterns/patterns-list.md` — is the router an agent uses when the full wiki is not reachable. Its entire specification was a parenthetical: "(id — title — one line)". A build session generated it by regex-pulling the first line after each page's `**Use when:**` marker. Pattern bodies are hard-wrapped at about eighty columns, so the regex captured the first *physical* line rather than the first sentence: **30 of 36 rows were cut mid-sentence**, and the one page using an allowed heading variant produced an empty description. Nothing errored. The file remained well-formed, and the failure was only visible to a reader who compared a row against the page it pointed at.

The same class of failure had already been identified in an earlier retrospective, as a proposed rule about grepping generated output for empty extracted fields. That rule was written down and never assembled into the project's agents file, so it bound nothing, and the artifact it described was still broken months later.

## Decision

Every generated file in the corpus has its row or line format specified in SPEC.md, and lint reads each generated file back before committing it.

Concretely: SPEC gains a section per generated artifact defining the row shape and what each field must contain; and a generation-check section requiring that generated output be read back and checked mechanically for empty fields, truncated rows, and every heading variant the source pages are permitted to use. AGENTS.md mirrors both as a lint step.

## Alternatives considered

- **Write a generator script.** Rejected: the corpus's own charter forbids scripts until a workflow proves too slow by hand, and a script would have had the same bug. The defect was an unspecified output format, not a missing tool. A script written against the same unstated contract truncates identically.
- **Fix the artifact and move on.** Rejected: the artifact had no contract, so the next regeneration would reproduce the truncation. The rows were rewritten *and* the contract written, in that order of importance.
- **Drop the artifact.** Rejected: it is the only index an agent has when the full corpus is unreachable, which is precisely the situation where a degraded index does most harm.
- **Rely on the earlier proposed rule.** Rejected as already falsified — the rule existed in a retrospective and changed nothing, because nothing assembled it into force.

## Consequences

Regenerating a derived artifact now costs more: each row is authored rather than extracted, and the output must be checked before commit. In exchange, the check is mechanical and cheap to run — this session's version verifies id-set equality, sort order, terminal punctuation, field emptiness, length, and agreement between each row's status label and the page's frontmatter, and it caught a label mismatch immediately after a status change.

The contract also makes a silent failure loud. A truncated row now fails a check rather than waiting for a future consumer to misbehave. The residual risk is that the check itself is prose in a lint step and can be skipped — which is the same weakness the corpus documents elsewhere, and an argument for eventually making it a hook.

## References

- [`../2026-09-13-50.md`](../2026-09-13-50.md) — the source retrospective.
- [`./SKILL-SPEC-b43c0c77d9-corpus-source-ingest.md`](./SKILL-SPEC-b43c0c77d9-corpus-source-ingest.md) — the ingest procedure whose final step is the read-back.
- `agent-patterns/SPEC.md` §5.11 and §5.11.1 — the contract and the generation check as adopted.
- PR #50.
