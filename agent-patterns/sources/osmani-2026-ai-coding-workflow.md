---
id: osmani-2026-ai-coding-workflow
title: My LLM coding workflow going into 2026
author: Addy Osmani
date: 2026-01-04
url: https://addyosmani.com/blog/ai-coding-workflow/
access: direct
accessed: 2026-08-29
scope: interactive
relevance: high
pass: distilled
patterns: [spec-first, plan-before-code, small-reviewable-steps, context-packing, model-switching-on-stuck, tests-as-safety-net, granular-commits, review-every-diff, project-rules-file, worktree-isolation, ci-feedback-loop]
---
## Summary

Osmani's end-of-year account of how he personally drives coding LLMs, framed
as "AI-augmented software engineering" rather than automation. The loop he
describes: brainstorm a spec with the model (letting it interrogate you until
requirements and edge cases are settled), have a reasoning model turn that
spec into a step-by-step plan, then implement one step at a time, testing and
committing after each. Around that loop he layers heavy up-front context
("brain dump" the goals, invariants, reference implementations, docs, and
approaches to avoid), a persistent rules file (CLAUDE.md / GEMINI.md) carrying
style and process preferences, and willingness to switch models when one gets
stuck. Verification is non-negotiable: read every diff, run the tests, treat
the output as coming from an over-confident junior, and merge only code you
can explain. CI, linters, and review bots feed their output back to the agent
as further prompts.

## Takeaways for our use case

- Do not start from a vague prompt: get the model to interrogate you into a
  written spec, then a numbered plan, and only then generate code.
- Implement one plan step per prompt; asking for large monolithic output
  produces inconsistent, duplicated code that is hard to untangle.
- Give the model the code, docs, and constraints it needs up front, including
  explicit "don't do X, it's too slow" and "ignore Y, out of scope" guidance.
- If a model stalls or gives mediocre output, paste the same prompt into a
  different model rather than iterating against a blind spot.
- A test suite is what lets an agent iterate safely; without one it will
  declare a broken change "done".
- Commit after every completed-and-tested chunk, so a bad suggestion costs one
  revert rather than hours; a tidy history also lets you brief the model with
  diffs and lets it bisect.
- Keep a rules file with style, lint, and process preferences and load it at
  session start; add anti-hallucination rules like "ask for clarification
  rather than inventing an answer".
- Feed failing test output and linter errors straight back into the session as
  the next prompt.
- Only merge code you understand; if the output is convoluted, have it
  explained or rewrite it simpler.

## Candidate patterns / evidence

- → spec-first: he compiles requirements, architecture, data models, and a
  testing strategy into a `spec.md` before any code is generated.
- → plan-before-code: the spec is fed to a reasoning model to produce a
  bite-sized task plan, which he critiques and refines before coding starts —
  a "waterfall in 15 minutes".
- → small-reviewable-steps: "let's implement Step 1 from the plan", test, then
  Step 2; large asks produce a jumbled mess.
- → context-packing: he pastes API docs, reference implementations, and
  relevant modules in, and uses repo-dump tools when a change spans several
  modules.
- → model-switching-on-stuck: each model has its own "personality"; copying
  the prompt into another service can rescue a stuck task.
- → tests-as-safety-net: agents "fly" on projects with a good test suite and
  blithely assume success without one, so testing is woven into the plan.
- → granular-commits: commits as save points after each small task, enabling
  cheap revert and precise bisecting of which change broke things.
- → review-every-diff: treat AI output as junior-developer code, review line
  by line, and never merge what you cannot explain.
- → project-rules-file: a maintained CLAUDE.md/GEMINI.md of style and process
  rules keeps the model on-script across sessions.
- → ci-feedback-loop: CI failures and linter errors are copied back into the
  prompt so the agent fixes against real tool output.
- → worktree-isolation: fresh git worktrees sandbox AI experiments so a failed
  one is discarded without touching main.

## Other-use-case material

- Asynchronous cloud agents (Jules, Copilot Agent) that clone a repo and open
  a PR unattended — long-running scope.
- Running 3-4 agents in parallel via orchestration tools; he notes it works
  but is mentally taxing and he sticks to one main agent plus a reviewer.
