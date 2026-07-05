# ADR: Analysis evidence packages are session-scratch, not repo artifacts

- **ID**: ADR-cf188b3dd6
- **Status**: Draft (not yet adopted to docs/adr/)
- **Date**: 2026-07-05
- **Source retrospective**: ../2026-07-05-26.md
- **PRs covered**: #26

## Context

The task-01 session produced four per-spec decomposition inventories
(~650 lines of line-cited classification — the evidence substrate behind
artifact-model.md §8's tables) plus mechanical heading maps. PR #26
deliberately shipped only the two files the task's Deliverables section
named; the inventories stayed in session scratchpad and were destroyed with
the container. The decision was made implicitly under "deliverable-only
PRs"; this draft makes it explicit *and reversible*, because the trade-off
is real: the inventories would have let a future session (or a reviewer)
audit every table row without re-running four analysts, at the cost of
~700 repo lines whose accuracy freezes at authoring time.

## Decision

Per-document analysis substrates (inventories, heading maps) produced while building a deliverable stay in session scratchpad; task PRs carry only the files the task's Deliverables section names.

## Alternatives considered

- **Commit evidence under `spec-completeness/evidence/`** — rejected for
  now: it doubles the review surface of every analysis PR, and stale
  evidence (upstream specs can drift) is worse than absent evidence because
  it *looks* authoritative. The deliverable itself carries the line
  citations that matter.
- **Attach evidence to the PR (comment or gist) without committing** —
  rejected: PR comments are a weaker retention surface than either choice
  and rot invisibly.

## Consequences

- Easier: task PRs stay reviewable at deliverable scope; no evidence-file
  maintenance burden; no false authority from frozen substrates.
- Harder: reproducing a table row's justification requires re-reading the
  cited lines (mitigated: every §8 claim carries its citation) or
  re-running an analyst.
- Accepted trade-off: if task-03's checkers want the beyond-audit defect
  corpus as machine-readable input, that specific list gets promoted into a
  deliverable *by task definition* — promotion by decision, not by default.

## References

- [`../2026-07-05-26.md`](../2026-07-05-26.md) — the source retrospective.
- [`./AGENTS-MD-c016bdd53a-deliverable-only-prs.md`](./AGENTS-MD-c016bdd53a-deliverable-only-prs.md) — the companion agents-file rule.
- PRs the decision was made in: #26.
