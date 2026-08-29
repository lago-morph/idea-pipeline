---
id: context-compaction
title: Compact context deliberately
type: pattern
status: adopted
durability: compensation
scope: interactive
tools: both
category: execution-loop
verified: 2026-08-29
models: [claude-5, gpt-5.6]
confidence: medium
sources: [horthy-2025-acefca, anthropic-2025-ccbp, every-2026-06-29-powerpoint-automation]
related: [fresh-context-reset, subagents-for-context, front-load-context]
aliases: []
---
# Compact context deliberately

**Use when:** a session is long but still on the right track — research, several
verified phases, or a lot of tool output behind you.

**Do:**
- Compact on your schedule, not when the window fills. Aim to stay in the middle of
  the budget rather than working up to the limit and summarising under duress.
- Compact *into an artifact*: distil searches, code-flow tracing, edits, and test
  logs into the plan or progress file after each verified phase.
- Say what to keep. Give the compaction a focus, and record in the instructions file
  what must survive it.
- Watch the loaded-material total, not just turn count; quality degrades well before
  the hard limit.

**Why:** quality drops as the window fills, so context is a budget to spend, not a
capacity to exhaust. A written artifact survives compaction and a chat summary does
not.

**Don't, when not:** the context contains a wrong assumption — summarising preserves
it, so reset instead.

**Evidence:**
- [horthy-2025-acefca] "frequent intentional compaction": hold utilisation around 40–60% and compact status back into the plan file after each verified phase.
- [anthropic-2025-ccbp] auto-compaction, `/compact <focus>`, summarize-from-here checkpoints, and instructions stating what compaction must preserve.
- [every-2026-06-29-powerpoint-automation] past roughly 200k tokens of loaded material the model starts making obvious mistakes ("context rot").

**Tool notes:** Claude Code: `/compact <focus>` plus automatic compaction; put
must-preserve items in `CLAUDE.md`.
