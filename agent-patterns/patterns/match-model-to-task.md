---
id: match-model-to-task
title: Match the model to the task
type: pattern
status: adopted
durability: structural
scope: interactive
tools: both
category: delegation
verified: 2026-08-29
models: [claude-5, gpt-5.6]
confidence: medium
sources: [every-2026-07-07-fable-unknowns, every-2026-04-27-most-expensive-model, every-2026-04-23-gpt-5-5-vibe-check, every-2026-08-26-cloning-coworkers-skills, osmani-2026-new-sdlc-vibe-coding, every-2026-07-22-biggest-launch-ever, osmani-2026-ai-coding-workflow, every-2026-07-28-taming-opus-5]
related: [subagents-for-context, full-brief-up-front]
aliases: []
---
# Match the model to the task

**Use when:** starting a task, or handing off between phases of one.

**Do:**
- Choose by how settled the goal is, not by how big the job is: an unsettled
  definition of "good" earns the frontier model; execution against a clear plan
  does not.
- Split the task into steps and downgrade the steps, not the whole task.
- Let planning and execution come from different models.
- Push heavy implementation into a cheaper model in a subagent; keep the expensive
  one on framing, delegation, and review.
- When a model stalls, re-run the prompt on a different one rather than iterating
  against its blind spot.

**Why:** models differ by task shape, not on one quality axis, and the expensive one
is slower and dearer without being better on most work.

**Don't, when not:** switching models is no substitute for a better prompt, plan, or
test; and release-day comparisons date fast.

**Evidence:**
- [every-2026-07-07-fable-unknowns] triage by uncertainty, not task size — the expensive model pays when the goal or the definition of good is unsettled.
- [every-2026-04-27-most-expensive-model] decompose before downgrading, so the expensive model only handles the steps that need it.
- [every-2026-04-23-gpt-5-5-vibe-check] the best reported benchmark run paired an Opus-written plan with GPT-5.5 execution; the same review routes one-shot builds elsewhere.
- [every-2026-08-26-cloning-coworkers-skills] one heavy user reports no relative gain from the top model on roughly 80% of tasks, while it is slower and costlier.
- [osmani-2026-new-sdlc-vibe-coding] route hard reasoning to a large model and routine generation and checking to a small one.
- [every-2026-07-22-biggest-launch-ever] one standing instruction to pick a lower-power model and run implementation in a subagent cut expensive-model token use.
- [osmani-2026-ai-coding-workflow] paste the same prompt into a different model when one stalls rather than iterating against a blind spot.
- [every-2026-07-28-taming-opus-5] identical presentation inputs produced an unusable draft from one model and a presentable one from another.
