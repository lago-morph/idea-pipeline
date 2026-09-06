---
id: extraction-mode
title: Guides double as an interview script over an existing system
status: idea
kind: conditional
event: something above the workbench
friction: None yet. The workbench is built from the method; nothing pre-existing has been captured.
agent-method-home: a new procedure in ai/procedures/, then a method procedure
depends-on: [status-vocabulary]
---

## Idea

For an existing system, the guide questions are an interview script. An agent reads code, configuration, and documents, proposes an answer per question with evidence, and a human confirms. Questions with no evidence become "undecided", which is discovered debt. Answers that contradict each other are flagged. Answers that come from a level above the system are marked inherited.

## Why it matters for agents

It is the same catalog used the other way round, so nothing new is authored. The output is a populated set of decisions notes plus a debt list, which is the input to guided new work.

## What it would look like in agent-method

Not applicable to the workbench, which is built from the method. It applies when the method is pointed at something that predates it. The procedure would mirror `implement-by-subagent.md` in shape: tiered access, a clean-context subagent, a review checklist, a metrics row.

## Open questions

- Whether evidence links point at code lines, which drift, or at commits.

## Source

Discussion 2026-09-05, the three modes of use.
