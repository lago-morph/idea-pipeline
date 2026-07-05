# Task 01 — Define the One-Shot Spec Artifact Model

**Status:** ready · **Depends on:** nothing (run this first) · **Feeds:** task-02 (process), task-03 (hardened checks)

## Why this task exists

Issue [#22](https://github.com/lago-morph/idea-pipeline/issues/22) asked what
one-shot-complete specs have in common. PR #23 answered descriptively: it
profiled four gold-example specs against a 14-dimension rubric and derived a
~45-item completeness checklist (`spec-completeness/README.md`). The next step
is structural: a gold spec is a single file, but it has internal anatomy. This
task names that anatomy as a set of **related artifacts with dependency and
traceability rules**, so that specs can be authored artifact-by-artifact,
checked artifact-by-artifact, and compiled into the single distributable
document.

The analogy is the Rational Unified Process's artifact set (Vision document,
use-case model, supplementary specification, glossary, test plan), but
**simplified to cover only what actually appears in one-shot specs**, and
**not constrained by RUP** — reuse its vocabulary only where it genuinely fits.

## Context to load before starting

Read, in this order:

1. `spec-completeness/README.md` — the commonality findings (§2), the
   checklist (§3), and the influence hypotheses (§4). Your artifact model must
   account for every §2.1 common attribute (A–L).
2. The four per-spec profiles in `spec-completeness/profiles/` — each is a
   14-dimension analysis with line-number evidence, including an **ambiguity
   audit** (dimension 13) listing each spec's known defects. You will need
   these audits for validation (see below).
3. The four source specs (fetch raw; each ~1,500–2,200 lines — skim structure,
   read sections your model must classify):
   - https://raw.githubusercontent.com/strongdm/attractor/main/attractor-spec.md
   - https://raw.githubusercontent.com/strongdm/attractor/main/coding-agent-loop-spec.md
   - https://raw.githubusercontent.com/strongdm/attractor/main/unified-llm-spec.md
   - https://raw.githubusercontent.com/openai/symphony/main/SPEC.md

## Objective

Produce `spec-completeness/artifact-model.md` defining:

1. A minimal set of named artifacts (with short stable IDs) that jointly
   contain everything a one-shot spec needs — and nothing more.
2. A dependency graph between artifacts (which is expressed in terms of
   which).
3. **Strict WHAT/HOW layering** — this is the owner's central requirement.
   Both are wanted, but not mixed: the WHAT (domain concepts, observable
   behavior, properties, failure semantics, quality constraints) is specified
   generically, implementation-free, and must be able to survive a total
   rewrite of the HOW. The HOW (interfaces, wire formats, pseudocode,
   defaults) is **layered on top**, with every HOW element explicitly citing
   the WHAT element it realizes.
4. Traceability rules that make the layering checkable, not aspirational.
5. A compilation scheme: fixed ordering that assembles the artifacts into the
   single-file spec shape the gold examples use, with citation tags surviving
   compilation.
6. **Validation by decomposition**: a mapping table for EACH of the four gold
   specs showing which sections instantiate which artifacts.

## Design direction (starting hypothesis from the planning session)

The planning session sketched the following. Treat it as a hypothesis to
refine or restructure — with stated reasons — not as settled:

- **Four layers plus a non-normative annex:**
  - Layer 0 Intent: `A-VS` Vision & Scope (goals as principles; non-goals
    each mapped to the extension point where they'd attach; boundary notes),
    `A-GL` Glossary (one authoritative definition per normative term).
  - Layer 1 Contract (WHAT, implementation-free): `C-DM` Domain Model
    (entities, complete enums, constraints), `C-BC` Behavioral Contract
    (state machines, ordering guarantees, precedence rules as total orderings
    with tie-breaks, invariants), `C-FM` Failure Model (taxonomy, retryable
    semantics, blast radius), `C-QC` Quality Constraints (concurrency
    *guarantees*, timing bounds, safety invariants, portability).
  - Layer 2 Realization (HOW): `R-IS` Interface Surface (signatures,
    tool/endpoint blocks, grammars, wire formats), `R-RA` Reference
    Algorithms (step-numbered pseudocode as *determinism witnesses* for C-BC
    rules; exact formulas), `R-CD` Configuration & Defaults (every knob
    defaulted at point of definition; resolution chains; consolidated
    cheat-sheet), `R-FR` **Freedom Register** — the seam artifact: each entry
    = (choice left open, bounding contract reference, documentation
    obligation on the implementer). The only place a contract element may
    lack a realization.
  - Layer 3 Gate: `G-AC` Acceptance Checklist (one mechanically checkable box
    per normative claim), `G-CM` Conformance Matrix (variation axes ×
    requirements), `G-ST` executable Smoke Test with ASSERTs.
  - Annex: `X-DR` Design Rationale (quarantined why-material), `X-WE` Worked
    Examples (promotable into G-ST as test vectors).
- **Candidate traceability rules:** (1) no HOW without a cited WHAT — orphan
  R-elements are either missing requirements or over-specification; (2) no
  WHAT left dangling — every C-element is realized by ≥1 R-element or
  registered in R-FR; (3) Layer 1 is self-sufficient — readable and closed
  (complete enums, total state×event coverage) without Layer 2; (4) on
  R-vs-C conflict, C wins for the implementer AND the conflict is a spec
  defect (internal analog of symphony's "the Codex protocol controls").
- **Known classification tension to resolve:** concrete input syntax (e.g.
  attractor's DOT BNF, the v4a patch grammar) — the planning session leaned
  toward R-IS (concrete surface) with the abstract model in C-DM, which
  implies gold specs sometimes interleave the two in one section. Your model
  must take a position and apply it consistently in the decompositions.

## Validation requirement (the acceptance test for the model)

The model is validated when:

1. **Every gold spec decomposes cleanly**: per-spec tables (artifact → spec
   sections → strength assessment) with no section left unclassified and no
   artifact requiring content the specs don't contain.
2. **The audited defects reappear as model violations.** Each profile's
   ambiguity audit lists 2–3 known defects (e.g. attractor's `heuristic_select`
   reading fields `Outcome` doesn't define; symphony's dangling "configured
   assignee"; unified-llm's missing non-goals section; symphony's missing
   smoke test; coding-agent-loop's byte-for-byte vs. behavioral-alignment
   contradiction). A good model expresses every one of them as a missing
   artifact, a thin artifact, or a traceability-rule violation. If a known
   defect is invisible to the model, the model has a hole — fix it.
3. **Best-of-breed references are identified**: for each artifact, name which
   gold spec's section is the exemplar (planning hypothesis: coding-agent-loop
   §8 for A-VS, unified-llm §6 for C-FM, symphony's `Implementation-defined`
   mechanism for R-FR, symphony §9.5 for C-QC — verify or correct).

## Deliverables

- `spec-completeness/artifact-model.md` — the model: layers, artifact table
  with IDs and contents, dependency graph (ASCII or Mermaid), traceability
  rules, compilation ordering, and the four decomposition tables with a
  closing "what the decomposition shows" section.
- A short cross-reference added to `spec-completeness/README.md` (one
  paragraph pointing to the new doc; do not restructure the README).

## Task acceptance checklist

- [ ] Every §2.1 common attribute (A–L) from README.md has a home in exactly
      one artifact (or an explicitly-justified split)
- [ ] Every checklist section (README §3 A–J) maps to ≥1 artifact
- [ ] WHAT artifacts contain no interface names, wire formats, defaults, or
      pseudocode
- [ ] Every HOW artifact's definition includes its citation obligation
- [ ] Dependency graph is a DAG; every edge is justified in one sentence
- [ ] All four decomposition tables complete; every audited defect from the
      profiles' dimension-13 sections is expressed as a model violation
- [ ] Compilation ordering reproduces the K-ordering observed in README §2.1
- [ ] Doc re-read top-to-bottom once for internal consistency (IDs, cross-refs)

## Out of scope

- Authoring templates for each artifact (belongs to task-02's skeleton stage)
- Implementing checkers for the traceability rules (task-03)
- Changing the checklist in README §3

## Working notes

Commit to a fresh branch and open a PR referencing issue #22. Artifact IDs you
define here become vocabulary for task-02 and task-03 — keep them short,
stable, and greppable.
