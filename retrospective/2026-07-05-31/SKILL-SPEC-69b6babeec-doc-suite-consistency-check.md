# Spec: `doc-suite-consistency-check`

- **ID**: SKILL-SPEC-69b6babeec
- **Source retrospective**: ../2026-07-05-31.md

## Intent

Cross-document consistency verification for documentation suites that state the same facts in more than one place — coverage tables vs. per-item fields, execution maps vs. definition blocks, printed counts vs. actual counts, status phrases vs. actual status. The skill scripts the checks (bidirectional set-diff over parsed tables and fields, recomputation of every self-describing statistic, obsolete-phrase sweep) and reports drift with file:line evidence instead of trusting a visual re-read. Born from PRs #30/#31 of the spec-completeness work, where the scripted pass found seven real defects that authoring-time care and a full human re-read had missed.

## Trigger

- Direct: "check the docs for drift", "verify the coverage table", "are these documents consistent?", "run a consistency check before I commit".
- Proactive: after any multi-section edit to a document suite that maintains a mapping in two places (a summary table plus per-entry fields); after any refactor that changes an item count or a document's status; before committing a deliverable whose acceptance criteria include a totality property ("every X maps to ≥1 Y").
- Negative: single-file, single-section edits; documents with no duplicated facts (nothing to cross-check); source code (linters own that).

## Inputs

- The paths of the documents forming the suite, and which pairs of locations duplicate a fact (e.g. `hardening/README.md` §8 table ↔ `hardening/checks.md` `**Hardens:**` fields).
- The expected item universe if one exists (e.g. "sections A–J with 5,7,4,3,4,5,4,3,6,5 items").
- Optionally, a list of status phrases the latest change obsoletes.

## Outputs

- A drift report printed inline: per finding, the file, the line or key, and the direction of the mismatch (present-in-A-only / present-in-B-only / count-mismatch / stale-phrase).
- Exit disposition: CLEAN or a finding list. No file modifications — this skill reports; the author fixes.

## Workflow

1. Parse side A (the table): extract per-row key → referenced-ID set with a regex tolerant of bold markers (`\b((?:D|DL|L|M|H)-\d\d)\b` was the session's shape). Skip separator rows.
2. Parse side B (the per-entry fields): split the document on entry headers (`^### CHECK `), extract the field line (`\*\*Hardens:\*\* …`), collect the item IDs.
3. Compute both directions: for every entry, the set of table rows listing it must equal the set of items its field names; report each asymmetry as `{entry, field-only: [...], table-only: [...]}`.
4. Verify the item universe: the table's key set must equal the expected enumeration exactly; report missing/unexpected keys.
5. Recompute every self-describing statistic the suite states ("N distinct checks", "46 items", "all five tiers"): grep the claims, compute the true values from the parsed data, diff.
6. Run the obsolete-phrase sweep: grep the whole suite for the supplied stale phrases plus the standing set (`until X merges`, `when they land`, `will execute`, `TBD`, `unnumbered`); report hits outside intentionally-historical files (task queues quoting old text).
7. Print the report. If CLEAN, say so explicitly with the counts verified (items, entries, statistics checked).

## Concrete examples

### Example 1: the PR #30 coverage check

Input: `hardening/README.md` (44-row coverage table), `hardening/checks.md` (49 `### CHECK` blocks). Step 3 output:

```
D-03: Hardens-only=['F.3'] table-only=[]
D-20: Hardens-only=['H.1'] table-only=[]
L-03: Hardens-only=['I.5'] table-only=[]
L-05: Hardens-only=['A.3'] table-only=[]
```

Four real asymmetries — each fixed by adding the check ID to the named table row. Re-run: `residual drift: NONE`, `items missing from table: []`, `checks not in coverage table: []`.

### Example 2: the PR #31 statistic and staleness pass

Step 5 caught `checks.md` §R claiming "exercise 17 distinct checks across all five tiers"; recomputation over the RD table's ID references gave 24 distinct checks and only three tiers represented — the sentence was rewritten to the computed values. Step 6, run with the phrases the refactor obsoleted, returned two hits: `hardening/README.md:437 "The bullets are unnumbered"` (they had just been numbered) and `README.md "will execute"` — both fixed before commit; the remaining hits were inside `tasks/task-04-refactor.md`, correctly skipped as intentional historical quotes.

## Anti-patterns

- **Trusting the full re-read.** The session's human-grade re-read of 1,277 fresh lines missed all four table asymmetries; the script found them in one run. Re-reads catch prose problems, not set-membership problems.
- **Checking one direction only.** "Every item has a check" passed while "every check maps to an item" would have failed; both directions are the property.
- **Flagging historical quotes as stale.** `task-04-refactor.md` deliberately quotes the obsolete phrases it replaced; the sweep must whitelist queue/log files or every reconciliation record becomes a permanent false positive.
- **Fixing silently inside the checker.** The session kept report-then-fix as separate steps; a checker that edits can mask a systematic authoring error you needed to see.

## Acceptance criteria

- [ ] Reports all four seeded asymmetries when run against the pre-fix state of PR #30's two files, and CLEAN against the merged state.
- [ ] Detects a count mismatch when a stated statistic is off by one.
- [ ] Both directions of every mapping are checked and reported distinctly.
- [ ] Zero false positives on intentionally-historical files when the whitelist is supplied.
- [ ] Runs in one tool call and needs no state between runs.

## Files this skill creates / modifies

- None (report-only). Optionally `scratchpad/consistency-report.txt` when the user asks for a saved copy.
