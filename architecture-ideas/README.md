# Architecture ideas

Status: draft, started 2026-09-05.

Ideas and structure for the decisions and designs that sit between an idea and a running system, other than the application source code. Two parts. The **nuggets** in `ideas/` are pulled into [agent-method](https://github.com/lago-morph/agent-method) one at a time as that method's workbench reaches the point where each is needed. The **spine** in `spine/` is the structure that keeps a whole system's artifacts, subjects, and decisions navigable, so that a real application does not collapse under free-form notes. Agent-method is about getting functional requirements and basic application architecture right, and adds process only when real friction shows it is needed. This directory respects that: nothing here lands in agent-method ahead of its trigger.

## How to read this directory

Read as far as you need.

1. **This file.** What is here and where to go.
2. **`objectives.md`** for what this is for, and **`spine/overview.md`** for the six structures, what rides on them, and the vocabulary. Those two files are the whole picture at one screen each.
3. **`spine/`** for each structure in detail, with fields, rules, a workbench example where one exists, and open questions. **`plan.md`** for how this matures alongside agent-method. **`inventory.md`** for what exists and what is still to create. **`decisions-log.md`** for what the owner has settled and what is only proposed.
4. **`ideas/`** for the nuggets, one screen each, with the agent-method event that triggers each and where it would land. The table below indexes them.
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

## How to pull a nugget into agent-method

1. The trigger in the idea's front matter has happened, or is about to.
2. Read the idea file and its `depends-on` list. A dependency still at `idea` or `discussed` usually goes first, or at least in the same round.
3. Author the change in agent-method in the home named in the front matter, using agent-method's vocabulary and its one-artifact-at-a-time rule. Where the nugget is also a spine field, carry the spine's name for it.
4. Update the idea file's status to `pulled` with a link to the agent-method file, and record anything that changed in translation.

Statuses: `idea` (named, not yet discussed in depth), `discussed` (discussed and written up here), `drafted` (a concrete draft exists here or in a branch of agent-method), `pulled` (landed in agent-method; link in the file).

## Nuggets

| Idea | One line | Trigger in agent-method | Spine home | Status |
|---|---|---|---|---|
| [status-vocabulary](ideas/status-vocabulary.md) | Every decision is undecided, decided, deliberately open, inherited, or not applicable with reason | Next guide written, or record 3 markup | decision record | discussed |
| [tight-fields-loose-guidance](ideas/tight-fields-loose-guidance.md) | Question lists are tight from the start; guidance starts loose | Writing any new guide | registry | discussed |
| [decision-inventory](ideas/decision-inventory.md) | The brainstorming notes are a seed list of future guides | Planning any new guide | registry seed table | discussed |
| [verification-per-question](ideas/verification-per-question.md) | Every guide question says how compliance is checked | Quality-standards execution methods get built | registry, verification | discussed |
| [binding-time](ideas/binding-time.md) | Each decision is tagged design, build, deploy, or runtime | First decision that belongs in configuration | registry question, decision record | discussed |
| [dependency-kinds](ideas/dependency-kinds.md) | Must-exist-before and must-be-consistent-with are different links | First guide that depends on another guide's answers | derivation graph | discussed |
| [concern-tags](ideas/concern-tags.md) | Concern is a tag for auditing; subject is the organizer | More than about five guides | registry question, subject catalog | discussed |
| [refinement-stages](ideas/refinement-stages.md) | The traditional layers are stages of one concern, not categories | Component and interface types are written | registry | discussed |
| [five-kinds-of-guidance](ideas/five-kinds-of-guidance.md) | A type carries authoring, relating, consuming, verifying, and reviewing guidance | Type descriptions written from real instances | registry entry | discussed |
| [guidance-pruning](ideas/guidance-pruning.md) | Guidance needs a removal rule | A run shows a guide was skimmed | harvest loop | discussed |
| [artifact-count-test](ideas/artifact-count-test.md) | Artifact count for the toy app is a health metric | Every implementation record | verification, level 3 | discussed |
| [system-profile](ideas/system-profile.md) | A short profile decides which guides are required and which are skipped with reason | Foreseen guides outgrow one implementation, or a second application | system profile | discussed |
| [binding-level](ideas/binding-level.md) | Decisions are owned at a level and inherited below | A platform the workbench does not own, or a second application | decision record, standards | idea |
| [extraction-mode](ideas/extraction-mode.md) | Guides double as an interview script over an existing system | Method applied to a pre-existing system | modes | idea |

The order above is a rough guess at the order the triggers will fire.

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
