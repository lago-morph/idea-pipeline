# Spec: `corpus-decomposition-fanout`

- **ID**: SKILL-SPEC-90925ead23
- **Source retrospective**: ../2026-07-05-26.md

## Intent

Validate or refine a structural model (an artifact set, taxonomy, rubric, or schema) against a corpus of large documents by dispatching one background analyst per document, each classifying every section of its document against the model from an identical, self-contained brief — while the dispatcher concurrently reads the crux sections itself. In the session this spec comes from, four analysts classified 7,911 lines / 379 headings of gold specs against a hypothesized 15-artifact model; two independently proposed the same missing artifact (Architecture Sketch), one refuted a boundary placement (observable formulas belong to the contract layer, not the algorithm layer), and collectively they surfaced 11 spec defects beyond the previously known audits. Independence across analysts converts agreement into signal; per-document isolation keeps each context small enough for line-level rigor.

## Trigger

- Direct: "decompose X against the model", "map every section of these docs
  to the artifacts", "validate the taxonomy/rubric against the corpus",
  "which parts of these documents are Y?"
- Proactive: any task requiring classification of ≥2 documents each ≥1,000
  lines against a shared structure, where the deliverable needs per-section
  evidence (line numbers) and the corpus exceeds what one context can hold
  alongside synthesis work.
- Negative: single short document (read it yourself); classification that
  needs no evidence trail; corpora the dispatcher has already fully read.

## Inputs

- The model/hypothesis: a complete, self-contained definition of every
  category (IDs, one-line definitions, boundaries). This gets inlined into
  every brief verbatim — subagents share no memory with the dispatcher.
- The corpus: local file paths (fetch first; do not make agents fetch).
- Optional: per-document known-defect lists to verify, working positions to
  test, exemplar hypotheses to confirm or refute.

## Outputs

- One inventory file per document in the scratchpad
  (`inventory-<doc>.md`): a table with one row per section (heading +
  line range + content forms + category IDs + notes), plus sections for
  misfits/tensions, crux findings, defect verification, and exemplars.
- One ≤500-word summary per analyst returned as its final message: file
  path, top misfits, defect→violation mapping, exemplar shortlist,
  working-position verdict.
- The dispatcher's synthesis (tables, deltas) built from those files.

## Workflow

1. Fetch every corpus document to the scratchpad. If prior analyses cite
   line numbers, verify the fetched copies match (`wc -l` equality is a
   cheap, effective check — in the source session all four matched exactly,
   which made hundreds of prior line citations safely reusable).
2. Generate a mechanical heading inventory per document
   (`grep -nE '^#{1,3} ' doc.md > headings-doc.txt`). This anchors the
   completeness requirement: every heading must appear in some inventory row.
3. Write one brief per document from a shared skeleton. Mandatory brief
   elements: role + goal sentence; the **full model definition inlined**
   (never "the model above"); exact input paths; the inventory-table format
   and its success criterion ("every heading in the headings file is
   accounted for by some row"); classification discipline (classify by role,
   never by notation or document position; "a flagged misfit is more
   valuable than a strained classification"; the model may gain categories
   but not rename them); per-document crux questions; known defects to
   verify at current line numbers, each mapped to which model rule it
   violates, with instructions to flag loudly if the model cannot express
   it; a **working position to attack** with a verdict + one-line evidence;
   don'ts (no repo writes outside the one inventory file, no network, no
   force-fitting); report format (≤500 words, enumerated sections, "plain
   data — no pleasantries").
4. Dispatch all analysts in one message, `run_in_background: true`,
   subagent type `general-purpose` (they must Write; `Explore` cannot).
5. While they run, the dispatcher reads the crux sections of each document
   itself — the places its own design decisions hinge on. Deliberate
   overlap with the analysts is a feature: independent convergence is
   validation, divergence is a review queue.
6. As reports arrive, read each inventory file in full. Spot-verify at
   least three line citations per document by reading the cited lines.
7. Integrate: apply evidence-forced changes to the model, build the
   synthesis tables from the inventories, and record which analyst finding
   forced which change.

## Concrete examples

### Example 1: The source session (artifact model vs. four gold specs)

Model: 15 hypothesized spec artifacts (A-VS, C-DM, … G-ST, X-DR/X-WE) with
WHAT/HOW layering. Corpus: four gold specs (attractor 2,090 lines;
coding-agent-loop 1,467; unified-llm 2,169; symphony 2,185), fetched from
raw.githubusercontent.com to scratchpad and line-count-verified against
existing profiles. Four briefs shared the model block verbatim and diverged
in crux questions (attractor: the DOT-grammar seam; unified-llm: the §2
architecture decomposition; symphony: the `Implementation-defined` keyword
mechanism; coding-agent-loop: the byte-for-byte contradiction). Results:
all 379 headings classified; `inventory-attractor.md` alone confirmed three
known defects at current lines and found four gate-vs-body contradictions
the prior audits missed (e.g., DoD line 1894 requiring `POST /run` while
§9.5 defines disjoint `/pipelines…` routes). Two analysts independently
proposed an Architecture artifact; the dispatcher had reached the same
conclusion from its crux reads — it shipped as `R-AS` in PR #26.

### Example 2: Hypothetical next use (task-03 checker dry-run)

Model: the hardened-check tiers (deterministic / constrained-LLM / human)
over the README §3 checklist. Corpus: the same four specs. The brief adds a
per-check question — "would this check, run on your document, fire on the
known defects and stay silent elsewhere?" — making each analyst a dry-run
of the checker suite, with the inventory recording expected-fire line
numbers as the regression corpus.

## Anti-patterns

- **Dispatching `Explore` agents for work that writes files**. They lack
  Write; the source session selected `general-purpose` for exactly this.
- **Briefs that reference shared context** ("classify against the model
  above"). Subagents start fresh; every brief must be self-contained.
- **Accepting notation- or position-keyed classifications**. The corpus
  used BNF for an *abstract* enum and kept normative wire contracts in
  appendices — both misfile under surface-form rules.
- **Rubber-stamping agent output without own crux reads**. The
  spot-verification reads are what made the citations publishable.
- **Letting analysts fetch the corpus themselves**. Fetch once, verify
  once, hand them local paths.
- **Asking analysts to confirm the working position instead of testing
  it**. The session's most valuable finding (formulas → contract layer)
  was a refutation.

## Acceptance criteria

- [ ] Every heading of every corpus document appears in some inventory row
      (checkable against the mechanical headings files).
- [ ] Every classification and finding carries a line citation into the
      document as fetched.
- [ ] Each analyst returns an explicit verdict on the working position
      with evidence, and an explicit list of model misfits (possibly empty).
- [ ] The dispatcher has read-verified ≥3 citations per document before
      any finding ships.
- [ ] Model changes made after integration each name the finding that
      forced them.

## Files this skill creates / modifies

- `<scratchpad>/headings-<doc>.txt` — mechanical heading inventory per document.
- `<scratchpad>/inventory-<doc>.md` — one per analyst; the evidence substrate.
- The dispatcher's deliverable (whatever document the synthesis feeds) —
  modified, not owned, by this skill.
