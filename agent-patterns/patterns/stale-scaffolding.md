---
id: stale-scaffolding
title: Stale scaffolding
type: anti-pattern
status: adopted
durability: structural
scope: interactive
tools: both
category: anti-pattern
verified: 2026-08-29
models: [claude-5, gpt-5.6]
confidence: medium
sources: [every-2026-07-16-case-against-skills, every-2026-07-28-taming-opus-5, osmani-2026-agent-harness-engineering, every-2026-04-17-opus-4-7-vibe-check]
related: [skill-authoring, agents-md-hygiene]
aliases: []
---
# Stale scaffolding

**Use when:** you are at risk of this — a model release just landed, or you are
carrying skills, rules and prompts written months ago for a weakness the model
may no longer have, or adopting a third-party skill you will not maintain.

**Do instead:**
- Audit at each release. Keep instructions carrying information the model cannot
  have: your taste, your templates, private data, a required exact sequence.
- Retest anything written to compensate for a model weakness, and retire what no
  longer demonstrably helps.
- Prove it earns its place: run the same input with and without it and compare,
  on a set of real examples of good output.
- When a new model behaves worse, re-tune the prompts before concluding it
  regressed; re-run your own fixed tasks head-to-head rather than trusting a
  general verdict.
- Adopt third-party skills only from authors who actively prune them.

**Why:** every piece of scaffolding encodes an assumption about what the model
cannot yet do alone. When the assumption expires the text does not — it stays in
context, competes with training, and costs tokens.

**Evidence:**
- [every-2026-07-16-case-against-skills] of 49 public engineering skills benchmarked, 39 had no effect and three made results worse; only seven helped.
- [every-2026-07-16-case-against-skills] many skills raised compute without improving output, the worst by 451%; durable ones supply private context.
- [osmani-2026-agent-harness-engineering] each harness component encodes an assumption about the model; the author's own context-anxiety mitigations became dead code.
- [every-2026-07-28-taming-opus-5] a release can invalidate prompts and agent instructions built for the previous model; expect to re-tune them.
- [every-2026-04-17-opus-4-7-vibe-check] old prompts went stale at the 4.7 release; five testers on fixed tasks produced a split verdict a single benchmark would hide.
