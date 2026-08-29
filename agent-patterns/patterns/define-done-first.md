---
id: define-done-first
title: Define done before starting
type: pattern
status: adopted
durability: structural
scope: interactive
tools: both
category: planning
verified: 2026-08-29
models: [claude-5, gpt-5.6]
confidence: medium
sources: [osmani-2026-practical-loop-engineering, osmani-2026-agent-harness-engineering, every-2026-06-10-fable-5-get-most-out, osmani-2026-agentic-autonomy-levels]
related: [give-a-runnable-check, demand-evidence-not-summary]
aliases: []
---
# Define done before starting

**Use when:** always, and especially before handing over a task you will not watch
turn by turn.

**Do:**
- State the finish line in measurable terms before the first prompt — tests passing,
  a score threshold, a named artifact and its shape.
- Name the evidence that confirms completion independently of the agent.
- Add the invariants ("don't change the public API"), the non-goals, and a budget in
  turns or attempts.
- Add an abort rule: no progress after N turns, stop and report.
- If you cannot state the end state, sharpen it or keep the task supervised instead.

**Why:** without a stated finish line the agent decides for itself what "good enough"
means and stops on "looks done". A written done-condition catches scope drift earlier
than any prompt tweak, and makes delegation defensible rather than hopeful.

**Don't, when not:** work whose whole point is open-ended exploration — but then don't
pretend it is delegable either.

**Evidence:**
- [osmani-2026-practical-loop-engineering] Deterministic criteria beat judgment calls; his worked goal bundles metric, invariants, a per-turn progress requirement, an abort rule and a turn cap.
- [osmani-2026-agent-harness-engineering] Writing the done-condition before starting caught more scope drift than any prompt change he has made.
- [every-2026-06-10-fable-5-get-most-out] A task is only worth delegating whole when you can supply context, one clear goal, an explicit definition of done, and a way to verify.
- [osmani-2026-agentic-autonomy-levels] Goal-driven autonomy needs a measurable, automatable stopping condition, written into a per-run contract with the evidence that would confirm it.

**Tool notes:** Claude Code: `/goal` iterates a bounded task until an evaluator model confirms the stated condition each time the agent tries to stop; recurring `/loop` runs are session-scoped and expire seven days after creation.
