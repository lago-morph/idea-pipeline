---
id: horthy-2025-acefca
title: "Advanced Context Engineering for Coding Agents (Getting AI to Work in Complex Codebases)"
author: Dex Horthy (HumanLayer)
date: 2025-08
url: https://github.com/humanlayer/advanced-context-engineering-for-coding-agents
access: direct
accessed: 2026-08-29
scope: interactive
relevance: high
pass: distilled
patterns: [research-plan-implement, context-budget, context-compaction, subagents-for-context, review-plans-not-code, spec-first, fresh-context-reset, small-reviewable-steps]
---
## Summary

Horthy's answer to the claim that coding agents fail on large brownfield
codebases: the constraint is context, and today's models suffice if you
engineer around it. His umbrella technique is "frequent intentional
compaction" — designing the whole workflow around context management and
holding utilisation in the 40–60% range. Concretely: a research → plan →
implement loop with a written artifact at each step — research mapping the
relevant files and control flow, a plan naming exact edits and per-phase
verification, then phase-by-phase implementation that compacts status back
into the plan after each verified phase. Search goes to subagents so its file
reads never enter the main window. The human's job moves upstream: a bad line
of code is one bad line, a bad line of plan is hundreds, a bad line of
research thousands — so review research and plans, not diffs. He is candid
about limits: it needs sustained engagement and a codebase expert.

## Takeaways for our use case

- Treat the context window as the only lever on output quality, and optimise it for correctness first, then completeness, then size — wrong information hurts more than missing information, which hurts more than noise.
- Keep context utilisation roughly in the 40–60% band by design rather than working until you hit the limit and then compacting under duress.
- Run a research step that produces a written artifact — which files matter, how information flows, likely cause — before planning anything.
- Read the research and be willing to throw it out: Horthy discarded a research doc whose conclusion was wrong and re-ran with more steering, and the plan built on good research fixed the bug in the right place with conventions-matching tests, while the no-research plan fixed it in the wrong place.
- Make the plan name the exact files and edits and be precise about verification steps per phase, then implement phase by phase, compacting status back into the plan file after each verified phase.
- When you need to reset, write a progress file first — end goal, approach taken, steps completed, the failure currently being worked — and start a fresh context from it rather than continuing in a filled window.
- Send file searching, code-flow tracing, and log/JSON digestion to subagents; the point is context control, not role-play.
- Spend your review attention on research and plans rather than diffs — a 200-line implementation plan is readable daily in a way that a 2,000-line PR is not.
- Only the implement step needs a git worktree; research and planning can run on main.
- Expect this to fail when nobody involved knows the codebase, or when research doesn't go deep enough through the dependency tree — Horthy reports a 7-hour attempt that went nowhere for exactly that reason.

## Candidate patterns / evidence

- → research-plan-implement: the core three-step loop with a prompt per step; the research-backed plan produced a maintainer-approved PR in an unfamiliar 300k-LOC Rust codebase where the no-research plan produced a worse fix.
- → context-budget: "frequent intentional compaction" is defined as keeping context utilisation in the 40–60% range across the whole workflow, with a stated ordering of context failures (incorrect > missing > noisy).
- → context-compaction: pause before the window fills and write the state to a progress file (goal, approach, steps done, current failure); commit messages serve the same purpose; compaction is distilling searches, code-flow tracing, edits, and test logs into structured artifacts.
- → subagents-for-context: subagents are for context control, not anthropomorphised roles — a fresh window absorbs the Glob/Grep/Read traffic and returns a compaction-shaped summary.
- → review-plans-not-code: a bad line of research can cost thousands of bad lines of code, so human attention buys more leverage reviewing research and plans than reviewing diffs.
- → spec-first: specs and plans became the team's source of truth over the PR diff, framed against the argument that discarding prompts and keeping only the code is like checking in the binary and throwing away the source.
- → fresh-context-reset: discarding a derailed session and restarting with steering added to the original prompt is the first improvement over chatting until the agent starts apologising.
- → small-reviewable-steps: implementation proceeds phase by phase against the plan, each phase verified before its status is folded back into the plan file.

## Other-use-case material

- The "Ralph Wiggum" technique (an agent re-run in a `while` loop on a fixed prompt) is cited approvingly as another answer to the context constraint — long-running scope.
- Team- and org-level material: mental alignment as the real purpose of code review, the 8-week transition cost, scaling these workflows across large teams, and the CodeLayer product pitch — organisational, not single-session.
- Cost signal worth noting rather than adopting: a three-person team reported roughly $12k/month on Opus running this way.
