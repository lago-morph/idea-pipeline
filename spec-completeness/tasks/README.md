# Spec-Completeness Work Queue

Session-sized task definitions extending the issue
[#22](https://github.com/lago-morph/idea-pipeline/issues/22) analysis
([../README.md](../README.md)). Each file is a self-contained prompt: a fresh
session should be able to read one task file (plus the context it lists) and
produce good work.

| Task | Deliverable | Depends on |
|---|---|---|
| [task-01-artifact-model.md](task-01-artifact-model.md) | `artifact-model.md` — RUP-like artifact decomposition of a one-shot spec, with WHAT/HOW layering, dependency graph, traceability rules, and validation by decomposing the four gold specs | — |
| [task-02-idea-to-spec-process.md](task-02-idea-to-spec-process.md) | `process.md` — explicit staged process from idea to checklist-passing spec, with roles, question-queue schemas, stage entry/exit criteria, defect routing, and a pressure-test protocol | task-01 |
| [task-03-hardened-checks.md](task-03-hardened-checks.md) | `hardening/` — the §3 checklist rebuilt as executable (claim, probe, pass-criterion) checks, tiered deterministic → constrained-LLM → human | task-01 (soft) |

Recommended order: 01 → 02 → 03, but 02 and 03 can run in parallel after 01
merges — both carry provisional-vocabulary fallbacks if they must start
earlier. Each task commits to its own branch and opens its own PR.
