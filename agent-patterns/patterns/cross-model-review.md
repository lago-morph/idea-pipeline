---
id: cross-model-review
title: Review with a different model
type: pattern
status: adopted
durability: structural
scope: interactive
tools: both
category: review-quality
verified: 2026-08-29
models: [claude-5, gpt-5.6]
confidence: medium
sources: [every-2026-07-16-case-against-skills, every-2026-08-10-vibe-coded-security-risk, openhands-2026-ccbp]
related: [review-plans-not-code, review-agent-diffs]
aliases: []
---
# Review with a different model

**Use when:** before shipping anything with an auth, payment, data, or public-endpoint surface — and on any high-stakes change.

**Do:**
- Package the change and hand it to a model from a different family for review; do not let the system that wrote the code be the only evidence it is ready.
- Loop: have the original model check each finding against the code, fix only what this change introduced, rerun the tests, and repeat until no actionable findings remain.
- Constrain the loop — tell it to stop and ask before any fix that would expand the original task.
- On high-stakes work, put the plan through a fresh model too, before code exists.
- Give the reviewing agent standing to halt: taking a feature down while it is investigated is a legitimate outcome.

**Why:** a model reviewing its own output shares its blind spots and its confidence. A different one arrives without the assumptions already baked into the original reasoning.

**Don't / when not:** a second model is a reviewer, not an approver — the findings still need your judgement, and it does not replace a human pass on security-sensitive code.

**Evidence:**
- [every-2026-07-16-case-against-skills] a review skill packages the agent's diff for a different model, then loops verify-fix-rerun until no snags remain, with an instruction to stop and ask before any fix that expands the task.
- [every-2026-08-10-vibe-coded-security-risk] a newer, different model pointed at a shipped codebase found a public registration route that had been live for weeks, and asked to take the connector down while it investigated.
- [openhands-2026-ccbp] on high-stakes changes, a fresh model reviewing the plan catches wrong turns the original reasoning had already baked in.
