---
id: review-agent-diffs
title: Review every agent diff yourself
type: pattern
status: adopted
durability: structural
scope: interactive
tools: both
category: review-quality
verified: 2026-08-29
models: [claude-5, gpt-5.6]
confidence: medium
sources: [osmani-2026-agentic-code-review, osmani-2026-code-review-ai, osmani-2026-cognitive-surrender, willison-2026-aep, anthropic-2025-ccbp, karpathy-2026-llmwiki]
related: [unreviewed-code, tier-review-by-risk, small-reviewable-steps]
aliases: []
---
# Review every agent diff yourself

**Use when:** before you merge, push, or open a PR containing anything an agent wrote.

**Do:**
- Read the diff yourself first, as if a junior teammate submitted it. "The tests pass" is not a review.
- Read the agent's PR description and commit messages just as critically — they are written to convince.
- Make the agent state what it tried to do and what it ruled out; keep that with the change.
- Read test-file changes before code changes.
- Add a fresh-context reviewer as a second pass; treat its verdict as a sensor, not a decision.
- Own the merge. If you cannot explain why the code works, do not merge it.

**Why:** the agent's reasoning is discarded before the diff exists, so review is the only place intent gets checked — and you are often the first human ever to read this code. Scanning and approving is ratification, not review.

**Don't / when not:** solo work with no users buys *deferred* review, not skipped verification.

**Evidence:**
- [osmani-2026-agentic-code-review] the agent's reasoning is thrown away before the diff, leaving the reviewer to reconstruct intent nobody wrote down.
- [osmani-2026-code-review-ai] reviewing an AI change means reviewing the plan behind it as much as the diff; a human signs off because a computer cannot be held accountable.
- [osmani-2026-cognitive-surrender] scanning and approving a 600-line PR is ratification — "the surrender was the absence of a decision".
- [willison-2026-aep] the first review pass is your job, and agent-written PR descriptions need validating too.
- [anthropic-2025-ccbp] a fresh-context reviewer sees the result, not the reasoning that produced it.
- [karpathy-2026-llmwiki] gist commenters reviewed the generated artifact rather than the agent's plan, reporting plan review catches far fewer problems.

**Tool notes:** Claude Code: run the second pass as a subagent in fresh context and tell it to report only correctness and requirement gaps — a reviewer asked for findings will invent them.
