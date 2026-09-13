---
id: no-progressive-disclosure
title: Reference material without progressive disclosure
type: anti-pattern
status: candidate
durability: structural
scope: interactive
tools: both
category: anti-pattern
verified: 2026-09-13
models: [claude-5, gpt-5.6]
confidence: medium
sources: [lagomorph-2026-k8s-forensics]
related: [bloated-instruction-surface, agents-md-hygiene, front-load-context, subagents-for-context]
aliases: []
---
# Reference material without progressive disclosure

**Use when (you are at risk):** you are writing reference material — a spec, a
runbook, a schema, a long skill — that an agent will have to load whole in order
to use any part of it.

**Do instead:**
- Structure it as a map plus detail: a short index the agent reads every time,
  pointing at sections it opens only when the task calls for them.
- Put the trigger conditions in the map, so the agent can tell whether a section
  is relevant without reading it.
- Keep one authoritative copy of each fact. Duplicated detail is where the
  contradictions come from.
- Measure the map, not the corpus: what must be read every session is the number
  that matters.

**Why:** best case, material that can only be loaded whole spends context the
task needed. Worst case the bulk hides contradictions inside itself, and the
behaviour you get then depends on which passage the model weights — unpredictable
in a way that is very hard to debug, because nothing is wrong on its face.

**Don't / when not:** short material that is genuinely read end-to-end every time
needs no index; an index over three paragraphs is its own kind of overhead.

**Evidence:**
- [own] 2026-09-13 reference material without progressive disclosure clogs the context window at best; at worst it carries contradictions, and unpredictable behaviour is the near-guaranteed result.
- [lagomorph-2026-k8s-forensics] moving rule text into 20 detail files cut what loaded each session without cutting what existed — evidence that the load-bearing number is what must be read, not what is written.
