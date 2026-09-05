# The harvest loop

Status: draft, 2026-09-05. Rides on the spine.

## What a run produces

Every regeneration run, in the shape of `implement-by-subagent.md`, yields four things the loop consumes.

| Product | Where it is today | What it holds |
|---|---|---|
| Ambiguity list | The subagent report, section "Ambiguities and gaps" | Every place the artifacts, guides, or procedures were silent, unclear, or contradictory; what the agent decided; where it recorded it |
| Records with provenance agent-made-while-building | The record's "Decisions made while building" section and the per-area notes | Every choice the artifacts did not dictate, with the alternatives seen and the reason |
| Checks | The automated-checks note and the script derived from it | Named booleans with a Source column, and the decisions made while writing them |
| Metrics row | The metrics table in the procedure | Tokens, tool uses, minutes, documents opened, checks, result, ambiguities, defects |

The report also carries suggested changes, one sentence each naming the file. Run 1 yielded 12. They are harvested like ambiguities.

## The four destinations

Each harvested item becomes exactly one of four things. An item that seems to need two is split into two items.

| Destination | What it means | Loop | Agent-method form today |
|---|---|---|---|
| Ratified record | The agent's answer stands. The owner says so in conversation; the record's ratification becomes ratified | Application | A line in a decisions note the owner marked up and left standing |
| Revised artifact | The artifact text that should have carried the answer was silent, unclear, or contradictory. It is corrected, and dependents regenerated | Application | Proposed markups to a ratified use case, listed for the owner, never applied by the reviewer |
| New question in a registry entry | The question was not asked by any artifact type, but an existing type is where it belongs | Method | A question added to a guide, with what to propose by default |
| New registry entry | No existing artifact type covers the ground | Method | A foreseen area in `decision-guides.md` becoming a guide; a note becoming a candidate for a real artifact type |

The decision rule, applied to one item at a time.

1. Does a registry entry already ask the question this item answers? If not, go to step 4.
2. Does the artifact instance hold a record for that question? If not, the agent chose in silence. The record it wrote is ratified, revised, or rejected. Ratified is the destination when the owner accepts the answer.
3. If a record or the governing text existed and was wrong, unclear, or contradictory, the destination is a revised artifact. The artifact is corrected first, per ADR 0007, and the derivation graph says what regenerates.
4. Does an existing registry entry cover the subject and concern? If yes, the destination is a new question in that entry. If no, it is a new registry entry, which the owner must approve.
5. A new question creates an undecided record for every subject it applies to. Those records are new items in the application loop, not part of this one (to confirm).

## Two loops, kept separate

| Loop | Evolves | Structures touched | Agent-method concern |
|---|---|---|---|
| Application loop | The application's specification | Decision records, artifacts, subject catalog | `workbench/` |
| Method loop | The method | Artifact type registry, guidance, applicability rules | `method/`, with the guides in `workbench/note/` as candidates until promoted |

Agent-method's three-concern layout is the existing form of this separation: `method/` holds what is reusable across applications, `workbench/` holds the application, `ai/` holds session context and working residue. The guides live in `workbench/note/` today as candidates for real artifact types. Promotion, the move of a guide into `method/types/`, is the moment an item crosses from the application loop into the method loop. The quality-standards guide already names the smaller form of promotion: a standard repeated unchanged for a second implementation is proposed for the implementation standards.

The separation matters because the two loops have different owners of change. An application decision is the owner's alone. A method change affects every future application and every future run, so it is proposed by retrospection and approved separately.

## The pruning rule

Every run adds questions and guidance. Without a removal rule the guides outgrow the tiered document access budget and a subagent skims. The rule, from the guidance-pruning idea:

1. Each question in a registry entry records the run in which it was added and the runs in which it caught something.
2. A question or piece of guidance that has not prevented an error in some number of runs is demoted to an appendix of the entry. The number is not yet chosen (to confirm).
3. The retrospective after each run proposes demotions alongside additions.
4. The metrics table carries a guide-size column, so the trend is visible.

A demoted question keeps its number. Questions are never renumbered, so records stay comparable across implementations.

## The gate

Every record with provenance agent-made-while-building and ratification unratified is harvested debt. All such records are ratified, revised, or rejected before the next implementation starts. This is the rule that keeps a prototype from silently becoming the specification.

In agent-method's procedure the gate sits at step 1: implementation record N is drafted first, as the subagent's whole input. Under the gate, record N cannot be drafted until every unratified record from implementation N-1 has a disposition. Rejected records with no replacement become undecided, and the next run must ask before choosing. Only the owner's word in conversation ratifies. A merge never does.

## What agent-method already does, and what the loop adds

Agent-method does most of this already. Step 8 of the review checklist folds findings back: questions into guides, decisions the review exposed into the implementation's notes, procedure revisions, and proposed markups to ratified use cases listed for the owner. The procedures in `ai/procedures/` are written by retrospecting on what was done. The decisions notes carry "repeated unchanged" and "new in implementation N" markers. The metrics table keeps one row per run.

The loop adds five things.

| Addition | Why |
|---|---|
| Provenance and ratification as fields | Unratified agent-made records become a query, not a reading exercise |
| The four destinations, named | Every item has exactly one place to go, and the reviewer records which |
| The application and method loops, named | A change to a guide and a change to a use case are different acts with different approvers |
| The gate | The next run cannot inherit unreviewed choices as if they were the specification |
| The pruning rule | Guidance has a removal path, so the tiers stay affordable |

## Worked example: implementation 2

Run 1 reported 15 ambiguities: 3 in the use cases, 10 in guides and procedures, 2 in the environment. The three use-case ambiguities were undo granularity, the new idea's position, and a contradictory clause. Each was found only by building.

| Item | What the agent did | Destination | Loop |
|---|---|---|---|
| Undo granularity | Chose snapshots with typed runs coalesced as one change; recorded in `implementation-structure-2.md`; the check `undoRevertsMostRecentChange` exercises it | Ratified record, if the owner accepts coalescing. If he wants the rule in the use case text, a revised artifact instead | Application |
| The new idea's position among placeholders | Placed it in the top group with the other empties; the check `newGivesEmptySelectedInTopGroup` exercises it | Revised artifact: the Edit ideas use case sentence is silent, and the reviewer lists a proposed markup for the owner (to confirm which sentence) | Application |
| A contradictory clause | Chose one reading and flagged it | Revised artifact: the owner resolves the contradiction in the use case | Application |
| The guides assumed the owner is present to close each decision | Invented a way to record decisions without him | New guidance in the registry entry: the guide now says what to write in that case | Method |
| "Repeated unchanged" was voluminous across seven notes | Wrote it out in full | A standard for repeated answers: promotion of a record to implementation "all" | Method |
| Two test hooks changed shape | Recorded old and new shape in the checks note | New question in a registry entry: question 10 of the test-method guide, which the guide says was added after implementation 2 | Method |
| WebKit not installable; Chromium stands in for Safari | Stated the gap in the report and the record's known gaps | Ratified record on the test-method question about harness and engine, status decided, with the gap as its bounds | Application |

The three use-case items stay in the application loop and reach the owner as proposed markups. The guide and procedure items are method changes and went into the guides and the procedure in the same review. Whether every one of the 15 was routed this way is not recorded in the files read (to confirm).

## Open questions

- Whether a new question's follow-on undecided records count as harvested items of the same run or of the next.
- How many runs without catching an error demote a question.
- Whether suggested changes and ambiguities are one list or two in the report.
- Whether the gate applies before a variance run on the same record, which by design starts from the same unratified state.
- Where the routing decision per item is recorded: the retrospective, the record's history field, or the metrics row (to confirm).
