# Hardened Checks — Framework

*Task-03 deliverable for [issue #22](https://github.com/lago-morph/idea-pipeline/issues/22).
Companions: [../README.md](../README.md) §3 is the checklist being hardened;
[../artifact-model.md](../artifact-model.md) supplies the artifact IDs, traceability rules
T1–T7, and the §5 tag grammar the deterministic tier greps; [../process.md](../process.md)
supplies the stages these checks execute in, the defect classes their failures route to,
and the record schemas their findings land in. All check definitions live in
[checks.md](checks.md). Compiled 2026-07-05.*

The README §3 checklist asks *whether things were done* — a DoD exists, defaults are
present. Existence checks are Goodhart-able: a bad DoD satisfies "a DoD exists." This
framework rebuilds every §3 item as one or more **executable checks** — (claim, probe,
pass-criterion) triples with concrete procedures — that decide whether the thing was done
**correctly and completely**. Division of labor with the process: **checks.md controls the
procedure of each check; process.md controls the routing of each failure** (its §8 table),
exactly as process.md's preamble stipulates.

Contents:

1. [Tiers and the escalation ladder](#1-tiers-and-the-escalation-ladder)
2. [The check-specification format](#2-the-check-specification-format)
3. [Conventions](#3-conventions)
4. [Inventories: how checks see the spec](#4-inventories-how-checks-see-the-spec)
5. [Tier-L constraint rules](#5-tier-l-constraint-rules)
6. [Constants](#6-constants)
7. [Execution map: checks × process stages](#7-execution-map-checks--process-stages)
8. [Coverage table: README §3 → checks](#8-coverage-table-readme-3--checks)
9. [The calibration hook](#9-the-calibration-hook)
10. [Follow-on implementation tasks](#10-follow-on-implementation-tasks)
- [Appendix: suggested §3 amendments](#appendix-suggested-3-amendments)

---

## 1. Tiers and the escalation ladder

Three tiers, strictly ordered by preference:

**Tier D — deterministic automation.** Scripts over the spec text or over structured
extracts (inventories, §4). Same input → same output; no model anywhere in the loop.
Implementable as regex/parse/set-arithmetic per the check's procedure sketch. Tier D is
possible far more often than it first appears because the artifact model gives specs a
grep surface: element IDs, `[realizes:]`/`[freedom:]`/`[checks:]` tags (artifact-model
§5), per-artifact files, and total record schemas.

**Tier L — LLM checks in constrained-context ephemeral sessions.** A fresh session per
check run, zero author context, a pinned prompt template versioned in this directory,
context limited to explicitly named artifact files, structured output against a declared
schema, `k` independent runs with a stated aggregation rule, and stability measured
across the runs (§5). Tier L is the instrument for properties that are *generative*
(list every question you'd need answered), *semantic* (does this box follow from these
elements), or *reader-empirical* (do k ignorant readers diverge) — none of which a
regex can decide.

**Tier H — human review.** Last resort, permitted only where the pass criterion
references intent that no artifact encodes ("is this what we want"). In this suite
exactly one check is Tier H (H-01, owner behavior acceptance) — everything else decides
at D or L. This is deliberate: process.md's OWNER is the scarcest resource (§2.1), and a
check that quietly assumes a human judgment is a check that never runs.

Composite tiers used by this suite:

- **D+L (hybrid, IDs `DL-*`)** — the pattern the closure family runs on: **Tier-L
  extraction into a typed inventory (JSON), Tier-D verification over the inventory**
  (§4). The *verdict* is deterministic; the model only reads, never judges.
- **L+D (mutation, IDs `M-*`)** — Tier-L generation of seeded spec-violations, then the
  gate (Tier D where G-ST is executable, Tier L for the cheap descriptor variant)
  attempts to catch them. The strongest and most expensive probe family: it tests the
  *gate*, not the body.

**The escalation ladder rule.** Every check is implemented at the lowest tier that can
decide it. A check that *could* be deterministic but is specified as an LLM judgment is
a defect in this suite. Two enforcement mechanisms:

1. **Ladder audit (standing).** Every Tier-L/M check block in checks.md carries a
   `Why not lower:` field — one sentence naming the specific sub-problem that resists
   the tier below. The Tier-H check carries one for both lower tiers. A check whose
   sentence can be refuted (someone exhibits the deterministic procedure) is demoted:
   the check is rewritten at the lower tier, keeping its ID.
2. **Write-D-first discipline.** When adding a check, write the Tier-D version of the
   procedure first and escalate only the residue that is genuinely judgment-shaped —
   usually that residue is the *extraction*, not the verdict, which is what `DL-*`
   exists for.

The ladder also runs downward over time: when an inventory becomes deterministically
extractable (because the spec under check carries artifact-model tags), a `DL-*` check
runs as pure Tier D automatically (§4) — no redefinition needed.

## 2. The check-specification format

Every check in checks.md is a (claim, probe, pass-criterion) triple written as:

```
CHECK <ID>            D-07, DL-04, L-02, M-01, H-01
Title:                one line
Hardens:              README §3 item(s), e.g. "F.2, F.3" (numbering per §8's table)
Tier:                 D | D+L | L | L+D | H
Inputs:               exact artifacts/sections/inventories consumed
Procedure:            numbered, concrete steps — for Tier D, pseudocode or a shell/regex
                      sketch precise enough to implement without decisions; for Tier L,
                      the verbatim prompt template, the context slice, the output
                      schema, k, and the aggregation rule
Metric:               name, formula, threshold (ratios preferred over booleans)
Output:               standard check record (§3.2) + check-specific evidence fields
Failure semantics:    what a failure means; defect class + routed stage (§3.3)
Why not lower:        (Tier L/M/H only) one sentence per ladder audit
```

Field-level rules: `Hardens` must name ≥1 §3 item (a check with no mapped item is a
suite defect — §8's table is bidirectionally total); `Metric` states the formula in
process.md §9.2's style and reuses its metric names verbatim where they exist
(`enum_closure`, `t1_orphans`, `gate_coverage`, …); `Procedure` may say "TBD" nowhere.

## 3. Conventions

### 3.1 Check IDs and §3 item IDs

Check IDs are tier-prefixed and stable: `D-##` (deterministic), `DL-##` (extraction
hybrid), `L-##` (LLM probe), `M-##` (mutation), `H-##` (human). IDs are assigned once
and never reused; gaps stay gaps (same policy as artifact-model §5 element IDs).

README §3 prints its item IDs inline (`A.1`…`J.5`; added by task-04 per this
framework's amendment A-1). Item IDs are stable and never renumbered — new items
append fresh IDs (C.4 and I.6 are the first two) — and the coverage table (§8) pins
every ID to an abbreviated restatement, so the mapping survives future §3 edits.

### 3.2 Standard check record

Every check emits one machine-parseable record per run (JSON line):

```
{ "check": "D-07", "spec": "<run-id or spec path>", "version": "<spec-version>",
  "verdict": "PASS" | "FAIL" | "INDETERMINATE",
  "metric": {"name": "config_ref_closure", "value": 0.96, "threshold": 1.0},
  "evidence": [ {"file": "artifacts/C-BC.md", "line": 214, "element": "C-BC-031",
                 "note": "references config key `assignee`; no C-DM field, no R-CD default"} ],
  "route": {"class": "CONTRACT_GAP", "stage": "S3"} | null }
```

Rules: `evidence` is non-empty on every FAIL (evidence-free failures are invalid);
`INDETERMINATE` is reserved for Tier-L runs that miss the agreement floor (§5) or
inventories that fail the stability gate (§4) — it is itself a finding (the spec is too
unclear to measure) and routes like a failure. Ratios are computed so that 1.0 is
perfect; `value < threshold` ⇒ FAIL.

### 3.3 Failure semantics: findings become process records

Checks never fix anything; they mint records that process.md routes:

- **During the producing stage** of the artifact concerned (it is still DRAFT): a FAIL
  mints a **question record** `Q-###` with `raised-by: CHECK` (process §4.2), severity
  per the process §4.3 rubric; the check's evidence is the triage input.
- **After the artifact is CONTROLLED** (routed re-entries, S6 lint, S7 rounds, or
  standalone grading of a finished spec): a FAIL mints a **build defect** `BD-###`
  (process §4.6) with the defect class the check block names, routed per process §8.1.

Class assignment follows process §8.1's signatures; each check block names its
*default* class, and the reclassification rule (process §8.1) still applies — e.g. a
D-07 dangling config key defaults to LINT-shaped routing but is CONTRACT_GAP whenever
the minimal fix would change what a conforming implementation is (symphony's
"configured assignee" is the type case). Checks whose failures are *triage-shaped* say
so: a T1 orphan (D-10) means "missing requirement **or** over-specification — a human
decides which" (artifact-model T1); the check detects, the routed stage dispositions.

### 3.4 Severity of check findings

Severity uses process §4.3's rubric unchanged. Default mapping, overridable at triage:
a closure hole on observable behavior (empty state×event cell, undefined helper on the
public path, contracted-scenario divergence) is BLOCKER; a closure hole on internal
behavior or a missing declaration (idempotency cell, boundary cell) is MAJOR; hygiene
findings (tag syntax, ToC anchors, annex force) are MINOR. Tier-L probes do not grade
their own severity — they supply the evidence (`forced-guess`, divergence spread) and
the AUTHOR grades at ingestion, keeping one grader across iterations (process §4.3).

## 4. Inventories: how checks see the spec

Closure checks compute cross-products (states × events, operations × failure classes).
The cross-product arithmetic is trivially Tier D; the hard part is producing the **typed
inventory** it runs over (the list of states, events, operations, enums, helpers…). The
framework fixes one acquisition rule:

**Inventory acquisition rule.** Every inventory named by a check has a JSON schema
(defined in the check block). It is produced by the cheapest path available:

- **Tagged spec** (authored per artifact-model §5, i.e. any process.md run): extraction
  is **Tier D** — grep element IDs and tags, parse the per-artifact record schemas. The
  check runs as pure Tier D end to end.
- **Untagged spec** (the four gold specs; any external spec being graded): extraction is
  **Tier L** — `k_extract` independent ephemeral sessions each produce the inventory
  from the same context slice, under the same pinned template (checks.md defines one
  template per inventory type, EXT-1…EXT-6).

**Extraction-stability gate.** Before any Tier-D verification runs over an L-extracted
inventory, the `k_extract` inventories are canonicalized (sorted keys, normalized
identifiers) and diffed. Rule: proceed on the **intersection** only if the pairwise
agreement ratio `|∩| / |∪| ≥ S_extract`; below that, the check returns INDETERMINATE
and mints a finding on the *spec's clarity* — if three careful readers cannot even
agree what the enum list *is*, the spec has a defect no closure arithmetic can reach.
Items in the union but not the intersection are attached as evidence (they are the
disputed territory). Disagreement is data, never noise to average away.

One consequence worth stating: for tagged specs the whole D and DL family is a lint
suite you can run in CI; for untagged specs the same checks still run, at the price of
`k_extract` cheap sessions per inventory. The regression suite (checks.md §R) runs the
untagged path against the gold specs.

## 5. Tier-L constraint rules

Codified once here; every `L-*`/`M-*` check inherits them. These are process.md's P4
regime (PROBE role, §2, §4.7) made check-shaped:

1. **Ephemeral session, zero author context.** One fresh session per run; a session
   that has seen an earlier draft, the question queue, or this framework is
   disqualified. Probes are never reused across iterations.
2. **Context = the named slice only.** The check block lists the exact files (artifact
   files or `dist/spec.md`); nothing else enters the session — no repo access, no web,
   no conversation history. The slice is part of the check's identity: changing it is a
   new check version.
3. **Pinned template.** The verbatim prompt template lives in the check block and is
   versioned with this repo; runs cite the template version. No ad-hoc rephrasing —
   a reworded probe is a different instrument.
4. **Structured output, schema-validated.** Output must parse against the block's
   schema; a run that fails validation after one re-prompt is discarded and redrawn
   (and counted — chronic schema failure is itself evidence of an unclear ask).
5. **k and aggregation, stated.** Default `k_L = 3` independent runs. Aggregation rule
   per output kind: **findings → union after dedupe** (dedupe key stated per check);
   **verdicts → majority, with agreement floor** `A_min` (below it: INDETERMINATE);
   **traces/values → exact match required** (any mismatch is a FAIL with the diff as
   evidence — Tier-D comparison of Tier-L outputs). One sanctioned k-variant: a probe
   embedded in a process loop whose exit already demands consecutive clean runs
   (S3's `D_dry = 2`, S1/S4's 1-clean-probe gates, S7's k builders) runs `k = 1` per
   iteration — the loop supplies the replication *sequentially*, per process §9.1's
   justifications, and this framework does not second-guess its constants. Standalone
   grading (no loop around it) always uses the parallel `k` in the check block.
6. **Evidence pointers, mandatory.** Every finding/verdict row carries a locus — a
   quoted passage, `file:line`, or element ID — so a human or a Tier-D step can audit
   it. Rows without loci are dropped at ingestion (and counted). One exemption:
   generative probes whose findings are by definition *absent from the text* (L-04's
   unstated assumptions) carry their category and mapping verdict instead of a locus.
7. **Verbatim archival.** Charters and reports are stored under the run's `probes/`
   directory exactly as process §3.1 lays out; the report is normalized into records by
   the consuming stage's ingestion rule, never edited.

Where a check hardens a probe process.md already charters (P-ASSUME, P-QCOUNT, P-IMPL,
BUILDER), the checks.md template is the **v2 of that charter** and supersedes the §4.7
v1 text, exactly as process.md's own supersession note provides; ingestion and routing
stay with process.md. The v2 templates keep the v1 prompt text and add the output
schema, k rules, and stability machinery around it.

## 6. Constants

Hardening-specific constants, one place, stated and justified (process P6). Process.md
§9.1's constants (`D_dry`, `k_iter`, `k_freeze`, …) are consumed as-is and not restated.

| Constant | Value | Used by | Justification |
|---|---|---|---|
| `k_L` | 3 | all Tier-L verdict/finding probes run standalone | Smallest k with a majority for verdicts and meaningful union growth for findings; matches process `k_iter`'s "smallest non-trivial replication" logic. |
| `k_extract` | 3 | §4 L-extraction | Two agreeing extractions could share a blind spot; three give a majority *and* a pairwise agreement statistic. |
| `S_extract` | 0.90 pairwise agreement (min over pairs) | §4 stability gate | Inventories are enumerations of things literally written in the text; readers should agree almost perfectly. Persistent <0.9 disagreement means the text under-determines its own inventory — a finding, not noise. |
| `A_min` | 2/3 | Tier-L verdict aggregation | With k=3, 2/3 is the smallest decisive majority; unanimous-only would let one noisy run block every verdict. |
| `N_scenario` | ≥1 per C-BC operation + ≥1 per C-FM failure class, cap 40 | L-02 | Ties probe cost to spec size with a budget ceiling; below 1-per-operation, divergence has blind spots exactly where contracts live. |
| `N_trace` | ≥1 vector per R-RA algorithm, ≥2 for algorithms with branching on enum values | L-03 | One vector proves executability; branchy algorithms need a second vector through the other arm or the trace never leaves the happy path. |
| `N_mut` | ≥2 mutants per taxonomy class (≥12 total) | M-01, M-02 | One mutant per class measures luck; two distinguish "gate covers the class" from "gate caught that instance." |
| `kill_min` | 1.0 at freeze-grade; 0.90 advisory during iteration | M-01, M-02 | A surviving mutant is a named hole in the gate (GATE_GAP) — freeze with a known hole is freeze-in-name-only; during iteration 0.9 keeps the signal without blocking every round on the tail. |
| `HW-LEX` | v1 hedge lexicon, defined in checks.md D-12 | D-12 | One canonical, versioned list so process T7/S6 and README §3.J.5 stop each carrying their own "and kin." |

## 7. Execution map: checks × process stages

Checks execute inside process.md's stage gates (its preamble names S3 closure, S6 lint,
S7 grading as the hardened checks' execution sites). This table is the binding: the
stage card's criterion stays the *requirement*; the check is the *procedure* that
decides it; the §8.1 routing table consumes the failure.

| Process gate | Checks run | Stage criteria they mechanize |
|---|---|---|
| S1 exit | D-13, D-15 · L-04 | S1-X1 (assumption probe clean), S1-X2 (A-VS complete per artifact-model §2.2) |
| S3 activity 4 + exit | D-01, D-02, D-03, D-04, D-16, D-20 · DL-01 (precedence half), DL-02, DL-03, DL-04, DL-05 (predicate half), DL-07, DL-08 · L-01 | S3-X1 (dry, via L-01 under `D_dry`), S3-X2 (`enum_closure`, `transition_closure`, `failure_closure`), S3-X4 (register fields) |
| S4 activity 4 + exit | D-05, D-06, D-08, D-10, D-11, D-17, D-18, D-19, D-26, D-27 · DL-01 (resolution-chain half), DL-06 · L-07 | S4-X1 (`t1_orphans`, `t2_dangling`), S4-X2 (`defaults_closure`), S4-X3 (implementation probe clean), S4-X5 (helper closure), S4-X6 (X-WE coverage) |
| S5 exit | D-22, D-23, D-24, D-25 · DL-05 (gate-linkage half) · L-05 | S5-X1 (`gate_coverage`), S5-X2 (`checkable_rate`), S5-X3 (ASSERT citations, R-FR boxes), S5-X5 (public-surface-only) |
| S6 lint | D-07, D-09, D-12, D-14, D-21, D-28, D-29 · L-08 (the activity-3 rationale sweep) — **plus a re-run of every D/DL check over the compiled `dist/spec.md`** | S6-X1 (`lint_errors = 0`), S6-X3 (derived views), S6-X5 (annex force); tags survive compilation (artifact-model §6.2), so the re-run certifies the exact text builders will see |
| S7 rounds | L-02, L-03, L-06, L-09 · M-01 on freeze-candidate rounds (M-02 optional, budget permitting) · H-01 at the round's owner review | S7 grading and divergence analysis; freeze evidence beyond `pass_rate` (a gate that mutants walk through makes `pass_rate = 1.0` vacuous) |
| Standalone grading (external or gold spec) | full suite via the §4 untagged extraction path | README §4.3's readiness gate, executed |

Two standing rules. **(1) Producing-stage-first:** each D/DL check first runs at the
exit of the stage that produces its inputs (so failures are Q records while the artifact
is still DRAFT — cheapest possible routing), then re-runs at every S6 compile.
**(2) Scoped re-runs:** on a routed re-entry (process §8.2), only the checks whose
inputs include a touched element re-run, mirroring the stage cards' scoped
re-verification.

## 8. Coverage table: README §3 → checks

Item IDs as printed in README §3 (§3.1). Every item maps to ≥1 check; every
check appears in this table (bidirectional totality — the task's no-orphan rule).
Bold check = the item's primary hardening; others corroborate.

| Item | Requirement (abbreviated) | Checks | Tier |
|---|---|---|---|
| A.1 | DoD exists, "done when every box checked" framing | **D-22**, M-01, M-02 | D, L+D |
| A.2 | Every DoD item mechanically checkable | **L-05**, D-23, M-01 | L, D, L+D |
| A.3 | Executable smoke test, ASSERTs + expected values | **D-24**, L-03, L-05, M-02 | D, L, L+D |
| A.4 | Parity matrix for cross-cutting variation | **D-25**, L-09, M-01 | D, L, L+D |
| A.5 | Optional features tagged core vs. extension | **D-25**, M-01 | D, L+D |
| B.1 | Core loops as step-ordered pseudocode | **D-11**, D-06, L-03 | D, L |
| B.2 | State machines with complete transition tables | **D-02**, D-01 | D+L |
| B.3 | Precedence rules total with tie-breaks | **DL-01**, L-03 | D+L, L |
| B.4 | Numeric behavior as exact formulas | **DL-02**, L-03 | D+L, L |
| B.5 | Ordering guarantees and idempotency stated | **DL-03**, L-02 | D+L, L |
| B.6 | Concurrency: guarantee AND mechanisms, cancellation, result order | **DL-04**, L-02, L-07 | D+L, L |
| B.7 | Invariants stated explicitly | **DL-05**, M-01 | D+L, L+D |
| C.1 | Typed field lists, language-neutral, legend | **D-16** | D |
| C.2 | Enums enumerate all values with semantics | **D-01** | D+L |
| C.3 | Field constraints inline with the field | **DL-06**, D-16, L-01 | D+L, D, L |
| C.4 | Every normative term has one authoritative definition | **D-09** | D+L |
| D.1 | Interfaces: exact names, typed params, returns | **D-17**, L-07 | D, L |
| D.2 | Tool/endpoint parameters/returns/errors blocks | **D-18** | D+L |
| D.3 | Wire surfaces: routes, methods, statuses, bodies | **D-19** | D+L |
| E.1 | Every knob defaulted at point of definition | **D-05** | D+L |
| E.2 | Contextual defaults state resolution chains | **DL-01** | D+L |
| E.3 | Open defaults marked implementation-defined + doc duty | **D-20**, L-09 | D, L |
| E.4 | Consolidated config cheat-sheet | **D-21** | D |
| F.1 | Named error taxonomy | **D-03**, D-18 | D+L |
| F.2 | Retryable vs. terminal per class, in a table | **D-04** | D+L |
| F.3 | Blast radius per failure | **D-04**, D-03, L-02 | D+L, L |
| F.4 | Boundary cases with pathological input or explicit N/A | **DL-07**, L-01 | D+L, L |
| F.5 | Timeouts scoped, defaults, kill sequences | **DL-08** | D+L |
| G.1 | Goals as named principles | **D-15**, L-04, H-01 | D, L, H |
| G.2 | Dedicated non-goals section | **D-15**, L-04 | D, L |
| G.3 | Exclusions name extension points | **D-15** | D |
| G.4 | Boundary notes where ignorant readers diverge | **L-02**, L-04 | L |
| H.1 | Every "up to you" explicit and bounded | **D-10**, D-11, D-12, D-20, L-07, L-09 | D, L |
| H.2 | External docs named, scoped, conflict-ruled | **D-13** | D |
| H.3 | Reference implementations inspiration-only | **D-14** | D |
| I.1 | Worked I/O pairs per format surface | **D-26** | D |
| I.2 | Complete realistic copy-pasteable sample input | **D-26**, D-27 | D |
| I.3 | Linked ToC | **D-28** | D |
| I.4 | Rationale quarantined in appendix | **D-29**, L-08 | D, L |
| I.5 | Redundancy by derivation (witnesses, derived views) | **D-11**, D-21, L-03, L-06 | D, L |
| I.6 | Types precede behavior; conformance last | **D-28** | D |
| J.1 | Every pseudocode helper defined | **D-06**, D-09 | D+L |
| J.2 | Every prose config field exists in schema | **D-07**, D-09 | D+L |
| J.3 | Every algorithm-read field exists on its record | **D-08**, D-09 | D+L |
| J.4 | No conflicting statements; gate/annex never beat body | **L-06**, L-02, L-03 | L |
| J.5 | Hedge words fixed or converted to freedom | **D-12** | D |

Cross-cutting note: **L-01** (question-count probe) is listed only where it is a
primary instrument (C.3, F.4), but it backstops *every* section — any hardening gap in
any item surfaces as implementer questions, which is why the process runs it to dryness
before anything freezes. Tier column reads "D+L" where the §4 acquisition rule makes
the check pure-D on tagged specs and hybrid on untagged ones.

## 9. The calibration hook

Checks must predict one-shot build success or they are ritual. README §4.2's ablation
protocol is the experiment; this is the plumbing that connects it to the suite:

1. **Calibration ledger.** `hardening/calibration.md` (created by follow-on task FT-6):
   one row per graded spec instance — a process run at a version, an ablation variant,
   or a gold spec — recording every check metric value at grading time plus the build
   outcomes for that instance (process §9.2's `pass_rate`, `div_defects`, `bd_by_class`,
   `inventions`), k ≥ 5 builds per instance per README §4.2.
2. **Signal.** Per metric: outcome separation — mean `pass_rate` (and BD counts) across
   instances where the metric passes vs. fails its threshold. With the small n this
   project will have, report separation with the raw rows; do not dress it as
   significance.
3. **Weight classes.** Every §3 item carries a weight: **W0 blocking** (a FAIL blocks
   dispatch/freeze), **W1 default** (FAIL routes a defect but an owner may waive with a
   ledger entry), **W2 advisory** (finding only). Initial assignment per README §4.3:
   sections A–C start W0; D–J start W1; nothing starts W2.
4. **Re-weighting rule.** After `N_cal = 5` graded instances touch a metric: an item
   whose checks' failures show no outcome separation is **demoted one class**; a W1/W2
   item with strong separation is promoted one. Demotions and promotions each cite
   their ledger rows, and are recorded as edits to §8's table (add a weight column at
   first re-weighting). Items are never deleted — down-weighting, not deletion, is the
   anti-ritual mechanism, because checklist rot accumulates by addition.
5. **Cheap proxy first.** Before spending build tokens on a new ablation axis, run
   L-01 (question-count) across the variants; if it does not separate them, the builds
   probably won't either (README §4.2's own gate).

## 10. Follow-on implementation tasks

Session-sized, independently pick-up-able (same contract as `../tasks/`). Specifying
was this task; *implementing* is these. Each loads this README + the named checks.md
sections as context.

**FT-1 — Implement the Tier-D lint suite (tagged path).** A CLI that takes a process
workspace (or `dist/spec.md`) authored with artifact-model §5 tags and runs every `D-*`
check, emitting §3.2 standard records (JSON lines) plus a human summary. Context:
checks.md §1; artifact-model §5's grep surface. Acceptance: zero false fires on a
small synthetic clean fixture (build one — it becomes the suite's own regression
anchor); every seeded violation in a deliberately-broken twin fixture fires exactly the
predicted check.

**FT-2 — Build the ephemeral-probe runner.** Charter compiler (packages a context
slice into a fresh session with nothing else), pinned-template store, output-schema
validation with one re-prompt, k-dispatch, aggregation (union/majority/exact-match),
agreement-floor and stability-gate arithmetic, verbatim archival under `probes/`.
Context: §5 here; checks.md §3 (L-check blocks). Acceptance: L-01 and L-04 run
end-to-end against `08-browser-history.md`-derived fixtures with k=3 and produce valid
standard records.

**FT-3 — Implement the untagged extraction path.** The EXT-1…EXT-6 extraction
templates (checks.md §2.1), canonicalization + `S_extract` stability gate, and the
inventory JSON schemas, wired so every D/DL check runs against an untagged single-file
spec. Context: §4 here. Acceptance: run the D/DL family against symphony's SPEC.md;
RD-11…RD-14 fire as checks.md §R predicts.

**FT-4 — Run the regression suite against all four gold specs.** Execute the full
suite (extraction path + L probes at k=3) against attractor, coding-agent-loop,
unified-llm, symphony; produce a firing report diffed against checks.md §R's expected
firings. Every miss is a suite defect: fix the check (keep its ID), rerun, and record
the revision. Acceptance: all RD rows fire; RX rows reported (informative).

**FT-5 — Run the mutation study (cheap variant) against attractor.** Generate the
M-01 mutant set (≥2 per taxonomy class) over attractor's behavior descriptions, grade
each against attractor's own §11 gate per M-01's procedure, report kill rate and every
surviving mutant as a named gate hole. Optional stretch: M-02 full variant against one
attractor OSS implementation (e.g. attractor-c), executing §11.13 for real. Context:
checks.md §4. Acceptance: kill-rate report + survivor list with evidence pointers.

**FT-6 — Stand up the calibration ledger and first ablation wiring.** Create
`hardening/calibration.md` (schema per §9.1), script the README §4.2 ablation variants
for one small target, run the L-01 proxy across variants, then k ≥ 5 one-shot builds on
the variants the proxy separates, grade with FT-1/FT-3 tooling, and produce the first
re-weighting memo per §9.4. Context: §9 here; README §4.2. Acceptance: ledger populated
with ≥ 2 instances; memo states keep/demote per touched item with ledger citations.

## Appendix: suggested §3 amendments

Task-03 could not change §3 wording; hardening surfaced items that were untestable as
written and proposed the rewordings below. **All seven were applied by task-04
(2026-07-05)** — A-1 printed the IDs in §3, A-2 added C.4, A-3 split I.6 out of I.3,
and A-4…A-7 landed as rewordings (dispositions in
[../tasks/task-04-refactor.md](../tasks/task-04-refactor.md)). Kept as the rationale
record:

- **A-1 — Add stable item IDs to §3.** The bullets were unnumbered; this suite's
  coverage table originally pinned IDs positionally. Printing `A.1`…`J.5` in §3 itself
  makes the mapping robust to future edits.
- **A-2 — Add a glossary item (new C.4).** "Every normative term has exactly one
  authoritative definition (A-GL or C-DM)." §3 has no glossary item, yet A-GL absence
  enabled two audited defects (artifact-model §11 finding 7: unified-llm's undefined
  "stable conversation prefix," attractor's stage/node synonymy). Currently reached
  only indirectly via D-09's term closure.
- **A-3 — Split I.3.** It bundles three independently checkable clauses (linked ToC /
  types-before-behavior / conformance-last); a spec can pass two and fail one.
- **A-4 — Scope J.4.** "No internal contradictions" is undecidable as written. Propose:
  "no two normative statements about the same element assign it conflicting values, and
  neither gate nor annex ever contradicts the body (T4)" — the decidable core, with
  L-02/L-03/L-06 as the empirical residue detectors.
- **A-5 — De-hedge F.4.** "…ideally with the motivating pathological input" makes the
  item non-binary. Propose requiring the pathological input or an explicit N/A per
  boundary case (DL-07's cell semantics).
- **A-6 — Make I.5 measurable.** "Critical rules stated redundantly" leaves "critical"
  to taste. Propose: "every C-BC rule has an R-RA witness, and every consolidated view
  is derived, never hand-maintained" — which is what D-11/D-21 actually decide, and
  matches artifact-model §6.3.
- **A-7 — Make G.4 reader-relative.** "Known scope-confusion risks" is author-relative
  (the author's blind spots are exactly the risk). Propose: "scope questions on which
  independent ignorant readers diverge carry boundary notes" — L-02/L-04's measurement,
  process P4's rationale.

