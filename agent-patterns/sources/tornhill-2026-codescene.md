---
id: tornhill-2026-codescene
title: "Agentic AI Coding: Best Practice Patterns for Speed with Quality"
author: Adam Tornhill (CodeScene)
date: 2026-02-20
url: https://codescene.com/blog/agentic-ai-coding-best-practice-patterns-for-speed-with-quality
access: direct
accessed: 2026-08-29
scope: interactive
relevance: high
pass: distilled
patterns: [pull-risk-forward, objective-quality-signal, guardrail-hooks, refactor-for-agent-readiness, agents-md-hygiene, coverage-as-guardrail, give-a-runnable-check]
---
## Summary

Tornhill reports that all his production code is now written and maintained by
agents, and argues the shift demands "more rigor, more structure, more code
quality", not less. His diagnosis: agents have no objective measure of good —
they will happily edit tangled code, and after a refactoring cannot tell
whether the result is better or merely rearranged. His six patterns supply
that missing signal: assess code health before pointing agents at an area;
automate quality safeguards at three points (as code is generated, before each
commit, before a PR opens); refactor large legacy functions to widen the
surface agents can work on safely, via a review → plan → refactor → re-measure
loop; write sequencing and decision logic into AGENTS.md so guardrails get
invoked predictably; gate on coverage regression so a deleted test is visible;
and back unit tests with end-to-end tests. The vehicle throughout is
CodeScene's own metric and MCP server.

## Takeaways for our use case

- Before starting agentic work in an area, judge whether the code is in good enough shape for an agent to succeed there; poor quality raises failure rates and token burn.
- If the target code is too tangled, refactor it first rather than asking the agent to implement a feature into the mess.
- Give the agent an explicit, measurable quality target plus a list of concrete issues, so it can form a structured refactoring plan instead of reshuffling complexity and calling it an improvement.
- Break oversized legacy functions into smaller cohesive units as a preparation step; subsequent agent work on them becomes far more reliable.
- Run the quality check at three points, not one: during generation, on staged files before each commit, and across the branch before opening a PR — small issues compound fast at agent speed.
- Write the intended sequencing and decision logic into the agents file, because agents left to themselves invoke available tools opportunistically or not at all, which quietly weakens the guardrails.
- Watch for the agent deleting a failing test; a strict coverage-regression gate makes that move immediately visible.
- Treat coverage as a regression signal against the change, not as an overall target number to hit, which historically just got gamed.
- Keep end-to-end tests that exercise the packaged product, since unit tests only validate local behavior and manual verification becomes the bottleneck at agent speed.

## Candidate patterns / evidence

- → pull-risk-forward: assess whether code is healthy enough for agents before starting; unhealthy code raises the chance an agent fails the task or burns excess tokens, with peer-reviewed work cited for the correlation.
- → objective-quality-signal: agents cannot verify their own improvements — after a refactor they can't tell better from differently-arranged, so a measurable score plus concrete issue list is what turns refactoring into a directed loop (review → plan → refactor → re-measure).
- → guardrail-hooks: three automated safeguard points — continuous review as code is generated, a pre-commit check on staged files, and a branch-vs-base pre-flight before opening a PR — that push the agent back into a fix loop on any regression.
- → refactor-for-agent-readiness: large complex legacy functions inflate error rates and token spend; splitting them into cohesive units first expands the surface where agents can operate safely.
- → agents-md-hygiene: the agents file must carry the workflow, not just the rules — MCP exposes individual tools but not the sequencing, so without documented decision logic agents invoke guardrails opportunistically or skip them.
- → coverage-as-guardrail: a common agent shortcut for a failing test is to delete it; high coverage thresholds used as a regression signal surface that erosion immediately rather than as a gamed vanity number.
- → give-a-runnable-check: unit tests are the foundation that lets agents iterate and converge, but end-to-end tests over the packaged product are what verify real outcomes, and Tornhill treats that higher-level automation as non-negotiable once agents set the pace.

## Other-use-case material

- Product pitch to discount: the patterns are described as productified in CodeScene's Code Health MCP server, and the specific tool names, the Code Health score, and the "aim for at least 9.5" threshold are vendor artifacts. The durable practice is the shape — an objective quality signal, checked at generation/commit/PR, encoded as a workflow in the agents file — not the particular metric or MCP server.
- Also vendor-tinged: the "2–3x speedup" figure is one team's self-report over four months, and the article itself warns off industry productivity numbers a few paragraphs earlier.
- The PR pre-flight check and coverage gates as described sit in CI on a shared branch; the interactive-scope version is running the equivalent check locally before you commit.
