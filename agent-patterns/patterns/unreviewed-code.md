---
id: unreviewed-code
title: Shipping unreviewed agent code
type: anti-pattern
status: adopted
durability: structural
scope: interactive
tools: both
category: anti-pattern
verified: 2026-08-29
models: [claude-5, gpt-5.6]
confidence: medium
sources: [willison-2026-aep, osmani-2026-agentic-engineering]
related: [review-agent-diffs]
aliases: []
---
# Shipping unreviewed agent code

**Use when:** you are at risk of this — the tests are green, the diff is large
and tidy, the agent's PR description reads convincingly, and you are at the end
of a session and inclined to hit merge.

**Do instead:**
- Read the whole diff yourself before filing anything. That first pass is your
  job, not the reviewer's.
- Read and correct the agent-written PR description too; it is persuasive
  enough to need validating.
- Ship several small commits or PRs rather than one large one.
- Attach evidence of your own testing — notes, a screenshot, a log.
- If you cannot explain what a module does, it does not go in.
- Name the mode out loud: if you genuinely are not reading the diffs, you are
  prototyping, not engineering.

**Why:** filing code you have not read delegates the real work to whoever
reviews it — who could have prompted an agent themselves. Not reading the diffs
is the defining feature of vibe coding, and the human still owns architecture,
correctness and long-term maintainability whoever typed the code.

**Don't / when not:** deliberate throwaway prototypes, personal scripts and
learning exercises are legitimately unreviewed — provided nobody ships them.

**Evidence:**
- [willison-2026-aep] "don't file pull requests with code you haven't reviewed yourself"; the agent-written description must be read and validated too.
- [willison-2026-aep] anti-patterns chapter: several small PRs beat one big one, with manual-testing notes or screenshots attached as evidence.
- [osmani-2026-agentic-engineering] not reading the diffs is what defines vibe coding, and it is legitimate only for prototypes and throwaway work.
- [osmani-2026-agentic-engineering] review agent output with the rigour of a teammate's PR; if you cannot explain a module, it does not go in.
