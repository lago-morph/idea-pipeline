# agent instruction

**Ratify batch amendments as separable hunks.** "When a one-line instruction ratifies a batch of semantic changes ('do the refactor'), keep each change a separable hunk (one bullet plus its dependent table row), name the per-item veto path in the PR body, and record the authority interpretation in the task's resolution log — batch approval must stay reversible per item."

*Grounded in: applying checklist amendments A-2…A-7 in PR #31 under the owner's blanket instruction.*

# justification

Task-04 had marked six checklist amendments as owner decisions; the owner's actual instruction was the single sentence "do the task-04-refactor." Applying all six as separable hunks — each one §3 bullet plus its matching coverage-table row — and saying so in the PR body kept the veto price at one bullet per item, honoring the repo's own per-item ratification semantics (process.md §2.1). Both alternative interpretations fail: blocking to ask six questions stalls an explicit instruction, and applying the changes entangled makes any later veto a manual unpick across files.
