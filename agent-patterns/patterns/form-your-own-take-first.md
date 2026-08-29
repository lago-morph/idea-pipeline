---
id: form-your-own-take-first
title: Form your own take first
type: pattern
status: adopted
durability: structural
scope: interactive
tools: both
category: review-quality
verified: 2026-08-29
models: [claude-5, gpt-5.6]
confidence: medium
sources: [every-2026-04-20-ai-autopilot, osmani-2026-cognitive-surrender, osmani-2026-dont-outsource-learning]
related: [cognitive-surrender, review-agent-diffs]
aliases: []
---
# Form your own take first

**Use when:** the task involves a judgement you will have to defend — a design
choice, a diagnosis, a fix in code you own.

**Do:**
- Before prompting, write a few lines: what you think the problem is, what you
  know, what you are unsure of, what you refuse to do.
- Use the agent's answer to test that view rather than to supply one; where it
  differs from your expectation, decide which is right and why.
- Out of your depth, ask for explanation, alternatives and tradeoffs before
  asking for code.
- Before accepting a recommendation, write one sentence on why it is right for
  this case. If the best you can write is "it sounds good", look again.
- Ask the model to argue against its own answer.

**Why:** order of operations matters — reaching for the model first lets it
frame the problem, and that framing sticks even when you do the rest of the
work. A written expectation is what turns output into something you can argue
with.

**Don't / when not:** disposable work — boilerplate, glue code, a script you
will never reopen.

**Evidence:**
- [osmani-2026-cognitive-surrender] writing down the expected answer before running the agent is his primary calibration heuristic; a mismatch forces a real decision.
- [osmani-2026-cognitive-surrender] asking the model to argue against itself is the cheap second pass that breaks borrowed confidence.
- [every-2026-04-20-ai-autopilot] a cited 2026 study found a forced one-sentence justification roughly halved mistaken acceptances.
- [osmani-2026-dont-outsource-learning] CHI 2026: early LLM access anchored problem framing and worsened decisions even when the human did the rest.
- [osmani-2026-dont-outsource-learning] conceptual-question users scored above 65% on comprehension versus under 40% for copy-paste users.
