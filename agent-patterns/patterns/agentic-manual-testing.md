---
id: agentic-manual-testing
title: Have the agent test like a human
type: pattern
status: adopted
durability: structural
scope: interactive
tools: both
category: review-quality
verified: 2026-08-29
models: [claude-5, gpt-5.6]
confidence: medium
sources: [willison-2026-aep, every-2026-06-10-fable-5-get-most-out]
related: [give-a-runnable-check, demand-evidence-not-summary, polish-pass]
aliases: []
---
# Have the agent test like a human

**Use when:** the suite is green and you are about to believe it.

**Do:**
- Ask the agent to exercise the change the way a person would: `python -c`, `curl` against a dev server, a throwaway script in `/tmp`, a real browser session.
- Make it verify in the environment where the thing actually runs, not by reading the code.
- Have it record the session as a document built from executed commands and their real output, so the record cannot drift into what it hoped happened.
- Turn anything it finds into a permanent test.

**Why:** passing automated tests and obviously broken software coexist routinely; a suite checks the cases someone already thought of, and running the thing checks the rest.

**Don't / when not:** this is an addition to the suite, not a replacement — findings that stay manual get lost.

**Evidence:**
- [willison-2026-aep] a dedicated chapter argues passing tests regularly coexist with broken software, and that agent-driven manual exercise surfaces what the suite missed; the Showboat pattern records the real command and real output to stop the agent writing down what it wished had happened.
- [every-2026-06-10-fable-5-get-most-out] a bug survived a confident code-only fix and was solved only once the model was told to run the app locally and watch it.
