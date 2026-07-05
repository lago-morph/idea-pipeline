# ADR: Closure checks consume typed inventories with a stability-gated extraction fallback

- **ID**: ADR-32ccba2b09
- **Status**: Draft (not yet adopted to docs/adr/)
- **Date**: 2026-07-05
- **Source retrospective**: ../2026-07-05-31.md
- **PRs covered**: #30

## Context

The hardening suite's closure checks compute cross-products (states × events, operations × failure classes, constructs × concurrency cells). The arithmetic is trivially deterministic; the hard part is producing the list it runs over. Two spec populations must be served by the same checks: process-authored specs carrying the artifact-model §5 tag grammar (where the inventory is a grep), and untagged specs — the four gold specs that form the regression corpus, plus any external spec being graded. Without a fixed acquisition rule, every check would need two definitions, and the LLM-extraction path would smuggle model judgment into nominally deterministic verdicts.

## Decision

Every closure/cross-product check computes its deterministic verdict over a schema-typed JSON inventory that is grep-extracted on tag-bearing specs and LLM-extracted at k=3 with a 0.90 pairwise-agreement stability gate on untagged specs; sub-threshold agreement returns INDETERMINATE as a spec-clarity finding rather than a silent average.

The inventory schema (EXT-1…EXT-6 in `hardening/checks.md` §2.1) is the stable interface: the check never knows which path produced its input. On the L path, the k extractions are canonicalized and diffed; verification proceeds on the intersection with union-minus-intersection attached as disputed-territory evidence.

## Alternatives considered

- **Single LLM extraction (k=1) on untagged specs** — rejected: one reader's blind spots become silent inventory holes, and the closure ratio computed over a wrong denominator reports false confidence with no signal that it did.
- **Majority-vote merge instead of intersection + gate** — rejected: voting hides the disagreement, and the disagreement is itself the finding — if three careful readers cannot agree what the enum list *is*, the spec has a defect no closure arithmetic can reach (the design turns extraction instability into a first-class INDETERMINATE verdict).
- **Two check definitions per property (tagged vs. untagged)** — rejected: doubles the suite's maintenance surface and lets the two definitions drift; the inventory interface keeps one definition per property with the acquisition rule factored out once (hardening README §4).

## Consequences

Easier: the whole D/DL family runs against gold specs (enabling the §R regression suite and FT-3/FT-4 tooling) and runs as a pure CI lint on process-authored specs; extraction quality is measured, not assumed. Harder: untagged grading costs k=3 cheap sessions per inventory, and INDETERMINATE verdicts create triage work — accepted, because the alternative is unmeasured false confidence. The 0.90 `S_extract` constant is stated once in the hardening constants table and is tunable with evidence, per the repo's stated-numbers principle (process.md P6).

## References

- [`../2026-07-05-31.md`](../2026-07-05-31.md) — the source retrospective.
- `spec-completeness/hardening/README.md` §4 (inventory acquisition rule, stability gate) and §6 (`k_extract`, `S_extract`).
- `spec-completeness/hardening/checks.md` §2.1 (EXT-1…EXT-6 schemas and the shared extraction template).
- [`./SKILL-SPEC-69b6babeec-doc-suite-consistency-check.md`](./SKILL-SPEC-69b6babeec-doc-suite-consistency-check.md) — the same parse-then-diff instinct applied to this repo's own documents.
- PR the decision was made in: #30.
