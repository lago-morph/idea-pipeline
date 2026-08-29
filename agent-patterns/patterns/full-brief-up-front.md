---
id: full-brief-up-front
title: Full brief up front, then hands off
type: pattern
status: adopted
durability: unknown
scope: interactive
tools: both
category: delegation
verified: 2026-08-29
models: [claude-5, gpt-5.6]
confidence: medium
sources: [every-2026-07-28-taming-opus-5, every-2026-06-10-fable-5-get-most-out]
related: [define-done-first, demand-evidence-not-summary, calibrate-autonomy]
aliases: []
---
# Full brief up front, then hands off

**Use when:** giving a slow, high-capability model a substantial job you are willing
to review only at the end.

**Do:**
- Assemble the context and directives in the first prompt instead of steering turn by
  turn.
- Say you are stepping away, and that it should batch work and surface only blocking
  questions.
- Ask for a specific artifact and shape — a ranked list of ten, evidence per
  recommendation, assumptions flagged — not "make a plan".
- Ask it to flag stale rules, conflicting sources and single-source conclusions.
- Ask for a close-out report: what changed, what was skipped, what needs review, how
  it was verified.
- Judge what comes back by the artifact, not the narration of how it got there.

**Why:** when you stop correcting every turn, the correcting has to happen before the
run instead. Stale context and conflicting goals now propagate undisturbed to the
wrong conclusion.

**Don't, when not:** quick edits, small bugs and back-and-forth brainstorming — those
stay in a tight loop with a faster model.

**Evidence:**
- [every-2026-07-28-taming-opus-5] Three people independently got good results handing over a substantial job with a clear finish line, saying they were away, and asking it to batch work and raise only blockers.
- [every-2026-06-10-fable-5-get-most-out] Work shifts from mid-task iteration to assembling context up front then reviewing the result; the failure mode becomes stale context propagating uncorrected.

**Tool notes:** Claude Code: push standing conciseness and tone rules into an output style so they filter every response instead of being re-corrected each turn.
