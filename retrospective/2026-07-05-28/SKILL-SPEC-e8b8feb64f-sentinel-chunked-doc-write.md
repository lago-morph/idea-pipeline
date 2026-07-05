# Spec: `sentinel-chunked-doc-write`

- **ID**: SKILL-SPEC-e8b8feb64f
- **Source retrospective**: ../2026-07-05-28.md

## Intent

Author very long documents (roughly 800+ lines) reliably by writing them as a bounded chain of tool calls: one initial Write ending in a sentinel comment, then successive Edits that replace the sentinel with the next chunk, each chunk ending in the sentinel again except the last. This session produced the 1,508-line spec-completeness/process.md in three such chunks with zero truncation and zero tail re-reads; a single giant Write risks output-length truncation mid-table, and ad-hoc appends without a sentinel require re-reading the file tail to find an anchor.

## Trigger

- About to author a document expected to exceed ~800 lines or ~25 KB in one sitting (a spec, a process document, a long report).
- Proactively: whenever the planned content of a single Write approaches the size where truncation becomes plausible.
- Negative triggers: files under a few hundred lines (one Write suffices); incremental edits to existing documents (plain Edit at a known anchor); code files (different QA loop).

## Inputs

- Target file path.
- The complete section outline, decided **before** chunk 1 is written.
- A chunk plan: 2–5 chunks, split only at top-level section boundaries.

## Outputs

- The complete document on disk, with no sentinel remaining.

## Workflow

1. Fix the full section outline first; choose chunk boundaries only at top-level section breaks (never mid-section, never mid-table).
2. Write chunk 1 with the Write tool, ending the content with the sentinel line `<!--CONT-->` — an HTML comment: unique, greppable, and invisible if a mistake ever ships it.
3. For each subsequent chunk: Edit with `old_string` exactly `<!--CONT-->` and `new_string` = the next chunk's text, ending again with `<!--CONT-->` — except the final chunk, which ends with the document's real last line.
4. After the final chunk, run `grep -n 'CONT' <file>` and confirm zero sentinel hits survive.
5. Run a full re-read pass (the post-edit-reread-pass skill). Chunked authoring makes cross-chunk drift the dominant defect class, so the re-read is part of this skill, not optional follow-up.

## Concrete examples

### Example 1: process.md (this session)

`spec-completeness/process.md`, 1,508 final lines, three chunks: Write (title through §4 Data structures, ending `<!--CONT-->`) → Edit (sentinel → §5–§6 stage cards, ending `<!--CONT-->`) → Edit (sentinel → §7 through Appendix A, no sentinel). Zero truncation, zero tail Reads between chunks; the re-read pass that followed found cross-chunk drift (a principle in chunk 1 pointing at the wrong stage card in chunk 2), which is exactly the defect class step 5 exists to catch.

### Example 2: the failure mode it prevents

The same document attempted as one ~60 KB Write risks the call being cut mid-table. Recovery then requires Reading the tail, locating the truncation point inside malformed markdown, and re-sending the remainder — three extra calls and a corruption risk, versus zero with the sentinel chain.

## Anti-patterns

- **Splitting mid-section or mid-table.** Section-boundary splits keep every intermediate file state well-formed markdown; a mid-table split leaves a broken table on disk between calls, which confuses any linter or reader that runs in between.
- **A prose sentinel** ("TO BE CONTINUED"). Non-unique and visible if forgotten; the HTML comment is invisible in rendering, which is also why step 4's grep — not a visual check — is the required verification.
- **Skipping the final sentinel grep.** A forgotten `<!--CONT-->` ships silently precisely because HTML comments do not render.
- **Re-Writing the whole file to append.** Write overwrites; it wastes the whole prior transfer and clobbers any fix applied to earlier chunks in between.

## Acceptance criteria

- [ ] Final file contains zero sentinel occurrences (grep-verified).
- [ ] Every chunk boundary coincided with a top-level section boundary.
- [ ] No Read of the file tail was needed between chunks.
- [ ] A full re-read pass ran after the final chunk.

## Files this skill creates / modifies

- The target document only.
