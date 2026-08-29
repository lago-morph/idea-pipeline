---
id: every-2026-08-04-think-like-designer
title: To Stay Ahead on AI, Think Like a Designer
author: Aishwarya Reganti
date: 2026-08-04
url: (Gmail export, local mbox)
access: gmail
accessed: 2026-08-29
scope: interactive
relevance: high
pass: distilled
patterns: [spec-first, targeted-review-questions, codify-failures-as-instructions, problem-before-tool, capture-lessons]
---
## Summary

Reganti argues that the durable work is no longer execution — which agents
absorb — but the layer above it: defining constraints, standards, and direction
before execution starts, so that people and agents make the decisions you would.
She gives five patterns. Write a spec first, because an agent will start
building before the problem is fully stated and will silently decide whatever
you left out; her worked example includes overview, hero scenario, functional
requirements, behavioral rules, explicit non-goals, and failure modes, and she
notes almost every line encodes something the model could not have known. Review
by asking a handful of pointed questions about auth, expiry, failure paths,
timeouts, and rate limiting rather than reading 200 generated files, since at
agent speed line-by-line review can cost more than generation. Turn recurring
corrections into reusable rules. Choose tools by the problem, not the novelty,
and ask whether an agent can drive the tool. Finally, treat the whole thing as a
loop: outputs are feedback on the constraints that produced them, so review and
update the constraints or quality quietly decays.

## Takeaways for our use case

- Write the spec before the agent writes code: overview, the one scenario that
  must feel right, functional requirements, behavioral rules, non-goals, and
  failure modes.
- Non-goals and failure modes are the highest-value part of a spec — they encode
  what the model cannot infer about your context and taste.
- When output volume exceeds what you can read, review decisions rather than
  lines: five targeted questions about auth, token expiry, failure paths,
  third-party timeouts, and rate limiting.
- Ask questions you know how to judge; the value comes from your own experience
  of the failures that follow from skipping them.
- When you find yourself making the same correction twice, write it into the
  instructions instead of correcting a third time.
- Choose a new tool because it solves a problem in work you understand, and
  because an agent can operate it — not because it is new.
- Schedule a look back at your rules and templates: AI output drifts as models,
  inputs, and needs change, and quality can degrade months later with no
  obvious cause.

## Candidate patterns / evidence

- → spec-first: "the first thing we do at my company is write a specification",
  with a full worked spec showing requirements, behavioral rules, non-goals, and
  failure modes for a small app.
- → targeted-review-questions: faced with 200 agent-generated files, she asks
  five specific questions (auth walkthrough, token expiry, payment failure
  paths, Stripe timeout, rate limiting) instead of inspecting every file.
- → codify-failures-as-instructions: repeated tone and structure corrections
  became a standing prompt rule ("each concept should build on what came
  before"), making one piece of judgment reusable by team and agents.
- → problem-before-tool: ask "does this solve a real problem in work I
  understand well?" and whether an agent can use the tool, rather than "should I
  learn this?".
- → capture-lessons: every output is feedback on the constraints that produced
  it; the loop is set constraints, review results, update the system, repeat —
  otherwise a template that worked for ten engagements silently breaks on the
  eleventh.

## Other-use-case material

- The career framing (moving from execution to the "design layer") and the
  onboarding analogy for setting agent permissions — organisational, not
  single-agent-session material.
- Guardrail questions for agents with system access (CRM, support inbox, group
  chats; send vs. draft) are long-running / builder scope.
