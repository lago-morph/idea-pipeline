# Maturity ladder

Status: draft, 2026-09-05. Structure 2 of the spine.

## What the ladder is

Six ordered levels, Sketch to Enterprise. A level says how far along a system is, not what it is; what it is lives in `system-profile.md`. Each level has entry criteria and a set of concerns that become required. Entry criteria are checkable facts about artifacts and the running system, never activities. "Persistence records ratified and data survives reopen" is a criterion. "Persistence designed" is not.

The gap between the level a system has and the level its owner targets is the work list. That is the ladder's whole purpose.

## The levels

| Level | Meaning | Entry criteria | Concerns that become required |
|---|---|---|---|
| Sketch | The system exists as artifacts and nothing runs | A vision exists. At least one use case exists. The profile is set. No runnable is claimed | documentation |
| Prototype | A runnable produced from the artifacts exists and the owner can use it | An implementation record exists for the runnable. Acceptance criteria, test method, test data, and automated checks exist and the checks pass. The run's ambiguity list is harvested. The runnable is on the owner's device | runtime environment; lifecycle at the level of how it is run and delivered; testing |
| Durable | State survives closing and reopening, and the owner can get the data out | Persistence records ratified: mechanism, on-disk format and its version, size limits, export path. Closing and reopening loses nothing, checked by an automated check. Data written by implementation N is read by implementation N+1, or the record says why not. External dependencies version pinned | persistence; configuration; external dependencies; concurrency and failure at the level of save failure |
| Shared | More than one user, device, or host depends on the same system | Identity and access records ratified for every interface. Communication records ratified per interface: transport, serialization, error codes, retry, timeout. Concurrency semantics stated per interface. Install on a second host or for a second user follows a written procedure. Releases are numbered | identity and access; communication; concurrency and failure; security at the boundary |
| Operated | The system runs continuously and someone is responsible for it | Observability records ratified: metrics, log aggregation, alarming, and each has a running instance. Backup and restore exercised at least once with evidence. Configuration held under management with changes traced. A release and deployment procedure with rollback, exercised. A troubleshooting and remediation procedure exists. End-user management has a ratified record | observability; lifecycle across install, update, and release; configuration management; security monitoring |
| Enterprise | Many teams and regulated or internal data; most answers are inherited from above the system | A level above the system exists, organization standard or platform, and records inherit from it with binding level stated. Audit log management, HA and DR with tested failover, SLA and SLO recorded and reported, and security incident management each have a ratified record and a running instance | every concern, with inheritance; whatever a standard mandates be documented |

The names are the levels. "Prototype" here is the ladder's word; agent-method avoids it outside descriptive prose and says implementation, which is unchanged.

## Criteria matrix

Rows are concerns. Cells say what must exist at that level for that concern, in a few words. A cell is cumulative with the cells to its left. "n/a" means the concern asks nothing new at that level.

| Concern | Sketch | Prototype | Durable | Shared | Operated | Enterprise |
|---|---|---|---|---|---|---|
| Persistence | n/a | memory only allowed, stated | mechanism, format version, export | shared store, ownership per component | backup and restore exercised | retention, HA and DR |
| Identity and access | n/a | n/a | n/a | mechanism, user model, per interface | end-user management | provider inherited, access audited |
| Observability | n/a | errors visible to owner | diagnostics retrievable after failure | logs per component, correlated | metrics, aggregation, alarming | SLO reporting, audit logs managed |
| Concurrency and failure | n/a | single flow, stated | save failure semantics, recovery on reopen | semantics per interface, retry, timeout | restart and retry policy, remediation procedure | failover tested |
| Configuration | n/a | none or in the file, stated | storage location, defaults recorded | per environment, secrets separated | under management, changes traced | tooling inherited |
| External dependencies | listed in vision | none or listed | version pinned | interfaces and data models specified | upgrade path, monitored | approved list inherited (to confirm) |
| Security | n/a | n/a | data at rest on owner device, stated | transport security, validation at interfaces | security monitoring, incident procedure | regulated controls, audited |
| Lifecycle | n/a | how it is run and delivered | update without data loss, carry data forward | install for second host or user, numbered releases | CI and CD, deployment with rollback | change management inherited, cross-team release |
| Runtime environment | n/a | one, named | storage on it identified | per host or service, environments named | provisioned reproducibly, platform services named | platform inherited |
| Communication | n/a | n/a, in process | n/a unless the store is remote | transport, SerDes, error codes per interface | timeouts and retries observed | protocols inherited |
| Testing | scenarios with test data drafted | acceptance criteria, test method, checks, test data | reopen check, migration check | integration tests, concurrency tests | checks run in CI, environment parity | quality standards inherited, compliance evidence |
| Documentation | vision, use cases | implementation record, decisions notes, ambiguity list | storage format, export documented | interface contracts with examples, install procedure | runbooks, troubleshooting | what a standard mandates |

The Sketch to Durable columns are validated against the workbench. The Shared to Enterprise columns are seeded from the DevOps and Ops sections of the brainstorming notes and are not yet validated against any system (to confirm).

## How profile and maturity combine

The profile caps the ladder. Some values make a level unreachable: a system with concurrent users one and deployment topology single device has no Shared, because Shared means more than one user, device, or host. A system with availability target best effort has no Operated. The cap is not a judgment; it follows from the values.

The profile skips rungs. When every concern a level requires is not applicable by profile, the level's records are all not-applicable with reason, and the level is claimed with no work. A stateless system passes through Durable this way. A system born with many users and continuous availability will find Durable collapses into Shared and Shared into Operated, and its work list starts at the higher level.

The required artifact set is a function of three things: the profile, the target maturity, and the current maturity. The profile says which registry entries apply at all. The target says which levels' concerns are required. The current level says which of those already have ratified records. The difference is the gap, and the gap is the work list: registry entries that need instances, questions that need records, checks that need to pass.

### The workbench as the worked example

Current level: Prototype (to confirm). Implementations 1 and 2 were delivered from the artifacts with acceptance criteria, test method, test data, and automated checks, and their decisions made while building are recorded in per-area decisions notes. Whether every record made while building has been ratified is not established here, and the level is claimed only when it is. Implementation 3's run and its ambiguity list are not yet recorded in the copy read.

Cap from the profile: Durable. Concurrent users one and deployment topology single device rule out Shared, and best effort rules out Operated. Durable is therefore also the plausible target, and it is what the vision's success criterion 3 describes.

The gap from Prototype to Durable is the following, with each item traced to a source.

| Gap item | Source |
|---|---|
| Persistent storage guide written and its decisions note ratified: what survives clearing browser data, on-disk format and its versioning, size limits, where durable storage concretely is, how the user gets the data out | decision-guides.md, guides to write; vision open issue on durable storage |
| Data model and identity guide and decisions note: identity preserved across saves and implementations | decision-guides.md, candidate ADRs from implementation 1 |
| Carrying data between implementations decided: whether implementation N+1 must read implementation N's data | decision-guides.md, guides to write |
| Delivery to the device decided as a durable route, not the working-session attachment | implementation record 3, build and installation method |
| An automated check that closing and reopening loses nothing, plus the restored UI state the vision names | vision success criterion 3; test-method-definition.md |
| Save failure semantics recorded: what the user sees when a save fails | concurrency and failure at Durable |
| External dependencies stated as none and pinned if that changes | implementation record 3 |
| Logging and diagnostics decided, since Durable requires diagnostics retrievable after a failure | decision-guides.md, guides to write |

Every gap item is either a guide agent-method already lists as "to write when the first implementation that needs them is being planned" or a check the vision already implies. That is the expected result: the ladder makes the existing rule computable and adds nothing to it.

## Rules

- A level is claimed per system, not per artifact and not per component. A component can be ahead of the system's level; the system is at the lowest level all its required records support.
- A level is claimed only when every decision record it requires is ratified. Undecided, unratified, or agent-made-while-building records for a required question block the claim. Not-applicable with reason counts as satisfied when the reason is a profile value.
- The claim is itself a decision record with the system as subject, owner-stated, and it carries the evidence: which checks passed, on which implementation.
- Regression is possible and is recorded. A ratified record that is superseded, a check that stops passing, or a profile revision that flips records to undecided can drop the level. The drop is a superseding claim record with the prior claim in its history field. The level is never silently kept.
- The target is set by the owner and revised deliberately, as the profile is.

## Open questions

- Whether Shared conflates two steps, a second device for the same user and a second user, and whether the profile resolves that without a seventh level.
- Whether the Prototype entry criteria should require the ambiguity list be harvested, or only recorded. Requiring harvest ties the claim to the harvest loop, which may be right.
- Whether the matrix's Shared to Enterprise cells belong here or in the registry entries' applicability rules, with the matrix generated from them. Generating it would keep one source of truth.
- Whether current level should be recorded in the implementation record, which already lists what each implementation covers, or in its own claim record as proposed above.
