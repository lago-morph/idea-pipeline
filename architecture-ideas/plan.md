# Plan

Status: draft, 2026-09-05. How this work matures in parallel with agent-method, builds the pieces agent-method needs as it needs them, and uses the idea-workbench application as its test bed.

## Principles

- **Agent-method's rule applies here too.** Nothing lands in agent-method ahead of its event, per the events table in `README.md`. Nothing here is defined without being instantiated against a real application in the same phase.
- **Shadow first, then pull.** Each spine structure is instantiated for the workbench here, in `testbed/`, before anything is proposed to agent-method. The shadow is the proof that the structure fits real content. When it does, the piece agent-method needs is proposed there through agent-method's own process, one artifact at a time, for the owner's markup.
- **One structure at a time.** The same discipline agent-method learned the hard way. Each phase below has an exit test. A phase does not start until the previous phase's exit test passes.
- **Six structures, no more.** Anything new must prove it cannot be a field on one of the six. The plan includes a standing check for this.
- **The owner ratifies.** Every conclusion here is proposed until the owner says otherwise in conversation. `decisions-log.md` tracks which is which.

## Phases

### Phase 0: capture

Everything from the 2026-09-05 session written down: the brainstorming transcription, objectives, the nuggets in `ideas/`, the spine drafts, this plan, and the inventory.

Exit test: the owner has marked up `objectives.md` and `spine/overview.md`, and the vocabulary in the overview is ratified or revised.

### Phase 1: definitions

The six structures and the three riders exist as definitions, each one file under `spine/`, each with fields, rules, and open questions. Drafts exist from phase 0. This phase is the owner's markup and the resulting revisions.

Exit test: every `spine/` file is ratified, or has its open questions reduced to ones that need an instantiation to answer.

### Phase 2: instantiate on the workbench

The workbench, as it stands in agent-method on the day this phase starts, is expressed through the spine in `testbed/workbench/`:

- Its system profile, from the vision's non-goals and the implementation records.
- Its current maturity level and a plausible target, with the gap listed.
- Its subject catalog, inferred from the vision, the use cases, and the implementations.
- Every decision in implementation records 1 to 3 and their per-area notes rewritten as decision records with status, provenance, and ratification. Decisions the owner has ratified in conversation are marked ratified. Decisions the run made are marked agent-made-while-building and left unratified unless the owner has since accepted them.
- The derivation links for implementation 2: use case to check to code, at artifact granularity.

This is the not-applicable walk from `ideas.md`, done through the spine instead of through a checklist. Expect most profile-driven skips to be "not applicable, single user by design" and similar.

Exit test: every existing decision in the workbench fits a record without forcing. Every place it does not fit has produced a change to a spine definition, recorded in `decisions-log.md`. The count of artifacts and records is recorded as the first metrics row.

### Phase 3: the registry, and the first piece agent-method needs

Seed the artifact type registry from agent-method's existing types, its six foreseen guides, and the brainstorming inventory, each row with an applicability rule in profile and maturity terms.

Write the persistent-storage entry in full, registry-shaped: numbered questions, each with concern, binding time, option space, and verified-by. This is timed to agent-method's Save ideas use case, which is the next in its build order and the trigger for its persistent-storage guide. The entry is proposed to agent-method as that guide, in agent-method's guide shape, with the registry fields as extra columns. That carries two riders across at once, `status-vocabulary` and `binding-time`, and the `verification-per-question` rule applies to the guide as it is written.

Exit test: the persistent-storage guide is in agent-method for markup, and the implementation that uses it produces decision records the owner can review by subject.

### Phase 4: verification and harvest

Write the three verification levels and the harvest loop as procedures, in the shape of agent-method's `ai/procedures/`. Run the next workbench implementation's harvest through them: ambiguities and build-time records sorted into the four destinations, the ratification gate applied before the following implementation, and the metrics table extended with artifact count, record count, guide size, and ambiguity count.

Propose to agent-method whatever the run shows it needs. The likely candidates are the ratification gate as a lesson, the extra metrics columns, and the artifact review checklist as the first "reviewing" guidance on a type description.

Exit test: one full loop has run on a real implementation, and every harvested item has a destination.

### Phase 5: modes

Greenfield is what phases 2 to 4 exercise. This phase adds the other two.

Capture: pick one existing small system with no specification and run the capture procedure with a clean-context subagent. The candidate should be small enough to finish and unfamiliar enough that the agent cannot guess. The output is a populated catalog with evidence and a debt list.

Re-engineering: revise one ratified workbench decision at the record, for instance the persistence answer, and regenerate through the derivation graph. Measure how much was regenerated and whether anything outside the graph had to change.

Exit test: both procedures have run once, and the derivation graph's reverse walk found the root cause of at least one prototype behavior the owner disliked.

### Phase 6: stress

Change the workbench's profile in one characteristic at a time and watch which records flip from not applicable to undecided. Then specify a second application with a different profile, small, to see whether the spine transfers. Then decide whether the spine moves to its own repository and agent-method registers its types into it.

Exit test: the artifact count for the workbench is still small, and the second application's required artifact set was computed from its profile rather than chosen by hand.

## Sync points with agent-method's own sequence

Event ids match the events table in `README.md`, which is where each nugget names its event.

| id | Agent-method event | What this work does at that point |
|---|---|---|
| E1 | Implementation record 3 is marked up and the implementation 3 run happens | Phase 2: rewrite its record as decision records; first metrics row |
| E2 | Save ideas is ratified and the persistent-storage guide is written | Phase 3: the registry-shaped guide is the proposal, carrying status-vocabulary and binding-time as riders |
| E3 | A guide is written whose questions depend on another guide's answers | dependency-kinds rides on it |
| E4 | Type descriptions are written in `method/types/` from real instances | five-kinds-of-guidance becomes the section list |
| E5 | The component and interface types are written | refinement-stages rides on them; the subject catalog informs them |
| E6 | The guide set outgrows one implementation | concern-tags, guidance-pruning, and system-profile become riders on whatever work the event creates; the registry and decision records are offered as the replacement for note clusters |
| E7 | A level above the workbench appears: a platform, a second application, or an existing system | Phase 6; binding-level and extraction-mode become riders; the spine's transfer test |
| G | A guide is written or revised | The four rules apply: tight-fields-loose-guidance, decision-inventory, verification-per-question, and for M below, artifact-count-test |
| M | A regeneration run's metrics row is recorded | artifact-count-test applies; phase 4's metrics columns |

## Standing checks

- **Seventh-structure check.** Any proposal for a new spine structure is first attempted as a field on an existing one. Recorded either way.
- **Artifact count.** Recorded at every implementation. A rising count without a maturity change is the warning.
- **Vocabulary drift.** New coinages are checked against `spine/overview.md` and agent-method's terms before use.
- **Shadow before canon.** No spine definition changes without a workbench instantiation that motivated it.

## Risks

- **Abstraction drift.** The failure mode of the archived attempts. Mitigated by the shadow-first rule and by the exit tests, every one of which requires real content.
- **Two homes for one thing.** The workbench in agent-method and its shadow here can diverge. Mitigated by the shadow being disposable: it is regenerated from agent-method at the start of each phase, never edited independently of it.
- **The spine growing.** Mitigated by the seventh-structure check. If it fails repeatedly, the six were wrong, and that is worth knowing early.
- **The owner's attention.** Every phase needs markup. The plan is paced by that, not by what an agent can produce.
