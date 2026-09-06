# Spec: `design-discussion-capture`

- **ID**: SKILL-SPEC-54447908e8
- **Source retrospective**: ../2026-09-06-41.md

## Intent

Turn a long design discussion between the owner and the agent into a durable, reviewable set of files: an objectives statement with inferred items flagged, a decisions log in which every conclusion is marked owner-stated or proposed, a set of one-screen idea files each tied to a named event in the project they will feed, and an index that reads in levels. The skill earns its place because a six-hour session produced dozens of conclusions and a half-formed framework that would have been lost at context truncation, and the owner needed to review them with provenance intact, ratify what he liked, and see at a glance which conditions each idea waits on.

## Trigger

Direct: "capture this", "write all this up", "preserve what we discussed", "capture my objectives", "we're trying to get the good stuff from this session captured", or a request to save ideas "in a structured, progressive disclosure way".

Proactive: a discussion has run for more than an hour, has produced conclusions the owner agreed to in conversation, and none of them is in a file yet. Offer once.

Negative: do not use for a retrospective on the agent's own work, which is the `self-retrospective` skill. Do not use to write the design itself; this captures the discussion, and the design documents are a separate deliverable the owner asks for.

## Inputs

- The conversation so far, including which conclusions the owner stated and which the agent proposed.
- The directory the owner named.
- The downstream project the ideas will feed, if any, and its vocabulary, obtained through `repo-orientation-report` when it is another repository.
- The owner's reading preferences. Load `human-scoped-deliverables` before writing.

## Outputs

- `objectives.md`: what is being built, why, who uses it, what it must do, the approach, boundaries, success criteria marked inferred where the owner did not state them, and what is not yet decided.
- `decisions-log.md`: one numbered row per conclusion, in order reached, each marked owner, owner-agreed, or proposed, plus open questions carried forward.
- `ideas/<id>.md`: one file per pullable idea with front matter (id, title, status, kind, event, friction, home, depends-on) and five short sections: the idea, why it matters, what it would look like in the downstream project, open questions, source.
- `README.md`: a three-level index, the interface with the downstream project as a table of named events and relationship kinds, the ideas table, and a table of what the downstream project already covers under its own names.
- A commit, a push, and a pull request.

## Workflow

1. Load `human-scoped-deliverables`. Its no-invented-jargon rule applies to everything below: no codes, no coined labels, names written out.
2. If the ideas will feed another repository, run `repo-orientation-report` on it first and keep its vocabulary list open.
3. Walk the conversation and list every conclusion in the order it was reached. For each, decide: did the owner state it, agree to it when the agent proposed it, or is it still only proposed? Write `decisions-log.md` from this list. Do not merge or reorder conclusions; the order is part of the record.
4. Write `objectives.md`. Anything the owner did not say but you believe is implied goes under a heading marked inferred, never mixed into stated objectives.
5. Split the proposals into ideas that can be adopted independently. For each, write one `ideas/<id>.md` file. Keep it to one screen.
6. Define the interface with the downstream project before filling in front matter. Build a closed list of named events from that project's own next steps, in its own words. Define three relationship kinds: rule, applied every time a recurring event happens; rider, carried into one specific work item's proposal; conditional, waiting on an event that may never happen. Give every idea exactly one kind and one event. Never join events with "or".
7. For each idea, write the friction the downstream project has already observed that justifies it. "None yet" makes the idea conditional. "Anticipated" marks a rider whose work item will create the friction.
8. Define what "pulled" means in one sentence: the idea's content appears in a ratified artifact of the downstream project, and the idea file links to it.
9. Write `README.md` with the levels in reading order: this file, then objectives and any overview, then detail, then ideas, then background. Include the events table, the kinds table, the ideas table with kind and event columns, and the already-covered table.
10. Run a consistency pass: every referenced file exists, no em or en dashes, headings within the agreed depth, and the events named in the README match the ones in every front matter and in any plan.
11. Commit, push, open the pull request, and in the reply list the judgment calls you made that the owner should confirm.

## Concrete examples

### Example 1: the architecture framework discussion

Input: a session that produced a framework for decisions between an idea and a running system, feeding `lago-morph/agent-method`. The owner stated about a third of the conclusions and the agent proposed the rest.

Steps: orientation on agent-method yields the words guide, decisions note, regeneration run, ambiguity, ratified. Thirty-seven conclusions go into the log, twelve marked owner. Fourteen ideas are written. The event list is agent-method's own sequence: any guide written or revised, any regeneration run recorded, implementation 3, persistent-storage guide, first guide that depends on another, type descriptions, component and interface types, guides outgrow one implementation, something above the workbench. Four ideas are rules, five are riders, five are conditionals.

Output: `architecture-ideas/README.md`, `objectives.md`, `decisions-log.md`, `ideas/` with fourteen files. The reply lists five judgment calls to confirm. The owner's first review asks for the interface to be less ambiguous and for codes to be replaced by names; both are one-pass fixes because the structure already separates kind, event, and friction.

### Example 2: a discussion about a testing strategy for an existing service

Input: a two-hour discussion in which the owner settles on contract tests for three interfaces and the agent proposes property-based tests and a mutation-testing gate.

Steps: no downstream repository, so the events are the service's own milestones: next interface version, first production incident, CI runtime over ten minutes. The log has nine rows, three owner-stated. Three ideas: contract tests as a rule on every interface change, property-based tests as a rider on the next interface version, the mutation gate as a conditional on CI runtime.

Output: the four files in `testing-ideas/`, a pull request, and a reply naming the one inference in objectives: that flakiness, not coverage, is the pain the owner is addressing.

## Anti-patterns

- **Free-text trigger fields.** The first version of the fourteen ideas had them, mixing work items, thresholds, symptoms, and external events. The owner called them confusing and ambiguous. Named events and one kind per idea fixed it.
- **Codes for events or levels.** The second version used E1 through E7 and M0 through M5. The owner rejected them; a twenty-file rewrite followed. Names only.
- **Presenting proposals as settled.** The decisions log exists so the owner can tell his conclusions from the agent's. Without the column the whole capture is untrustworthy.
- **Writing the design instead of capturing the discussion.** The spine documents were a separate request made after the capture, not part of it.
- **Skipping the already-covered table.** Eight discussed ideas turned out to exist in agent-method under other names; without the table they would have been proposed twice.

## Acceptance criteria

- [ ] Every conclusion in the log is marked owner, owner-agreed, or proposed, and the owner can find each of his own statements in the log.
- [ ] Every idea file has exactly one kind and one event, and the event appears verbatim in the README's events table.
- [ ] No coined codes or labels appear anywhere; a grep for patterns like `\bE[0-9]\b` and `\bM[0-9]\b` returns nothing.
- [ ] The README reads in levels, and a reader who stops after level two knows what the directory is for.
- [ ] The consistency pass runs clean before the push.

## Files this skill creates / modifies

- `<dir>/README.md`: the index and the interface with the downstream project.
- `<dir>/objectives.md`: objectives with inferred items flagged.
- `<dir>/decisions-log.md`: numbered, labeled conclusions and open questions.
- `<dir>/ideas/<id>.md`: one file per idea.
