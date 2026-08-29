---
id: plan-before-code
title: Plan before code
type: pattern
status: adopted
durability: structural
scope: interactive
tools: both
category: planning
verified: 2026-08-29
models: [claude-5, gpt-5.6]
confidence: medium
sources: [anthropic-2025-ccbp, openhands-2026-ccbp, osmani-2026-ai-coding-workflow, osmani-2026-good-spec, every-2026-04-23-gpt-5-5-vibe-check, horthy-2025-acefca]
related: [spec-first, review-plans-not-code, small-reviewable-steps]
aliases: []
---
# Plan before code

**Use when:** the change spans several files, the codebase is unfamiliar, or the
approach is still uncertain.

**Do:**
- Explore read-only first, then have the agent write a short plan before any edit.
- Make the plan name the exact files, the edits, and the verification per phase.
- Put its open questions in the plan; answer them; iterate until the plan is boring.
- Only then switch to editing, one plan step at a time.

**Why:** a wrong plan costs far more than a wrong line, and the plan is the cheapest
thing to review. Models also execute better against an existing plan than a blank
slate.

**Don't, when not:** when you could describe the diff in one sentence — planning has
real overhead and buys nothing on a trivial change.

**Evidence:**
- [anthropic-2025-ccbp] Explore → plan → implement → commit in plan mode; skip planning when the diff fits in a sentence.
- [openhands-2026-ccbp] Plan mode as read-only exploration; reasoning up front on thorny architecture saves backtracking.
- [osmani-2026-ai-coding-workflow] Feeds the spec to a reasoning model for a numbered plan he critiques before any code.
- [osmani-2026-good-spec] Read-only Plan Mode blocks edits until the plan leaves "no room for misinterpretation".
- [every-2026-04-23-gpt-5-5-vibe-check] Every's best benchmark run paired an Opus-written plan with GPT-5.5 execution.
- [horthy-2025-acefca] The research-backed plan produced a maintainer-approved PR where the unresearched plan fixed the wrong place.

**Tool notes:** Claude Code: plan mode, entered at startup, with Shift+Tab, or `/plan`.
