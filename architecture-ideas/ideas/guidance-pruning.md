---
id: guidance-pruning
title: Guidance needs a removal rule, not just an accumulation rule
status: discussed
trigger: A regeneration run shows the subagent skimmed or ignored a guide, or a guide exceeds a size the procedure's document tiers can afford.
agent-method-home: decision-guides.md as a rule; implement-by-subagent.md metrics
depends-on: []
---

## Idea

Every implementation run adds questions and guidance. Nothing removes any. Within a year the guides exceed the context an agent will actually read, and it skims. A pruning rule is needed from the start. A simple one: guidance that has not prevented an error in some number of runs is demoted to an appendix.

## Why it matters for agents

Cognitive load is a real resource for agents as much as for humans. The tiered document access in the implementation procedure is already a context budget. Guides that grow monotonically will break it.

## What it would look like in agent-method

Each guide question records the run in which it was added and the runs in which it caught something. The metrics table in the implementation procedure gains a column for guide size. The retrospective after each run proposes demotions alongside additions.

## Open questions

- What counts as "prevented an error" when the evidence is that the agent simply did the right thing.

## Source

Discussion 2026-09-05.
