# Artifact type registry

Status: draft, 2026-09-05. Structure 4 of the spine.

## What a registry entry is

One entry per artifact type. An entry says which subjects the type attaches to, which refinement stage its questions answer, what it asks, when an instance is required, and how to author, relate, consume, verify, and review an instance. Agent-method holds the same thing as a guide note under the guide / decisions / standard pattern. A registry entry is a guide with its fields made explicit. Agent-method's existing guides already have the shape: what the artifact would be, rules for scoping, questions to walk through, guidance for the walkthrough.

### Entry fields

| Field | Values or form | Purpose |
|---|---|---|
| id | lowercase, hyphenated | Names the type. Agent-method: the `type` value, or the guide note's id |
| attaches to | one or more subject kinds: system, component, interface, data store, environment | Which catalog entries an instance can belong to |
| stage | logical, mechanism, infrastructure, operations | Which refinement stage the entry's questions answer |
| authoring guidance | prose | How to write an instance. Agent-method: "What the artifact would be" plus "Rules for scoping" |
| relating guidance | prose naming link types | Which artifacts must exist before this one, and which it must stay consistent with |
| consuming guidance | prose | What an implementer reads from an instance, in what order, and what an open answer licenses |
| verifying guidance | prose | How an implementation is checked against an instance; where the checks are specified |
| reviewing guidance | checklist | The definition of done for the instance itself, before anyone consumes it |
| questions | numbered list, fields below | What the type asks. Agent-method: "Questions to walk through" |
| applicability rule | profile values and a maturity level | When an instance is required for a subject. Outside the rule, every question is not applicable, and the rule is the reason |

### Question fields

| Field | Values or form | Purpose |
|---|---|---|
| number | integer, assigned at the end of the list, never renumbered | Records stay comparable across implementations |
| text | one question | What is asked. Behavior questions belong to use cases, never here |
| concern | persistence, identity and access, observability, concurrency and failure, configuration, external dependencies, security, lifecycle, runtime environment, communication | The audit view across subjects |
| binding time | design, build, deploy, runtime | Which artifact holds the answer: an ADR, the specification and decisions note, configuration, policy |
| option space | a list of options or example answers, with a default where one exists | What agent-method's guides put in brackets |
| verified by | automated check, review checklist item, or none | How compliance with the answer is checked. "None" means the question is reclassified as a standard or as walkthrough advice, and leaves the list |

## The seed registry

Source: existing means an agent-method type or guide; foreseen means one of the six guides decision-guides.md foresees; notes means the brainstorming notes. First required at is the maturity level at which a subject the rule applies to must have an instance, or an explicit not-applicable record. The maturity ladder is not yet written, so these values assume: M0 vision and use cases ratified; M1 an implementation runs and is checked; M2 data survives closing and a regeneration run passes; M3 delivered by a durable route and used daily; M4 operated or hosted by someone other than the owner; M5 more than one team or a production service (to confirm). Merged areas are named in the purpose column.

| id | attaches to | stage | source | first required at | purpose |
|---|---|---|---|---|---|
| vision | system | logical | existing | M0 | Why the system exists and what success is; the root artifact |
| ui-use-case | interface | logical | existing | M0 | The single home of the UI design for one kind of interface, per ADR 0006 |
| functional-use-case | system | logical | existing | M0 | UI-neutral behavior with corner cases and an Interface guidance section |
| component | component | logical | existing, no instance yet | M1 (to confirm) | What a component promises: responsibility, lifecycle states, contract per state, state machine with complete transitions, data ownership. Notes' component items merge here |
| interface | interface | logical | existing, no instance yet | M1 (to confirm) | Example input and output, preconditions, function, postconditions and error semantics, synchronous or asynchronous, typed structures, concurrency semantics, edge cases. Notes' interface items merge here |
| note | any | any | existing | never required | Free-form; the escape hatch. Becomes a type only when it recurs |
| implementation-record | system | mechanism | existing | M1 | One line per decision area for one implementation, linking to per-area notes |
| ui-decisions | interface | mechanism | existing | M1 | Appearance and interaction values for one implementation; guide is ui-standards-definition |
| implementation-structure | component | mechanism | existing | M1 | Model, identity, ordering, rendering, code shape for one implementation. Splits into code-conventions and data-model when those guides exist |
| test-method | environment | infrastructure (to confirm) | existing | M1 | How checks run: harness, engine, sizes, loading, output contract, what a person checks |
| acceptance-criteria | system | logical (to confirm) | existing | M1 | One row per use-case sentence or record decision: source, check, result per environment |
| test-data | system | logical (to confirm) | existing | M1 | The data sets and the walk-throughs that exercise corner cases. Notes' scenarios with test data merge here |
| automated-checks | system, interface | mechanism (to confirm) | existing | M1 | The specification a check script is regenerated from, including the hooks contract |
| quality-standards | system | infrastructure (to confirm) | existing | M1 | What is wanted of unit, type, static, integration, UI, and end-to-end checks; not how. Notes' coding, testing, and naming standards merge here |
| persistent-storage | data store | mechanism | foreseen | M2 | Where durable storage concretely is, format, limits, export. Worked entry below. Notes' persistence mechanism merges here |
| delivery-to-device | environment | infrastructure | foreseen | M1 | How the runnable reaches the device. Notes' install and update merge here |
| code-conventions | component | mechanism | foreseen | M2 (to confirm) | Language level, file structure, naming, traceability to use-case sentences, what a comment says |
| logging-diagnostics | component | mechanism | foreseen | M1 | What is logged, where, and how the owner reads it on the device. Notes' logging mechanism merges here |
| data-model | system, data store | logical | foreseen | M1 | What an idea is in memory and in storage, identity across saves, glossary. Notes' data model and glossary merge here |
| data-migration | data store | mechanism | foreseen | M2 | Whether implementation N+1 reads implementation N's data, and how |
| business-rules | component | logical | notes | M1 | Validation rules and algorithms in pseudocode with examples. The Edit ideas use case holds one inline today |
| error-taxonomy | system | logical | notes | M2 (to confirm) | Kinds of error, behavior for each, decision tables |
| external-dependencies | system, component | logical | notes | M1 | What outside the system is relied on, stated explicitly; "none" is an answer |
| not-specified | system, component | logical | notes | M1 | The deliberately open records for a subject, with bounds. May be a generated view over records rather than an authored artifact (to confirm) |
| non-functional-requirements | system | logical | notes | M2 (to confirm) | Properties the running system must satisfy and the supporting components that satisfy them. Overlaps the system profile (to confirm) |
| implementation-mechanism | component | mechanism | notes | M1 | Language, stack, and the runtime the component requires. Answered once for the whole system in the implementation record today |
| concurrency-mechanism | component, interface | mechanism | notes | M2 (to confirm) | Threads, workers, event loop, locking: the mechanism behind an interface's concurrency semantics |
| failure-restart-retry | component, interface | mechanism | notes | M2 (to confirm) | What happens on failure: restart, retry, timeout, give up. Notes' interface retry and timeout merge here |
| authn-z | component, interface | mechanism | notes | M4 (to confirm) | Authentication and authorization mechanism, and transport security. Notes' interface security merges here |
| transport-serdes | interface | mechanism | notes | M2 (to confirm) | Channel, protocol, serialization, error codes for an interface that crosses a process or network boundary |
| configuration-parameters | system, component | mechanism | notes | M2 (to confirm) | Which answers bind at deploy time, how they are supplied, their defaults |
| dependency-pinning | component | mechanism | notes | M1 | Versions of external dependencies pinned; their interfaces and data models specified |
| execution-environment | environment | infrastructure | notes | M1 | The host itself: device, browser, runtime, cluster, and any stand-in used for checks. Notes' digital twins merge here |
| observability-infrastructure | environment | infrastructure | notes | M4 (to confirm) | Metrics, log aggregation, traces, profiling tooling, for production and development alike |
| auth-tools | environment | infrastructure | notes | M4 (to confirm) | Identity provider and access tooling, including dev and test user management |
| persistence-infrastructure | data store, environment | infrastructure | notes | M2 (to confirm) | Disk, object store, browser origin: what the persistence mechanism runs on |
| platform-services | environment | infrastructure | notes | M4 (to confirm) | Database, message queue, and other services used but not owned |
| ci-cd | environment | infrastructure | notes | M3 (to confirm) | What runs on every change and before delivery, and where |
| release-management | system | infrastructure | notes | M3 (to confirm) | Numbering, packaging, where releases live, how one is chosen for deployment |
| source-control-and-tooling | environment | infrastructure | notes | M1 | Repository layout, branching, review; IDEs, issue tracking, docs, comms. Implementation standards decide the layout today |
| shared-libraries | component | infrastructure | notes | M4 (to confirm) | Code shared across components or systems, and who owns it |
| troubleshooting | system, component | operations | notes | M3 (to confirm) | How a problem is diagnosed and remedied by whoever operates the system |
| alarming | system | operations | notes | M4 (to confirm) | Which conditions raise an alarm, to whom, how |
| ha-dr-backup | data store | operations | notes | M2 (to confirm) | Backup and restore as soon as data persists; high availability and disaster recovery by profile |
| sla-slo | system | operations | notes | M4 (to confirm) | Service levels promised and the objectives measured against them |
| end-user-management | system | operations | notes | M4 (to confirm) | Onboarding, roles, and removal of end users |
| security-monitoring | system | operations | notes | M4 (to confirm) | Security monitoring and incident management |
| configuration-management | environment | operations | notes | M3 (to confirm) | How deploy-time and runtime values are set, tracked, and changed in a running environment |
| audit-log-management | data store, system | operations | notes | M4 (to confirm) | What is audited, retention, who may read the audit log |

## Worked entry: persistent storage

The next guide agent-method will need, first required by the Save ideas use case. Option space and questions come from the foreseen storage section of decision-guides.md.

| Field | Value |
|---|---|
| id | persistent-storage |
| attaches to | data store |
| stage | mechanism |
| applicability rule | profile statefulness is anything other than memory only, and maturity M2 or above (to confirm). Otherwise every question is not applicable with the profile value as the reason, which is what implementation records 1 to 3 say today |
| authoring | One decisions note per data store per implementation, linked to this guide. Values, not adjectives. Where the owner says "whatever is conventional", take the default and mark it as a default. The guide asks and lists; it never decides |
| relating | depends-on: data-model, and the use case that names durable storage. Must be consistent with: data-migration, test-data question 4 on where the set lives once the loader goes, delivery-to-device, and configuration-parameters for any deploy-time answer |
| consuming | Read questions 1, 3, and 5 before writing any storage code, and the rest before writing the checks. An answer that is deliberately open is license only within its stated bounds |
| verifying | Every question names its check. The implementation's automated-checks note gains one named check per question verified automatically; the review checklist gains one item per question verified by review |
| reviewing | Done when every question has a record with a status; no question is silent; every default is marked; the format in question 3 has a sample in the test data; an ADR exists if the answer to question 1 became a standard |

| # | Question | Concern | Binding time | Option space | Verified by |
|---|---|---|---|---|---|
| 1 | Where is the durable storage the Save ideas use case names? | persistence | build | browser storage: localStorage, IndexedDB, the origin-private file system; a file the user saves and reopens; the File System Access API; a remote store; a git repository. No default | automated check: after a change and a reload, the ideas are present, read from the named store |
| 2 | What survives clearing the browser's site data? | persistence | build | nothing; everything; only what was exported | automated check where the harness can clear site data; otherwise a review checklist item that the record states the consequence |
| 3 | What is the stored format, and how is it versioned? | persistence | build | JSON with a version field; one plain-text file per idea; a schema with numbered migrations. Default proposed with data-model | automated check: a saved sample parses under the stated format and carries the version |
| 4 | What are the size limits, and what happens at them? | concurrency and failure | build | the store's quota in bytes or items; at the limit: a message, refuse the change, degrade | automated check with a test data item sized past the limit (to confirm feasible); otherwise review checklist item |
| 5 | When is the store written? | persistence | build | on every change; debounced by a stated interval; on close; only on an explicit Save. Default: on every change, per the vision's automatic saving | automated check: change, reload with no explicit save, the change is present |
| 6 | What happens when a write fails? | concurrency and failure | build | a message in the message area and a retry; refuse further edits; silent | automated check where the harness can force a failure; otherwise review checklist item |
| 7 | How does the user get the data out? | persistence | build | an Export command producing text files; the store is already user-visible files; a git repository the user can clone | automated check where export is a command; review checklist item where the store is user-visible files |
| 8 | Where on the device or network does the store live, and is that chosen at deploy time? | runtime environment | deploy | fixed by the mechanism, such as the browser origin; a path chosen at install; a configured remote | review checklist item: the value appears in configuration-parameters, or the record says it is fixed |

Which earlier implementation's data this one must read is asked by data-migration, not here. One question lives in one entry.

## Rules

- Question lists are tight from the first draft: numbered, added at the end, never renumbered. Guidance starts loose and is tightened from use. Per tight-fields-loose-guidance.
- A question whose verified-by is none is reclassified before the entry is used: to a standard in a standards note, or to walkthrough guidance. It does not stay in the list. Per verification-per-question.
- Instances are written only when the applicability rule fires for a real system. Agent-method's rule: when the first implementation that needs them is being planned, not before. The row may exist earlier as a placeholder with no questions.
- A question about what the software does belongs to a use case and is moved there.
- Stage and concern are tags on questions. An entry is filed under the subject kinds it attaches to.
- A merged area in the table gets its own row only when an implementation shows it needs separate questions. A row is split, never renumbered.
- Every run's ambiguity list is checked against the registry. An ambiguity with no question becomes a new question at the end of an entry, or a new entry. Per the harvest loop.

## Open questions

- The maturity level meanings above are assumed; maturity-ladder.md is not written. Every "first required at" value is to confirm against it.
- Whether not-specified is an authored type or a view over records with status deliberately open.
- Whether the verification rows, test-method, acceptance-criteria, test-data, automated-checks, and quality-standards, stay in the registry or are described under verification.md with the registry holding only their ids.
- Whether implementation-standards is a type or, as decision-record.md says, a set of records with implementation "all".
- Whether stage belongs on the entry or on each question. The table puts it on the entry.
- Which profile characteristic names the applicability rule uses. The worked entry assumes "statefulness".
