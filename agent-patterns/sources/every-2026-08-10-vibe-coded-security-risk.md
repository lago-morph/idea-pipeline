---
id: every-2026-08-10-vibe-coded-security-risk
title: I Vibe Coded a Security Risk
author: Katie Parrott
date: 2026-08-10
url: (Gmail export, local mbox)
access: gmail
accessed: 2026-08-29
scope: interactive
relevance: high
pass: distilled
patterns: [test-failure-paths, security-review-before-shipping, cross-model-review, codify-failures-as-instructions, pause-before-irreversible-actions]
---
## Summary

A first-person account of shipping an agent-built vulnerability. The author, a
non-engineer, had Claude build an MCP connector for her live app so agents could
fetch and extend a user's style guide. She asked an engineer friend whether the
idea was risky in principle, relayed the gist to the model as "do the safe
version", tested that the connector connected, and deployed. Weeks later she
pointed a different, newer model at the codebase expecting structural criticism;
it found a public registration route that should not have been public, and asked
permission to take the connector down and invalidate active sessions while it
was investigated. Her diagnosis is not hubris but the illusion of explanatory
depth: watching a chain of thought that makes sense feels like understanding the
work. She tested what she wanted the feature to do, never whether someone who
should not connect could. Her rules now: learn the basics of the field you enter,
get a human expert to look for what you are missing, and never let the system
that built the thing be the only evidence it is ready. The AGENTS.md rules she
added are paywalled.

## Takeaways for our use case

- A passing happy-path test proves the feature works, not that it is safe; test
  who or what should be refused, not only what should succeed.
- The agent's reassurance that it "ran its checks" is evidence from the same
  system that wrote the code, and does not count as review.
- Have a different model (or a person) review before shipping anything with an
  auth surface — that is what actually surfaced the open registration route.
- Watching a coherent chain of thought creates a false sense of understanding;
  the test is whether you can state, step by step, what the code does.
- The riskiest gap is the question you don't know to ask, so name the field you
  have wandered into and learn its basic principles before deploying.
- After an incident, write the lesson into the agent's instructions file so the
  next session inherits the speed bump.
- Give the reviewing agent authority to stop things — hers asked to shut down
  the connector and invalidate sessions, and that was the right call.

## Candidate patterns / evidence

- → test-failure-paths: "I had tested what I wanted Tastemaker to do... But I
  didn't test whether somebody who was not supposed to connect could do it
  anyway"; she cites testing research that people probe expected behaviour
  rather than ways a program can fail.
- → security-review-before-shipping: a friend's general advice about agent-used
  APIs "was good advice, but not a security review of what I built" — the live
  feature carried a public registration route for weeks.
- → cross-model-review: a newer model pointed at the same codebase found the
  open route; her rule is that if AI built the thing, the same system's
  reassurance must not be the only evidence it is ready.
- → codify-failures-as-instructions: she added standing instructions to
  AGENTS.md, the file her agent reads before acting, so the failure mode is
  caught next time.
- → pause-before-irreversible-actions: "commit and deploy" is named as among the
  most perilous words a vibe coder can say; the remedy is more speed bumps where
  someone can say "hold on", including a prompt making agents pause before
  irreversible steps (paywalled).

## Other-use-case material

- The "task crossover" statistic (16.8 percent of work-related ChatGPT messages
  involve work from another occupation) — context on who is shipping this kind
  of code, not a practice.
