---
id: tight-fields-loose-guidance
title: Define question lists tightly and guidance loosely
status: discussed
kind: rule
event: any guide written or revised
friction: The implementation 1 versus 2 comparison worked because the decisions notes repeated the same numbered questions. UI-standards questions 11 and 12 were added at the end after implementation 2, which is the practice this rule names.
agent-method-home: decision-guides.md as a rule
depends-on: []
---

## Idea

Guidance improves with use and should start loose. The list of questions a guide asks should be tight from the start, because loose question lists produce decisions notes that cannot be compared across implementations, so the lessons never accumulate. Where the right question is not yet known, ask it anyway and let the answer be "deliberately open".

## Why it matters for agents

The comparison between implementations 1 and 2 worked because the decisions notes repeated the same questions and marked each "repeated unchanged" or "new". That only works when the question list is stable.

## What it would look like in agent-method

A sentence in `decision-guides.md`. Questions are added at the end, numbered, never renumbered, so decisions notes stay comparable. The existing guides already do this in practice.

## Open questions

None.

## Source

Discussion 2026-09-05, closing pushback.
