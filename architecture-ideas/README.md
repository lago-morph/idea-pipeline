# Architecture ideas

Status: draft, started 2026-09-05.

Ideas about the decisions and designs that sit between an idea and a running system, other than the application source code. They are kept here so they can be pulled into [agent-method](https://github.com/lago-morph/agent-method) one at a time, as that method's workbench reaches the point where each is needed. Agent-method is about getting functional requirements and basic application architecture right, and it adds process and artifact types only when real friction shows they are needed. This directory respects that: nothing here is meant to land in agent-method ahead of its trigger.

## How to read this directory

Three levels, read as far as you need:

1. **This file.** The table below is one line per idea, with the event in agent-method that makes it needed and where it would land. Also a list of what agent-method already covers, so those ideas are not re-invented.
2. **One file per idea** in `ideas/`. Each is one screen: the idea, why it matters for agents, what it would look like in agent-method, open questions, and the source.
3. **Background.** `objectives.md` is what this exercise is for. `ideas.md` is the process-level discussion the idea files were extracted from. `reference/brainstorming.md` is the transcribed handwritten notes that started it.

## How to pull an idea into agent-method

1. The trigger in the idea's front matter has happened, or is about to.
2. Read the idea file and its `depends-on` list. A dependency that is still `idea` or `discussed` usually needs to go first, or at least be considered in the same round.
3. Author the change in agent-method in the home named in the front matter, using agent-method's vocabulary and its one-artifact-at-a-time rule.
4. Update the idea file's status to `pulled` with a link to the agent-method file, and record anything that changed in translation.

Statuses: `idea` (named, not yet discussed in depth), `discussed` (discussed and written up here), `drafted` (a concrete draft exists here or in a branch of agent-method), `pulled` (landed in agent-method; link in the file).

## Ideas

| Idea | One line | Trigger in agent-method | Status |
|---|---|---|---|
| [status-vocabulary](ideas/status-vocabulary.md) | Every decision is undecided, decided, deliberately open, inherited, or not applicable with reason | Next guide written, or record 3 markup | discussed |
| [tight-fields-loose-guidance](ideas/tight-fields-loose-guidance.md) | Question lists are tight from the start; guidance starts loose | Writing any new guide | discussed |
| [decision-inventory](ideas/decision-inventory.md) | The brainstorming notes are a seed list of future guides | Planning any new guide | discussed |
| [verification-per-question](ideas/verification-per-question.md) | Every guide question says how compliance is checked | Quality-standards execution methods get built | discussed |
| [binding-time](ideas/binding-time.md) | Each decision is tagged design, build, deploy, or runtime | First decision that belongs in configuration | discussed |
| [dependency-kinds](ideas/dependency-kinds.md) | Must-exist-before and must-be-consistent-with are different links | First guide that depends on another guide's answers | discussed |
| [concern-tags](ideas/concern-tags.md) | Concern is a tag for auditing; subject is the organizer | More than about five guides | discussed |
| [refinement-stages](ideas/refinement-stages.md) | The traditional layers are stages of one concern, not categories | Component and interface types are written | discussed |
| [five-kinds-of-guidance](ideas/five-kinds-of-guidance.md) | A type carries authoring, relating, consuming, verifying, and reviewing guidance | Type descriptions written from real instances | discussed |
| [guidance-pruning](ideas/guidance-pruning.md) | Guidance needs a removal rule | A run shows a guide was skimmed | discussed |
| [artifact-count-test](ideas/artifact-count-test.md) | Artifact count for the toy app is a health metric | Every implementation record | discussed |
| [system-profile](ideas/system-profile.md) | A short profile decides which guides are required and which are skipped with reason | Foreseen guides outgrow one implementation, or a second application | discussed |
| [binding-level](ideas/binding-level.md) | Decisions are owned at a level and inherited below | A platform the workbench does not own, or a second application | idea |
| [extraction-mode](ideas/extraction-mode.md) | Guides double as an interview script over an existing system | Method applied to a pre-existing system | idea |

The order above is a rough guess at the order the triggers will fire.

## Already in agent-method

These came up in discussion and need no pulling. They are listed so the idea files can refer to them by agent-method's names.

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

## Not yet placed

- The data model for the framework itself. The discussion concluded that agent-method's artifact graph with typed two-way links already is a data model, and that the ideas above are fields, statuses, and link types on it rather than a separate model. This should be confirmed before any separate data model is drafted.
