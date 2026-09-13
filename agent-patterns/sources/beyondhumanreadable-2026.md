---
id: beyondhumanreadable-2026
title: "Beyond Human-Readable: Rethinking Software Engineering Conventions for the Agentic Development Era"
author: Dmytro Ustynov
date: 2026-04-08
url: https://arxiv.org/abs/2604.07502
access: direct
accessed: 2026-09-13
scope: interactive
relevance: medium
pass: distilled
patterns: [over-compressed-context, agent-legible-code, comprehension-debt, context-compaction]
---

## Summary

A single-author arXiv preprint (no sign of peer review) arguing that software
engineering conventions were optimised for one consumer — the human developer —
and that LLM agents are now a second consumer with different constraints: token
budgets, a tool call per file read, and sessions that start with no codebase
knowledge. Its design principle is *semantic density*: remove tokens carrying
zero information (boilerplate, ceremony, framework scaffolding), preserve tokens
carrying high information (descriptive names, type annotations, docstrings,
diagnostic error text). One small log-format experiment supports the "don't
compress meaning" half. Everything else — a taxonomy of conventions under
pressure, a `CODEMAP.md` program-skeleton artifact, re-evaluated anti-patterns,
per-language ceremony analysis — the author himself labels as theoretically
motivated and awaiting experiment. The limitations section is unusually candid:
one model, one dataset, plus training-distribution, lost-in-the-middle, and
human-reviewer-cost objections to his own proposals.

## Takeaways for our use case

- The actionable claim is narrow and worth keeping: when you shorten something an
  agent has to *read and interpret*, abbreviating the meaningful parts can cost
  more total tokens than it saves on input.
- The experiment measured session **tokens**, not dollars or quality: correctness
  was 5/5 in every condition, including the most compressed. The penalty showed up
  as tokens and wall-clock time, not wrong answers.
- Judge a trimming change on total session tokens and time, not on the input-token
  count of the file you trimmed.
- The cut that is safe is ceremony and structural boilerplate; the cut that
  backfires is names, labels and explicit relationships. Both look like "making it
  shorter" when you are editing a rules file or a log format.
- Rich, explicit commit messages are argued to be a good token investment for an
  agent, against the 50-character convention — assertion, not measured here.
- The paper's headline finding rests on four single sessions with one model. Treat
  the direction as plausible and the 17%/67% numbers as illustrative, not as a
  measured effect size.
- The paper softens its own abstract: it explicitly does **not** claim classical
  anti-patterns become best practices, only that their cost-benefit shifts, by an
  amount it calls an open empirical question.

## Candidate patterns / evidence

- → `over-compressed-context`: in a log-format experiment, replacing full service
  and event names with abbreviated codes cut file tokens ~17% but raised total
  session tokens ~67%, which the author attributes to a "reasoning tax" — the model
  spent tokens decoding abbreviations and remarked on undefined service codes.
  Strength: one dataset of 200 generated log events, four encodings, one session
  per encoding with claude-sonnet-4-6, five diagnostic questions each, no repeats
  and no statistics. Direction is credible; magnitude is not.
- → `over-compressed-context` (boundary): the same experiment's tool-assisted
  condition (compressed format plus a decoder script) cut the reasoning tax versus
  raw compression but added 5–7 tool calls and an execution error, so at 200 lines
  it still lost to plain prose. The author says a crossover must exist once volume
  exceeds context capacity but did not establish where.
- → `agent-legible-code` (no page yet): argues agents are now a primary consumer of
  code, that descriptive naming rises in value rather than falling, and that
  optimising for machines means semantically dense, not compressed — which he says
  usually coincides with human readability rather than opposing it.
- → `comprehension-debt` (supporting argument, not evidence): the paper's own
  limitations section warns that optimising a codebase for agents transfers
  cognitive load to human reviewers, and that a convention is only optimal if agent
  cost plus human review cost is minimised.
- → `context-compaction` (boundary only): supports compaction-with-selective-access
  once material exceeds the window, while arguing against squeezing meaning out of
  what is loaded.
- → do **not** add an evidence line to `auto-generated-agents-md` from this paper:
  its §2.4 cites the same ETH Zurich context-file study already in that page via
  `osmani-2026-agents-md`, secondhand. Citing it here would double-count one study.

## Other-use-case material

- The `CODEMAP.md` program skeleton — a committed, lossy semantic map of module
  topology, entry points, call chains and signatures, complementary to LSP — is a
  proposal with no evaluation; its controlled test is listed as future work. It is
  also aimed at IDE vendors, who already compute the analysis. Flag as builder-side
  until someone measures it.
- Architectural recommendations (consolidate files, flatten abstraction, revisit
  SOLID, vertical slices, Go over Java-style ceremony) are repo-design decisions
  rather than session practice, and the author marks all of them unvalidated.
- Per-language and per-framework ceremony-to-logic ratios, and the proposal for an
  LLM-native language, are builder-side.
