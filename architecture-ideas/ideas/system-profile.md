---
id: system-profile
title: A system profile decides which guides are required
status: discussed
trigger: The list of foreseen guides grows past what one implementation needs, or the method is applied to a second application with a different shape.
agent-method-home: a new note first (per the promotion path), then possibly a method-level artifact type
depends-on: [status-vocabulary, decision-inventory]
---

## Idea

A short profile of the system, six to eight characteristics with two or three levels each, drives which guides and artifacts are required and which are skipped with a reason. Candidate characteristics: number of concurrent users, statefulness, availability target, deployment topology, data sensitivity, expected lifetime, number of teams. A single-user memory-only TUI and a Kubernetes transaction processor differ on these few values, and the required artifact set falls out of the values.

## Why it matters for agents

Every traditional architecture framework collapsed under its own artifact count. The profile is the antidote: a small system produces a small artifact set mechanically, and "skipped because" is the profile value rather than a judgment call. Adding a non-functional requirement changes the profile, which turns guides on. That is the stress test, made structural.

## What it would look like in agent-method

The workbench today does this by hand: guides are written "when the first implementation that needs them is being planned, not before". The profile makes that rule computable. It would start as a note with a table, artifact type by characteristic, and the workbench's own profile filled in. The vision's non-goals already state most of the workbench's profile values.

## Open questions

- Whether the profile is a section of the vision, a note, or its own type.
- How coarse the characteristics can be and still discriminate usefully.

## Source

Discussion 2026-09-05, prompted by the single-user TUI versus Kubernetes example.
