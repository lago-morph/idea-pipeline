# Task 03 — Harden the Completeness Checklist into Executable Checks

**Status:** ready · **Depends on:** task-01 (artifact vocabulary; soft dependency — see Context) · **Feeds:** task-02's stage gates (S3 closure, S6 lint, S7 grading)

## Why this task exists

The checklist in `spec-completeness/README.md` §3 (~45 items, sections A–J)
currently asks "was this thing done" — a DoD section *exists*, defaults *are
present*. Existence checks are Goodhart-able: a bad DoD satisfies "a DoD
exists." The owner's requirement is to harden every item into "was this done
**correctly and completely**," with **concrete logic for how each thing is
checked** — not additional bullet points, but executable check definitions.

Tier preference, strictly ordered:

1. **Tier D — deterministic automation**: scripts over the spec text or over
   structured extracts; same input → same output; no model in the loop.
2. **Tier L — LLM checks in constrained-context ephemeral sessions**: a fresh
   session per check, fixed prompt template, context limited to named
   artifacts, structured output, stability measured across k runs.
3. **Tier H — human review**: last resort, only where the pass criterion
   references intent ("is this what we want") that no artifact encodes.

The **escalation ladder rule**: every check must be implemented at the lowest
tier that can decide it. A check that *could* be deterministic but is
specified as an LLM judgment is a defect in this task's deliverable.

## Context to load before starting

1. `spec-completeness/README.md` — §3 is your work queue (every item A.1–J.5
   must be covered); §2.3 lists the residual-defect classes even gold specs
   have (your checks must catch these); §4.2's ablation protocol is the
   calibration hook.
2. `spec-completeness/profiles/` — the four ambiguity audits (dimension 13)
   are your **regression corpus**: each names concrete defects in real gold
   specs (attractor's `execute_subgraph` invoked but never defined;
   symphony's "configured assignee" referencing a config field that exists
   nowhere; unified-llm's gate item testing a behavior declared
   implementation-defined; coding-agent-loop's byte-for-byte vs.
   behavioral-alignment contradiction). A hardened check suite that would NOT
   have flagged these on the gold specs is inadequate.
3. `spec-completeness/artifact-model.md` (task-01 deliverable) if merged —
   checks should target artifacts (C-DM, R-RA, G-AC…) and traceability rules.
   If task-01 isn't done yet, read `tasks/task-01-artifact-model.md` and
   write checks against the design-direction artifact IDs, marked provisional.
4. The four source specs (raw URLs in task-01) — your worked examples and any
   prototype runs use these as test subjects.

## Objective

Produce the hardening framework and the full set of check definitions:

- `spec-completeness/hardening/README.md` — the framework: tier definitions
  and rules, the check-specification format, the escalation ladder, and a
  coverage table mapping every README §3 item to its check(s).
- `spec-completeness/hardening/checks.md` — every check, fully specified in
  the format below. (Split into multiple files if length demands; keep IDs
  stable.)

This task specifies checks; *implementing* runnable tooling may be delegated —
see "Follow-on tasks" below.

## The check-specification format

Every check is a (claim, probe, pass-criterion) triple, written as:

```
CHECK <ID>            e.g. D-03, L-07
Title:                one line
Hardens:              README §3 item(s), e.g. "F.2, F.3"
Tier:                 D | L | D+L | H
Inputs:               exact artifacts/sections consumed
Procedure:            numbered, concrete steps — for Tier D, pseudocode or a
                      shell/regex sketch precise enough to implement without
                      decisions; for Tier L, the verbatim prompt template,
                      the context slice, the output schema, k, and the
                      aggregation rule
Metric:               name, formula, threshold (prefer ratios over booleans)
Output:               PASS/FAIL + metric value + evidence pointers
                      (file:line), machine-parseable
Failure semantics:    what a failure means; which process stage it routes to
                      (task-02's routing table)
```

## Design direction (starting hypothesis from the planning session)

Three probe families cover the hardening; distribute the A–J items across
them:

**1. Completeness → closure/cross-product checks (mostly Tier D, with Tier-L
extraction).** Don't ask "is there an error section"; compute a cross-product
and require no silent empty cells:

- enum closure: every enum-typed field referenced by any algorithm resolves
  to a complete value list; every value is consumed somewhere or marked
  reserved
- state machine closure: every state × event has a transition or a declared
  impossibility
- failure closure: operations × failure classes (timeout, malformed input,
  missing resource, concurrent modification) — defined behavior or explicit
  N/A per cell
- defaults closure: config-fields-referenced ÷ config-fields-with-default = 1.0
- identifier closure: every helper invoked in pseudocode is defined; every
  config field named in prose exists in the schema; every field an algorithm
  reads exists on the record it reads from
- traceability closure (task-01 rules 1–2): no orphan HOWs, no dangling WHATs

Hybrid pattern where extraction needs reading: **Tier-L extraction into a
typed inventory (JSON), Tier-D verification over the inventory** — plus an
extraction-stability requirement (k independent extractions must agree on the
inventory before the deterministic check runs; disagreement is itself a
finding about the spec's clarity).

**2. Correctness → independent-reader probes (Tier L).** Ambiguity is
invisible to the author but measurable as disagreement between readers:

- question-count probe: fresh session lists every question it would need
  answered before implementing; count × severity (severity rubric from
  task-02); trend must be monotonically decreasing across spec revisions
- inter-reader divergence: k fresh sessions answer the same concrete scenario
  questions ("what happens when X?") from the spec alone; divergence rate
  localizes imprecision to sections
- determinism trace: k fresh sessions trace a concrete input through a
  pseudocode algorithm under a constrained output schema; outputs must match
  exactly (Tier-D comparison of Tier-L outputs)
- assumption probe (scope): fresh session lists what it assumes is in scope;
  every assumption must map to a goal, a non-goal, or a freedom entry

Tier-L constraint rules to codify in the framework: ephemeral session, zero
author context, context = explicitly listed artifact files only, pinned
prompt template (versioned in the repo), structured output schema, k ≥ 3 with
a stated aggregation rule (e.g. majority for verdicts, union for findings),
and every verdict accompanied by evidence pointers so a human or Tier-D step
can audit it.

**3. Gate adequacy → mutation testing (Tier L+D, the strongest and most
expensive).** For section A: seed deliberate spec-violations into a reference
implementation (or into *descriptions* of behavior, for a cheaper variant)
and verify G-AC + G-ST catch each one; surviving mutants are holes in the
gate. Score = mutation kill rate. Define the mutant taxonomy (wrong default,
skipped ordering guarantee, missing failure handling, off-by-one in a
formula, violated invariant) and both variants: full (against a real
implementation, e.g. one of the attractor OSS implementations) and cheap
(mutated behavior descriptions judged against the checklist, no code).

**Also specify:** the residual-defect regression suite (the profile-audit
defects as named test cases with expected check firings), and the
**calibration hook** — how check metrics get validated against real one-shot
build outcomes per README §4.2, so items that don't predict build success get
down-weighted rather than accumulating as ritual.

## Deliverables

- `spec-completeness/hardening/README.md` (framework, tiers, format,
  escalation ladder, coverage table README §3 item → check IDs → tier)
- `spec-completeness/hardening/checks.md` (all check definitions)
- One-paragraph cross-reference added to `spec-completeness/README.md`
- A "Follow-on tasks" section in the hardening README: session-sized
  implementation tasks (e.g. "implement the Tier-D lint suite," "build the
  ephemeral-probe runner," "run the mutation study against attractor-c"),
  each with enough context to be picked up independently — same style as the
  files in `spec-completeness/tasks/`.

## Task acceptance checklist

- [ ] Every README §3 item (all sections A–J) maps to ≥1 check in the
      coverage table; no check exists without a mapped item
- [ ] Every check follows the specification format completely — no
      "Procedure: TBD"
- [ ] Escalation ladder audit: each Tier-L check includes one sentence on why
      it cannot be Tier D; each Tier-H check on why it cannot be Tier L
- [ ] Tier-L checks specify: verbatim prompt template, context slice, output
      schema, k, aggregation rule, and evidence-pointer requirement
- [ ] Every named residual defect from the four profiles' ambiguity audits is
      caught by ≥1 check (show the mapping explicitly)
- [ ] Metrics are ratios/scores with thresholds wherever possible, booleans
      only where genuinely binary
- [ ] Failure semantics route to task-02 process stages (use its defect
      classes; if task-02 isn't merged, use INTENT_GAP / CONTRACT_GAP /
      REALIZATION_GAP / GATE_GAP / LINT, marked provisional)
- [ ] Follow-on implementation tasks are defined and session-sized
- [ ] Docs re-read once for ID consistency (check IDs, artifact IDs, §3 item
      references)

## Out of scope

- Implementing the runnable tooling (defined as follow-on tasks instead)
- Running the mutation study or calibration experiments
- Changing README §3 item wording (propose rewordings in a "suggested
  amendments" appendix if hardening reveals an item is untestable as written)

## Working notes

Commit to a fresh branch, PR referencing issue #22. Prefer boring,
greppable check IDs. When in doubt about a check's tier, write the Tier-D
version of the procedure first and only escalate what remains genuinely
judgment-shaped.
