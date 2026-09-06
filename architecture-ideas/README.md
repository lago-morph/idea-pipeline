# Architecture ideas

Status: draft, started 2026-09-05.

Ideas and structure for the decisions and designs that sit between an idea and a running system, other than the application source code. Two parts. The **nuggets** in `ideas/` are pulled into [agent-method](https://github.com/lago-morph/agent-method) one at a time as that method's workbench reaches the point where each is needed. The **spine** in `spine/` is the structure that keeps a whole system's artifacts, subjects, and decisions navigable, so that a real application does not collapse under free-form notes. Agent-method is about getting functional requirements and basic application architecture right, and adds process only when real friction shows it is needed. This directory respects that: nothing here lands in agent-method ahead of its event, and every nugget names the friction that justifies it.

## How to read this directory

Read as far as you need.

1. **This file.** What is here and where to go.
2. **`objectives.md`** for what this is for, and **`spine/overview.md`** for the six structures, what rides on them, and the vocabulary. Those two files are the whole picture at one screen each.
3. **`spine/`** for each structure in detail, with fields, rules, a workbench example where one exists, and open questions. **`plan.md`** for how this matures alongside agent-method. **`inventory.md`** for what exists and what is still to create. **`decisions-log.md`** for what the owner has settled and what is only proposed.
4. **`ideas/`** for the nuggets, one screen each, with its relationship kind, its agent-method event, and where it would land. The table below indexes them.
5. **Background.** `ideas.md` is the process-level discussion the nuggets were extracted from. `reference/brainstorming.md` is the transcribed handwritten notes that started it.

## The spine

| # | Structure | File |
|---|---|---|
| 1 | System profile | `spine/system-profile.md` |
| 2 | Maturity ladder | `spine/maturity-ladder.md` |
| 3 | Subject catalog | `spine/subject-catalog.md` |
| 4 | Artifact type registry | `spine/artifact-type-registry.md` |
| 5 | Decision records | `spine/decision-record.md` |
| 6 | Derivation graph | `spine/derivation-graph.md` |
| | Modes of entry | `spine/modes.md` |
| | Verification, three levels | `spine/verification.md` |
| | Harvest loop | `spine/harvest-loop.md` |

## The interface with agent-method

Every nugget has one relationship kind and one agent-method event. The events are the rows of the sync table in `plan.md`, given ids here so both files say the same thing.

### Events

| id | Agent-method event | Fires |
|---|---|---|
| G | A guide is written or revised | every time |
| M | A regeneration run finishes and its metrics row is recorded | every time |
| E1 | Implementation record 3 is marked up and the implementation 3 run happens | once, next |
| E2 | The Save ideas use case is ratified and the persistent-storage guide is written | once |
| E3 | A guide is written whose questions depend on another guide's answers | once, first occurrence |
| E4 | The agent-facing type descriptions are written in `method/types/` from real instances | once |
| E5 | The component and interface types are written | once |
| E6 | The guide set outgrows one implementation: guides exist that no implementation needs, a run reports a guide skimmed, or the notes become hard to navigate | conditional |
| E7 | A level above the workbench appears: a platform it does not own, a second application, or an existing system to capture | conditional |

### Kinds

| Kind | Meaning | How it reaches agent-method |
|---|---|---|
| rule | Applied every time the event happens. Never "pulled" once | One sentence added to the guide or procedure the rule governs, proposed the first time the event fires after the rule is ratified here |
| rider | Carried into one specific agent-method work item | Extra columns or sections in that work item's proposal, for the owner's markup in the same round. Never a standalone change to agent-method |
| conditional | Waits on an event that may never happen for the workbench | Stays here until the event is observed. Then handled as a rider on whatever work the event creates |

### Friction

Agent-method adds process only where real friction has been observed. Each nugget's front matter names the friction in agent-method that justifies it. "None yet" is what makes a nugget conditional rather than a rider. "Anticipated" marks a rider whose friction the work item itself will create.

### What "pulled" means

A nugget is pulled when its content appears in a ratified agent-method artifact. Ratified means the owner said so in conversation; a merge is never ratification. The nugget's status becomes `pulled`, with a link to the agent-method file, and the nugget records anything that changed in translation. Until then the nugget stays `idea`, `discussed`, or `drafted`.

### How to pull

1. The nugget's event has fired, or the work item it rides on is about to be proposed.
2. Read the nugget and its `depends-on` list. A dependency still at `idea` or `discussed` goes in the same round, or first.
3. Include the nugget's content in the agent-method work item, in agent-method's vocabulary and shape, using the spine's name for the field where one exists.
4. When the owner ratifies the work item, mark the nugget `pulled` with the link.

## Nuggets

| Idea | One line | Kind | Event | Spine home | Status |
|---|---|---|---|---|---|
| [tight-fields-loose-guidance](ideas/tight-fields-loose-guidance.md) | Question lists are tight from the start; guidance starts loose | rule | G | registry | discussed |
| [decision-inventory](ideas/decision-inventory.md) | The brainstorming notes are a seed list of future guides | rule | G | registry seed table | discussed |
| [verification-per-question](ideas/verification-per-question.md) | Every guide question says how compliance is checked | rule | G | registry, verification | discussed |
| [artifact-count-test](ideas/artifact-count-test.md) | Artifact count for the toy app is a health metric | rule | M | verification, level 3 | discussed |
| [status-vocabulary](ideas/status-vocabulary.md) | Every decision is undecided, decided, deliberately open, inherited, or not applicable with reason | rider | E2 | decision record | discussed |
| [binding-time](ideas/binding-time.md) | Each decision is tagged design, build, deploy, or runtime | rider | E2 | registry question, decision record | discussed |
| [dependency-kinds](ideas/dependency-kinds.md) | Must-exist-before and must-be-consistent-with are different links | rider | E3 | derivation graph | discussed |
| [five-kinds-of-guidance](ideas/five-kinds-of-guidance.md) | A type carries authoring, relating, consuming, verifying, and reviewing guidance | rider | E4 | registry entry | discussed |
| [refinement-stages](ideas/refinement-stages.md) | The traditional layers are stages of one concern, not categories | rider | E5 | registry | discussed |
| [concern-tags](ideas/concern-tags.md) | Concern is a tag for auditing; subject is the organizer | conditional | E6 | registry question, subject catalog | discussed |
| [guidance-pruning](ideas/guidance-pruning.md) | Guidance needs a removal rule | conditional | E6 | harvest loop | discussed |
| [system-profile](ideas/system-profile.md) | A short profile decides which guides are required and which are skipped with reason | conditional | E6 | system profile | discussed |
| [binding-level](ideas/binding-level.md) | Decisions are owned at a level and inherited below | conditional | E7 | decision record, standards | idea |
| [extraction-mode](ideas/extraction-mode.md) | Guides double as an interview script over an existing system | conditional | E7 | modes | idea |

E1 carries no nugget. It is the next event in agent-method's sequence and is listed because phase 2 of `plan.md` uses its output.

## Already in agent-method

These came up in discussion and need no pulling. They are listed so the idea and spine files can refer to them by agent-method's names.

| Discussed as | Agent-method already has |
|---|---|
| Decision debt log during implementation | The ambiguity list from a regeneration run, and "decisions made while building" in each implementation record |
| Variance across runs measures spec completeness | The regeneration test, ADR 0007, and the implementation 1 versus 2 comparison in the decisions notes |
| Subject-primary organization | `component` and `interface` as artifact types; one implementation record as the subagent's whole input |
| Artifact definition plus guidance | The guide / decisions / standard pattern in `workbench/note/decision-guides.md`, and definitions kept separate from instances, ADR 0004 |
| Stress the toy app with non-functional requirements one at a time | The use-case build order; Save ideas triggers the persistent-storage guide |
| Lessons learned with every use | Guide questions added after each run, `ai/procedures/` revised after each run, retrospectives |
| Progressive disclosure to agents | Tiered document access in `ai/procedures/implement-by-subagent.md` |
| Definition of done per artifact | Partly: the review checklist in the implementation procedure. The rest is `five-kinds-of-guidance` |
| Not-applicable-with-reason | Partly: "Persistent storage: none, memory only" in the records. Naming it is `status-vocabulary` |
| Ratified versus merged | Ratification is the owner's word in conversation; a merge is never ratification. The decision record's ratification field uses the same rule |
