# Spec: `refactor-queue-execute`

- **ID**: SKILL-SPEC-b047218881
- **Source retrospective**: ../2026-07-05-31.md

## Intent

Execute a recorded cross-document reconciliation queue (the "task-04 pattern"): take a task file whose items each name an exact edit site and proposed change, apply or explicitly reject every item, keep semantic changes as separable hunks, synchronize every dependent artifact (coverage tables, per-item fields, counts, link targets), append a per-item resolution log to the task file, and ship the whole queue as one reviewed PR. Born from spec-completeness/tasks/task-04-refactor.md, which was recorded during task-03 under a don't-modify constraint and executed to completion the same day on the owner's one-line instruction.

## Trigger

- Direct: "do the task-NN refactor", "execute the reconciliation queue", "apply the recorded cleanup".
- Proactive: offer when a deliverable merges whose companion documents carry supersession notes or placeholder pointers naming it ("when X merges, …"), and a queue file for them exists.
- Negative: no queue file exists (that is recording, not executing — a different activity); the queue items are vague themes without edit sites (send it back for sharpening first).

## Inputs

- The queue file path (e.g. `spec-completeness/tasks/task-04-refactor.md`) with numbered items, each naming file + section + proposed edit.
- The current branch (restart it from the default branch first if its PR merged).
- The authority context: which items the queue marks as owner decisions, and what instruction ratified the run.

## Outputs

- Edits across the named documents, one separable hunk per queue item.
- The queue file updated: `Status:` flipped to done with date, a `## Resolution log` section with a per-item disposition (Applied/Rejected + one line), acceptance boxes checked only if actually verified.
- One commit + push + PR whose body lists per-item dispositions and names the per-item veto path for anything applied under blanket ratification.

## Workflow

1. Read the queue file end to end; list the items and their edit sites. Restart the working branch from the default branch if the previous PR merged (`git fetch origin main && git checkout -B <branch> origin/main`), then re-Read every file you will edit — resets void earlier reads.
2. For each item in queue order: Grep the exact current text at the edit site (never reconstruct from memory), apply the edit, and immediately apply its dependent ripples (table rows, counts, `Hardens:`-style fields, link targets) named by the item.
3. For items marked owner-decision under a blanket instruction: apply each as a separable hunk and note the interpretation ("instruction taken as the ratification batch; per-item veto = revert one bullet + its table row").
4. Reject an item only with a one-line reason recorded in the resolution log — never silently skip.
5. Run the suite's consistency verification (see `doc-suite-consistency-check`): mapping totality both directions, recomputed statistics, obsolete-phrase sweep seeded with the phrases this refactor retires.
6. Update the queue file: status line, resolution log, acceptance checkboxes.
7. Commit with a body summarizing per-file changes; push; open the PR with per-item dispositions and the veto note.

## Concrete examples

### Example 1: the supersession trim (task-04 item 1)

Item text named the edit site: "process.md §4.7 … templates supersede … keep dispatch rationale + ingestion." Execution: replaced the three probe templates with pointers (`P-ASSUME = check L-04, P-QCOUNT = check L-01, P-IMPL = check L-07`), kept the R-FR slice rationale and module-selection rule (a downstream check cites it), kept the BUILDER charter (not superseded) — and fixed its now-dangling "same invention log as above" to "as the implementation probe", recording that wording fix in the resolution log since it touched pinned template text.

### Example 2: the ratified amendment with ripples (task-04 item 4)

"Add C.4 (glossary term closure)" rippled across three files: the new §3 bullet in `README.md`, a new coverage-table row `| C.4 | … | **D-09** | D+L |` in `hardening/README.md`, and `D-09`'s `Hardens:` field in `hardening/checks.md`. All three landed in one hunk-cluster; the verification script then confirmed 46/46 items bidirectionally total. A missed ripple here is exactly what step 5 exists to catch.

## Anti-patterns

- **Executing from memory of the analysis.** The queue file is the contract; the session that wrote it knew things this session doesn't. Re-derive nothing; follow the edit sites.
- **Batch-editing without separability.** Entangled amendments make a later per-item veto a manual unpick — the session kept each §3 amendment one bullet + one row for exactly this reason.
- **Marking acceptance boxes aspirationally.** The session checked them only after the verification script returned zero drift; a checked box is a claim.
- **Leaving the queue file untouched.** Without the resolution log, the queue looks perpetually pending and the dispositions live only in a PR body.

## Acceptance criteria

- [ ] Every queue item has a resolution-log entry: Applied (with edit) or Rejected (with reason).
- [ ] Suite-level consistency verification runs clean after the edits (mappings total, statistics recomputed, staleness sweep clean outside historical quotes).
- [ ] Each owner-decision item is a separately revertible hunk, and the PR body says so.
- [ ] The queue file's status line and checkboxes reflect the actual end state.

## Files this skill creates / modifies

- The documents named by the queue items — the reconciliation edits themselves.
- The queue file (e.g. `tasks/task-NN-*.md`) — status, resolution log, checkboxes.
- No new files besides the PR.
