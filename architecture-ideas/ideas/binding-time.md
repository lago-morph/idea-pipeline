---
id: binding-time
title: Tag each decision with when it binds
status: discussed
kind: rider
event: persistent-storage guide
friction: Anticipated, not yet observed. The storage guide's question on where the store lives is the first deploy-time question agent-method will ask, so the column is proposed with that guide.
agent-method-home: workbench/note/decision-guides.md, as a column on each guide question
depends-on: [status-vocabulary]
---

## Idea

Each guide question is tagged with its binding time: design, build, deploy, or runtime. The tag says which artifact holds the answer. Design-time answers live in ADRs. Build-time answers live in the specification and the decisions notes. Deploy-time answers live in configuration. Runtime answers live in policy.

## Why it matters for agents

Without the tag, an agent puts a deploy-time choice into code, or asks the owner to decide at design time something that should stay a parameter. The brainstorming notes' "configuration parameter methods and tools" bullet is the deploy-time bucket named as its own topic.

## What it would look like in agent-method

One extra column in the question tables of every guide. Today every question in the existing guides is build-time, so the column would be uniform. It earns its place the first time a question is not build-time.

## Open questions

- Whether runtime binding is a real category for the workbench before it has an operator other than the owner.

## Source

Discussion 2026-09-05. Brainstorming notes: "Configuration parameter methods + tools" under technical architecture.
