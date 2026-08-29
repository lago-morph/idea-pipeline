---
id: beyondhumanreadable-2026
title: "Beyond Human-Readable: Rethinking Software Engineering Conventions for the Agentic Development Era"
author: Dmytro Ustynov
date: 2026-04-08
url: https://arxiv.org/abs/2604.07502
access: direct
accessed: 2026-08-29
scope: interactive
relevance: medium
pass: distilled
patterns: [agent-legible-code, dont-over-compress-context]
---

## Summary

**Abstract page only — the PDF/HTML full text was not read.** The experiment
result below is quoted as the author reports it; the setup, baseline and
statistical treatment were not seen.

A single-author position paper arguing that six decades of software engineering
conventions were optimized for one consumer — the human developer — and that
LLM agents reading, writing, navigating and debugging codebases are a second
consumer with different constraints. Its proposed design principle is *semantic
density optimization*: strip tokens that carry no information while preserving
tokens that carry high semantic value. The author tests this on log format token
economy across four conditions (human-readable, structured, compressed,
tool-assisted compressed) and reports a counterintuitive result — aggressive
compression cut input tokens by 17% but raised total session cost by 67%,
because the interpretive burden moved into the model's reasoning phase. From
there the paper argues for rehabilitating some classical anti-patterns,
introduces a "program skeleton" idea for agent code navigation, and argues for
decoupling semantic intent from human-readable representation.

## Takeaways for our use case

- Write code, logs and docs for two readers now; conventions that only serve a
  human reader are no longer automatically right.
- Do not optimize an agent's context by compressing text into terse forms: the
  reported experiment shows the cost simply moves from input tokens to reasoning
  tokens and gets worse, not better.
- The useful cut is *zero-information* tokens (boilerplate, ceremony, noise),
  not *high-semantic-value* tokens (names, structure, explicit relationships) —
  those two are easy to confuse when trimming a CLAUDE.md or a log format.
- Judge any context-trimming change on total session cost, not on the input
  token count alone.
- **Can claim from the abstract:** the semantic-density principle, the four log
  conditions, the +67% session cost / −17% input tokens headline, and that a
  program-skeleton concept and anti-pattern rehabilitation are proposed.
  **Cannot claim:** what the program skeleton actually is, which anti-patterns
  are rehabilitated, the experiment's scale, models or task, or whether the
  finding generalizes past log formats. Confidence in the specific number should
  stay low until the full text is read — it is one controlled experiment by one
  author.

## Candidate patterns / evidence

- → `agent-legible-code`: argues LLM agents are now a primary consumer of code
  and that conventions (naming, structure, representation) should be designed
  for their constraints, not only for human readability.
- → `dont-over-compress-context`: controlled log-format experiment reports
  aggressive compression reduced input tokens 17% but increased total session
  cost 67% by shifting interpretive burden into model reasoning.
- → (weak, needs full text) a `program-skeleton` navigation aid for agents is
  proposed but not described in the abstract; do not write a pattern on it yet.

## Other-use-case material

- The "decouple semantic intent from human-readable representation" argument
  points at tooling and language design (a build/IDE-layer concern) rather than
  anything a single practitioner does in a session — flag as builder-side if it
  comes up again.
