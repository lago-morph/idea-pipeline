---
id: bloated-instruction-surface
title: Bloated instruction surface
type: anti-pattern
status: candidate
durability: structural
scope: interactive
tools: both
category: anti-pattern
verified: 2026-09-13
models: [claude-5, gpt-5.6]
confidence: medium
sources: [lagomorph-2026-k8s-forensics]
related: [agents-md-hygiene, no-progressive-disclosure, prefer-deterministic-controls, stale-scaffolding]
aliases: []
---
# Bloated instruction surface

**Use when (you are at risk):** you are adding to an AGENTS.md, a skill, or a set
of ADRs that has been growing for months, and you cannot name what the last ten
additions actually changed.

**Do instead:**
- Budget the surface and hold the budget: a line added means a line removed.
- Before adding, check what it contradicts. Two rules that disagree are worse
  than neither, because which one wins is not something you control.
- Move anything mechanically checkable out to a hook, check or linter rather than
  restating it more firmly — see
  [prefer-deterministic-controls](prefer-deterministic-controls.md).
- Retire scaffolding whose original failure mode is gone.

**Why:** best case, an accreted instruction surface spends context the task
needed. Worst case it contradicts itself, and which rule wins is unpredictable —
and differs between models reading the same words. Size disguises this: a longer
file feels like more control while buying less.

**Don't / when not:** a short, earned file is not bloat — see
[agents-md-hygiene](agents-md-hygiene.md) for the positive form. Note that
splitting rules into detail files reduces what *loads*, not what *exists*; that
helps context, but it is not a prune. And the alternative is not free either:
this page and [prefer-deterministic-controls](prefer-deterministic-controls.md)
are two sides of one problem — what to do with a failure you have seen before.
A mechanism costs design time and binds indiscriminately; prose costs context
and binds nothing. Prefer the mechanism because the trade is better, not because
it is cheap.

**Evidence:**
- [lagomorph-2026-k8s-forensics] one project's instruction surface reached 748 lines plus 46 detail files and 21 skills totalling 5,415 lines — roughly 15,200 tokens loaded every session before any project code — while 8 of 12 tracked failure classes recurred after the rule meant to stop them already existed.
- [own] 2026-09-13 instructions accreted across AGENTS.md, skills and ADRs lose effectiveness as they grow, and different models read the same prose differently; new projects now keep the instruction file very tight.
