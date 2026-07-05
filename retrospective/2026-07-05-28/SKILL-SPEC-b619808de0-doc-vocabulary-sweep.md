# Spec: `doc-vocabulary-sweep`

- **ID**: SKILL-SPEC-b619808de0
- **Source retrospective**: ../2026-07-05-28.md

## Intent

Mechanically verify the internal vocabulary of a long multi-section document — named constants, criterion labels, metric names, section cross-references — by grepping every name class and confirming each usage resolves to exactly one definition and each definition is used. Prose re-reading catches vocabulary drift slowly and stochastically; a sweep catches it exhaustively in seconds. In this session the sweep over spec-completeness/process.md verified 7 constants, 40 criterion labels, and 24 metric names in one pass, and its section-reference leg exposed two references to a nonexistent "§0".

## Trigger

- After authoring, or multi-section editing, any document that defines named vocabulary: constants, labeled criteria, metric names, statuses, element IDs.
- As the exit gate of a post-edit-reread-pass loop (the sweep is the mechanical half; the re-read is the semantic half).
- Direct: "check the doc's consistency", "vocabulary sweep", "do the names all resolve?".
- Negative triggers: short documents; documents with no defined name classes (nothing to sweep).

## Inputs

- The document path.
- The list of name classes with each class's single canonical definition site (e.g. constants → §9.1 table; metrics → §9.2 table; criterion labels → stage cards).

## Outputs

- An inline pass/fail sweep report: per-class table of defined / used / unresolved names. No file modifications — findings route back to the editing loop.

## Workflow

1. Identify the name classes by scanning for definition tables and enum blocks.
2. For each class, build the canonical name list from its definition site. If a class turns out to have more than one definition site, stop — that is already a finding (see the one-table-per-name-class rule).
3. Grep each name across the document and record its count. Flag: count == 1 (defined but never used — drift waiting to happen) and usages matching no definition (a defect).
4. Sweep cross-references: extract every reference token (`grep -oE '§[0-9A-Z.]+'`, plus structured labels like `S[0-9]-[EX][0-9]` and appendix refs like `A.6`) and verify each target exists as a heading or definition.
5. Report a table — class, defined, used, unresolved — and declare pass only at zero unresolved.

## Concrete examples

### Example 1: process.md (this session)

A shell loop `for c in D_dry M_abort I_S3max k_iter k_freeze R_freeze R_S7max; do grep -c "$c" process.md; done` proved all 7 constants defined-and-used; `grep -oE "S[0-9]-[EX][0-9]" | sort | uniq -c` resolved all 40 criterion labels to their stage-card definitions; 24 metric names each appeared ≥2 times (definition + use). The section-reference leg surfaced `§0` twice — a citation of the document's unnumbered intro — fixed by referring to the target in words.

### Example 2: status enums

For a document defining `Enum{OPEN, TRIAGED, PROPOSED, PENDING-OWNER, ANSWERED, APPLIED, CLOSED, REJECTED, SPLIT}`: grep each value. A value appearing only inside the enum (never in a lifecycle or rule) flags a dead status; a status used in a rule but absent from the enum flags an incomplete enum. This is how process.md's APPLIED gap was confirmed: the S6 hygiene rule enumerated open statuses, and the sweep showed APPLIED belonged to neither the open set nor the terminal set.

## Anti-patterns

- **Sweeping before the vocabulary is tabled.** Names scattered through prose make the canonical list unbuildable; fix the document's structure first.
- **Treating count == 1 as fine.** Defined-but-unused names are the seed of the next drift.
- **Fixing semantics during the sweep.** The sweep detects; the editing loop fixes — the same detection/fix separation process.md's S6 lint imposes via its reclassification rule.

## Acceptance criteria

- [ ] Every name class has exactly one definition site.
- [ ] Every usage resolves to a definition; every defined name is used or its non-use justified.
- [ ] Every section/label cross-reference resolves to an existing target.
- [ ] The sweep output is a table a commit message can cite verbatim.

## Files this skill creates / modifies

- None (read-only; findings go to the editing loop).
