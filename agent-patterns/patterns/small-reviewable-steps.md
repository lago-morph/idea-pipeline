---
id: small-reviewable-steps
title: Work in small reviewable steps
type: pattern
status: adopted
durability: structural
scope: interactive
tools: both
category: execution-loop
verified: 2026-08-29
models: [claude-5, gpt-5.6]
confidence: medium
sources: [osmani-2026-ai-coding-workflow, osmani-2026-agentic-code-review, osmani-2026-cognitive-surrender, willison-2026-aep, openhands-2026-ccbp, horthy-2025-acefca]
related: [review-agent-diffs, checkpoint-commits, plan-before-code]
aliases: []
---
# Work in small reviewable steps

**Use when:** the agent is editing code — i.e. almost always, and especially once a
plan exists to cut into steps.

**Do:**
- Ask for one plan step, one function, or one phase per turn. Have the agent stub
  the pieces first and fill them in one at a time if it keeps drifting.
- Verify each step before starting the next: run the tests, read the diff, then
  commit.
- Size the unit to what you will actually read. If you would only skim it, it is
  too big.
- Fold the finished step's status back into the plan file, then continue.

**Why:** writing is cheap and reading is not, so the diff you can actually review is
the binding constraint. Small units keep review honest, keep a bad step to one
revert, and stop the agent compounding a wrong turn across many files.

**Don't, when not:** one-line or mechanical changes, and throwaway spikes you do not
intend to keep.

**Evidence:**
- [osmani-2026-ai-coding-workflow] implement one plan step per prompt; large monolithic asks produce inconsistent, duplicated code.
- [osmani-2026-agentic-code-review] agent PRs ran 51% larger, and oversized diffs get rejected outright or waved through.
- [osmani-2026-cognitive-surrender] a 50-line change is readable, a 600-line one gets ratified rather than reviewed.
- [willison-2026-aep] several small PRs beat one big one, and the agent now does the Git splitting work for you.
- [openhands-2026-ccbp] ask for one function at a time, or stub-then-fill, to stop mid-change drift.
- [horthy-2025-acefca] implement phase by phase against the plan, verifying each phase before recording it.
