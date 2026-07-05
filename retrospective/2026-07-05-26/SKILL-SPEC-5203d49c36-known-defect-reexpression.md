# Spec: `known-defect-reexpression`

- **ID**: SKILL-SPEC-5203d49c36
- **Source retrospective**: ../2026-07-05-26.md

## Intent

Acceptance-test a model, rubric, checklist, or checker suite by re-expressing every *independently audited* defect in its terms. If a known defect cannot be expressed as a violation the model would flag, the model has a hole — fix the model, not the defect list. In the source session this was the task's own acceptance test for a spec artifact model: 14 defects from four prior ambiguity audits all had to land as "missing artifact", "thin artifact", or "traceability-rule violation". Running the test did two things the session could not have gotten otherwise: it forced two rule generalizations (gate-vs-body conflicts were invisible to the hypothesized rules — an analyst flagged "MODEL HOLE" on attractor's DoD requiring HTTP endpoints its own §9.5 contradicts), and it surfaced 11 *new* defects beyond the audits, which became a ready-made regression corpus for the downstream checker task.

## Trigger

- Direct: "validate the model against the known defects", "would this
  checklist have caught X?", "prove the rubric has no holes".
- Proactive: whenever building or revising any quality gate (lint rules,
  review checklist, taxonomy, schema validator) for a domain where prior
  audits, postmortems, or bug lists exist.
- Negative: no independent defect inventory exists (build one first — the
  test is only as strong as the audit's independence from the model).

## Inputs

- The model under test: categories plus its violation vocabulary (e.g.
  missing artifact / thin artifact / rule T1–T7 violation).
- The defect inventory: independently produced, with evidence anchors
  (line numbers, repro steps). Independence matters — defects derived
  *from* the model cannot test it.
- The corpus the defects live in, locally available.

## Outputs

- A defect table: one row per audited defect — evidence anchor, the model
  expression (which category/rule fires and why), and a violation class.
- A loud list of inexpressible defects (ideally empty after iteration),
  each paired with the model amendment that fixed it.
- A "beyond the audits" list: new defects the classification pass
  surfaced, kept as a regression corpus for future checkers.

## Workflow

1. Freeze the defect inventory before touching the model (no editing
   defects to fit). Confirm each defect at current evidence anchors —
   corpora drift.
2. For each defect, attempt the expression: name the exact category or
   rule that fires, and state the mechanism ("`execute_subgraph` is a
   single-occurrence undefined helper → reference-closure rule"). "The
   model disapproves of this" is not an expression; a specific check must
   fire.
3. Where nothing fires, record a hole verbatim — do not soften. Decide:
   generalize an existing rule (preferred) or add one. In the source
   session, gate-layer contradictions forced generalizing the precedence
   rule to "any two artifacts" with the clause "the gate never creates
   obligations", rather than adding a bespoke gate rule.
4. Distinguish **defect** from **discipline**: some audited items turn out
   to be conforming behavior under the model. Symphony's delegated enums
   were declared with a discovery procedure and documentation obligations
   — the model expresses the *residual* problem (a too-wide freedom), not
   the delegation itself. Mislabeling disciplined practice as violation
   makes the model cry wolf.
5. Re-run the full table after any model amendment (amendments can orphan
   earlier expressions).
6. Harvest the by-catch: classification at this rigor finds defects the
   audits missed. Record each with anchors and the rule that catches it.
   These are the future checker's regression tests.

## Concrete examples

### Example 1: Expressible, multi-rule (symphony's "configured assignee")

Audited defect: symphony's eligibility rule references "the configured
assignee" (line 729–30), a config field defined nowhere (absent from the
§5.3 schema and §6.4 cheat sheet). Expression: reference-closure violation
(a contract term resolving to no domain field or default) + contract-
closure violation (no realization or registered freedom) + gate-coverage
violation (no test bullet covers assignee routing). Three independent
rules fire — the model sees it redundantly, which is the desired failure
mode.

### Example 2: Hole → amendment (attractor's gate-vs-body drift)

Audited-adjacent finding: attractor's DoD line 1894 requires `POST /run`,
`GET /status`, `POST /answer`; its §9.5 table defines only `/pipelines…`
routes. The hypothesized rules governed only contract↔realization
citations — nothing fired on a gate-vs-body conflict. Recorded as MODEL
HOLE; fixed by generalizing the precedence rule (T4: any cross-artifact
contradiction is a defect; the gate checks obligations, never creates
them) and adding gate cite-and-agree discipline (T5). The re-run then
expressed this and five sibling gate-drift defects across two other specs.

## Anti-patterns

- **Relabeling without mechanism** — writing "defect 7 → rule T5" when no
  concrete check keyed on the evidence would actually fire.
- **Editing the defect inventory to fit the model**. The inventory is
  frozen; only the model moves.
- **Treating disciplined delegation as violation**. Symphony's
  `Implementation-defined` entries are the model's own prescribed pattern;
  only the residual width is a defect.
- **Stopping at the audited set**. The beyond-audit findings were the
  source session's highest-leverage output (11 new defects, 6 of them a
  defect *class* the audits systematically missed).
- **Running the test once and not re-running after amendments**.

## Acceptance criteria

- [ ] Every audited defect has a row with an evidence anchor and a named
      category/rule that fires by a stated mechanism.
- [ ] Zero unexpressed defects remain, or each remaining one has an
      explicit open-hole entry.
- [ ] Every model amendment made during the test names the defect that
      forced it.
- [ ] The beyond-audit list exists (even if empty) and each entry has
      anchors.
- [ ] Conforming-by-design cases are explicitly marked as such, not
      counted as violations.

## Files this skill creates / modifies

- The model document's validation section (defect table + beyond-audit
  list) — in the source session, `spec-completeness/artifact-model.md` §9.
- Optionally a standalone regression-corpus file when a downstream checker
  task will consume it.
