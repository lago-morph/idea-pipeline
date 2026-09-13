# ADR: Corroboration requires independent sources, not independent evidence lines

- **ID**: ADR-a4e4ec4f8e
- **Status**: Draft (not yet adopted to docs/adr/)
- **Date**: 2026-09-13
- **Source retrospective**: ../2026-09-13-50.md
- **PRs covered**: #50

## Context

The corpus promotes a pattern from `candidate` to `adopted` — which is what puts it in the injectable checklist agents load — on an evidence threshold. That threshold was written as "promote candidates with ≥ 2 evidence lines". Read literally, a page clears the bar by quoting one source twice.

This was not hypothetical. Twice in one session the threshold had to be worked around by hand. A page whose only source supported two distinct observations was deliberately given **one** evidence line, because two would have tripped an automatic promotion on a single finding. A second page was given one line for the same reason. Meanwhile three existing candidate pages were found carrying two and three evidence lines each, all from a single source, and correctly left unpromoted — the build session had silently applied the stricter reading the written rule did not state.

A sharper case arrived with the session's first-hand source. The corpus ingested a practitioner's own project, and the same practitioner separately stated his position in conversation, which the corpus records as `[own]` experience. Counted as documents these are two sources. Counted as perspectives they are one person, and two evidence lines from them corroborate nothing.

## Decision

A pattern is promoted to adopted only when at least two independent sources back it, where a practitioner's own project and their own stated experience count as one source.

## Alternatives considered

- **Leave the rule as written and rely on judgement.** Rejected: judgement had already silently diverged from the text in two directions — the build session applied a stricter rule than was written, and this session twice shaped page content around the looser one. A rule that everyone quietly reinterprets is not a rule.
- **Raise the threshold to three evidence lines.** Rejected: it makes gaming more expensive without making it wrong, and it penalises a genuinely well-corroborated pattern for having concise evidence.
- **Count `[own]` experience as automatically independent.** Rejected on the case above: it would have promoted two anti-patterns on one practitioner's word appearing in two formats.

## Consequences

Two pages in this session stayed `candidate` that would otherwise have been promoted, which is the intended effect: the injectable checklist stays conservative, and `candidate` carries real information rather than being a waiting room. Writing evidence also gets easier, because a page can now record everything a source supports without worrying that a second line triggers a status change.

The cost is a judgement call the rule cannot fully mechanise: deciding whether two sources are genuinely independent. The own-project case is settled, but a vendor blog citing a study, and the study, are a harder call. The rule names the clear case and leaves the rest to be argued in the log.

## References

- [`../2026-09-13-50.md`](../2026-09-13-50.md) — the source retrospective.
- [`./AGENTS-MD-026b872bee-own-project-and-own-experience-are-one-source.md`](./AGENTS-MD-026b872bee-own-project-and-own-experience-are-one-source.md) — the per-rule agents-file addition derived from this decision.
- [`./AGENTS-MD-76b21f2973-two-evidence-lines-from-one-source-is-not-corroboration.md`](./AGENTS-MD-76b21f2973-two-evidence-lines-from-one-source-is-not-corroboration.md) — the companion rule.
- `agent-patterns/AGENTS.md` lint step 2, and `agent-patterns/SPEC.md` §8 — the rule as adopted.
- PR #50.
