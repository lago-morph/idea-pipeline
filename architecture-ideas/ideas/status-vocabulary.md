---
id: status-vocabulary
title: Every decision carries an explicit status
status: discussed
kind: rider
event: E2
friction: Run 1 reported 15 ambiguities, every one a place the artifacts were silent and the agent chose. Implementation records already write skips with reasons by hand: "persistent storage: none, memory only".
agent-method-home: workbench/note/decision-guides.md (the guide / decisions / standard pattern) and implementation-record-definition.md
depends-on: []
---

## Idea

Every question a guide asks gets one of five statuses in the decisions note that answers it: undecided, decided, deliberately open with stated bounds, inherited from a higher level, or not applicable with a reason. Silence is never a valid state.

## Why it matters for agents

An agent treats silence and deliberate freedom the same way: as license. The regeneration runs already show this. The 15 ambiguities from implementation 2 are places where the artifacts were silent and the agent chose. A status makes silence visible before the run instead of after.

## What it would look like in agent-method

Implementation records already do this informally. "Persistent storage: none, memory only" is "not applicable, with reason". The change is to name the five statuses in `decision-guides.md` and require each decisions note to give one per guide question. A guide question with no entry in the decisions note is a defect the review checklist catches.

## Open questions

- Whether "deliberately open" needs its bounds stated in the decisions note or in the guide.
- Whether "inherited" is useful before a second application or a platform exists. See `binding-level.md`.

## Source

Discussion 2026-09-05. Brainstorming notes: "Explicit items not specified" appears twice, under application and technical architecture.
