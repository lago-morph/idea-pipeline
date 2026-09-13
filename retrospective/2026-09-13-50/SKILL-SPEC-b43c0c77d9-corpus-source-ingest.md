# Spec: `corpus-source-ingest`

- **ID**: SKILL-SPEC-b43c0c77d9
- **Source retrospective**: ../2026-09-13-50.md

## Intent

Ingest a large, multi-file source into a curated corpus without letting the raw material, or the readers' disagreements, leak into the result. This session ingested ~40,000 words across seventeen files of someone's own project into a wiki that allows one note per source. Three parallel readers returned findings only; the single coherent note was composed centrally. Done naively — each reader writing its own note, or the orchestrator reading everything itself — the result is either three incompatible notes or an orchestrator whose context is full of raw material it will never need again.

## Trigger

**Direct**: "ingest this source", "add these files to the corpus", "pull in <repo/directory> as a source", "process this according to the ingest protocol".

**Proactive**: offer when the user points at more than ~10,000 words of material that must become a single curated artifact, especially when the corpus has a one-note-per-source rule.

**Negative**: do not use for a single short document — read it directly. Do not use when each input file is meant to become its own separate corpus entry; that is a different (simpler) fan-out.

## Inputs

- The source location (a repo to clone, a directory, a set of paths). If a repo, clone it **outside the working tree** so raw material can never be committed.
- An explicit file list, and an explicit exclusion list. The user may name files that are *not* in scope; honour that exactly.
- The corpus's schema and guardrails (in this repo: `agent-patterns/AGENTS.md` §2 and §4).
- The corpus's existing vocabulary — the list of entries readers should map findings onto rather than inventing names.

## Outputs

- One source note in the corpus, composed by the orchestrator.
- Evidence lines added to existing corpus entries.
- A triage row and a bibliography row.
- A log entry recording what was ingested, what was excluded and why.
- Nothing from the raw material committed anywhere.

## Workflow

1. Place the raw material outside the repository (`/tmp`, or a gitignored cache). Verify with `git status` that nothing from it is stageable.
2. Measure the corpus: `wc -w` every in-scope file. Use the word counts to cut slices of roughly equal size.
3. Slice by **document role**, not just by size — the analysis layer, the raw evidence layer, and any first-person record are different kinds of material and warrant different instructions.
4. Write one brief per slice. Every brief must contain: the corpus's guardrails; the file list for that slice **and the exclusion list**; the existing vocabulary, with an instruction to reuse it and to flag any new name explicitly; the instruction to **return findings only and write no files**; and a requirement to separate findings that belong to a different use case.
5. Add to each brief the three questions that produce the most value: *what does this contradict?*, *what does the existing note get wrong?*, and *what cuts against the position I just told you?* Say explicitly: do not soften it in either direction.
6. Where a brief asserts something about the source, instruct the reader to verify that assertion against the source and correct you if it is wrong.
7. Dispatch the readers in parallel, in the background.
8. Compose the note yourself from the returned findings. Do not concatenate the readers' output.
9. Reconcile naming collisions before writing: readers working in parallel will propose the same idea under different names. Merge them into one entry.
10. Read back everything the readers wrote, and everything you wrote, against the corpus's format rules before committing.

## Concrete examples

**Example 1 — the session's own run.** Source: `lago-morph/k8s-platform`, cloned to `/tmp/k8s-platform`. In scope: `ai/LESSONS.md`, all of `forensics/`, and one transcript. Slices: (a) `LESSONS.md` alone, ~4,800 words; (b) the nine forensics analysis documents, ~8,200 words; (c) the six raw evidence files, ~18,000 words. Each brief carried the wiki's paraphrase-only rule and the instruction to flag long-running and multi-agent material separately. All three returned structured findings; the orchestrator wrote one 150-word summary and thirteen evidence bullets. Three readers independently proposed the same new idea as `hand-fixed-validation`, `fix-source-not-environment` and `verify-from-clean-state`; it shipped as one page.

**Example 2 — mid-flight scope change.** The user said one named file was incomplete and must be dropped. The correct response is to message the affected reader with a scope change that says: discard everything drawn from that file, keep a finding only if the remaining files support it alone, and re-word it to cite only what they say. In this session the readers had already been stopped by an interrupt, so all three were relaunched with the exclusion written into the brief instead — which is the more reliable path whenever the readers are early.

## Anti-patterns

- **Letting readers write corpus files.** Three readers writing three notes produces three voices and three overlapping claims. They return findings; you compose.
- **Cloning into the working tree.** The corpus in this session forbids committing source text. A clone inside the repo makes that one `git add -A` away from happening.
- **Naming the file instead of quoting the text.** A reader asked to "check `patterns/foo.md`" reviews the page. A reader given the exact line, quoted, returns a verdict on that line.
- **Asking for confirmation.** "Does this source support X?" returns yes. "What does this source contradict, and what does the existing note get wrong?" returns the three corrections that actually mattered in this session.
- **Trusting the brief over the source.** One brief in this session told a reader to treat part of its file as low-fidelity. The reader read the file, found a note superseding that caveat, and corrected the brief. That only happened because it was told it could.
- **Skipping the naming reconciliation.** Merge collisions before writing, not after — a published entry is harder to rename than a draft.

## Acceptance criteria

1. `git status` shows nothing from the raw material at every point in the run.
2. The corpus gains exactly one note per source, in the orchestrator's voice.
3. Every new claim in the note traces to a reader finding, and every reader finding that was dropped is recorded as dropped, with a reason.
4. Names proposed by more than one reader for the same idea are merged before anything is committed.
5. The exclusion list is honoured, and the note states what was excluded and why.

## Files this skill creates / modifies

- `sources/<bib-id>.md` — the composed source note.
- `patterns/*.md` — evidence lines on existing entries.
- `sources/_triage.md`, `bibliography.md` — one row each.
- `log.md` — what was ingested, excluded, and dropped.
