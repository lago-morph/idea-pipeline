---
id: fresh-context-reset
title: Reset instead of arguing
type: pattern
status: adopted
durability: compensation
scope: interactive
tools: both
category: debugging-recovery
verified: 2026-08-29
models: [claude-5, gpt-5.6]
confidence: medium
sources: [anthropic-2025-ccbp, openhands-2026-ccbp, horthy-2025-acefca]
related: [context-compaction, small-reviewable-steps]
aliases: []
---
# Reset instead of arguing

**Use when:** you have corrected the same mistake twice, the agent keeps reverting to
an assumption you already rejected, or the session is full of failed approaches.

**Do:**
- Stop correcting. Write a short progress file first: the end goal, the approach
  taken, the steps completed, and the failure you are on.
- Clear the context and restart from that file with a sharper prompt that names what
  you learned.
- Fold the correction into the prompt itself, not into another turn of argument.
- Prefer a clear over a compaction when the problem is a wrong belief — summarising
  carries the wrong belief forward.

**Why:** a filled window holds every failed attempt, and the model keeps drawing on
them. A clean session with a better prompt beats a long one that has been talked out
of its mistakes.

**Don't, when not:** the session is long but coherent and the work so far is sound —
compact it instead. Do not reset before capturing the progress, or you pay for the
exploration twice.

**Evidence:**
- [anthropic-2025-ccbp] treat a second correction on the same issue as the signal to clear and re-prompt.
- [openhands-2026-ccbp] when context holds an assumption the model keeps reverting to, /compact preserves it — dump progress, clear, restart.
- [horthy-2025-acefca] discarding a derailed session and restarting with steering added to the original prompt is the first improvement over chatting until the agent apologises.

**Tool notes:** Claude Code: `/clear` to reset, not `/compact`; Esc interrupts and
rewind/checkpoints restore earlier conversation or code state.
