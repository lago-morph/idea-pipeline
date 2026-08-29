---
id: comprehension-debt
title: Comprehension debt
type: anti-pattern
status: adopted
durability: structural
scope: interactive
tools: both
category: anti-pattern
verified: 2026-08-29
models: [claude-5, gpt-5.6]
confidence: medium
sources: [osmani-2026-comprehension-debt, willison-2026-aep, osmani-2026-dont-outsource-learning]
related: [cognitive-surrender, review-agent-diffs]
aliases: []
---
# Comprehension debt

**Use when:** you are at risk of this — the codebase is growing faster than your
model of it, or the agent changed behaviour and updated many tests to match, and
nothing feels wrong because the suite is green.

**Do instead:**
- Say explicitly what a change is supposed to do before it is written, so there
  is an intent to check the result against.
- When tests were rewritten to match new behaviour, ask whether each edit was
  necessary — only comprehension answers that.
- Pay the debt down deliberately: commission a walkthrough that quotes real code
  pulled with `sed`/`grep`/`cat`, or an explanation of the one mechanism you
  cannot picture.
- In unfamiliar territory, ask for explanation, alternatives and tradeoffs
  before code; afterwards ask what concepts were used and what to read.
- Track a second question beside "did it ship": how much of what shipped do you
  understand?

**Why:** review used to be the bottleneck that forced comprehension, and
generation now outpaces audit. Unlike technical debt it announces nothing —
clean code, green tests, a reckoning later. Tests and specs both help and
neither substitutes.

**Don't / when not:** disposable code — boilerplate, glue, a CI script you will
never reopen.

**Evidence:**
- [osmani-2026-comprehension-debt] defined as the gap between code that exists and code any human understands; a student team hit the wall in week seven.
- [osmani-2026-comprehension-debt] the AI-updates-hundreds-of-tests case is named: the question becomes whether those edits were necessary.
- [osmani-2026-comprehension-debt] a cited RCT found AI-assisted learners scored 17% lower on comprehension, worst on debugging.
- [willison-2026-aep] treats not understanding your own codebase as cognitive debt, paid down with a generated walkthrough or an animated explanation.
- [osmani-2026-dont-outsource-learning] one follow-up prompt on concepts used and what to read converts a closed task into retained understanding.
