---
id: demand-evidence-not-summary
title: Demand evidence, not summaries
type: pattern
status: adopted
durability: structural
scope: interactive
tools: both
category: review-quality
verified: 2026-08-29
models: [claude-5, gpt-5.6]
confidence: medium
sources: [osmani-2026-code-review-ai, osmani-2026-agentic-autonomy-levels, every-2026-06-29-powerpoint-automation, osmani-2026-practical-loop-engineering, every-2026-07-28-taming-opus-5]
related: [give-a-runnable-check, agentic-manual-testing]
aliases: []
---
# Demand evidence, not summaries

**Use when:** any time an agent reports that a task is finished.

**Do:**
- End every task in concrete evidence: the command that ran and its real output, a test result, a log, a trace, a screenshot, repro steps.
- Ask for the packet a manual review would need — diff, tests, logs, risks, known gaps.
- Judge the artifact itself, not the agent's narration of how it got there.
- Spell out the verification steps, and require a rerun from step one if any of them fails.
- Have a different agent verify the work than the one that produced it.
- Refuse "looks done" and self-graded scores as the exit condition.

**Why:** the summary is written by the system whose work you are checking, and a confident report can be true about the wrong dimension entirely. Evidence is cheaper to review than to re-derive.

**Don't / when not:** evidence you cannot read is not evidence — keep the packet small enough to inspect.

**Evidence:**
- [osmani-2026-code-review-ai] "insist on proof, not promises" — no change goes up without new tests or a demonstration of it working.
- [osmani-2026-agentic-autonomy-levels] names summary substitution as an anti-pattern and prescribes the evidence packet a manual review would demand.
- [osmani-2026-practical-loop-engineering] a separate subagent verifies, because the agent that did the work may have evaluated only one dimension of the problem.
- [every-2026-06-29-powerpoint-automation] after eight self-graded rounds the agent declared success without ever looking at a rendered deck; its own metrics checked content, not appearance.
- [every-2026-07-28-taming-opus-5] evaluate the finished artifact on its own terms; the model's account of its process is not the deliverable.

**Tool notes:** Claude Code: encode the verification steps as a skill (start the dev server, interact, screenshot before/after, zero new console errors); `/goal`'s evaluator only checks whether your hard rules were met, never whether the result is good.
