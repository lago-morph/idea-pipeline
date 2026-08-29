---
id: front-load-context
title: Front-load the context the task needs
type: pattern
status: adopted
durability: structural
scope: interactive
tools: both
category: session-setup
verified: 2026-08-29
models: [claude-5, gpt-5.6]
confidence: medium
sources: [osmani-2026-ai-coding-workflow, every-2026-06-10-fable-5-get-most-out, horthy-2025-acefca, anthropic-2025-ccbp, willison-2026-aep]
related: [context-compaction, spec-first]
aliases: []
---
# Front-load the context the task needs

**Use when:** starting any task bigger than a one-sentence diff, especially with a slow,
expensive model you don't intend to babysit turn by turn.

**Do:**
- Name the files, the scenario, the constraint, and an existing example of the pattern
  you want.
- State the out-of-scope and the approaches to avoid, not just the goal.
- Point at working code instead of describing behaviour — an analogous feature, a sibling
  project, or a reference repo cloned to `/tmp` so it never gets committed.
- In unfamiliar areas, run a research step that writes down which files matter and how
  information flows, and read it before planning.
- Open an existing repo with "review changes made today" to load recent code and intent.

**Why:** correctness of context beats completeness, which beats size — wrong or stale
context propagates all the way to a wrong result, and it does so silently once you stop
correcting every turn.

**Don't / when not:** don't dump the whole repo; noise costs context you will need later.

**Evidence:**
- [osmani-2026-ai-coding-workflow] brain-dump goals, invariants, reference implementations, docs, and "don't do X" up front.
- [every-2026-06-10-fable-5-get-most-out] with a strong model the work shifts to assembling context up front; stale context and conflicting goals then propagate unchecked.
- [horthy-2025-acefca] a research artifact before planning fixed the bug in the right place where the no-research plan did not.
- [anthropic-2025-ccbp] prompt with file, scenario, constraint, and a pointer to an existing example; vague prompts are for exploration only.
- [willison-2026-aep] naming known software and cloning a reference repo to `/tmp` substitute for paragraphs of spec.
