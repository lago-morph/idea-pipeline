---
id: verification-per-question
title: Every guide question states how compliance is checked
status: discussed
trigger: The execution methods for the quality-standards guide are built, which the handoff schedules for after the first rounds of implementing the workbench.
agent-method-home: decision-guides.md as a rule; test-method-definition.md and automated-checks notes as the mechanism
depends-on: []
---

## Idea

Every question a guide asks states how an implementation's compliance with the answer would be checked. A question with no verification method is one of three things: a standard, which belongs in a standards note; advice, which belongs in the guide's walkthrough guidance; or not really a decision. This is the discipline that keeps a guide from turning into prose.

## Why it matters for agents

It is what makes an artifact a specification rather than documentation. The automated-checks notes already do this for use-case behavior: "the script is derived from this note". The idea extends the same rule to every guide question, including ones whose check is a review step rather than a script.

## What it would look like in agent-method

A "verified by" column on each guide question, filled with one of: automated check (names the check), review checklist item, or none. Any "none" gets reclassified or removed. The review checklist in `implement-by-subagent.md` gains a step: every decided question has a check.

## Open questions

- Whether UI-standards questions (colors, sizes) are checked automatically or by screenshot review.

## Source

Discussion 2026-09-05. Brainstorming notes: the four DoD candidates are all verifiable items.
