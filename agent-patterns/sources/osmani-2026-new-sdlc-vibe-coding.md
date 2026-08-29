---
id: osmani-2026-new-sdlc-vibe-coding
title: The New Software Lifecycle
author: Addy Osmani
date: 2026-06-16
url: https://addyosmani.com/blog/new-sdlc-vibe-coding/
access: direct
accessed: 2026-08-29
scope: mixed
relevance: high
pass: distilled
patterns: [harness-first-debugging, static-vs-dynamic-context, progressive-disclosure, tests-vs-evals, spec-quality-is-the-bottleneck, model-routing-by-task]
---
## Summary

Osmani pulls the ideas he considers load-bearing out of a Google whitepaper he
co-wrote on how AI changes the software lifecycle. An agent is a model plus a
harness, with the paper's rough split at 10% model and 90% harness, so when an
agent misbehaves he debugs the harness first — usually a missing tool, a loose
rule, a forgotten guardrail, or a context window full of junk. Inside the
harness, the decision that shows up on your bill is what lives in static
context (loaded every turn, reliable, expensive) versus dynamic context (loaded
on demand); he argues that boundary deserves to be reviewed and versioned like
code. Verification is what separates vibe coding from engineering, split into
tests for deterministic behaviour and evals for the rest, with output
evaluation and trajectory evaluation as distinct questions. Because
implementation compresses while requirements, architecture and verification
stay slow, specification quality becomes the bottleneck.

## Takeaways for our use case

- Debug the harness before blaming the model: most agent failures are
  configuration failures, and configuration is the part you can fix today.
- Treat the static/dynamic context boundary as an architectural decision —
  static rule files are paid for on every call, dynamic skills and tool results
  only when a task touches them.
- Getting that balance wrong burns tokens and buries the signal in one
  direction, and loses the rules that keep the agent safe in the other.
- Progressive disclosure is what makes dynamic context scale: metadata at
  startup, full instructions when a task matches, heavy reference material only
  when actually needed.
- Use tests for the deterministic parts and evals for the parts that aren't;
  ask both whether the final output is correct and whether the trajectory (tool
  calls, reasoning) was sound.
- An answer that looks right but skipped its checks is more dangerous than one
  that is obviously broken; set the bar at the eval, not the demo.
- Expect the gain to show up as reviewing rather than writing — he cites both
  25–39% productivity surveys and a METR study finding experienced developers
  19% slower on some tasks once checking and fixing are counted.
- Specification quality is now the bottleneck and verification moves to the
  middle of the lifecycle; architecture stays the most stubbornly human phase.
- Context engineering and model routing are financial levers: route hard
  reasoning to a large model and routine work (test generation, review, CI
  checks) to a small cheap one.
- Maintenance work that was "too risky to touch" — migrations, deprecation
  cleanups — becomes tractable because an agent can read and refactor it.
- The residual ceiling is the 80% problem: the last 20%, edge cases and seams
  between systems, still needs context the model usually lacks.

## Candidate patterns / evidence

- → harness-first-debugging: paper's 10% model / 90% harness split, plus two
  public results (Terminal Bench top-30 to top-5 by harness change alone;
  LangChain +13.7 points from system prompt, tools and middleware only).
- → static-vs-dynamic-context: static rule files are reliable and expensive
  because you pay every turn; dynamic context is paid only when touched, and
  the boundary should be reviewed in a PR and versioned like code.
- → progressive-disclosure: metadata at startup, full skill on match, heavy
  reference last is how one agent carries dozens of skills affordably.
- → tests-vs-evals: tests cover deterministic input/output, evals cover the
  rest, split further into output evaluation and trajectory evaluation.
- → spec-quality-is-the-bottleneck: implementation drops from weeks to hours
  while requirements, architecture and verification stay slow because they are
  judgment work.
- → model-routing-by-task: hard reasoning to a big model, routine generation
  and checking to a small one — "the quality holds and the bill comes down."

## Other-use-case material

- Fleet economics and total-cost-of-ownership framing (vibe coding cheap up
  front, 3–10x more per feature past a crossover point) is a leader/org lens,
  and he flags the crossover as illustrative rather than measured.
- The conductor (real-time, in-IDE) versus orchestrator (async, hand a goal to
  several agents) mode split: only the conductor half is our use case.
- Prototype-to-production agent tooling (Google Agents CLI, Agent Engine, MCP
  and A2A standards) and an Anthropic team's multi-agent C-compiler experiment
  are builder-side.
