---
id: review-plans-not-code
title: Review plans, not just code
type: pattern
status: adopted
durability: structural
scope: interactive
tools: both
category: planning
verified: 2026-08-29
models: [claude-5, gpt-5.6]
confidence: medium
sources: [horthy-2025-acefca, openhands-2026-ccbp]
related: [plan-before-code, review-agent-diffs]
aliases: []
---
# Review plans, not just code

**Use when:** the agent has produced research or a plan and you are deciding where to
spend your own attention.

**Do:**
- Read the research and the plan properly, before reading any diff.
- Be willing to throw the research out and re-run it with more steering when its
  conclusion is wrong.
- Have the agent list its open questions in a planning file; answer them and iterate
  until the plan is boring.
- On a high-stakes change, get a fresh model to review the plan before implementation
  starts.

**Why:** the leverage is upstream. A bad line of code is one bad line; a bad line of
plan is hundreds; a bad line of research is thousands. A 200-line plan is also
something you can actually read, in a way a 2,000-line PR is not — and a plan the
original reasoning got wrong is exactly what a second reader catches.

**Don't, when not:** this replaces neither reading the diff nor running the tests —
it decides which review happens first, not which one you skip.

**Evidence:**
- [horthy-2025-acefca] Human attention buys more reviewing research and plans than diffs; a discarded bad research doc, re-run with steering, produced a plan that fixed the bug in the right place.
- [openhands-2026-ccbp] The plan is reviewed before a line of code, via a planning.md of open questions, with a fresh model reviewing the plan on high-stakes work.
