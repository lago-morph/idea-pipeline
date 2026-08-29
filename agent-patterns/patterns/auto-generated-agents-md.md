---
id: auto-generated-agents-md
title: Auto-generated AGENTS.md
type: anti-pattern
status: adopted
durability: structural
scope: interactive
tools: both
category: anti-pattern
verified: 2026-08-29
models: [claude-5, gpt-5.6]
confidence: medium
sources: [osmani-2026-agents-md, openhands-2026-ccbp]
related: [agents-md-hygiene]
aliases: []
---
# Auto-generated AGENTS.md

**Use when (at risk of it):** setting up a repo for agent work and reaching for the
generate-my-context-file command as the first step.

**Do instead:**
- Start nearly empty — or with one line telling the agent to flag anything surprising.
- Add entries one at a time, only after the agent actually gets something wrong.
- Delete any generated line the agent could have discovered by listing directories and
  reading the README.
- When it keeps erring, fix the codebase first — reorganise the directory, add a lint
  rule, fix the build — then decide whether a line is still needed.

**Why:** generated files are near-universally codebase overviews, duplicating what the
agent finds anyway. They add reconciliation work and cost for the same outcome, and every
speculative line dilutes the rules that were earned.

**Don't / when not:** the objection is to generated overviews, not to the file — a short,
human-written instructions file measurably helps.

**Evidence:**
- [osmani-2026-agents-md] 100% of Sonnet 4.5's and 99% of GPT-5.2's auto-generated context files contained codebase overviews — exactly what the agent can discover itself.
- [osmani-2026-agents-md] an ETH Zurich study found LLM-generated context files cut task success 2-3% while raising cost over 20%, where developer-written ones raised success ~4%.
- [osmani-2026-agents-md] one workable technique is to start nearly empty and fix what the agent flags rather than keeping the note.
- [openhands-2026-ccbp] start the instructions file late, once you know what the agent gets wrong, and add entries one at a time as mistakes occur.
- [openhands-2026-ccbp] real rules buried under speculative ones get weighted equally and followed none.

**Tool notes:** Claude Code: `/init` is the command this warns about; skipping it is the
default position.
