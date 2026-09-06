# The spine

Status: draft, 2026-09-05. This is the structure that holds everything else in this directory together. The individual ideas in `../ideas/` are fields, statuses, and link types on the spine. The spine is what keeps a real application navigable as its artifacts grow, which free-form notes alone do not.

## Why a spine

Agent-method grows a specification organically, as typed artifacts and free-form notes, adding process only when friction shows it is needed. That is the right way to discover what the artifacts should be. It is not enough to keep a real application usable once the artifact count passes a few dozen, because nothing says which artifacts are required, where a decision lives, who made it, whether it is ratified, or what to change when the result is wrong. Two earlier attempts at agent-method collapsed for the opposite reason: structure designed in the abstract, ahead of any content. The spine is the minimum structure that can be validated against a real application at every step.

The spine is six structures. Three things ride on it: modes of entry, verification, and the harvest loop. The rule for keeping it a spine and not a framework: anything new must prove it cannot be a field on one of the six.

## The six structures

| # | Structure | What it holds | One-line role | Detail |
|---|---|---|---|---|
| 1 | System profile | Six to eight characteristics of the application, coarse values | What the system *is*; sets the ceiling and skips rungs | `system-profile.md` |
| 2 | Maturity ladder | Ordered levels Sketch to Enterprise with criteria | How far along the system is; the gap to target is the work list | `maturity-ladder.md` |
| 3 | Subject catalog | System, components, interfaces, data stores, environments | What every artifact and decision attaches to; the navigation axis | `subject-catalog.md` |
| 4 | Artifact type registry | One entry per artifact type: questions, tags, guidance, applicability rule | Which artifacts exist, what each asks, when each is required | `artifact-type-registry.md` |
| 5 | Decision records | One record per subject per question: status, provenance, ratification, rationale, evidence | Where humans and agents record and ratify decisions | `decision-record.md` |
| 6 | Derivation graph | Links from requirement to decision to artifact field to generated thing | Root-cause revision: walk backward from a bad behavior to the decision that caused it | `derivation-graph.md` |

### How they relate

- The **profile** and the **maturity ladder** together compute the required artifact set: which entries in the **registry** must have instances, at which completeness, for which **subjects**.
- Every registry entry's questions, answered for a subject, are **decision records**.
- Every produced thing, code, configuration, or check, is linked in the **derivation graph** back to the records and artifacts it came from.
- The profile is set by the owner. The maturity target is set by the owner. Subjects are proposed by whoever is designing and ratified by the owner. Records are written by humans or agents and carry provenance saying which.

## What rides on the spine

**Modes of entry** (`modes.md`). Greenfield authors outward from the vision. Capture reads an existing system and fills decision records with evidence, leaving undecided where there is none. Re-engineering is capture, then targeted revision of the records to change, then regeneration. All three are operations over the same six structures. The spine has to exist before capture or re-engineering is attempted.

**Verification** (`verification.md`), at three distinct levels. Artifact review: is the artifact complete and consistent before anyone consumes it? Implementation compliance: do the checks derived from artifact fields pass? Method validation: does the method itself hold up, measured by regeneration variance, ambiguity counts, and artifact counts? All three are first-class. Scattering testing across per-artifact guidance is how it gets lost.

**The harvest loop** (`harvest-loop.md`). Every agent run yields an ambiguity list and a set of decisions made while building. Each item becomes exactly one of: a ratified decision record, a revised artifact, a new question in a registry entry, or a new registry entry. The first two evolve the application. The last two evolve the method. The two loops stay separate.

## The owner's workflow this enables

The purpose of the whole thing, in one paragraph. An agent builds a prototype from the artifacts. The owner finds it unsatisfactory in places. Instead of patching code or starting over, the owner walks the decision records by subject. Each record shows who decided it and whether it is ratified. Records the owner likes are ratified. Records the owner dislikes are revised at the record, which is the root cause, and the derivation graph says what downstream artifacts and generated things must be regenerated. Modifying is cheaper than rebuilding because every choice the agent made is explicit, attributed, and reversible in one place.

## Coexistence with agent-method

Agent-method keeps its ground: the functional artifact types (vision, use case, component, interface), the workbench, the one-artifact-at-a-time discipline, and the regeneration test. The spine lives here and is built in phases small enough to validate against the workbench at each step. See `../plan.md`. The ideas in `../ideas/` continue to flow into agent-method's guides as their triggers fire. When agent-method's note pile becomes hard to use, which the artifact-count test will show, agent-method's types register into the spine. The spine is not retrofitted onto them.

## Vocabulary

Terms used throughout this directory. Where agent-method has a word for the same thing, that word is used.

- **spine**: the six structures above.
- **subject**: a thing in the system an artifact can attach to. System, component, interface, data store, environment.
- **concern**: a topic that cuts across subjects. Persistence, identity and access, observability, concurrency and failure, configuration, external dependencies, security, lifecycle, runtime environment, communication. A tag, not an organizer. The maturity criteria matrix adds testing and documentation as rows because every level asks something of them, but they are not concern tags on questions.
- **refinement stage**: logical, mechanism, infrastructure, operations. The traditional application, technical, DevOps, and Ops layers, understood as stages of one concern.
- **binding time**: design, build, deploy, runtime. Says which artifact holds an answer.
- **binding level**: organization standard, platform, system, component. Says who owns an answer and who inherits it.
- **artifact type**: an entry in the registry. Agent-method: type. **artifact**: an instance for a subject.
- **question**: one thing an artifact type asks. Agent-method: a guide question.
- **decision record**: the answer to one question for one subject. Agent-method: a line in a decisions note.
- **status**: undecided, decided, deliberately open with bounds, inherited, not applicable with reason.
- **provenance**: owner-stated, owner-ratified, agent-proposed, agent-made-while-building, extracted-with-evidence.
- **ratification**: unratified, ratified, rejected, superseded. Agent-method: ratified means the owner said so in conversation; a merge is never ratification.
- **regeneration**: producing an implementation again from artifacts alone. Agent-method: regeneration run, ADR 0007.
- **ambiguity**: a place the artifacts were silent, unclear, or contradictory, reported by an agent run. Agent-method: the run's ambiguity list.
- **harvest**: turning a run's ambiguities and build-time decisions into records, artifact revisions, or registry changes.
- **guide**: agent-method's term for the question list of an artifact type, held in a note under the guide / decisions / standard pattern.
