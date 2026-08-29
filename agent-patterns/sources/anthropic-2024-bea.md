---
id: anthropic-2024-bea
title: Building effective agents
author: Anthropic (Erik Schluntz, Barry Zhang)
date: 2024-12-19
url: https://www.anthropic.com/engineering/building-effective-agents
access: direct
accessed: 2026-08-29
scope: builder
relevance: high
pass: distilled
patterns: [start-simple, workflow-or-agent, evaluator-loop]
---

## Summary

Anthropic's engineering post on what works when building LLM agent systems,
drawn from working with dozens of teams. Its core architectural move is to split
"agentic systems" into **workflows**, where LLMs and tools run through
predefined code paths, and **agents**, where the LLM directs its own process and
tool use. Its core advice is to find the simplest solution that works and add
complexity only when it demonstrably improves outcomes — often that means no
agentic system at all, just a well-optimized single call with retrieval and
examples. It then catalogues five composable workflow patterns (prompt chaining,
routing, parallelization, orchestrator-workers, evaluator-optimizer) with
when-to-use notes, describes autonomous agents as an LLM using tools in a loop
against environmental ground truth with checkpoints and stopping conditions, and
closes on three principles: simplicity, transparency about planning steps, and a
carefully engineered agent-computer interface. A 2026 banner notes the tooling
landscape has since changed. **Nearly all of this is builder-side** — see the
final section.

## Takeaways for our use case

- Start with the simplest thing that could work and add structure only when it
  demonstrably improves the outcome: the same discipline applies to a session's
  scaffolding (skills, subagents, custom commands) as to an agent architecture.
- The workflow-vs-agent distinction transfers as a per-task decision: when the
  steps are known and fixed, spell them out; when the number and nature of steps
  can't be predicted in advance, hand the goal over and let the model direct
  itself.
- Complexity has a price the post states plainly — agentic systems trade latency
  and cost for task performance, and autonomy brings compounding errors — so
  more machinery is a tradeoff to justify, not a default.
- Evaluator-optimizer is the one workflow pattern that maps cleanly onto a solo
  interactive session as a review loop: one pass generates, a second pass
  critiques against explicit criteria, repeat. The post gives two conditions for
  when this is worth doing — the output is demonstrably improved when a human
  articulates feedback, *and* the model can produce that feedback itself. If
  either fails, the loop just burns tokens.
- The post's own coding-agent notes: code is a good fit because tests verify
  solutions and the agent can iterate on test results as feedback — but "human
  review remains crucial" for whether a solution fits the broader system, which
  automated tests can't check.
- Ground truth matters more than narration: an agent should be assessing
  progress from real tool results and code execution at each step.

## Candidate patterns / evidence

- → `start-simple`: explicit recommendation to find the simplest solution and
  increase complexity only when needed, restated in the summary as "add
  multi-step agentic systems only when simpler solutions fall short."
- → `workflow-or-agent`: the workflows-vs-agents distinction, with the selection
  rule that workflows give predictability for well-defined tasks and agents suit
  open-ended problems where you can't hardcode the path.
- → `evaluator-loop`: the evaluator-optimizer workflow — generation and critique
  in a loop — plus its two stated fit conditions (articulated feedback helps,
  and the model can supply that feedback).
- → `tests-as-agent-feedback` (weak here, better evidenced elsewhere): coding is
  called a strong agent fit because solutions are verifiable by automated tests
  and the agent iterates on test results, while human review still decides
  system fit.

## Other-use-case material

This source is builder-side; most of it should not become interactive patterns.

- **The five workflow patterns as architecture** — prompt chaining (with
  programmatic gates), routing (including cheap-model/strong-model routing),
  parallelization by sectioning or voting, and orchestrator-workers — are
  designs for systems you build and run, not moves inside one session. Useful as
  shared vocabulary; flag as `scope: builder` if any are written up.
- **Frameworks advice** (start from LLM APIs directly, understand what's under
  any framework's abstraction, since wrong assumptions about the internals are a
  common source of error) is for people writing agent code.
- **Appendix 2, prompt-engineering your tools / the agent-computer interface** —
  give the model room to think before it commits, keep formats close to what
  appears naturally in text, avoid formatting overhead like line counting or
  string escaping, poka-yoke the arguments, test with many example inputs — is
  MCP/tool-author material. Relevant only if the user writes their own tools;
  overlaps `anthropic-2025-tools`.
- **Appendix 1A, customer support agents**, is out of scope entirely.
- Dated: the post carries a 2024 date and a publisher's note that the tooling
  landscape has changed, pointing at Claude Managed Agents. The simplicity and
  workflow-vs-agent arguments look durable; anything about specific tooling
  should not be cited as current.
