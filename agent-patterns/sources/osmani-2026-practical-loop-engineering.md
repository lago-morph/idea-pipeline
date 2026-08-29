---
id: osmani-2026-practical-loop-engineering
title: Practical Loop Engineering
author: Addy Osmani
date: 2026-08-14
url: https://addyosmani.com/blog/practical-loop-engineering/
access: direct
accessed: 2026-08-29
scope: interactive
relevance: high
pass: distilled
patterns: [done-condition-first, verify-like-reviewer, dont-delegate-judgment, separate-generator-from-verifier, autonomy-calibration, stop-on-no-progress]
---
## Summary

Osmani walks through the two loop primitives now built into Claude Code: `/goal`,
which keeps a single bounded task iterating until a measurable finish line is
met (an evaluator model checks the stated condition each time the agent tries
to stop), and `/loop`, which re-runs a prompt on an interval like cron. He
quotes the Claude Code team's four-rung framing of loops, from the manual
agentic loop of a single prompt up to proactive scheduled loops. The practical
core is what makes a loop safe: deterministic stopping conditions, an explicit
verification skill that makes the agent check work the way a human reviewer
would, and a separate verifying agent rather than letting the agent that did
the work grade it. He describes his own delegate-versus-watch split, and tells
a story about nearly pushing agent-written PRs he had not read closely — the
lesson being that delegating the task must not slide into delegating judgment.

## Takeaways for our use case

- Define what done looks like in measurable terms before starting; if you can't
  state the end-state, that work is a poor fit for an autonomous loop.
- Deterministic criteria work best — tests passed, a score threshold — because
  the agent never has to decide what "good enough" means and stop early.
- His worked `/goal` example bundles goal, metric, tool that reports it,
  invariants ("do not change the public API of any hooks"), a per-turn progress
  requirement, an abort rule after two flat turns, and a turn cap.
- Know what the evaluator is not: it reads the transcript for whether your hard
  rules were met, and makes no judgement about whether the content is good.
- Encode verification as a skill that spells out reviewer-like steps — start
  the dev server, interact with the change, screenshot before/after, require
  zero new console errors, run a performance trace — and never report a UI
  change complete on a successful edit alone.
- If any verification step fails, fix and rerun from step one rather than
  handing back partially verified work.
- Don't let the agent that did the work decide the work is good: one subagent
  drafts, a separate one verifies. A confident agent may have evaluated only
  one dimension (desktop performance, say) of a problem you care about on
  another (mobile).
- Calibrate per task: safe, well-bounded work (write the docs for this feature,
  check test coverage) can be delegated; complex work, or anything touching
  authentication, security or finance, gets watched closely.
- You still have to read the generated code. He nearly pushed agent-written
  PRs after reading only its research, and found on inspection they added
  complexity for little gain.
- Watch for a loop spinning in place — the same command tried a third time with
  no change in result is the signal to stop.
- Pick your first loop from a check you already run by hand every morning.
- Claude Code mechanics: recurring loops expire seven days after creation and
  are session-scoped (`--resume`/`--continue` brings them back inside the
  window); `/schedule` moves work to the cloud so it outlives the session.

## Candidate patterns / evidence

- → done-condition-first: a vague goal like "keep going until this UI design is
  good" is unusable — good to whom, evaluated how — while measurable stopping
  conditions are what make delegation defensible.
- → verify-like-reviewer: his quoted verification skill instructs the agent to
  verify a UI change the way a human reviewer would, with browser interaction,
  screenshots, a clean console and a performance trace as the exit evidence.
- → dont-delegate-judgment: he nearly shipped agent-written PRs after reading
  the research but not the implementations — "you're delegating the task, and
  then you are actually checking back that it's meeting your bar."
- → separate-generator-from-verifier: one subagent drafts the change, a
  separate one verifies, because a confident agent can miss the dimension it
  wasn't evaluating.
- → autonomy-calibration: documentation and test-coverage tasks get full
  delegation; complex or auth/security/finance-adjacent work gets watched.
- → stop-on-no-progress: same command, third attempt, no change in result means
  the loop is spinning and should be stopped.

## Other-use-case material

- Osmani runs five to ten agents a day, up to five concurrently — the parallel
  fleet framing is a different use case, though the primitives are per-task.
- `/loop` plus `/goal` composition for unattended PR/issue triage on a popular
  repo (auto-closing PRs that violate contribution guidelines) is scheduled,
  long-running work.
- The Claude Code team's proactive-loop rung, `/schedule` cloud routines, auto
  mode, and dynamic workflows orchestrating parallel worktrees with an
  adversarial judge are orchestration-side.
- Suitability caveat worth carrying: loops fit evergreen codebases far better
  than a brownfield system with historical complexity and real users.
