# Task 02 — Specify the Idea→Spec Process

**Status:** ready · **Depends on:** task-01 (artifact vocabulary) · **Feeds:** task-03 (checks run at stage gates)

## Why this task exists

`spec-completeness/README.md` (merged via PR #23, for issue
[#22](https://github.com/lago-morph/idea-pipeline/issues/22)) established what
a one-shot-complete spec looks like and gave a completeness checklist (§3).
Task-01 defines the artifact anatomy of such a spec. This task defines the
**process that produces those artifacts from a raw idea** — and the owner's
requirement is that the process be *explicit and well-specified enough to be
pressure-tested against real ideas*, not a vibes-level "iterate until good."

Concretely: the process description must be precise enough that a session
executing it on a real idea can tell, at every moment, which stage it is in,
what to do next, whether the stage's exit criteria are met, and where a
discovered problem routes back to. Give the process the same treatment the
gold specs give systems: states, deterministic steps, data structures, exit
gates, and its own definition of done.

## Context to load before starting

1. `spec-completeness/README.md` — especially §3 (the checklist the finished
   spec must satisfy) and §4.2 (the ablation protocol; your probe-build stage
   reuses its grading idea).
2. `spec-completeness/artifact-model.md` (task-01's deliverable) — your
   process produces these artifacts; use its IDs (A-VS, C-DM, C-BC, C-FM,
   C-QC, R-IS, R-RA, R-CD, R-FR, G-AC, G-CM, G-ST) as the names of work
   products. If task-01 is not yet merged, read its task file
   (`tasks/task-01-artifact-model.md`) and use the design-direction IDs,
   flagging the dependency.
3. `spec-completeness/profiles/` — skim the ambiguity audits (dimension 13);
   the process must be designed to catch exactly these defect types before
   freeze.
4. The repo root's numbered idea files (`01-*.md` … `12-*.md`) — these are the
   real ideas the process will be pressure-tested against; calibrate the
   process's entry expectations to their actual shape (a few paragraphs of
   intent, no structure).

## Objective

Produce `spec-completeness/process.md`: a staged, loop-structured process from
"I have an idea" to a compiled spec that passes the README §3 checklist,
specified with roles, data structures, per-stage entry/exit criteria, defect
routing, metrics, and abort criteria — plus a pressure-test protocol for
evaluating the process itself.

## Design direction (starting hypothesis from the planning session)

Refine or restructure with stated reasons. The central insight to preserve:
**one-shot building removes build-time interactivity, so the entire
clarification dialogue must be pre-run at spec time** (research anchor:
Ambig-SWE, arXiv:2502.13069 — interactivity recovers underspecification;
one-shot has none). And because one-shot builds are cheap, **the build is the
test of the spec**: iterate the spec against real builds, fixing the spec —
never the generated code.

**Roles:** OWNER (human; intent authority; the only role that can answer
INTENT questions), AUTHOR (persistent session that drafts artifacts), PROBE
(fresh *ephemeral* session with no author context — its ignorance is the
measurement instrument), BUILDER (one-shot build session).

**Core data structures** (define schemas precisely):

- *Question record:* id, text, raised-by, target artifact, class
  (`INTENT` — only the owner can answer; `ARBITRARY` — any consistent answer
  works, author proposes and owner batch-ratifies; `DEFERRABLE` — becomes a
  Freedom Register entry with a bounding contract), severity, status,
  resolution reference.
- *Severity rubric:* BLOCKER = two reasonable implementers would produce
  observably different behavior; MAJOR = the builder must invent a decision
  but implementations likely converge; MINOR = cosmetic.
- *Decision log* (question ids → decision → artifact delta) and *Freedom
  Register* entries (choice, bounding contract ref, documentation obligation).
- *Build defect record:* class (`INTENT_GAP` / `CONTRACT_GAP` /
  `REALIZATION_GAP` / `GATE_GAP` / `LINT`), evidence, routed-to stage.

**Stage sketch** (each needs: purpose, executor roles, activities, inputs,
outputs, entry criteria, exit criteria, loop condition):

- **S0 Capture** — idea paragraph + intended user + one observable success
  statement.
- **S1 Scope** — produce A-VS. Key activity: the *assumption probe* — a PROBE
  given only the idea lists everything it assumes is included; OWNER
  dispositions each assumption in or out (out ⇒ non-goal with extension-point
  note). Exit: a fresh probe yields zero undispositioned assumptions.
- **S2 Skeleton** — instantiate every artifact as a template whose sections
  contain either content or enumerated open questions; no blanks. This makes
  incompleteness visible and countable from day one.
- **S3 Contract loop (WHAT)** — the core loop. Per iteration: PROBE (given
  Layer 0–1 drafts only) lists implementation-blocking questions; triage by
  class; answers flow into C-artifacts or the Freedom Register. Run closure
  checks (complete enums, state×event coverage, operations×failure-classes).
  Exit: two consecutive probes yield no new BLOCKER/MAJOR questions AND
  closure ratios = 1.0 ("loop until dry").
- **S4 Realization layering (HOW)** — author R-IS/R-RA/R-CD, each element
  citing its C-parent; PROBE implements one representative module from the
  draft and reports every decision it had to invent. Exit: bidirectional
  traceability holds (no orphan HOWs; no dangling WHATs) and the probe's
  invention list contains no BLOCKERs.
- **S5 Gate construction** — backfill G-AC one checkbox per normative claim;
  any claim that resists a mechanical check is itself defective — route it
  back to S3/S4 for rewrite (the DoD is a forcing function on body
  precision, not documentation of it). Build G-CM if variation axes exist;
  write G-ST covering the primary C-BC flow.
- **S6 Assembly & lint** — compile artifacts into the single-file K-ordering;
  run the deterministic lint checks (task-03). Exit: zero lint errors.
- **S7 Probe builds** — k one-shot BUILDER runs (k≥3 during iteration, k≥5
  before freeze); grade each against G-AC + G-ST; produce a cross-run
  *divergence report* (where did builders make different choices?). Classify
  every failure/divergence/invented-decision as a build defect and route via
  a **routing table** (e.g. builder needed intent → S3; interface mismatch →
  S4; builds pass but owner says behavior is wrong → gate hole, S5 + S3).
  Freeze when two consecutive rounds have all builds passing G-AC with no
  BLOCKER divergence; tag v1.0.

**Abort criterion** (the pressure-test signal): if S3 iterates more than M
times without the open-question count declining, the idea is not ready —
return to OWNER with the question backlog as the diagnosis.

**Metrics** (so pressure testing yields numbers, not impressions): open
questions by severity per iteration (burn-down), closure ratios, G-AC
coverage ratio, probe-build pass rate, divergence count, iterations per
stage.

## Pressure-test protocol (include as an appendix in the deliverable)

Define how to evaluate the *process* on real ideas from this repo: pick ≥1
numbered idea file (choose one small, e.g. a skill-sized idea, and optionally
one large); execute S0→S6 (S7 optional against a cheap target); record per
stage: iterations, question counts, wall time, and — most importantly —
**process defects**: every point where the executor couldn't tell what to do
next, an exit criterion was ambiguous, or a data structure didn't fit.
Process defects feed a process v2. The pressure test is itself a session-sized
task; write its runbook here so a future session can execute it directly.

## Deliverables

- `spec-completeness/process.md` — the full process spec: roles, data
  structures (with field-level schemas), stage cards (uniform format), the
  defect routing table, loop/abort/freeze criteria, metrics, and the
  pressure-test protocol appendix.
- One-paragraph cross-reference added to `spec-completeness/README.md`.

## Task acceptance checklist

- [ ] Every stage has explicit entry criteria, exit criteria, executor
      role(s), inputs, and outputs — uniform card format
- [ ] Every artifact from artifact-model.md is produced by exactly one stage
      (and revised via defined routing, not ad hoc)
- [ ] Question classes, severity rubric, and all data structures have
      field-level schemas
- [ ] The routing table covers all five build-defect classes
- [ ] Loop-until-dry, abort, and freeze conditions are stated numerically
      (choose and justify M, k, consecutive-round counts)
- [ ] The WHAT loop (S3) closes before the HOW layering (S4) begins, and the
      process text explains why (freedom must be *declared*, not leaked)
- [ ] A fresh session could run the pressure test from the appendix alone
- [ ] Doc re-read top-to-bottom once; stage names, artifact IDs, and metric
      names consistent throughout

## Out of scope

- Actually running the pressure test (that's the follow-on session the
  appendix enables)
- Building the lint/probe tooling (task-03)
- Modifying the README checklist

## Working notes

Commit to a fresh branch, PR referencing issue #22. Where you must choose
constants (M, k, thresholds), choose and justify — a pressure test can tune a
stated number, but not an unstated one.
