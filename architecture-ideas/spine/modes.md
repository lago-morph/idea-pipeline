# Modes of entry

Status: draft, 2026-09-05. Rides on the spine.

## Three modes, one set of structures

Greenfield, capture, and re-engineering are three ways into the same six structures. None adds a structure. Each is a sequence of operations over the profile, the maturity ladder, the subject catalog, the registry, the records, and the derivation graph. What differs is where the answers come from: the owner's head, the existing system, or a mix. The spine has to exist before capture or re-engineering is attempted.

## Greenfield

Author outward from the vision. The owner decides. The agent orders the questions, supplies context, checks consistency, and cross-references.

Preconditions on the spine: the system profile is set; the maturity target is set; the registry has entries for every artifact type required at the target level; the subject catalog holds at least the system subject.

1. The owner sets the profile and the maturity target. Together they compute the required artifact set: which registry entries need instances, at which completeness, for which subjects.
2. The agent proposes subjects from the vision. The owner ratifies them into the subject catalog.
3. The agent creates an undecided record for every required question of every subject. This is the work queue.
4. The agent orders the queue by the must-exist-before links of the derivation graph. This is the guided walk.
5. For each record in order, the agent presents the question, the records it depends on with their answers, the records it constrains, and prior decisions on the same subject.
6. The owner answers, or marks the record deliberately open with bounds, or not applicable with a reason.
7. The agent checks the answer against the must-be-consistent-with links and raises conflicts immediately. Example: a synchronous interface on a component whose concurrency answer is a background worker.
8. Answers with design-time binding get an ADR, referenced from the record's rationale. Answers with other binding times are recorded in the artifact their binding time names.
9. Artifact review, level 1, runs on each artifact before it is consumed.
10. A regeneration run builds the implementation. Its products enter the harvest loop.

Outputs: a populated subject catalog; artifacts with a record per required question, provenance owner-stated; ADRs for design-time decisions; the derivation graph at artifact level.

## Capture

The guides are an interview script over an existing system. Nothing new is authored. The catalog is used the other way round.

Preconditions on the spine: the profile is set; the maturity ladder exists, so the level to capture at is known; the registry has entries for the types required at that level. The subject catalog need not exist: proposing it from the system is the first step.

1. The owner sets the profile and the maturity level to capture at.
2. The agent reads the system and proposes the subject catalog with evidence. The owner ratifies it.
3. For each required question of each subject, the agent reads code, configuration, and documents and proposes a record with evidence, provenance extracted-with-evidence.
4. A question with no evidence becomes a record with status undecided. This is discovered debt, not a gap in the registry.
5. Records whose evidence contradicts other records are flagged as conflicts for the owner to resolve.
6. Records whose answer comes from a level above the system, platform or organization standard, are marked inherited and point at the source.
7. The owner confirms, corrects, or rejects each proposed record. Confirmation is ratification.
8. The output is a populated catalog plus a debt list: every undecided record, ordered by dependency.
9. The debt list is the first input to the greenfield walk, from step 4 above.

Outputs: the subject catalog; a record per required question with evidence links; the debt list; the conflict list; the derivation graph's reverse edges, since each evidence link runs from a record to the thing in the system that embodies it.

## Re-engineering

Capture, then mark the records to change, then regenerate through the derivation graph. This is where "modifying is easier than building" pays off: every choice is explicit, attributed, and reversible in one place, and the graph bounds what must be rebuilt.

Preconditions on the spine: capture is complete and its records are ratified; the derivation graph exists at least at artifact level, linking records to the artifacts and to the existing generated things.

1. Capture the system, per the procedure above, including ratification.
2. The owner walks the records by subject and marks the ones to change. Each becomes a superseding record with provenance owner-stated and a link to the record it replaces.
3. For each revised record, the agent performs the forward walk of the derivation graph and lists what depends on it: artifacts, other records, generated code, checks.
4. Artifact review, level 1, runs on every artifact the walk touched. Records that must agree with the revised one are revised or flagged.
5. A regeneration run rebuilds the affected set from the artifacts. Nothing outside the walk is touched.
6. Implementation compliance, level 2, runs the checks derived from the revised fields.
7. The run's products enter the harvest loop.

Outputs: a superseded chain in the records' history fields; regenerated artifacts and generated things for the affected set; a metrics row.

## Running a mode with a clean-context subagent

Each mode runs in the shape of `implement-by-subagent.md`: a clean-context subagent, tiered document access, the forbidden set named, outputs named by the artifacts' own conventions, state changes forbidden, a report with fixed sections, a review checklist, and a metrics row. The unit of work is one subject, or one artifact, per subagent, keeping the one-artifact-at-a-time discipline.

| Element | Greenfield | Capture | Re-engineering |
|---|---|---|---|
| Tier 1, read fully | The registry entry, the profile, the subject catalog entry, the conventions, the ADRs | The same, plus the maturity level to capture at | The same, plus the revised records and their forward-walk list |
| Tier 2, on demand | The records the question depends on, with their answers | The code, configuration, and documents named for the subject | The artifacts the walk touched, and the previous generated things |
| Forbidden by name | Session context: the handoff, plans, lessons, retrospectives, archives, git history | The same | The same |
| Outputs | Proposed records, provenance agent-proposed; undecided where it cannot propose; a conflict list | Proposed records, provenance extracted-with-evidence; undecided where no evidence; conflicts; inherited markers | Regenerated artifacts and generated things; checks; records made while building |
| Report sections | Documents read; questions it could not answer; conflicts raised; suggested changes | Documents read; records proposed; undecided; conflicts; inherited; suggested changes | Documents read; ambiguities and gaps; procedure deviations; check results; time sinks; suggested changes |
| Metrics row | Questions presented, answered, deferred; conflicts | Questions asked, answered with evidence, undecided, conflicts, inherited | The existing row of the implementation procedure |
| Review | The owner decides and ratifies each record | The owner confirms, corrects, or rejects each record | The existing review checklist, plus a diff of the affected set against the walk |

In greenfield, the subagent never decides. It proposes, and the human decides in conversation. In capture, the subagent proposes with evidence, and no evidence means undecided rather than a guess. In re-engineering, the subagent builds, and the records it makes while building are harvested like any run's.

## Comparison

| | Greenfield | Capture | Re-engineering |
|---|---|---|---|
| Starting input | The vision and the owner | An existing system | A captured, ratified catalog |
| Who proposes records | The agent, from the walk order | The agent, from evidence | The owner, by revising |
| Dominant provenance | owner-stated | extracted-with-evidence | owner-stated superseding extracted-with-evidence |
| What undecided means | Not yet reached in the walk | No evidence found: discovered debt | A rejected record with no replacement |
| Walk order | must-exist-before, forward | By subject, in any order | Forward walk of derives-from from each revised record |
| First structure that must exist | Profile and maturity target | Profile and registry | The derivation graph |
| Main output | Populated artifacts and ADRs | Populated catalog plus debt list | Regenerated affected set |
| Agent-method today | The workbench itself, one artifact at a time | Not applicable to the workbench; a new procedure would be needed | Not attempted |

## Open questions

- Whether evidence links in capture point at code lines, which drift, or at commits.
- Whether "inherited" is useful before a second application or a platform exists.
- Whether capture at a low maturity level and then raising the level is the same as greenfield over the debt list, or a fourth path (to confirm).
- How a capture subagent is scoped when a subject's evidence is spread over many files: by subject, or by concern (to confirm).
- Whether re-engineering's regeneration run should be a full run of the implementation record, or a partial run over the affected set only, since the procedure today regenerates whole implementations.
