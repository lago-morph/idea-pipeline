---
id: unreviewed-code
title: Shipping unreviewed agent code
type: anti-pattern
status: deprecated
durability: compensation
scope: interactive
tools: both
category: anti-pattern
verified: 2026-09-13
models: [claude-5, gpt-5.6]
confidence: medium
sources: [willison-2026-aep, osmani-2026-agentic-engineering]
related: [review-agent-diffs, prefer-deterministic-controls, tier-review-by-risk]
aliases: []
---
# Shipping unreviewed agent code

> **Deprecated 2026-09-13 — kept for the record, do not apply.** Reading every line
> an agent writes was necessary in 2025; against 2026 models it is not the working
> norm, and the wiki owner's own practice is not to. Re-rated `compensation`: this
> page was working around a model weakness that has eased. What survives is not
> "read every diff" but "don't ship what nothing has checked" — that point now lives
> in [prefer-deterministic-controls](prefer-deterministic-controls.md) and
> [tier-review-by-risk](tier-review-by-risk.md). The evidence below predates the
> judgement and is left unedited. Worth recording: in a captured session covering six merged
> pull requests, neither defect that surfaced — an agent claiming an artifact it
> had never produced, and a validator pinned to the wrong release — was the kind a
> human would have caught by reading a diff.

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
