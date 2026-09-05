# Requirements and Architecture

2026-08-26

Transcribed from handwritten brainstorming notes. Content is verbatim; spelling and formatting have been normalized. Items marked "DoD" in the original are collected in the [DoD candidates](#dod-candidates) section at the end.

## Functional requirements/design

- Project vision - what, why, alternatives, guiding principles, goals/non-goals, explicitly out of scope, functional boundary
- Use cases - flow through application (main use is to identify requirements)
- Scenarios w/test data - conform to use cases, used for final e2e tests, include edge cases
- Data models - re-usable data structures with relationships
- Glossary linked to data model
- Business rules -
  - Validation (use pseudocode/regular expressions) + examples
  - Algorithms (specific in pseudocode)

## Non-functional requirements

- Apply to running system
- Properties system must satisfy

## Application architecture

- <u>Logical</u> model of system
- Define components and interfaces
- Components
  - Lifecycle/state (e.g., startup, shutdown)
  - Contracts - what it promises for each of its states
  - Persistence/data ownership
  - State machines w/complete transitions
- Interfaces - each interface has
  - Example input/output
  - Preconditions (incl. validation, state)
  - Function (algorithm)
  - Post conditions (state transitions, error semantics)
  - Synchronous/asynchronous
  - Input/output data structures (typed), validation rules
  - Explicit concurrency semantics
  - Required/optional, defaults, min/max
  - Edge cases + behavior
- Error taxonomy/behavior/decision tables
- Explicit items not specified
- Explicit external dependencies

## Technical architecture

- Map components to
  - Implementation mechanism (language, tech stack)
  - Runtime environment
  - Persistence mechanism
  - Concurrency mechanism
  - Failure/restart/retry
  - Logging mechanisms
  - AuthN/Z
- Map interfaces to
  - Communication channels/transports
    - SerDes/methods/protocol
    - Error handling/codes
    - Retry/timeout
    - Security
- Supporting components to satisfy non-functional requirements
- Explicitly not-specified (implementation flexibility)
- Configuration parameter methods + tools
- External dependencies version pinned, interfaces/data models specified

## DevOps architecture

### Both

- Execution environment
- Install/update
- Observability
  - Monitoring (metrics)
  - Log aggregation
- AuthN/Z tools
- Persistence infrastructure (disk, S3)
- Platform services (database, message queue)
- CI/CD
- Release/deployment management
- Source control

### Dev architecture (dev platform)

- IDEs/tools (incl. issue tracking, docs, comms)
- Shared libraries/code
- Standards (coding, testing, naming)
- Test automation, test data mgmt.
- Dev observability (traces, profiling)
- Digital twins
- User management (dev/test)

### Ops architecture

- Troubleshooting/remediation
- Alarming
- HA/DR, backup/restore
- SLA/SLO
- User management (end-users)
- Security monitoring + incident mgmt.
- Configuration management
- Audit log mgmt.

## Closing notes

ADRs stand alone. They are to capture intent behind decisions. They are referenced in relevant design/implementation artifacts.

Code, compiled programs, images, config files are all part of development.

Documentation is not included, except that standards can mandate what must be documented.

## DoD candidates

Items marked with a "DoD" box in the original notes, as tentative parts of a definition of done.

| Item | Architecture type |
|------|-------------------|
| Scenarios w/test data - conform to use cases, used for final e2e tests, include edge cases | Functional requirements/design |
| Components: Contracts - what it promises for each of its states | Application architecture |
| Interfaces: Example input/output | Application architecture |
| Interfaces: Post conditions (state transitions, error semantics) | Application architecture |
