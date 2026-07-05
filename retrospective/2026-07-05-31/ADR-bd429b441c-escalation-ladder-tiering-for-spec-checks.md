# ADR: Spec checks are tiered by an escalation ladder with a refutable why-not-lower audit

- **ID**: ADR-bd429b441c
- **Status**: Draft (not yet adopted to docs/adr/)
- **Date**: 2026-07-05
- **Source retrospective**: ../2026-07-05-31.md
- **PRs covered**: #30, #31

## Context

Task-03 rebuilt the 46-item spec-completeness checklist as 49 executable checks (`spec-completeness/hardening/`). The immediate design risk was the opposite of Goodharting: reaching for LLM judgment on properties that a regex over the artifact-model tag grammar can decide. An LLM check costs more per run, is non-deterministic across runs, and cannot certify anything in CI; a checklist whose items quietly assume model judgment is a checklist that never actually runs. The task defined the tier preference; the binding decision made in PR #30 was how to make that preference *enforceable* rather than aspirational — and how far down to push the human tier (the final suite has exactly one Tier-H check, H-01 owner behavior acceptance, because intent is the only property no artifact encodes).

## Decision

Every hardened check is implemented at the lowest tier that can decide it — deterministic (D) before extraction-hybrid (D+L) before LLM probe (L) before mutation (L+D) before human (H) — and every non-deterministic check carries a one-sentence 'why not lower' claim that, when refuted, demotes the check while keeping its ID.

Mechanically: tier-prefixed stable IDs (`D-`, `DL-`, `L-`, `M-`, `H-`); a `Why not lower:` field required on every non-D check block; a write-D-first authoring discipline (escalate only the judgment-shaped residue, which is usually the extraction, not the verdict); and automatic downward mobility — a `DL-` check runs as pure D on tag-bearing specs without redefinition.

## Alternatives considered

- **Judgment-first ("an LLM reads the spec and scores each item")** — rejected: non-reproducible, uncalibratable, and exactly the Goodhart-able existence-checking the task exists to eliminate; it also makes CI certification impossible.
- **Two flat tiers (automated / manual) with no ladder rule** — rejected: without the demotion mechanism, checks specified at too high a tier accumulate permanently; the audit sentence makes each tier assignment a falsifiable claim someone can attack with a counter-procedure.
- **No human tier at all** — rejected: "passes all gates but isn't what the owner wants" is real (process.md §8.3's INTENT_GAP + GATE_GAP pair) and no artifact encodes unstated intent; capping the ladder with exactly one H check acknowledges the limit instead of hiding it inside an L probe that would grade the spec against itself.

## Consequences

Easier: CI-grade certification of tagged specs (the whole D/DL family is greppable); arguing about tier assignments (refute the sentence, demote the check); keeping the suite honest as tooling improves (checks migrate down, never up, without ID churn). Harder: authoring — each check costs a tier argument, and hybrid checks need an inventory schema; the suite accepts that cost as the price of the escalation-ladder rule stated in the task ("a check that could be deterministic but is specified as an LLM judgment is a defect in this deliverable"). Accepted trade-off: some D procedures are conservative (lexical screens like D-23) and rely on a paired L check for the semantic residue, so a few properties are covered by two checks instead of one.

## References

- [`../2026-07-05-31.md`](../2026-07-05-31.md) — the source retrospective.
- `spec-completeness/hardening/README.md` §1 (tiers and the escalation ladder) and §8 (coverage table) — the decision as shipped.
- `spec-completeness/hardening/checks.md` — the 49 check blocks carrying the `Why not lower:` audit fields.
- PRs the decision was made in: #30 (defined), #31 (reconciled into companions).
