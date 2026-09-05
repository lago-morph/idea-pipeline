# System profile

Status: draft, 2026-09-05. Structure 1 of the spine.

## What the profile is

The profile is a short statement of what the system is: six to eight characteristics, each with a coarse value. A single-user memory-only page and a Kubernetes transaction processor differ on these few values, and the required artifact set falls out of the difference. The profile is one of two inputs to the required artifact set. The other is the maturity ladder in `maturity-ladder.md`.

The two are different axes. The profile says what the system is. Maturity says how far along it is. A system whose profile says "shared durable state" can still be at M1 Prototype with no persistence yet. The profile does not change when a level is reached, and reaching a level does not change the profile. The profile caps the ladder: some values make higher levels unreachable, and some make whole rungs collapse. That interaction is described in `maturity-ladder.md`.

The profile is not a requirements document, not a design, and not a list of decisions. It holds no answers to registry questions. It only says which questions are asked.

## The characteristics

Eight characteristics. Each value is one line. The last column says which concerns and artifact types a characteristic tends to switch on when its value rises. The concerns are the ten tags from `overview.md`; the artifact types named are agent-method's existing guides and foreseen guides where one exists.

| Characteristic | Values | Definition per value | Tends to switch on |
|---|---|---|---|
| Concurrent users | one | One person, no accounts | |
| | few trusted | A known handful who share access without hostility between them | identity and access; concurrency and failure; user management for dev and test |
| | many | An open or large population, some of it untrusted | security; user management for end users; SLA and SLO |
| Statefulness | none | Nothing survives closing the application | |
| | local | State survives on the device or host it runs on | persistence; the persistent storage guide; data model and identity; carrying data between implementations |
| | shared durable | State lives in a store more than one process or host reads | persistence infrastructure; platform services; backup and restore; concurrency and failure |
| Availability target | best effort | It runs when the owner runs it | |
| | working hours | Expected up during a stated window, with someone to call | observability; alarming; troubleshooting and remediation |
| | continuous | Expected up always, with recovery objectives stated | HA and DR; SLA and SLO; security monitoring |
| Deployment topology | single device | One runnable on one device, no server | |
| | single host | One host, possibly several processes, possibly a server | runtime environment; install and update; configuration |
| | distributed | Several hosts or services that must find each other | communication; external dependencies; release and deployment management; CI and CD |
| Data sensitivity | personal | The owner's own data, on the owner's own device | |
| | internal | Data an organization would not want outside it | security; identity and access; audit log management |
| | regulated | Data a law or contract governs | audit; retention; security incident management; organization standards |
| Expected lifetime | throwaway | Discarded after it answers its question | |
| | years | Used long enough that its data outlives any one implementation | lifecycle; carrying data between implementations; external dependencies version pinned |
| | indefinite | No planned end; must survive turnover of people and platforms | documentation mandated by standards; binding level above the system |
| Number of teams | one person | One owner who is also the builder, with or without an agent | |
| | one team | Several people who share one set of decisions | code conventions; standards for coding, testing, naming; source control practice |
| | many teams | Decisions are made above the team and inherited | binding level: organization standard and platform; shared libraries; release coordination |
| Integration surface (to confirm) | none | Nothing enters or leaves except by a manual act | |
| | consumes | Calls services or stores it does not own | external dependencies; communication; failure and retry |
| | provides | Exposes interfaces other systems depend on | interface contracts; communication; security at the boundary; versioning |

The eighth characteristic, integration surface, is added because none of the seven from discussion switches on the communication and external dependencies concerns by itself. A single-user, single-device, memory-only system can still call a remote service. It is marked to confirm because it may be derivable from deployment topology in practice.

Values are deliberately coarse. The test of a characteristic is whether the workbench and an enterprise transaction processor take different values on it, and whether moving one step changes which registry entries are required. A characteristic that fails either test is cut.

## Rules

**Who sets it.** The owner. The profile is a set of owner-stated decision records with the system as subject. An agent may propose a profile during capture, with provenance extracted-with-evidence, but the profile is not in force until the owner ratifies it. Only the owner's word in conversation ratifies; a merge never does.

**When it is revised.** Deliberately, as its own act, never as a side effect of a build. A revision is a superseding record for the changed characteristic, with the prior value in the history field. Adding a non-functional requirement is the usual reason: the requirement moves a value, and the value turns registry entries on. When a value changes, every decision record whose status is not-applicable with that value as its reason flips to undecided automatically, per the status rules in `decision-record.md`. Those undecided records are the immediate work list.

**How a value maps to skip-with-reason.** Each registry entry carries an applicability rule that names profile characteristics and values. When the system's value makes an entry not required, every question in that entry gets a record for the subject with status not-applicable with reason, and the reason is the characteristic and value, written as "not applicable: concurrent users is one". The record is still written; silence is never a valid state. Agent-method's implementation records do this by hand today. "Persistent storage: none, memory only" in implementation record 3 is a skip with reason, and the reason is the statefulness value of that implementation. The profile makes the reason a value the validator can check rather than a sentence it cannot.

**Where it lives.** Not decided. The candidates from `../ideas/system-profile.md` stand: a section of the vision, a note, or its own artifact type. For the workbench it starts as a note, per agent-method's promotion path.

## The workbench's profile

Filled in from the vision's non-goals, the v1 scope note, and implementation records 2 and 3. Values describe what the workbench is, not what implementation 3 has reached; the gap between the two is the maturity axis.

| Characteristic | Value | Justification |
|---|---|---|
| Concurrent users | one | Vision, who will use it: "me, and me alone. There are no other users, no accounts, and no sharing." Non-goal: multi-user operation, authentication, sharing |
| Statefulness | local | Vision success criterion 3: close and reopen with nothing lost. Implementations 1 to 3 are memory only, which is a maturity fact, not a profile fact. The vision's open issue on what durable storage concretely is remains open |
| Availability target | best effort | No server and no hosting; the file is opened directly in Safari on an iPad, per implementation records 2 and 3. Nobody is on call |
| Deployment topology | single device | Implementation record 3: a single-page HTML file, opened directly, no server. Non-goal: hosting for anyone but me |
| Data sensitivity | personal | The owner's own ideas on the owner's own device. No accounts, no sharing (to confirm: whether anything imported is more sensitive than personal) |
| Expected lifetime | years | Vision success criterion 4: the workbench replaces scattered lists as the place ideas go. Data must outlive individual implementations, which is why the decision-guides note foresees a guide on carrying data between implementations (to confirm: the v1 scope note allows halting the project at a checkpoint) |
| Number of teams | one person | One owner with an agent partner. Implementation standards and decisions are all system level today; `../ideas/binding-level.md` says nothing above system exists |
| Integration surface | none | Non-goal: automated integration with agent-method or any other system; content enters as plain text typed, pasted, or imported by a manual act. No external dependencies, per implementation record 3 |

Every value sits at the lowest step of its characteristic except statefulness and lifetime. That is the expected shape for a system meant to test whether the method scales down, and it is why `../ideas/artifact-count-test.md` predicts a small required artifact set.

## Open questions

- Whether integration surface earns its place or collapses into deployment topology (to confirm).
- Whether "few trusted" and "one team" are really two characteristics or one, since both mean a handful of known people.
- Whether the profile is per system only, or whether a component can carry an override, as binding level would allow.
- What the profile of the second application will look like, and whether its values discriminate from the workbench's on more than two characteristics. If not, the characteristics are too coarse.
