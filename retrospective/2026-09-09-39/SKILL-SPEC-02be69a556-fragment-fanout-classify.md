# Spec: `fragment-fanout-classify`

- **ID**: SKILL-SPEC-02be69a556
- **Source retrospective**: ../2026-09-09-39.md

## Intent

Classify or triage a large corpus of small items (dozens to hundreds of files) by fanning out parallel subagents that each process a batch of 10–15 items and write rows to a per-batch fragment file, which the orchestrator merges into the canonical table afterward. This avoids two failure modes observed while triaging 234 cached sources for the agent-patterns wiki: per-item subagent invocations whose overhead dwarfs the work, and parallel agents appending to one shared file and clobbering each other's writes.

## Trigger

- Direct: "triage these files with subagents", "classify everything in this directory", "rate each of these against <criteria>".
- Proactive: any task requiring the same small judgment (a rating, a category, a one-line summary) applied independently to ≥ 30 files, where the orchestrator only needs the merged table, not the per-item reasoning.
- Negative: fewer than ~15 items (do it inline); items requiring deep multi-file reasoning each (use one focused subagent per item instead); outputs that are whole documents rather than table rows (use a plan-file writing fan-out instead — see `planned-evidence-synthesis`).

## Inputs

- A directory (or explicit list) of item files to classify.
- The classification contract: rating scale, per-row column schema, and the use-case framing the rater must judge against.
- A batch size (default 12; range 10–15) and a parallelism cap (default 8 concurrent subagents).
- A scratch/fragment directory that is gitignored (e.g. `.cache/triage/`).

## Outputs

- One merged canonical table file (e.g. `sources/_triage.md`) with exactly one row per input item.
- Per-batch fragment files left in the fragment directory for audit.
- An inline summary: item count, rows merged, per-rating distribution.

## Workflow

1. `ls` the corpus into a sorted list file; `split -l <batch-size> -d` it into batch list files in the scratchpad.
2. Write (or reuse) one prompt template containing: the classification contract, the exact one-row output format, the id-derivation rule for items, the fragment file path for the batch, and a fixed return contract ("return ONLY batch name + counts per rating"). Keep the per-batch prompt identical except for the batch id.
3. Dispatch subagents in waves no larger than the parallelism cap, each pointed at its batch list and its own fragment file. Use a cheap model — the whole point of batched triage is that each item needs a skim, not analysis.
4. As each completion notification arrives, record its counts; do not read fragments yet.
5. After the last batch: merge fragments into the canonical table with a shell loop that strips per-fragment headers/separator rows, then verify (a) row count == item count, (b) every row has the full column count (`awk -F'|' '{print NF}' | sort | uniq -c`).
6. Report the distribution and any malformed rows; fix malformed rows by re-reading only the affected fragment.

## Concrete examples

### Example 1: 148 newsletter emails (agent-patterns Phase 2)

Input: `.cache/every/` with 148 files named `YYYY-MM-DD-<slug>.txt`. `split -l 15` produced `ebatch-00`…`ebatch-09`. Each Sonnet subagent got the wiki's use-case framing ("single-human/single-agent interactive development; marketing emails get relevance none"), the row format `| <id> | <date> | <title> | <relevance> | <scope> | no | <takeaway> |`, an id rule (`every-<yyyy-mm-dd>-<short-slug>`), and its fragment path `.cache/triage/ebatch-NN.md`. Returns were one line each, e.g. `ebatch-00: 15 items — high 1, medium 1, low 3, none 10`, keeping the orchestrator's context flat.

### Example 2: 86 fetched web pages (same session)

Input: `.cache/web/*.txt`, each with a `SOURCE-URL:` first line. Same template, two changes only: id = filename minus `.txt`, plus a note that `willison-aep-*` files are chapters of one guide but triage individually. Merge step: `for f in .cache/triage/*.md; do grep -h '^|' "$f" | grep -v '^\s*|\s*-\+' | grep -viE '^\|\s*id\s*\|'; done >> sources/_triage.md`, then the NF check confirmed 236 lines = 234 rows + 2 header rows, all with 9 fields.

## Anti-patterns

- **Shared append target.** The original subagent design appended to `sources/_triage.md` directly; running 16 of them concurrently against one file would interleave or clobber rows. Fragments exist precisely to make concurrency safe.
- **One item per invocation.** 234 dispatches for 234 items pays prompt+notification overhead 234 times to skim files that are often two paragraphs long.
- **Fat returns.** Letting raters return their takeaway bullets inline floods the orchestrator; the takeaways belong in the fragment rows, the return is counts only.
- **Merging without validation.** A fragment with a stray header row or a 7-field row silently corrupts the table; the row-count and field-count checks are two commands.

## Acceptance criteria

- [ ] Merged table has exactly one row per input item, verified by count.
- [ ] Every row parses to the same field count.
- [ ] No two subagents were ever pointed at the same output file.
- [ ] Orchestrator context received only batch-level summaries, never per-item content.
- [ ] Fragment files remain available for audit until the merge is verified.

## Files this skill creates / modifies

- `<fragment-dir>/<batch>.md` — one fragment per batch (scratch, gitignored).
- `<canonical-table>.md` — the merged classification table (committed).
- `<scratchpad>/<batch-list files>` — item lists per batch (scratch).
