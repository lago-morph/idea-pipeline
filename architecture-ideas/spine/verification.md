# Verification

Status: draft, 2026-09-05. Rides on the spine.

## Why three levels

The overview names three levels and says all three are first-class. Each answers a different question, consumes different inputs, and is run by a different party. Keeping them apart is what stops testing from being scattered across per-artifact guidance and lost. Agent-method already holds pieces of each level. This note says which piece belongs to which level, and what the spine adds.

## The three levels at a glance

| Level | Question it answers | Consumes | Produces | Who runs it | When it runs |
|---|---|---|---|---|---|
| 1. Artifact review | Is this artifact complete and consistent before anyone consumes it? | One artifact, its registry entry, the records it holds, the records it must agree with | A pass, or a defect list of missing and disagreeing records | Agent first; the owner at markup | Before the artifact is consumed; before a regeneration run starts |
| 2. Implementation compliance | Does the produced thing honor what the artifacts decided? | The artifact fields that state a check, the automated-checks note, the implementation | Check results, a PASS/FAIL line, review findings | A script for automated checks; a reviewer for checklist items; the owner at the checkpoint | Before delivery; at the checkpoint |
| 3. Method validation | Does the method itself hold up? | Metrics rows across runs, ambiguity lists, artifact counts, guide sizes | A trend, and method changes proposed through the harvest loop | A human reading the metrics table; an agent extracting the numbers | After every regeneration run |

### Level 1: artifact review

The definition of done for an artifact is per artifact type. It is the reviewing guidance in the artifact type's registry entry, the fifth of the five kinds of guidance. The brainstorming candidates for a definition of done are reviewing guidance for specific types: scenarios with test data, contracts per state, example input and output, postconditions.

Three checks apply to every artifact regardless of type.

| Check | What it asks | Scope |
|---|---|---|
| Completeness | Does every question the registry entry asks have a record with a status? "Not applicable with reason" counts. Silence does not | One artifact against its registry entry |
| Consistency | Do the records that must agree agree? Uses the must-be-consistent-with links of the derivation graph | One artifact against the records it links to |
| Silence check | Across the required artifact set for this subject, computed from the profile and the maturity level, is any required question without a record anywhere? This catches artifacts that do not exist at all, which completeness cannot see | One subject against the required set (to confirm: whether this is a separate check or completeness run at subject scope) |

What agent-method has for it: the decision-guides pattern, under which a decisions note answers every question its guide asks; the status-vocabulary rule that a guide question with no entry in the decisions note is a defect; the review checklist in `implement-by-subagent.md`, whose steps 4 and 5 read every per-area note and run the link validator; the use-case neutrality check against ADR 0006; and ADR 0007's rule that reviewing an implementation includes reviewing the artifact it was derived from. The consistency check has no mechanism yet beyond `related-to` links and a reader.

### Level 2: implementation compliance

The checks are derived from artifact fields. The pattern is the automated-checks note: the script is derived from the note, and when they disagree the note is corrected first and the script regenerated. Each check in the note is a named boolean with its step, its expected observation, and a Source column naming the use-case sentence or record decision it traces to. The hooks the implementation must expose are a table, a contract between implementation and checks.

Per question, the registry entry states how compliance is verified. The verified-by value is one of: automated check, naming the check; review checklist item; or none. See the rule below for what happens to "none".

The reviewer's side is the review checklist in `implement-by-subagent.md`: rerun the delivered check script and PASS must reproduce; read the record, every per-area note, and the implementation source; run the link validator; write and run an independent script from the use case text, not from the checks note; look at one screenshot per orientation. The owner's side is the checkpoint on the real device, which the test-method guide describes as what he is asked to look at, never what he found.

What agent-method has for it: the test-method guide, with its ten questions about harness, sizes, loading, output, pass rule, and what a person checks; the quality-standards guide, which states what is wanted per kind of check and leaves the how to execution methods built later; the automated-checks notes for implementations 1 and 2; `verify.js` per implementation; and the procedures in `ai/procedures/`. Not done for implementations 1 or 2, so no procedure exists: unit tests, type checking, linting, integration tests.

### Level 3: method validation

This level measures the method, not the application. Every measure comes from a regeneration run, which is why the run is done for every implementation and not as an experiment.

| Metric | What it measures | Source | In agent-method today |
|---|---|---|---|
| Regeneration variance | Where the artifacts were silent: each divergence between two runs of the same record names a missing or underspecified question | Two or more runs of the same implementation record on different models or thinking settings; compare the decisions notes | Planned. Run 1 exists; no second run yet |
| Ambiguities reported | The specification's defect count per run | The subagent report, section "Ambiguities and gaps" | A column in the metrics table. Run 1: 15 |
| Defects found in review | What the checks and the artifacts missed | The review checklist | A column. Run 1: 0 |
| Artifact count | Whether the method has collapsed under its own weight; a proxy for how much a subagent must read | Artifacts given to the subagent, by type, per maturity level | "Repo docs opened" column, 25 for run 1. A by-type column is proposed |
| Guide size | Whether the tiered document access budget still holds | Size of each guide in tier 3 | Proposed column, from the guidance-pruning idea |
| Checks per orientation | Coverage of the check script | The script's output | A column. Run 1: 46 |
| Tokens, tool uses, minutes | Cost of a run | The completion notification and the transcript | Columns |

The maturity ladder gives the expected shape: artifact count should rise with maturity level and stay small at Sketch and Prototype. The workbench is the standing test. If it needs around five artifacts the method scales down; if it needs twenty, the applicability rules are not working.

What agent-method has for it: the metrics table and its extraction commands in `implement-by-subagent.md`, the one row for run 1, and the note that comparing rows across models answers the repeatability and context questions.

## Every question states its verification

The rule: every question in a registry entry states how an implementation's compliance with its answer would be checked. This is what makes an artifact a specification rather than documentation.

| Verified-by value | Meaning | Where the check lives |
|---|---|---|
| Automated check | Names the check | The automated-checks note; the script derived from it |
| Review checklist item | A step a reviewer performs | The review checklist of the procedure |
| None | The question is not a verifiable decision | Reclassified, see below |

A question with verified-by "none" is one of three things, and is reclassified accordingly.

1. A standard. It moves to a standards note. In the spine it becomes a record with implementation "all" and a binding level.
2. Advice. It moves into the walkthrough guidance of the registry entry and stops being a question.
3. Not really a decision. It is removed.

The review checklist gains one step: every decided question has a check. On the record, the evidence field points at where the check ran or where the reviewer looked.

## How verification results feed the harvest loop

Each level produces items the harvest loop routes. The routes are fixed by level.

| Level | Result | Harvest destination |
|---|---|---|
| 1 | A required question with no record | An undecided record in the owner's work queue |
| 1 | A question that cannot be answered even as not applicable | A badly phrased question: revised in the registry entry |
| 1 | Two records that must agree and do not | A conflict for the owner; one record is revised |
| 2 | A failing check | The artifact is corrected first, then the file regenerated, per ADR 0007 |
| 2 | A check that could not be written for a decided question | The question has verified-by "none"; reclassify it |
| 2 | A reviewer finding the checks missed | A new check in the automated-checks note, and a "defects found in review" count |
| 3 | A divergence between two runs | A missing question in a registry entry |
| 3 | Guide size over budget, or a question that caught nothing in N runs | A demotion proposed under the pruning rule |
| 3 | Artifact count rising faster than maturity level | A revised applicability rule in the registry |

Levels 1 and 2 mostly feed the application loop. Level 3 feeds the method loop. See `harvest-loop.md`.

## Open questions

- Whether UI-standards questions such as colors and sizes are verified automatically or by screenshot review.
- Whether the silence check is its own check or the completeness check run at subject scope (to confirm).
- What counts as "prevented an error" when the evidence is that the agent simply did the right thing.
- Whether per-area decisions notes count individually in the artifact count or as part of their implementation record.
- How regeneration variance is measured once two runs exist: a diff of decisions notes, or a count of records that differ (to confirm).
