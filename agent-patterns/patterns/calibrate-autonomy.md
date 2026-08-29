---
id: calibrate-autonomy
title: Calibrate autonomy to verification
type: pattern
status: adopted
durability: structural
scope: interactive
tools: both
category: delegation
verified: 2026-08-29
models: [claude-5, gpt-5.6]
confidence: medium
sources: [osmani-2026-agentic-autonomy-levels, osmani-2026-practical-loop-engineering, dontvibe-2025]
related: [full-brief-up-front, tier-review-by-risk]
aliases: []
---
# Calibrate autonomy to verification

**Use when:** deciding, per task, how far to let the agent run before you look.

**Do:**
- Set the autonomy level from the verification you have, not from the task's name.
- Ask the three questions first: how fast would you know you're wrong, how cleanly
  could you undo it, and what would prove you're right.
- Delegate bounded work with a clean rollback and a real check; watch anything
  touching auth, security, money, or your own still-forming judgment.
- Raise autonomy only as evidence accumulates, and decide task-by-task whether the
  work suits an agent at all.
- When a long run drifts, narrow the scope and improve the evidence rather than
  extending trust.

**Why:** "not quickly, with difficulty, trusting the summary" is not high autonomy —
it is exposure. Verification is the thing that makes delegation defensible, so the
level of delegation has to follow it.

**Don't, when not:** don't turn this into a per-turn approval habit; undifferentiated
approvals dull review and push you toward granting broader access than the task needs.

**Evidence:**
- [osmani-2026-agentic-autonomy-levels] Autonomy should follow the verification process, not the task name, tested by how fast you'd know you're wrong, how cleanly you could undo it, and what would prove you're right.
- [osmani-2026-practical-loop-engineering] Safe, well-bounded work such as docs or coverage checks can be delegated, while complex or auth/security/finance work gets watched closely.
- [dontvibe-2025] A field and survey study of professional developers reports they deliberately keep agency over design and implementation and exercise judgment about which tasks suit an agent.
