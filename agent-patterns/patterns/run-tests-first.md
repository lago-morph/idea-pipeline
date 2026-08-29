---
id: run-tests-first
title: Open the session by running the tests
type: pattern
status: candidate
durability: structural
scope: interactive
tools: both
category: session-setup
verified: 2026-08-29
models: [claude-5, gpt-5.6]
confidence: medium
sources: [willison-2026-aep]
related: [red-green-tdd, agentic-manual-testing]
aliases: []
---
# Open the session by running the tests

**Use when:** starting work in an existing repo, especially one the agent (or you) has not
touched recently.

**Do:**
- Open with "first run the tests" before describing the task.
- Let the agent discover the test command itself rather than supplying it.
- Read the result as a baseline: what already fails is not yours.
- Follow with the actual request once the suite has run.

**Why:** four words unlock a whole practice. Running the suite makes the agent find the
test command, gives it a size estimate of the project, and biases it toward testing its own
later changes.

**Don't / when not:** a repo with no suite, or one whose suite takes long enough that the
opening move costs more than it returns.

**Evidence:**
- [willison-2026-aep] a dedicated "First run the tests" chapter: the opener makes the agent discover the test command, reveals project size, and puts it in a testing mindset for the rest of the session.
- [willison-2026-aep] short canonical phrases such as "first run the tests" carry a whole engineering practice the models already know.
