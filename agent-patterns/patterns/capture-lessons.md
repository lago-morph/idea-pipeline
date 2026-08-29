---
id: capture-lessons
title: Capture lessons into instructions
type: pattern
status: adopted
durability: structural
scope: interactive
tools: both
category: compounding
verified: 2026-08-29
models: [claude-5, gpt-5.6]
confidence: medium
sources: [willison-2026-aep, every-2026-05-29-compound-engineering-upgrade, cheapcode-2026, osmani-2026-intent-debt, every-2026-08-26-cloning-coworkers-skills, osmani-2026-agent-harness-engineering, every-2026-08-04-think-like-designer]
related: [intent-ledger, skill-authoring, agents-md-hygiene]
aliases: []
---
# Capture lessons into instructions

**Use when:** the agent got something wrong and you corrected it, or a session
taught you something the next session would need.

**Do:**
- Fix the artifact, then separately fix the instructions.
- Hand the agent the specific gap — what it produced, what a better answer was —
  before asking it to propose the rule edit.
- Write a narrow behavioural rule traceable to that failure, not a principle.
- Record failed approaches and the why behind expensive decisions at session end.
- If you have made the same correction twice, write it down instead of a third.

**Why:** every session starts cold; anything not in a file the agent reads is
re-paid each time, and it fills the gap with a confident guess. The rules you
actually need surface from working at speed, so they cannot be written up front.

**Don't / when not:** one-off mistakes with no pattern behind them, or rules the
agent already follows — every line competes for attention.

**Evidence:**
- [willison-2026-aep] end each project by writing what you learned into the instructions the agent reads next.
- [every-2026-05-29-compound-engineering-upgrade] "compound" is the loop's most important step: each cycle should make the next easier.
- [osmani-2026-intent-debt] a session-end learnings file captures root causes and failed approaches that otherwise stay in your head.
- [osmani-2026-agent-harness-engineering] convert each agent mistake into an AGENTS.md line, hook, or reviewer check so it cannot recur.
- [every-2026-08-26-cloning-coworkers-skills] a self-improve skill interrogates the bad output and proposes a targeted edit to the operating instructions.
- [every-2026-08-04-think-like-designer] a correction made twice becomes a standing rule rather than a third correction.
- [cheapcode-2026] (abstract only) controls that sustain agentic velocity are discovered from failures during the work, not derived up front.
