---
id: give-a-runnable-check
title: Give the agent a runnable check
type: pattern
status: adopted
durability: structural
scope: interactive
tools: both
category: session-setup
verified: 2026-08-29
models: [claude-5, gpt-5.6]
confidence: medium
sources: [willison-2026-aep, anthropic-2025-ccbp, tornhill-2026-codescene]
related: [agentic-manual-testing, define-done-first]
aliases: []
---
# Give the agent a runnable check

**Use when:** starting any task where "looks done" and "is done" could differ — which is
most of them.

**Do:**
- Decide up front what pass/fail signal the agent can run itself: test suite, build exit
  code, linter, coverage regression, screenshot diff.
- Put the command in the prompt and require it back with its real output, not an
  assertion of success.
- Escalate the check with the stakes: in-prompt check, goal condition re-evaluated each
  turn, blocking stop hook, second-opinion pass.
- Where no check exists, build one — a small CLI whose `--help` teaches an agent beats a
  longer prompt.
- Keep an end-to-end check over the packaged product, not just unit tests.

**Why:** without a signal it can run, the agent stops when the work looks done and you
become the verification loop.

**Don't / when not:** a passing suite is not proof the thing works; pair it with exercising
the code the way a human would.

**Evidence:**
- [anthropic-2025-ccbp] without a check it can run, "Claude stops when the work looks done"; the guide grades checks from in-prompt to stop hook to second-opinion subagent.
- [willison-2026-aep] the highest-leverage thing you can hand an agent is a way to check its own work; agent-oriented `--help` text is the delivery trick.
- [tornhill-2026-codescene] unit tests let agents iterate and converge, but end-to-end tests over the packaged product are what verify real outcomes.
- [tornhill-2026-codescene] a coverage-regression gate makes the agent's habit of deleting a failing test immediately visible.

**Tool notes:** Claude Code: a `Stop` hook can refuse to let the turn end until the check
passes, which instructions cannot.
