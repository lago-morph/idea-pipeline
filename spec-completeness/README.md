# What One-Shot-Complete Specs Have in Common

*Analysis for [issue #22](https://github.com/lago-morph/idea-pipeline/issues/22). Compiled 2026-07-05.*

Four specs with a track record of being implemented by an agent in one shot were
profiled against an identical 14-dimension rubric:

| Spec | System | Lines | Source |
|---|---|---|---|
| attractor-spec | DOT-digraph workflow engine | 2,090 | [strongdm/attractor](https://github.com/strongdm/attractor/blob/main/attractor-spec.md) |
| coding-agent-loop-spec | Programmable coding-agent loop library | 1,467 | [strongdm/attractor](https://github.com/strongdm/attractor/blob/main/coding-agent-loop-spec.md) |
| unified-llm-spec | Multi-provider LLM client library | 2,169 | [strongdm/attractor](https://github.com/strongdm/attractor/blob/main/unified-llm-spec.md) |
| symphony SPEC.md | Issue-tracker-driven agent orchestration daemon | 2,185 | [openai/symphony](https://github.com/openai/symphony/blob/main/SPEC.md) |

Full per-spec profiles (with line-number evidence for every claim below) are in
[`profiles/`](profiles/).

This document has four parts:

1. [Method](#1-method) — how the analysis was done and how to extend it
2. [Findings](#2-findings-common-attributes) — attributes common to all four, and instructive differences
3. [Checklist](#3-the-spec-completeness-checklist) — the operational deliverable
4. [Measuring influence](#4-which-attributes-most-strongly-influence-success) — hypothesis ranking + an experiment protocol for the causal question

A companion document, [`artifact-model.md`](artifact-model.md), takes the structural
next step (task-01): it names the internal anatomy these findings describe as a set of
sixteen artifacts with strict WHAT/HOW layering, a dependency graph, traceability
rules, and a compilation scheme — validated by decomposing all four gold specs and by
re-expressing every defect in the profiles' ambiguity audits as a model violation.
Every §2.1 attribute and §3 checklist section below has a designated home there; its
artifact IDs (`A-VS`, `C-DM`, `R-FR`, `G-AC`, …) are the working vocabulary for
task-02 (authoring process) and task-03 (hardened checks).

A second companion, [`process.md`](process.md), supplies the authoring process (task-02):
an eight-stage, loop-structured path (S0 Capture → S7 Probe builds) from a raw idea to a
compiled spec that passes §3, with four roles (OWNER, AUTHOR, PROBE, BUILDER), field-level
schemas for its question/decision/defect records, per-stage entry/exit gates, a defect
routing table over five build-defect classes, numeric loop/abort/freeze criteria, and a
pressure-test protocol for evaluating the process itself against this repo's numbered
idea files. Its S3 question loop and S7 build-and-grade loop operationalize §4.2's
question-count probe and ablation-grading ideas respectively, and its stage gates
(S3 closure, S6 lint, S7 grading) are where task-03's hardened checks execute.

A third companion, [`hardening/`](hardening/), rebuilds the §3 checklist below as
executable checks (task-03): every item A–J maps to one or more (claim, probe,
pass-criterion) definitions — deterministic closure/lint computations over the
artifact-model tag grammar wherever possible, constrained-context ephemeral LLM probes
where reading is unavoidable, mutation testing of the gate artifacts, and exactly one
human check (owner behavior acceptance). [`hardening/README.md`](hardening/README.md)
holds the tier framework, the escalation ladder, the item→check coverage table, and the
calibration hook that ties check metrics back to §4.2's ablation outcomes;
[`hardening/checks.md`](hardening/checks.md) holds the check definitions plus a
regression suite in which every residual defect from the four profiles' ambiguity
audits (§2.3) reappears as an expected check firing. Check procedures live there;
failure routing stays with `process.md` §8.

---

## 1. Method

Two distinct questions require two distinct methods:

**Q1 — "What is common across these examples?"** is *descriptive*. Method:
fix a rubric of document-level dimensions (structure, data-model precision,
behavioral determinism, defaults, error coverage, examples, acceptance
criteria, normative language, implementation freedom, self-containedness,
ambiguity), profile each spec independently against it, then intersect.
Independence matters: each spec was profiled by a separate analysis pass with
no knowledge of the others' results, so convergence is signal, not anchoring.

**Q2 — "What most strongly influences success?"** is *causal*, and commonality
alone cannot answer it. All four specs share many attributes; with n=4 positive
examples and no negatives, every shared attribute is confounded with every
other. Two escapes:

- **Contrast sets.** Compare against specs that *failed* one-shot, or against
  graded variants of the same target (Kilroy's `research/` folder —
  vague/moderate/complex versions of one app — is exactly this design).
- **Ablation.** Take one known-good spec, surgically remove one attribute at a
  time, run one-shot builds, and measure the delta. See §4.2.

Everything in §4.1 below is therefore a *ranked hypothesis*, supported by the
published research cited in issue #22, pending ablation data.

---

## 2. Findings: common attributes

### 2.1 Shared by all four specs

**A. A binary, mechanically checkable Definition of Done.** The single most
striking commonality. Every spec ends in a checkbox conformance section framed
identically: *"An implementation is done when every item is checked off."*

| | attractor | coding-agent-loop | unified-llm | symphony |
|---|---|---|---|---|
| DoD checklist items | 76 | 59 | 71 | ~26 |
| Parity/test matrix cells | 22 | 45 | 45 | ~90 test-matrix assertions |
| Executable smoke test with ASSERTs | ✅ §11.13 | ✅ §9.13 | ✅ §8.10 | ➖ (test matrix instead) |

Three of four also include a runnable end-to-end smoke test with concrete
assertions and expected values. This converts "build the system" from an
open-ended generation problem into a bounded search problem with an oracle —
the agent can loop against the checklist. (Notably, jmccarthy's attractor-c
was built by a pipeline whose literal goal was "satisfy every DoD checkbox.")

**B. Deterministic behavioral semantics — algorithms, not vibes.** Core
control flow is given as step-numbered language-agnostic pseudocode, state
machines appear as explicit transition tables, tie-breaks are total ("sort by
weight DESC, then to_node ASC"), and numeric behavior is given as exact
formulas (three of four specify retry backoff as an equation, e.g.
`delay = min(10000 * 2^(attempt-1), max_backoff)`; the fourth explicitly
delegates retry to its companion spec's formula rather than leaving it vague). Precedence/priority chains
(edge selection, config resolution, prompt layering) are enumerated
exhaustively. Nothing about the core loop is left to inference.

**C. Complete, typed, language-neutral data model with inline defaults.**
Entities as `RECORD`/`ENUM` pseudo-structs or field lists using a portable
type vocabulary (`String | None`, `List<T>`), with a notation legend where
needed. Enums are enumerated *completely* (all 15 event kinds, all 5 statuses…).
Nearly every configurable field carries its default at the point of
definition (`max_command_timeout_ms : Integer = 600000`).

**D. Exact public interface surface.** Interface names, method signatures,
typed parameters, return types, and per-method error contracts — even though
the implementation language is free. Tools/endpoints get structured
`parameters / returns / errors` blocks; HTTP surfaces get exact routes,
methods, status codes, and full JSON bodies.

**E. Systematic error taxonomy with decision tables.** Not scattered
"handle errors gracefully" prose but named error hierarchies, explicit
retryable-vs-terminal classification tables, error→recovery mappings, and
per-failure blast radius ("template errors fail only the affected run
attempt; workflow file errors block all new dispatches"). Boundary cases are
called out by name, often with the motivating pathological input ("a 2-line
file where each line is a 10MB CSV").

**F. Explicit scope fencing: goals AND non-goals.** Three of four have a
dedicated Non-Goals/Out-of-Scope section; symphony adds repeated "boundary
notes" pre-empting a whole class of misimplementation ("Symphony is a
reader/runner, not a ticket-writer"). The best versions also map each
excluded feature to the extension point where it *would* attach.

**G. Implementation freedom that is *declared and bounded*, never accidental.**
Every spec is explicitly language-agnostic and marks where the implementer may
choose ("how you provide that is up to you") — but always bounds the freedom
with an interface, an output contract ("transport may vary, but normalized
outputs MUST match §4"), or an invariant ("externally visible behavior must
remain identical"). Symphony even coins a custom normative term —
`Implementation-defined` — that *obligates the implementer to document* the
choice. Ambiguity that remains is a declared degree of freedom, not an
oversight.

**H. Managed external dependencies with a conflict-resolution rule.** None of
the four is hermetically sealed, but each *manages* its dependencies:
companion specs are named and scoped (coding-agent-loop imports exactly 10
named types from unified-llm), reference implementations are explicitly
"inspiration, not dependencies," and symphony states outright which document
wins on conflict ("the Codex protocol controls").

**I. Worked examples at the I/O boundary.** Complete sample inputs (full DOT
files, JSON payloads with realistic values), sample outputs, and input→output
pairs ("Alice is 30" → `{"name":"Alice","age":30}`). Examples cluster where
formats/parsing live — the places prose is weakest.

**J. Deliberate redundancy, rationale quarantined.** All four state critical
material twice (prose + pseudocode; body tables + consolidated appendix;
config spread through sections + a single "cheat sheet"). Symphony is explicit
about *why*: the cheat sheet exists "so a coding agent can implement the
config layer quickly." Meanwhile *why*-material (design rationale) is pushed
to appendices so the normative body stays prescriptive. These specs are
consciously written for an agent reader: retrieval-friendly, prescription
uncontaminated by discussion.

**K. Consistent macro-structure.** All four order sections
overview/goals → architecture → data model → behavior → interfaces/integration
→ errors → conformance, with a linked ToC. Types precede the operations that
consume them; acceptance criteria come last and reference everything.

**L. Similar mass.** 1,400–2,200 lines, 70–115 KB, single file. Big enough to
be exhaustive; small enough to fit an agent's working context whole.

### 2.2 Instructive differences (what is *not* required)

Differences among successful specs identify attributes that are **not
necessary conditions** — useful for keeping the checklist honest:

- **RFC-2119 keywords are optional.** Symphony uses them rigorously (26 MUST,
  50 SHOULD, 23 MAY, declared up front); the three StrongDM specs use almost
  none (2–6 uppercase keywords each), carrying prescription through imperative
  pseudocode and the DoD instead. What's constant is *testable prescription*,
  not the keyword convention.
- **Markdown tables are optional.** unified-llm uses ~22 tables as its dominant
  instrument; symphony uses **zero** (nested bullets throughout). What's
  constant is *complete enumeration*, not the surface form.
- **A single end-to-end narrative walkthrough is optional.** Symphony has none;
  its ~90-assertion test matrix substitutes.

### 2.3 Even the gold specs leak — and where

The per-spec ambiguity audits found residual defects, and they cluster in the
same two places across all four:

1. **Concurrency mechanisms** — the *guarantee* is stated but the *mechanism*
   (cancellation, actor vs. mutex, result ordering) is underspecified; helper
   functions are invoked in pseudocode but never defined (`execute_subgraph`,
   `steer_cooldown_elapsed`).
2. **Delegated/subjective territory** — enums deferred to external schemas,
   "mirror the reference system prompt structure," estimation without a
   formula, dangling references to config fields that don't exist in the
   schema ("the configured assignee").

These are exactly the defect classes a spec *linter* should target — see
checklist section J.

---

## 3. The spec-completeness checklist

Score a spec before pointing a one-shot harness at it. Items are phrased to be
auditable (yes/no), and ordered roughly by hypothesized impact (§4.1). Item IDs are
stable — new items append fresh IDs, nothing renumbers — and every item maps to
executable checks in [`hardening/`](hardening/) (its README §8 coverage table).
Wording amendments applied by task-04 are recorded in the hardening README's appendix
and [`tasks/task-04-refactor.md`](tasks/task-04-refactor.md).

### A. Acceptance (the oracle)
- [ ] **A.1** A Definition-of-Done section exists, framed as "done when every box is checked"
- [ ] **A.2** Every DoD item is mechanically checkable (a test could assert it) — no "mirrors the structure of X" items
- [ ] **A.3** An executable end-to-end smoke test with concrete ASSERTs and expected values is included
- [ ] **A.4** Cross-cutting variation (providers, platforms, modes) has a parity matrix — every cell must pass
- [ ] **A.5** Optional features are tagged so conformance splits into core vs. extension profiles

### B. Behavior (determinism)
- [ ] **B.1** Every core loop/algorithm appears as step-ordered language-agnostic pseudocode
- [ ] **B.2** Stateful lifecycles have an explicit state machine with a complete transition table
- [ ] **B.3** Every priority/precedence rule is a total ordering with a deterministic tie-break
- [ ] **B.4** Numeric behavior (backoff, limits, thresholds) is an exact formula, not adjectives
- [ ] **B.5** Ordering guarantees and idempotency rules are stated ("X MUST run before Y")
- [ ] **B.6** Concurrency: both the guarantee AND the permitted mechanisms are specified, including cancellation and result ordering
- [ ] **B.7** Invariants are stated explicitly (ideally as a numbered invariants list)

### C. Data model
- [ ] **C.1** Every entity is a typed field list in language-neutral notation, with a notation legend
- [ ] **C.2** Every enum enumerates ALL values, each with semantics
- [ ] **C.3** Field constraints (nullability, ranges, formats, derivations) are inline with the field
- [ ] **C.4** Every normative term has exactly one authoritative definition (glossary/conventions section)

### D. Interfaces
- [ ] **D.1** Public interfaces give exact names, typed parameters, return types
- [ ] **D.2** Every tool/endpoint has a parameters / returns / errors block
- [ ] **D.3** Any wire surface (HTTP etc.) gives exact routes, methods, status codes, and full example bodies

### E. Configuration
- [ ] **E.1** Every knob has an explicit default at its point of definition
- [ ] **E.2** Contextual defaults state their resolution chain
- [ ] **E.3** Deliberately open defaults are marked `implementation-defined` AND require the implementation to document its choice
- [ ] **E.4** A consolidated config cheat-sheet restates all fields + defaults in one place

### F. Errors and edge cases
- [ ] **F.1** A named error taxonomy exists (hierarchy or category table)
- [ ] **F.2** Every error class is classified retryable vs. terminal, in a table
- [ ] **F.3** Every failure states its blast radius (what halts vs. what degrades)
- [ ] **F.4** Boundary cases are named concretely with the motivating pathological input, or carry an explicit N/A per boundary class
- [ ] **F.5** Timeouts are scoped (connect vs. request vs. stream/stall) with defaults and kill sequences

### G. Scope
- [ ] **G.1** Goals stated as named design principles
- [ ] **G.2** A dedicated Non-Goals/Out-of-Scope section exists
- [ ] **G.3** Each exclusion names the extension point where it would attach
- [ ] **G.4** Scope questions on which independent ignorant readers diverge get explicit boundary notes

### H. Freedom management
- [ ] **H.1** Every "up to you" is explicit, and bounded by an interface, output contract, or invariant
- [ ] **H.2** External documents this spec depends on are named, scoped (which types/sections), and given a conflict-resolution rule ("on conflict, X controls")
- [ ] **H.3** Reference implementations are marked inspiration-only, not dependencies

### I. Examples and ergonomics
- [ ] **I.1** Worked input→output pairs exist for every format/parsing surface
- [ ] **I.2** At least one complete, realistic sample input (full config file, full workflow file) is copy-pasteable
- [ ] **I.3** A linked ToC exists
- [ ] **I.4** Rationale ("why") lives in an appendix, out of the normative body
- [ ] **I.5** Critical rules are stated redundantly by derivation: every behavioral contract rule has a reference-algorithm witness (prose + pseudocode), and every consolidated view is derived, never hand-maintained
- [ ] **I.6** Section ordering: types precede the behavior that consumes them; conformance comes last

### J. Lint pass (the defects even gold specs have)
- [ ] **J.1** Every function/helper referenced in pseudocode is defined somewhere in the spec
- [ ] **J.2** Every config field referenced in prose exists in the config schema
- [ ] **J.3** Every field referenced by an algorithm exists on the record it's read from
- [ ] **J.4** No two normative statements about the same element assign it conflicting values, and neither gate nor annex contradicts the body (artifact-model T4)
- [ ] **J.5** Grep the spec for hedge words ("appropriately", "leniently", … — canonical lexicon: HW-LEX v1, hardening checks.md D-12) — each hit is either fixed or converted into a declared `implementation-defined` freedom

---

## 4. Which attributes most strongly influence success?

### 4.1 Ranked hypotheses (with research support)

1. **Executable acceptance criteria (checklist A).** One-shot harnesses work by
   looping until a gate passes; the DoD *is* the gate. Embedding tests in the
   prompt measurably raises pass rates ([arXiv:2311.07599](https://arxiv.org/abs/2311.07599));
   executable specs convert open-ended problems into bounded ones
   ([arXiv:2603.25773](https://arxiv.org/abs/2603.25773)). Practitioner
   confirmation: attractor-c was one-shot-built by literally iterating on the
   upstream DoD checkboxes.
2. **Deterministic behavioral semantics (B).** When a spec is ambiguous, models
   silently guess rather than ask ([HumanEvalComm, arXiv:2406.00215](https://arxiv.org/abs/2406.00215)).
   Interactivity can recover underspecification (+74% on underspecified
   issues, [Ambig-SWE, arXiv:2502.13069](https://arxiv.org/abs/2502.13069)) —
   but one-shot has no interactivity, so the spec must pre-answer every
   question the agent would otherwise ask. Pseudocode + state machines +
   formulas are the pre-answers.
3. **Complete typed data model with defaults (C, E).** Specification
   completeness anchors generation; partial anchoring already helps
   ([arXiv:2510.26130](https://arxiv.org/abs/2510.26130)). Defaults eliminate
   an entire class of arbitrary decisions that otherwise diverge across the
   build.
4. **Declared-and-bounded freedom + explicit non-goals (G, H).** Undeclared
   ambiguity forces guessing; *declared* freedom ("implementation-defined,
   must document") turns the same gap into a non-blocking decision. Non-goals
   prevent scope wandering on long-horizon builds, where drift compounds
   ([SlopCodeBench, arXiv:2603.24755](https://arxiv.org/abs/2603.24755)).
5. **Systematic error/edge coverage (F).** Error paths are where LLM-generated
   code is chronically thin ([arXiv:2512.18131](https://arxiv.org/abs/2512.18131));
   ArchCode shows making non-functional requirements explicit yields
   measurable lift ([arXiv:2408.00994](https://arxiv.org/abs/2408.00994)).
   Also the attribute cheapest to verify from the DoD, compounding with #1.
6. **Ergonomics and redundancy (I).** Plausibly matters for context retrieval
   (agents re-read sections, not whole docs), and symphony's authors believed
   in it enough to state it. Weakest direct evidence; rank last pending data.

Interaction worth flagging: **A is a force multiplier for everything else.**
Defaults, error tables, and enum completeness only pay off in one-shot mode if
the gate checks them; conversely a great DoD over a vague body just documents
failure precisely. The four specs never separate them — which is exactly why
this needs the experiment below.

### 4.2 Ablation protocol (the causal experiment)

The design that no published study has run at whole-app scale (per issue #22's
research survey — nearest is Kilroy's `research/` vague/moderate/complex
gradient, which varies *overall* detail rather than isolating attributes):

1. **Fix one target + harness.** Pick one known-good spec small enough to
   build repeatedly (coding-agent-loop is shortest at 1,467 lines, though it
   needs its companion unified-llm spec in context; a Kilroy-scale toy target
   re-specified to this rubric is cheaper still).
2. **Produce surgical ablations**, one attribute at a time, holding all else
   constant:
   - strip the DoD + smoke test (keep body intact)
   - convert pseudocode to faithful prose (keep information, lose determinism)
   - delete all defaults (keep fields)
   - delete error taxonomy/retryability tables
   - delete non-goals + freedom declarations
   - as a positive control: Kilroy-style "vague" rewrite (everything degraded)
3. **Run k ≥ 5 one-shot builds per variant** (one-shot outcomes are
   high-variance; single runs are noise).
4. **Grade every run against the ORIGINAL spec's full DoD + smoke test**,
   regardless of which variant the builder saw. Metrics: fraction of DoD items
   passing, smoke-test pass (binary), tokens/wall-clock to termination,
   count of arbitrary decisions the agent had to invent.
5. **Weight the checklist** in §3 by the measured deltas.

**Cheap proxy before spending build tokens:** the *question-count probe*. Give
an agent the spec and ask it to list every question it would need answered
before implementing, then count and severity-classify the questions. This is
the one-shot analog of HumanEvalComm's clarification-seeking measure; specs
that elicit fewer/lower-severity questions should one-shot better. Run it on
all variants first — if question-count doesn't separate the ablations, the
expensive builds probably won't either.

### 4.3 Using this operationally

- **Readiness gate:** score any new spec against §3 before dispatching a
  one-shot build; treat sections A–C as blocking, D–J as advisory until
  ablation data says otherwise.
- **Spec linter:** section J is mechanized by [`hardening/`](hardening/)
  (checks D-06…D-12; hedge lexicon HW-LEX v1) — and its §R regression suite
  pins the pass to the real defects it catches in all four gold specs.
- **Authoring template:** the §2.1 K-ordering (goals → non-goals → data model
  → behavior → interfaces → config → errors → examples → DoD) is a fill-in
  skeleton for new specs.
