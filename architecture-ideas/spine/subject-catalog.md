# Subject catalog

Status: draft, 2026-09-05. Structure 3 of the spine.

## What a subject is

A subject is a thing in the system that an artifact can attach to. Every artifact and every decision record names exactly one subject. The catalog is the list of subjects for one system.

Subject is the primary navigation axis. An implementer works on one component or one interface at a time and needs one artifact as the primary driver for implementing it, with everything about that thing reachable from there. Agent-method already works this way: one implementation record is the subagent's whole input, and a component definition is meant to be the driver for building that component. Concern is the other axis, and it is a tag. The concern view answers "show me every persistence decision across all subjects". It is the audit view, used for completeness and consistency review, not for building.

## Subject kinds

| Kind | Definition | Artifact types that typically attach | Agent-method mapping |
|---|---|---|---|
| system | The whole application: one vision, one profile, one maturity target | vision, the system profile, use cases, acceptance-criteria, implementation-record, non-functional-requirements, release-management, sla-slo | The vision's subject. Not a type; the vision is the root artifact |
| component | A part of the system with a responsibility, a lifecycle, and data it owns | component, implementation-structure, code-conventions, business-rules, logging-diagnostics, implementation-mechanism | Already a type in CONVENTIONS.md; no instance yet |
| interface | A boundary across which one thing calls or presents to another. Includes the user interface and the hooks contract the checks use | interface, ui-use-case, ui-decisions, transport-serdes, automated-checks | Already a type; no instance yet. The UI use case is the home of the UI design, per ADR 0006 |
| data store | A place data lives, with a lifetime: memory, browser storage, a file, a database | data-model, persistent-storage, data-migration, persistence-infrastructure, ha-dr-backup | New. Today it is the "persistent storage" line in each implementation record |
| environment | Where something runs or is checked: a device, a browser, a runtime, a cluster, the working environment | execution-environment, test-method, delivery-to-device, ci-cd, configuration-management | "Target execution environment" in implementation records; the harness in test-method notes |

## Fields of a catalog entry

| Field | Values or form | Purpose |
|---|---|---|
| id | lowercase, hyphenated, unique within the system | What records and artifacts name |
| kind | system, component, interface, data store, environment | Which registry entries can attach |
| parent | a system or component id; none for the system | Nesting. An interface belongs to the component or system that exposes it; a data store to the component that owns it |
| responsibility | one line | What the subject is for, in the vocabulary the use cases use |
| artifacts attached | list of artifact ids | Everything about this subject, reachable from here |
| owned at | organization standard, platform, system, component | The binding level: who owns the subject's decisions and who inherits them |
| status | proposed, ratified, placeholder, retired | Proposed by whoever designs; ratified by the owner in conversation; placeholder while no artifact is attached; retired when the subject is gone but its records are kept |

## Worked example: the workbench

Inferred from the vision, the two use cases, and implementation records 1 to 3. No component or interface artifact exists yet, so every entry other than the system is inferred from the use cases' functional areas and the implementation-structure notes. Every entry is owned at the system level, because the workbench has no platform above it and no organization standard.

| id | kind | parent | responsibility | artifacts attached | owned at | status |
|---|---|---|---|---|---|---|
| idea-workbench | system | none | One home for every idea, organized without moving or copying | vision, initial-ui, edit-ideas, implementation-record-1 to 3, implementation-standards, acceptance-criteria-1 and 2 | system | ratified (inferred) from the ratified vision |
| idea-list (inferred) | component | idea-workbench | Lists ideas in order, keeps the selection visible, updates after every change | initial-ui, edit-ideas, implementation-structure-1 and 2 | system | proposed |
| idea-editor (inferred) | component | idea-workbench | Plain-text editing of the active idea, with the undo history and the leading-whitespace rules | edit-ideas, implementation-structure-2 | system | proposed |
| message-area (inferred) | component | idea-workbench | Shows the most recent message and the session's message list | initial-ui | system | proposed |
| idea-store (inferred) | component | idea-workbench | Holds the ideas, assigns identity, orders them, strips and deletes blanks at each update | implementation-structure-1 and 2, edit-ideas | system | proposed |
| test-data-loader (inferred) | component | idea-workbench | Scaffolding: appends one copy of the test data set per press | initial-ui, test-data-1 and 2 | system | proposed; retired when save exists |
| ui (inferred) | interface | idea-workbench | The three-pane touch web UI with the header commands and the message area | initial-ui, ui-decisions-1 and 2, ui-standards-definition | system | proposed |
| check-hooks (inferred) | interface | idea-workbench | The element ids and classes the checks locate; a contract between implementation and checks | automated-checks-1 and 2, test-method-definition | system | proposed |
| ideas-array (inferred) | data store | idea-store | In-memory array of `{ id, content }`; lost when the application is closed | implementation-structure-1 and 2, the "persistent storage: none" line of each implementation record | system | proposed |
| ipad-safari-file (inferred) | environment | idea-workbench | Target: a single HTML file opened over `file://` in Safari on an iPad | implementation-record-1 to 3, the open delivery-to-device area | system | proposed |
| headless-chromium (inferred) | environment | idea-workbench | Check environment: Playwright with headless Chromium at both iPad sizes, standing in for Safari | test-method-1 and 2, automated-checks-1 and 2 | system | proposed |
| working-repository (inferred) | environment | idea-workbench | Where artifacts and implementations live and are reviewed: git, one PR per change, `implementations/<N>/` | implementation-standards, CONVENTIONS.md | system | proposed (to confirm it is an environment) |

What the example shows. The five component rows fall out of the use cases' named functional areas plus the two things the implementation-structure notes describe that no use case names: the store and the loader. Two of the twelve subjects, the ideas-array and the loader, are the ones the Save ideas use case will change first, which is where the persistent-storage entry attaches.

## Rules

- Subjects are proposed by whoever designs and ratified by the owner. An agent may propose a subject while building; the proposal is harvested like a record and ratified, revised, or rejected before the next implementation starts.
- Every decision record names exactly one subject. A decision that seems to span subjects is a standard, held at a higher binding level and inherited below.
- A subject with no attached artifacts is a placeholder, not a defect. It becomes a defect only when the profile and maturity level require an artifact for it.
- Ids are stable. A subject that changes shape is retired and a successor proposed, with the records carried across and the history kept.
- The implementation record's "use cases and components included" line is checked against the catalog: every component it names is a catalog entry.

## Open questions

- Whether the UI is one interface subject or one per kind of interface. ADR 0006 gives each kind its own UI use case, which suggests one subject per kind.
- Whether the hooks contract is an interface subject in its own right or a section of automated-checks attached to the system.
- Whether the working repository is an environment or belongs to the method rather than to the system.
- Whether an implementation is a subject. Records carry an implementation number today; the catalog does not.
- Whether component subjects are proposed before the component type is written, or only when its first instance is.
- Where the catalog lives as a file: a section of the vision, a note, or its own artifact type.
