---
id: over-compressed-context
title: Over-compressed context
type: anti-pattern
status: candidate
durability: unknown
scope: interactive
tools: both
category: anti-pattern
verified: 2026-09-13
models: [claude-5, gpt-5.6]
confidence: low
sources: [beyondhumanreadable-2026]
related: [context-compaction]
aliases: []
---
# Over-compressed context

**Use when (you are at risk):** you are shrinking something the agent has to read and
interpret — a log stream, a data dump, a handoff summary — and judging the change by
the input tokens it saves.

**Do instead:**
- Cut zero-information tokens: ceremony, boilerplate, repetition.
- Keep the high-value tokens: names, structure, and explicit relationships. These are
  the easiest thing to mistake for padding when trimming.
- Judge any trimming change on total session tokens and wall-clock time, not on input
  tokens alone.
- Treat terse, encoded formats as a hypothesis to measure, not a default.

**Why:** compression does not remove interpretive work, it relocates it. What the
text no longer states, the model has to reconstruct in its reasoning — which can cost
more than the tokens saved.

**Don't, when not:** this is not an argument against compaction or against short
instruction files. Removing genuine noise still helps; the failure is squeezing
meaning out. Past the context window, compressing and fetching selectively is the
right move — and a compressed format paired with a decoder tool beat raw compression.

**Evidence:**
- [beyondhumanreadable-2026] a four-session log-format demo (200 generated events, one session per format, no repeats and no statistics) found abbreviated names cut file tokens 17% but raised session tokens 67% and wall-clock time 4x, the burden moving into the model's reasoning. Correctness was 5/5 in every condition — a token-and-latency finding, not a quality one — and the author disclaims generality beyond linear retrieval.
