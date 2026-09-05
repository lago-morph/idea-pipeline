---
id: dependency-kinds
title: Must-exist-before and must-be-consistent-with are different dependencies
status: discussed
trigger: The first guide whose questions depend on another guide's answers, most likely the persistent-storage guide depending on a data-model guide.
agent-method-home: method/CONVENTIONS.md link types
depends-on: []
---

## Idea

Two kinds of dependency between artifacts. "Must exist before" gives authoring order and drives a guided walk through undecided questions. "Must be consistent with" gives cross-references and drives the audit. Real dependencies are often on one field, not a whole artifact: a technical design depends on an interface's synchronous-or-asynchronous answer, not on the whole interface.

## Why it matters for agents

The guided-work process presents each undecided question with the answers it depends on. That needs the first kind. The consistency check needs the second. Conflating them makes the walk order wrong or the audit noisy.

## What it would look like in agent-method

The conventions have `depends-on` and `related-to`. The first maps to must-exist-before, the second could carry must-be-consistent-with. Start at artifact granularity, which the conventions already support. Refine to field granularity only when a real case demands it.

## Open questions

- Whether `related-to` is precise enough to mean "must be consistent with" or whether a new link type is needed.

## Source

Discussion 2026-09-05.
