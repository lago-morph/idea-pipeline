# Ideas

Status: draft. Captured 2026-09-05 from discussion. Process suggestions for filling out the framework in its different modes of use. The data model is a separate piece of work and comes first; these processes are written against the fields they will need from it.

## Working premise

The three uses named in `objectives.md`, extraction, guided new work, and checklist, are all operations over one thing: a catalog of decision slots. A decision slot is a question the architecture must answer for a particular subject. The framework is the slot schema, the inventory of slots, and the processes that operate on them.

Two distinctions carry most of the weight:

- **Silence is not the same as deliberate freedom.** An agent treats both as license. A slot that has not been discussed must look different from a slot that has been deliberately left open with stated bounds.
- **A decision is not the same as the constraints it produces.** One decision can constrain several layers. The slot holds the decision; the layered specification is a projection of the answers.

## Fields the processes depend on

These belong to the data model and are listed here only so the processes below can refer to them.

- Question, phrased so an unanswered slot is visibly unanswered.
- Subject and scope: system, component, interface, environment.
- Binding time: design, build, deploy, runtime. Determines which artifact holds the answer (ADR, specification, configuration, policy).
- Binding level: org standard, platform, system, component. Determines who decides and whether the answer is inherited.
- Status: undecided, decided, deliberately open with bounds, inherited, not applicable with reason.
- Answer and rationale, with rationale usually a link to an ADR.
- Relations to other slots: depends on, constrains, conflicts with, satisfies.
- Evidence: where the answer is implemented or documented.
- Verification: how to check the answer is honored.

## Process: extraction from an existing system

The catalog acts as an interview script.

1. For each slot, an agent reads code, configuration, and documents, and proposes an answer with evidence.
2. A human confirms, corrects, or rejects each proposal.
3. Slots with no evidence become "undecided". These are discovered debt, not gaps in the catalog.
4. Slots whose evidence contradicts other slots are flagged as conflicts for a human to resolve.
5. Slots that appear to be answered at a level above the system (platform, org standard) are marked inherited and point at the source.

The output is a populated catalog plus a debt list. The debt list is the first input to guided new work.

## Process: guided new work

The relation edges give a partial order over slots.

1. Take the undecided slots and order them by dependency.
2. For each slot, present the slots it depends on with their answers, the slots it constrains, and any prior decisions on the same subject.
3. The human answers, or marks the slot deliberately open with bounds, or marks it not applicable with a reason.
4. The agent checks the answer against related slots and raises conflicts immediately. Example: a synchronous interface on a component whose concurrency answer is a background worker.
5. Answers with design-time binding get an ADR. Answers with other binding times get recorded in the artifact their binding time names.

Humans decide. The agent's job is ordering, context, consistency, and cross-referencing.

## Process: checklist and status view

The slot list with the status field is the checklist. Views worth generating:

- Everything undecided, ordered by dependency, which is the work queue.
- Everything deliberately open, which is the list of freedoms an implementer has.
- Everything not applicable, with reasons, which is the list that will change when requirements change.
- Everything about one subject, such as a component or an interface, across all layers.
- Everything inherited, which is the list of things the system does not own.

## Process: validate coverage with the toy application

The toy application can answer every slot now, even where the answer is trivial.

1. Walk the full catalog against the toy application.
2. Answer each slot. Expect many "not applicable, because single user", "not applicable, because in-memory", and similar.
3. Any slot that cannot be answered at all, even as not applicable, has a badly phrased question. Fix the question.
4. Any decision the toy application embodies that has no slot is a missing slot. Add it.

This tests whether the catalog covers the ground. It does not test whether the answers are hard. Those are separate questions and only the first is needed to build the framework.

## Process: stress with non-functional requirements

Each non-functional requirement forces a class of decisions into existence. Add them one at a time and watch which slots flip from not applicable to real.

Candidate requirements and the slots they should activate:

| Requirement added to toy app | Slots expected to activate |
|---|---|
| Survive a restart mid-operation | Persistence mechanism, idempotency, recovery, state machine completeness |
| Two users | Identity, authentication, data ownership |
| Two tenants | Data isolation, authorization granularity, per-tenant configuration |
| Audit who changed what | Provenance, audit log management, identity |
| Change the data schema without downtime | Migration, versioning, backward compatibility |
| Run in two environments | Configuration parameters, environment scope, install and update |
| Someone else operates it | Alarming, troubleshooting, SLO, runbooks |

If a requirement activates no slots, either the requirement is not really non-functional or the catalog has a gap.

## Process: capture decisions during implementation

An agent implementing from a specification keeps a running log. Every time it makes a choice the specification did not dictate, it records the choice, the alternatives it saw, and why it picked one.

That log is decision debt. After the run, each entry either becomes a slot answer with an ADR, a deliberately open slot with bounds, or a new slot the catalog was missing.

## Process: measure completeness by variance across runs

Run the same specification through two or more different models or thinking settings. Where the implementations diverge, the specification was silent. Each divergence names a missing or underspecified slot.

This is a direct, cheap measurement of specification completeness, and it is only possible because agents make repeated runs affordable.

## Process: retrospection into ADRs

The implementation log and the variance findings feed a retrospective. The retrospective produces ADR drafts for decisions worth binding, and catalog changes for slots that were missing or badly phrased. The existing `self-retrospective` skill in this repository is a starting point for the mechanics.

## Deferred: physical form

The data model comes first. When it renders into files, the leading candidate is one markdown file per slot with structured front matter and a generated index. That is human-readable, diffable, and easy for an agent to query. Tooling should wait until the schema has survived one extraction pass and one guided pass.

## Open questions

- Whether scope or layer is the top-level organizer. See the discussion on taxonomy.
- Whether relations are links in files or edges in a real graph. The data model decides this.
- How much of the catalog is a fixed inventory and how much is a method for finding new slots. Enterprise checklists never finish, so the method matters.
