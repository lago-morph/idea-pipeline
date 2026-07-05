# Task 04 — Post-Task-03 Refactor: Reconcile the Four Documents

**Status:** done (executed 2026-07-05, immediately after task-03's merge — see the
resolution log below) · **Depends on:** task-03 (hardening/) merged · **Feeds:**
process v2, README §3 v2

## Why this task exists

Task-03 was executed under a constraint: finish the hardening deliverables **without
modifying** the task-01 and task-02 deliverables (`artifact-model.md`, `process.md`).
Nothing found was blocking — every tension was resolvable inside `hardening/`'s own
scope — but the work surfaced a queue of cross-document inconsistencies and
now-stale placeholders that should be reconciled in one deliberate pass rather than
drift. This file is that queue, recorded as they were found. Items are ordered by
value; each names the exact edit site.

## Context to load before starting

1. `spec-completeness/hardening/README.md` — especially §3.1 (item numbering), §5
   (Tier-L rules), §6 (constants), and the appendix (suggested §3 amendments A-1…A-7).
2. `spec-completeness/process.md` — §4.7 (probe charters), §9.1–9.2 (constants,
   metrics), S5-X2, S6 activity 4, and the preamble's "until hardening/ merges" clause.
3. `spec-completeness/README.md` §3 and §4.3.
4. `spec-completeness/artifact-model.md` §5 (tag grammar).

## The refactor queue

1. **Trim process.md §4.7 to ingestion/routing (its own supersession note, now
   triggered).** §4.7 says: "when task-03's hardened probe definitions merge, its
   templates supersede these and this document keeps only the ingestion/routing
   rules." Hardening's L-01/L-04/L-07 are those v2 charters (prompt text kept
   verbatim). Edit §4.7 to keep charter identity, context-slice rules, module-selection
   rule, and ingestion rules, and point at `hardening/checks.md` §3 for templates,
   schemas, k, and aggregation. Same pass: the preamble's "Until `hardening/` merges,
   the manual procedures written into the stage cards apply" sentence is now stale.

2. **Replace the process's other placeholder pointers with check IDs.** S6 activity 4:
   "the deterministic suite; task-03's Tier-D checks when merged, these greps until
   then" → cite the S6 row of hardening README §7 (D-07, D-09, D-12, D-14, D-21,
   D-28, D-29 + the compiled-spec re-run rule). S5-X2's "(AUTHOR-judged in v1,
   hardened by task-03's checks when they land)" → cite L-05 (+ D-23 screen).

3. **Add stable item IDs to README §3.** Hardening pins A.1–J.5 positionally
   (README §3.1 + the §8 coverage table); printing the IDs in §3 itself makes the
   mapping robust to future edits. This is hardening appendix amendment **A-1**.

4. **Triage the remaining §3 amendments (A-2…A-7).** Owner decision per item:
   new glossary item (A-2), split I.3 (A-3), scope J.4 to its decidable core (A-4),
   de-hedge F.4 (A-5), make I.5 measurable (A-6), make G.4 reader-relative (A-7).
   Each accepted amendment also updates the hardening coverage table row.

5. **State the finding-vs-verdict replication rule in one place.** process.md
   justifies k = 1 probe per loop iteration (sequential replication via `D_dry`,
   §9.1); hardening codifies `k_L = 3` parallel for standalone runs and majority-only
   for verdict probes (hardening §5.5). Both are consistent, but the
   finding-probe/verdict-probe distinction that reconciles them currently lives only
   in hardening. Add one paragraph to process §9.1 (or §4.7) naming the rule, so the
   next process version can't accidentally run a verdict probe at k = 1.

6. **Unify the hedge lexicon.** Three lists exist: README §3.J.5's examples,
   process S6/T7's list "and kin," artifact-model T7's list. Hardening D-12 pins
   HW-LEX v1 as canonical. Point the other three at it (or at least at its name) so
   lexicon growth happens in one versioned place. Same for D-23's JW-LEX.

7. **Absorb hardening's new metric names into process §9.2 (or declare the table
   extensible).** Hardening reuses §9.2 names verbatim where they exist but adds
   metrics the process doesn't know (`divergence_rate`, `trace_match`, `kill_rate`,
   `witness_coverage`, `concurrency_closure`, …). Either §9.2 grows rows at process
   v2, or it gains one sentence delegating check-metric definitions to
   `hardening/checks.md` — the current split invites double-definition drift.

8. **Minor: artifact-model §5 regex headroom.** The tag grammar hard-codes
   `[A-Z]-[A-Z]{2}-[0-9]{3}`. Fine today; note that element counts past 999 or any
   future artifact whose ID isn't `X-YY`-shaped will need a widened pattern in
   lockstep across artifact-model §5, hardening D-09, and any FT-1 tooling.

9. **Minor: README §4.3 staleness.** The "spec linter: section J is mechanizable
   today" bullet predates hardening; it could cite D-06…D-12 rather than describing
   them hypothetically. (The §-level cross-reference paragraph was already added by
   task-03; this is just the stale bullet.)

## Resolution log (2026-07-05)

All nine queue items **applied**; none rejected. Dispositions:

1. **Applied.** process §4.7 now carries only dispatch rationale + ingestion per
   charter; templates, slices, schemas, k, and aggregation point at hardening
   L-04/L-01/L-07. The BUILDER charter stays process-owned; its template's "same
   invention log as above" became "as the implementation probe" (the P-IMPL template
   it pointed at no longer precedes it — meaning unchanged). Stale preamble sentence
   replaced; `hardening/` added to the header companions line.
2. **Applied.** S6 lint bullets annotated with their check IDs (D-16, D-06…D-09,
   D-12, D-09, D-29; question hygiene marked process-owned — a queue query, not a
   text check); S5-X2 cites L-05 with the D-23 screen.
3. **Applied** (amendment A-1). IDs `A.1`…`J.5` printed in README §3.
4. **Applied, all six** (A-2…A-7). New C.4 (→ check D-09) and I.6 (split from I.3,
   → D-28); J.4, F.4, I.5, G.4 reworded as proposed. Hardening coverage table and the
   two Hardens fields updated; the item count is now 46. Note on authority: the six
   semantic amendments were owner decisions per this file — the owner's instruction
   to execute this task was taken as the ratification batch, and each lands as a
   separable hunk in the PR so per-item veto stays cheap.
5. **Applied.** Finding-vs-verdict replication paragraph added to §4.7's intro.
6. **Applied.** README §3.J.5, process S6 lint, and artifact-model T7 all name
   HW-LEX v1 (hardening check D-12) as the canonical lexicon.
7. **Applied** as the delegation option: one paragraph after the process §9.2 table —
   check-level metrics are defined in their check blocks; shared names keep §9.2's
   formulas authoritative.
8. **Applied.** Headroom note added at artifact-model §5's grep surface.
9. **Applied.** README §4.3's spec-linter bullet cites D-06…D-12 and the §R
   regression suite.

## Task acceptance checklist

- [x] Every queue item either applied (with the edit) or explicitly rejected (with a
      one-line reason recorded in this file)
- [x] No duplicated normative text remains between process.md §4.7 and
      hardening/checks.md §3 (templates live in exactly one place)
- [x] README §3, process.md, artifact-model.md, and hardening/ all grep-consistent on:
      item IDs, check IDs, metric names, HW-LEX/JW-LEX references
- [x] Docs re-read once end-to-end for cross-references after the edits

## Out of scope

- Any change to check procedures or thresholds (that is suite evolution, governed by
  hardening's ladder-audit and regression rules, not this refactor)
- Implementing tooling (hardening README §10's FT-1…FT-6 own that)

## Working notes

Recorded by the task-03 session (2026-07-05) per the owner's instruction to track
non-blocking inconsistencies rather than edit merged deliverables. Commit to a fresh
branch, PR referencing issue #22. Most items touch process.md, which is a task-02
deliverable — that is the point of doing this as its own reviewed pass.
