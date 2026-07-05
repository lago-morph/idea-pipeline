# agent instruction

**Sweep for the phrases your change obsoletes.** "After a refactor that changes a document's status (merging a deliverable, superseding a section, renumbering items), grep the whole doc suite for the now-false phrases — 'until X merges', 'when they land', 'are unnumbered', 'will execute' — and fix or justify every hit before committing."

*Grounded in: the PR #31 staleness sweep catching two leftovers after the deliberate edits were done.*

# justification

PR #31's whole point was retiring "when task-03 merges"-style placeholders, and the deliberate edits still left two behind: a hardening-appendix entry asserting §3's bullets "are unnumbered" (they had just been numbered by that very PR) and a "will execute" tense in the README companion paragraph. A single grep over six phrases found both in seconds. Stale status phrases are worse than typos: they make a reader distrust the cross-references exactly where the document suite's authority lives, and they multiply — every future reader must re-derive which of the two contradictory statements is current.
