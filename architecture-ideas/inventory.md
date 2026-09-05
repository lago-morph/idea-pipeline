# Inventory

Status: draft, 2026-09-05. Everything needed for a complete draft of this work, with what exists and what is still to be created. Statuses: `draft` exists in this directory; `stub` exists as a row or sketch only; `to write`; `to instantiate` means it is created by filling in from the workbench, not by authoring.

## Spine definitions

| Item | File | Status | Depends on | Phase |
|---|---|---|---|---|
| Overview, relations, vocabulary | `spine/overview.md` | draft | | 0 |
| System profile | `spine/system-profile.md` | draft | overview | 1 |
| Maturity ladder and criteria matrix | `spine/maturity-ladder.md` | draft | profile | 1 |
| Subject catalog | `spine/subject-catalog.md` | draft | overview | 1 |
| Artifact type registry, entry schema, seed table | `spine/artifact-type-registry.md` | draft | subject catalog, profile, maturity | 1 |
| Decision record | `spine/decision-record.md` | draft | registry, subject catalog | 1 |
| Derivation graph | `spine/derivation-graph.md` | draft | decision record | 1 |
| Verification, three levels | `spine/verification.md` | draft | registry, derivation graph | 1 |
| Harvest loop | `spine/harvest-loop.md` | draft | decision record, verification | 1 |
| Modes of entry | `spine/modes.md` | draft | all six | 1 |

## Templates

One per structure, so instances have a fixed shape. Written after the definitions are marked up, so they encode the ratified fields.

| Item | File | Status | Phase |
|---|---|---|---|
| Profile template | `templates/system-profile.md` | to write | 1 |
| Maturity claim template | `templates/maturity-claim.md` | to write | 1 |
| Subject entry template | `templates/subject.md` | to write | 1 |
| Registry entry template | `templates/artifact-type.md` | to write | 1 |
| Decision record template, both candidate file shapes | `templates/decision-record.md` | to write | 2 |
| Derivation link conventions | in `spine/derivation-graph.md` | draft | 1 |

## Workbench instantiation (test bed)

| Item | File | Status | Phase |
|---|---|---|---|
| Workbench profile | `testbed/workbench/profile.md` | stub, in `spine/system-profile.md` | 2 |
| Workbench maturity claim and gap | `testbed/workbench/maturity.md` | stub, in `spine/maturity-ladder.md` | 2 |
| Workbench subject catalog | `testbed/workbench/subjects.md` | stub, in `spine/subject-catalog.md` | 2 |
| Decision records for implementations 1 to 3 | `testbed/workbench/records/` | to instantiate | 2 |
| Derivation links for implementation 2 | `testbed/workbench/derivation.md` | to instantiate | 2 |
| First metrics row | `testbed/workbench/metrics.md` | to instantiate | 2 |

## Registry entries written in full

The seed table lists every type. These are the entries written out with numbered questions, in the order agent-method will need them.

| Entry | Status | Trigger | Phase |
|---|---|---|---|
| Persistent storage | draft example, in `spine/artifact-type-registry.md` | Save ideas use case | 3 |
| Delivery to the device | to write | when delivery stops being manual | 3 or later |
| Data model and identity | to write | first data-model change across implementations | 3 or later |
| Logging and diagnostics | to write | first implementation with logging | 4 |
| Component contract, lifecycle and state machine | to write | component type written in agent-method | 4 |
| Interface contract, pre and postconditions, error semantics | to write | interface type written in agent-method | 4 |
| Code conventions | to write | second language or a shared library | later |
| Carrying data between implementations | to write | first persistent implementation superseded | later |
| Everything else in the seed table | stub rows | per applicability rule | as triggered |

## Procedures

In the shape of agent-method's `ai/procedures/`: observed in, what was done, what was not, pitfalls, notes for formalizing. Written retrospectively after each first run, never as a forward design step.

| Procedure | Status | Phase |
|---|---|---|
| Artifact review, level 1 checklist | to write after first run | 4 |
| Harvest a run into the four destinations | to write after first run | 4 |
| Ratification gate before next implementation | to write after first run | 4 |
| Regeneration metrics, extended table | to write after first run | 4 |
| Capture an existing system | to write after first run | 5 |
| Re-engineer from a revised record | to write after first run | 5 |
| Guided walk for greenfield, dependency order | to write after first run | 5 |

## Tables that must exist

| Table | Where | Status |
|---|---|---|
| Applicability matrix: artifact type by profile value and maturity level | derived from registry rows | stub, one column in the seed table |
| Criteria matrix: concern by maturity level | `spine/maturity-ladder.md` | draft |
| Concern list, ten concerns | `spine/overview.md` vocabulary | draft |
| Nuggets and their triggers | `README.md` | draft |
| Already in agent-method | `README.md` | draft |

## Working documents

| Item | File | Status |
|---|---|---|
| Objectives | `objectives.md` | draft, revised 2026-09-05 |
| Plan | `plan.md` | draft |
| Decisions log for this work | `decisions-log.md` | draft |
| Process-level discussion | `ideas.md` | draft, being decomposed |
| Nuggets for agent-method | `ideas/` | 14 files, draft |
| Brainstorming transcription | `reference/brainstorming.md` | done |

## Tooling, deliberately deferred

- Front matter and link validator for spine instances, extending agent-method's third link check. After phase 2.
- Applicability computation from profile and maturity. After phase 3, and only if computing by hand has been done at least twice.
- Concern view as a generated index. When guides pass about five.
