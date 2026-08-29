---
id: tier-review-by-risk
title: Tier review depth by risk
type: pattern
status: adopted
durability: structural
scope: interactive
tools: both
category: review-quality
verified: 2026-08-29
models: [claude-5, gpt-5.6]
confidence: medium
sources: [osmani-2026-agentic-code-review, osmani-2026-code-review-ai]
related: [review-agent-diffs, test-the-failure-paths, calibrate-autonomy]
aliases: []
---
# Tier review depth by risk

**Use when:** deciding how much of your attention a given change deserves — which is every change, once the agent produces more diff than you can read closely.

**Do:**
- Rate the change on three variables: blast radius, how long the code will live, and how many people must understand it. Set review depth from the rating, not from the task's name.
- Give a config tweak a linter and a glance; give a payments or auth path types, tests, two independent reviewers, a security pass, and a named human owner.
- Write a short contract for the change: what and why, proof it works, risk tier plus which parts the agent wrote, and the one or two places you want scrutiny. If you cannot fill it in, you do not understand the change yet.
- Keep deterministic gates — CI, lint, coverage thresholds — strict at every tier.

**Why:** one fixed review standard either burns attention on trivia or waves through the change that can actually hurt you. Advice written for an enterprise misfires on a solo project, and vice versa.

**Don't / when not:** a low tier is not permission to skip verification; it defers it.

**Evidence:**
- [osmani-2026-agentic-code-review] review depth should follow blast radius, code lifetime, and reader count — a config change earns a linter and a glance, a payments path earns types, tests, two AI reviewers, a human owner, and a security pass; deterministic gates must stay strict because agents weaken CI to reach green.
- [osmani-2026-code-review-ai] the PR contract carries risk tier and which parts were AI-written, and auth/payments/secrets/untrusted-input always get a human threat-model pass plus a security tool.
