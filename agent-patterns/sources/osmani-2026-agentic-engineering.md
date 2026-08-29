---
id: osmani-2026-agentic-engineering
title: Agentic Engineering
author: Addy Osmani
date: 2026-02-04
url: https://addyosmani.com/blog/agentic-engineering/
access: direct
accessed: 2026-08-29
scope: interactive
relevance: high
pass: distilled
patterns: [name-the-mode, spec-first, plan-before-code, review-every-diff, tests-as-safety-net, own-what-you-ship]
---
## Summary

A terminology argument with a practical core. Osmani says "vibe coding" has
become a suitcase term covering both reckless prototyping and disciplined
agent-assisted engineering, and that conflating them causes real damage. Vibe
coding is defined narrowly: you prompt, you accept, you do not read the diffs
— legitimate for prototypes, personal scripts, learning, and deliberate
over-generation you intend to throw away. The professional counterpart, which
he adopts Karpathy's term "agentic engineering" for, keeps the human as
architect and reviewer: write a plan or spec before prompting, hand the agent
well-scoped tasks, review its output with the rigour you'd apply to a
teammate's PR, and lean on a test suite so the agent can iterate to green
rather than declaring broken code done. His claim is that AI-assisted work
rewards existing good practice more than hand-coding did, and that it
disproportionately benefits engineers who already have the fundamentals.

## Takeaways for our use case

- Decide explicitly which mode you are in before you start: throwaway
  prototyping where code quality is irrelevant, or engineering where you own
  the result — the failure cases come from drifting between them unnoticed.
- Vibe coding's defining feature is not reading the diffs; if you are reading
  them, you are doing something else and should hold yourself to that bar.
- Write the design or spec and break the work into well-defined tasks before
  prompting anything; this is precisely the step that gets skipped and where
  projects derail.
- Review agent output as you would a human colleague's PR: if you cannot
  explain what a module does, it does not go in.
- Testing is the single biggest differentiator — with a solid suite the agent
  loops until green, without one it will cheerfully declare done on broken code.
- Keep owning documentation, version control, CI, and production monitoring;
  acceleration does not transfer responsibility.
- Expect the trade to be typing time for review time; the fundamentals matter
  more, not less, and leaning on the agent before you have them risks skill
  atrophy.

## Candidate patterns / evidence

- → name-the-mode: he draws a clean line — "Vibe coding = YOLO. Agentic
  engineering = AI does the implementation, human owns the architecture,
  quality, and correctness" — and argues the distinction must be stated.
- → spec-first: agentic engineering "starts with a plan": a design doc or spec
  written before any prompting, sometimes with AI help.
- → plan-before-code: the work is broken into well-defined tasks and the
  architecture decided up front, the step vibe coders skip.
- → review-every-diff: each generated change gets the same rigour as a
  teammate's PR, with an explain-it-or-drop-it rule for modules.
- → tests-as-safety-net: a solid test suite is what turns an unreliable agent
  into a reliable system by letting it iterate until tests pass.
- → own-what-you-ship: the human remains accountable for architecture,
  correctness, edge cases, and long-term maintainability regardless of who
  typed the code.
