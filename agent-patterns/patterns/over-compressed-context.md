---
id: over-compressed-context
title: Over-compressed context
type: anti-pattern
status: candidate
durability: unknown
scope: interactive
tools: both
category: anti-pattern
verified: 2026-08-29
models: [claude-5, gpt-5.6]
confidence: low
sources: [beyondhumanreadable-2026]
related: [context-compaction]
aliases: []
---
# Over-compressed context

**Use when (you are at risk):** you are shrinking something the agent reads — a rules
file, a log format, a summary handed between steps — and judging the change by the
input-token count it saves.

**Do instead:**
- Cut zero-information tokens: ceremony, boilerplate, repetition.
- Keep the high-value tokens: names, structure, and explicit relationships. These are
  the easiest thing to mistake for padding when trimming.
- Judge any trimming change on total session cost and result quality, not on input
  tokens alone.
- Treat terse, encoded formats as a hypothesis to measure, not a default.

**Why:** compression does not remove interpretive work, it relocates it. What the
text no longer states, the model has to reconstruct in its reasoning — which can cost
more than the tokens saved.

**Don't, when not:** this is not an argument against compaction or against short
instruction files. Removing genuine noise still helps; the failure is squeezing
meaning out.

**Evidence:**
- [beyondhumanreadable-2026] a log-format experiment reports aggressive compression cut input tokens 17% while raising total session cost 67%, the burden moving into the reasoning phase — read from the abstract only, so scale, models, and generality beyond log formats are unverified.
