---
id: five-kinds-of-guidance
title: An artifact type carries five kinds of guidance
status: discussed
kind: rider
event: type descriptions
friction: The vision type description carries authoring guidance only. Reviewing guidance exists but lives in the implementation procedure's checklist, and consuming guidance exists only as tiered document access.
agent-method-home: method/types/*.md, as a standard set of sections
depends-on: [verification-per-question]
---

## Idea

Each artifact type ships with five kinds of guidance: how to author it, how to relate it to other artifacts, how to consume it when implementing, how to verify an implementation against it, and how to review the artifact itself for completeness before anyone consumes it. The fifth is the definition of done. The DoD candidates in the brainstorming notes are review guidance for specific types: scenarios with test data, contracts per state, example input and output, postconditions.

## Why it matters for agents

Authoring and consuming are different readers with different needs. The vision type description today is authoring guidance. A subagent implementing from a component definition needs consumption guidance, and the review checklist needs review guidance. Naming the five keeps a type description from silently covering only one.

## What it would look like in agent-method

A fixed section list for every `method/types/<type>.md`: Intent, Authoring, Relating, Consuming, Verifying, Reviewing, Template. The vision type already has Intent, Authoring, and Template. Each type plus its five kinds of guidance is close to a skill in shape, which suggests how the method proper might eventually package them.

## Open questions

- Whether "relating" is its own section or folds into authoring, since links are set at authoring time.

## Source

Discussion 2026-09-05. Brainstorming notes: DoD boxes.
