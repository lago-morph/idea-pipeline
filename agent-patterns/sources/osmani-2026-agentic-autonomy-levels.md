---
id: osmani-2026-agentic-autonomy-levels
title: Agentic Autonomy Levels
author: Addy Osmani
date: 2026-07-02
url: https://addyosmani.com/blog/agentic-autonomy-levels/
access: direct
accessed: 2026-08-29
scope: mixed
relevance: medium
pass: distilled
patterns: [autonomy-calibration, per-run-contract, done-condition-first, evidence-not-summary, avoid-approval-fatigue, autonomy-calibration-retro]
---
## Summary

Osmani proposes a two-axis replacement for single-ladder autonomy scales:
agency (how far a single agent goes from you) and orchestration (how many
agents you coordinate), collapsed into six levels. Levels 0–2 — assist,
supervised action, scoped task delegation — are the single-session range, with
level 1 the default posture for most people and level 2 the current centre of
gravity. Level 3 is goal-driven autonomy, viable only where the stopping
condition is measurable and automatable; levels 4–5 are parallel delegation and
managed-by-exception factories. His central claim is that the autonomy level
should follow the verification process rather than the task name, tested by
three questions: how fast you'd know you're wrong, how cleanly you could undo
it, and what would prove you're right. He proposes a written per-run contract,
lists four autonomy anti-patterns, and cites Anthropic data on ~400K sessions.

## Takeaways for our use case

- Ask of each task: what autonomy level does this deserve, and what
  verification makes that level defensible? Classify by risk and by how easily
  the work can be undone, raising autonomy only as evidence accumulates.
- The three-question test for whether autonomy is real: how quickly will you
  know you're wrong, how cleanly can you undo it, and what would prove you're
  right. "Not quickly, with difficulty, trusting the summary" means you don't
  have high autonomy, you have exposure.
- Precede every run with a written contract: goal (an outcome, not an activity
  or technique), scope and allowed techniques, non-goals, tools and
  permissions, stopping condition (ideally a measurable variable), evidence
  that can confirm completion independently of the agent, escalation, and a
  budget in time, tokens, attempts and parallelism.
- Level 0 fits delicate work and work where your own judgment is still forming;
  level 1 fits most exploration near the boundary of what you understand; level
  2 fits bounded tasks with likely unknown gotchas.
- At level 2, verification shifts from you to evidence the agent produces:
  passing tests, clean types, lint results, screenshots, repro steps.
- Goal-driven work needs a specific, measurable, automatable target — not
  "improve user experience" or "make the codebase more testable."
- The failure mode of supervised action is approval fatigue: every approval
  feels the same regardless of what it approves. Counter with heuristics for
  what actually needs squinting at, or a separate reviewer agent for boundary
  conditions.
- Anti-pattern to guard against: summary substitution, where the agent's
  summary stands in for review. Ask for the same evidence packet you'd want
  from a manual review — diff, tests, logs, screenshots, risks and gaps.
- Anti-pattern: permission laundering, where approval fatigue leads to granting
  much broader access than needed; fix with sandbox profiles, scoped writable
  roots, allowlisted commands and hooks.
- Anthropic's analysis of ~400K sessions found people make ~70% of planning
  decisions while the agent does ~80% of execution — high autonomy means
  choosing direction, not being out of the loop.
- Longer single-agent runs bring drift, context rot and strayed objectives; the
  fix is narrower scope, better evidence and cheaper rollback, not more trust.
- Calibration exercise worth running: review your last ten agent-assisted
  tasks, recording autonomy level used, risk, undoability, evidence produced,
  review time, whether rework was needed, and whether that level still fits.

## Candidate patterns / evidence

- → autonomy-calibration: "The autonomy level should follow the verification
  process, not the task name" — a well-tested payments refactor with clean
  rollback supports more autonomy than a docs task with no canonical truth.
- → per-run-contract: goal / scope / non-goals / tools and permissions /
  stopping condition / evidence / escalation / budget, written before the run.
- → done-condition-first: level 3 is only useful when the stopping condition is
  measurable in a way that can be automated; vague goals don't qualify.
- → evidence-not-summary: the summary-substitution anti-pattern, fixed by
  bundling the same evidence packet a manual review would require.
- → avoid-approval-fatigue: undifferentiated approvals both dull review and
  drive permission laundering; scope boundaries and reviewer agents instead.
- → autonomy-calibration-retro: the last-ten-tasks exercise turns autonomy
  choices into a reviewable record rather than a habit.

## Other-use-case material

- Levels 4 and 5 (parallel delegation across isolated worktrees; a manager
  agent waking on triggers, dispatching workers, verifying, retrying and
  escalating) are multi-agent/factory territory, along with the OpenAI
  Symphony orchestration spec and per-issue agent workspaces.
- Level 4's failure mode, false parallelism — overlapping slices producing
  merge conflicts and duplicated decisions instead of throughput — and the
  orchestration tax on the human side.
- Fleet cosplay anti-pattern (many agents, but a human still coordinating every
  dependency by hand) and the fleet metrics list (mean time between
  interventions, longest unattended run, token cost per accepted change) are
  operator-scale instrumentation.
- Portable principle from the top of the ladder: at scale, independent
  verification means separate implementers and reviewers, separate test runners
  and QA, separate security checks.
