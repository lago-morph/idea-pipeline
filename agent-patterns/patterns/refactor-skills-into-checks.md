---
id: refactor-skills-into-checks
title: Refactor skills into checks
type: pattern
status: candidate
durability: structural
scope: interactive
tools: both
category: compounding
verified: 2026-09-13
models: [claude-5, gpt-5.6]
confidence: low
sources: []
related: [prefer-deterministic-controls, capture-lessons, skill-authoring, bloated-instruction-surface]
aliases: []
---
# Refactor skills into checks

> **Placeholder — direction stated, evidence pending.** Recorded so it is not
> lost; the practitioner behind it has done this to instruction files but not yet
> to a body of skills, and has offered evidence from real projects later. Ask
> before promoting this past `candidate`, and do not put it in `quickref.md`.

**Use when:** you have a set of skills that encode a repeated process in prose,
and you already apply [prefer-deterministic-controls](prefer-deterministic-controls.md)
to new failures.

**Do:**
- Read the skill for the steps that are actually checkable — an ordering, a
  required artifact, a forbidden state — and move those into a hook or a lint.
- Leave in the skill only what needs judgement: what to weigh, when the procedure
  does not apply, what a good result looks like.
- Let the check be the enforcement and the skill be the explanation, rather than
  asking the skill to be both.

**Why:** the same argument as for instruction files. A skill is prose an agent
may or may not follow, it competes for context with everything else loaded, and
it drifts as the surrounding project changes. The checkable part of a procedure
does not need to be re-read every session to hold.

**Don't / when not:** skills that are genuinely all judgement, and skills you are
still discovering the shape of — mechanise a procedure only once it has stopped
changing.

**Evidence:**
- [own] 2026-09-13 stated direction, not yet demonstrated: instruction files on new projects are now kept very tight with the checkable parts moved to hooks and CI, and applying the same treatment to skills is the next intended step. Evidence from real projects offered at a later date.
