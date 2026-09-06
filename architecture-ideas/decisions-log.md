# Decisions log

Status: draft, 2026-09-05. Conclusions reached in the working session of 2026-09-05, in order. Each is marked **owner** where Jonathan stated or agreed it in conversation, or **proposed** where the AI partner proposed it and the owner has not yet ruled. Proposed items are strawmen until ratified. This log is for future sessions to know what is settled and what is open.

| # | Conclusion | Standing |
|---|---|---|
| 1 | The exercise is to structure all the decisions needed to go from an idea to a running system, because architecture left fuzzy fails when agents must produce detailed specifications and environments from it | owner |
| 2 | A spec is complete when every decision an implementing agent would otherwise make is answered or explicitly left open with bounds. Silence and deliberate freedom must be distinguishable | proposed |
| 3 | Non-functional requirements generate the decisions the toy app will not surface on its own. Stress the toy app by adding them one at a time | owner |
| 4 | Variance across runs of the same spec on different models or settings measures spec incompleteness. Agent-method's regeneration test is this | proposed, and already agent-method practice |
| 5 | Binding time, design, build, deploy, or runtime, is worth capturing on every decision | owner |
| 6 | The three uses, extraction, guided new work, and checklist, are operations on one catalog of decisions | proposed |
| 7 | Every decision carries a status: undecided, decided, deliberately open with bounds, inherited, not applicable with reason | proposed |
| 8 | The toy app can answer every decision now, mostly as not applicable, which validates coverage without needing hard answers | owner agreed |
| 9 | Subject-based organization is better in the long run. Concern is for auditing and completeness review. One artifact as the primary driver gives implementation its boundaries | owner |
| 10 | The end state is artifact definitions with dependencies, canned guidance for creating and relating them, guidance for agents implementing from them, and guidance for testing compliance | owner |
| 11 | Define artifacts loosely and stress-test with every use, collecting lessons learned | owner. Amended by proposed: question lists tight from the start, guidance loose |
| 12 | An applicability matrix says when each artifact is needed and where it can be skipped with a reason | owner |
| 13 | The applicability matrix is driven by a system profile of six to eight coarse characteristics, not by example system types | proposed |
| 14 | The four kinds of guidance are five: authoring, relating, consuming, verifying, and reviewing. Reviewing is the definition of done, which is what the DoD boxes in the notes mark | proposed |
| 15 | Every question states how compliance is verified. A question that cannot is a standard, advice, or not a decision | proposed |
| 16 | Guidance needs a pruning rule as well as an accumulation rule | proposed |
| 17 | The artifact count the toy app needs is a health metric for the method | proposed |
| 18 | The brainstorming taxonomy follows traditional architect roles. The layers are refinement stages of one concern, and concern should be a tag, not a top-level split | proposed |
| 19 | Requirements are inputs that decisions trace to, not decisions. Standards constrain how decisions are answered and are a separate kind of thing | proposed |
| 20 | Agent-method is the home for functional requirements and basic application architecture. Architecture ideas are pulled in over time as needed | owner |
| 21 | Nuggets alone reproduce the free-form-notes collapse. A spine is needed: the structure that ties artifacts, concerns, and subjects together for a whole system | owner |
| 22 | The framework must support greenfield, capture of an existing system, and re-engineering, and must make it cheap to ratify what the owner likes and revise the rest at root cause | owner |
| 23 | The framework must show what needs to be done to reach each level of maturity | owner |
| 24 | The spine is six structures: system profile, maturity ladder, subject catalog, artifact type registry, decision records, derivation graph. Three things ride on it: modes, verification at three levels, the harvest loop | proposed. Owner: "love it", pending markup |
| 25 | The spine is the data model. The earlier "start with a data model" objective is satisfied by defining the six structures, not by a separate model | proposed |
| 26 | Anything new must prove it cannot be a field on one of the six structures before becoming a seventh | proposed |
| 27 | The spine is instantiated for the workbench here as a shadow before anything is proposed to agent-method, and agent-method receives pieces only at their triggers | proposed |
| 28 | Provenance on every decision record, including agent-made-while-building, is what makes review by ratification possible | proposed |
| 29 | The profile has an eighth characteristic, integration surface, because none of the seven switches on communication or external dependencies by itself. May collapse into deployment topology | proposed, to confirm |
| 30 | The workbench's profile caps it at Durable, from concurrent users one, single device, and best effort alone. Durable is therefore also its plausible target | proposed |
| 31 | The workbench's statefulness is "local" not "none", because the vision commits to durable storage; memory-only implementations are a maturity fact, not a profile fact | proposed |
| 32 | The registry seed merges the brainstorming areas to 49 rows; a merged area gets its own row only when an implementation shows it needs separate questions | proposed |
| 33 | The persistent-storage registry entry is the first piece to propose to agent-method, timed to the Save ideas use case, carrying status vocabulary, binding time, and verification per question with it | proposed |
| 34 | The workbench catalog treats the check-hooks contract as an interface subject and the working repository as an environment subject, so the inference is visible | proposed, to confirm |
| 35 | End-user management is an Operated criterion, not Enterprise | proposed, resolving a contradiction between the ladder's criteria and matrix |
| 36 | Each nugget has one relationship kind, rule, rider, or conditional, and one agent-method event from a fixed, named list shared with the plan. A nugget names the friction in agent-method that justifies it. "Pulled" means its content appears in a ratified agent-method artifact | owner asked for the ambiguity removed; the scheme is proposed |
| 37 | No invented codes for things the owner reviews or follows. Events and maturity levels are written out by name everywhere | owner |

## Open questions carried forward

- Whether decision records are one file per record or one decisions note per subject per implementation. Decided in phase 2 by trying both on real content.
- Whether the spine eventually lives in its own repository. Decided in phase 6.
- Whether "system" is a subject kind or the vision's implicit subject. To be settled when the subject catalog is instantiated.
- How coarse the profile can be. Six to eight characteristics is the starting bet.
- Whether runtime binding time exists for the workbench before it has an operator other than the owner.
- Whether the criteria matrix in the maturity ladder stays authored or is generated from the registry rows' applicability rules. Both files raise it. One source of truth is wanted.
- Whether the five verification-related rows in the registry stay there or move under verification.md.
