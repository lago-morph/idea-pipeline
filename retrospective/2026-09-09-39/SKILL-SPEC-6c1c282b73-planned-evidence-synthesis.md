# Spec: `planned-evidence-synthesis`

- **ID**: SKILL-SPEC-6c1c282b73
- **Source retrospective**: ../2026-09-09-39.md

## Intent

Turn a pile of distilled source notes into a set of uniform, evidence-linked wiki pages by first writing one authoritative plan file — one line per page carrying slug, title, type, category, status, durability, confidence, sources, and related links — and then producing pages from that plan under an evidence-discipline contract: read every cited source note before writing, cite only what the note supports, and drop or narrow unsupported citations rather than keeping them. In the agent-patterns Phase 4 build this produced 36 pattern pages that passed a link-and-frontmatter lint on the first try.

## Trigger

- Direct: "synthesize the patterns from the source notes", "write the pages from the plan", "cluster the candidates into pages".
- Proactive: whenever ≥ 10 documents must be written that (a) share a strict frontmatter schema, (b) cross-reference each other, and (c) must cite a corpus of notes truthfully.
- Negative: one-off documents (write directly); pages whose sources have not been distilled into notes yet (distill first — writing from raw material skips the traceability layer).

## Inputs

- A directory of source notes with stable ids (`sources/<bib-id>.md`).
- Candidate material: the digests/slug inventory produced by distillation.
- The page schema (frontmatter fields + fixed body headings + word cap) — for agent-patterns, SPEC §5.1.
- Fixed metadata values that must not vary per writer (verification date, model families).

## Outputs

- One plan file: sections of pipe-delimited lines, one per page — `slug | title | type | category | status | durability | confidence | sources | related`.
- One page file per plan line, at `patterns/<slug>.md` (or the project's equivalent).
- A lint result showing id==filename, valid frontmatter, and every `sources:`/`related:` entry resolving.

## Workflow

1. Cluster the candidate slugs yourself (this is the judgment step — do not delegate it): merge synonyms, decide status by the evidence threshold (e.g. ≥ 2 distinct sources → adopted), assign category/durability/confidence per the project's rules.
2. Write the plan file with every page's full metadata line, grouped into batches of 6–8 pages that share source notes (shared sources minimize duplicate reading).
3. For each batch, write the pages from the plan section. The writing contract, whether executed inline or delegated: (a) follow the schema file (read it first), (b) use the plan's metadata verbatim, (c) READ each cited source note before writing its evidence line, (d) evidence lines are `- [<bib-id>] <one-line paraphrase of what the note actually supports>`, (e) a source the note doesn't support gets dropped from both the evidence and the frontmatter list, and the drop gets reported.
4. After all pages exist, lint: parse every page's frontmatter; check id==filename, required fields present, every source id has a note file, every related slug has a page; print status/category/durability distributions.
5. Generate downstream artifacts (index, quickref, lists) only after the lint is clean, and spot-check generated files for empty extracted fields.

## Concrete examples

### Example 1: the W3 batch (agent-patterns)

Plan line: `match-model-to-task | Match the model to the task | pattern | delegation | adopted | structural | medium | every-2026-07-07-fable-unknowns, every-2026-04-27-most-expensive-model, … (8 sources) | subagents-for-context, full-brief-up-front`. The writer read all 8 notes, kept all 8 (each supported a line), and noted that no Codex tool-notes were possible because codex-docs documents only AGENTS.md and skills — an honest omission the discipline licensed.

### Example 2: a narrowed citation (W4 batch)

The plan asserted `openhands-2026-ccbp` supported `cross-model-review`. The writer, having read the note, found it supports only *fresh-model plan review*, not different-model code review — and scoped the evidence line to exactly that claim, reporting the narrowing. The alternative (writing the plan's assertion) would have fabricated evidence in a wiki whose premise is traceability.

## Anti-patterns

- **Delegating the clustering.** Merging ~90 candidate slugs into 36 pages is the highest-judgment step; the session did it in the orchestrator with all digests in view. Writers execute; they don't decide the taxonomy.
- **Restating metadata in prompts instead of pointing at the plan.** Copies drift; the plan file is the single source of truth.
- **Evidence lines from digests.** Digests are second-hand; the contract requires reading the note itself. The narrowed-citation example only happened because the writer read the note.
- **Skipping the lint because writers were careful.** The lint is ~30 lines of Python and found the categories/status distributions that went into the review summary; it is also the only cross-writer check of `related:` links.

## Acceptance criteria

- [ ] Every page's frontmatter fields match its plan line exactly.
- [ ] Lint reports zero missing sources, zero unresolved related links, zero id/filename mismatches.
- [ ] Every evidence line names a source note that exists and supports the claim.
- [ ] All citation drops/narrowings were reported, not silent.
- [ ] Generated downstream artifacts contain no empty extracted fields.

## Files this skill creates / modifies

- `<scratchpad>/pattern-plan.md` — the authoritative plan (scratch; consider committing for audit).
- `patterns/<slug>.md` — one page per plan line (committed).
- Generated artifacts (index, quickref, lists) — regenerated after lint (committed).
