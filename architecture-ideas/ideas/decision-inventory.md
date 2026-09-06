---
id: decision-inventory
title: The brainstorming notes are a seed list of future guides
status: discussed
kind: rule
event: G
friction: The decision-guides note already keeps a foreseen-areas list and writes guides only when needed. This rule adds the brainstorming areas to that list so the check happens before a run reports the gap.
agent-method-home: workbench/note/decision-guides.md, the foreseen-areas list
depends-on: []
---

## Idea

The brainstorming notes in `../reference/brainstorming.md` list decision areas across application, technical, DevOps, dev, and ops architecture. Each area is a candidate guide. Agent-method's decision-guides note foresees six: persistent storage, delivery to the device, code conventions, logging and diagnostics, data model and identity, carrying data between implementations. The notes add, among others: component lifecycle and state machines, interface contracts with pre- and postconditions, concurrency semantics, error taxonomy, external dependency pinning, configuration parameters, AuthN/Z, observability beyond logging, install and update, CI/CD and release, HA/DR and backup, SLA/SLO, security monitoring, audit logs.

## Why it matters for agents

The list is the answer to "what did we forget", asked before a guide is written rather than after a regeneration run reports an ambiguity.

## What it would look like in agent-method

Extend the foreseen-areas list in `decision-guides.md` with the areas from the notes, each with the trigger that would make it needed. Guides are still written only when triggered. The list itself is the pull-in point for most of the architecture ideas in this directory.

## Open questions

- Which of the areas the workbench will ever trigger, given its non-goals. Most Ops-architecture areas may never apply, which is fine and should be recorded as such.

## Source

Brainstorming notes 2026-08-26, transcribed in `../reference/brainstorming.md`.
