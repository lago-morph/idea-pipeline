---
id: red-green-tdd
title: Prompt for red/green TDD
type: pattern
status: candidate
durability: structural
scope: interactive
tools: both
category: review-quality
verified: 2026-08-29
models: [claude-5, gpt-5.6]
confidence: medium
sources: [willison-2026-aep]
related: [run-tests-first, give-a-runnable-check]
aliases: []
---
# Prompt for red/green TDD

**Use when:** the change has a statable behaviour and the project has a test suite the agent can run.

**Do:**
- Say "use red/green TDD" in the prompt — the canonical phrase unlocks the whole practice without you specifying it.
- Require the failing test first, and make the agent show you the failure before it writes the implementation.
- Only then let it make the test pass.

**Why:** test-first guards against two different agent failure modes at once — code that does not work, and code nobody ever calls. Watching the test fail first is what stops a test that passes vacuously.

**Evidence:**
- [willison-2026-aep] a dedicated chapter: test-first suits agents because it guards against both non-working and never-used code, and watching the tests fail first is what stops a vacuously passing test; short canonical phrases like "use red/green TDD" carry the discipline in four words.
