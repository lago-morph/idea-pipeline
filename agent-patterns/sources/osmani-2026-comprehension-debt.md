---
id: osmani-2026-comprehension-debt
title: Comprehension Debt - the hidden cost of AI generated code
author: Addy Osmani
date: 2026-03-14
url: https://addyosmani.com/blog/comprehension-debt/
access: direct
accessed: 2026-08-29
scope: interactive
relevance: high
pass: distilled
patterns: [comprehension-debt, scrutinize-rewritten-tests, explicit-intent-before-change, explanation-before-code, review-agent-diffs, maintain-system-mental-model]
---
## Summary

Comprehension debt is the growing gap between how much code exists in a system
and how much of it any human genuinely understands. Unlike technical debt, which
announces itself through friction, comprehension debt breeds false confidence:
clean codebase, green tests, and a reckoning that arrives later. Osmani's core
mechanism is a speed asymmetry — review used to be a productive bottleneck that
forced comprehension, and AI broke that loop because generation now outpaces
critical audit. He argues two popular escapes are insufficient rather than
wrong. Tests cannot cover behaviour nobody thought to specify, and a suite that
covered everything would be more complex than the code; specs cannot capture the
mass of implicit decisions an implementation makes, and a spec detailed enough
to replace the program is the program. A cited RCT found AI-assisted learners
scored 17% lower on comprehension, with the largest drop in debugging. The
scarce resource becomes the person who holds a real model of the system.

## Takeaways for our use case

- Track a second question alongside "did it ship": how much of what shipped do
  you actually understand? Nothing in normal velocity metrics captures this.
- Surface correctness is not systemic correctness — clean formatting, passing
  linters and green tests are exactly the signals that historically earned merge
  confidence and now mislead.
- Be ruthlessly explicit about what a change is supposed to do before it is
  written, so there is an intent to check the result against.
- Treat verification as a structural constraint on the work rather than a step
  afterwards.
- When an agent changes behaviour and updates many tests to match, the question
  is no longer "is the code correct" but "were those test edits necessary" —
  and only comprehension can answer that.
- Keep a system-level mental model so you can catch mistakes at architectural
  scale instead of line by line, and know which behaviours are load-bearing.
- Use the agent for conceptual inquiry, not just delegation: cited data puts
  delegation-style users below 40% on comprehension tests and question-driven
  users above 65%.
- Deferring comprehension is a loan, not a saving; it accrues interest quickly
  and is paid at the worst moment.

## Candidate patterns / evidence

- → comprehension-debt (anti-pattern): named and defined here as the gap between
  code that exists and code any human understands; a student team hit the wall
  in week seven, unable to change anything without breaking something because
  "the theory of the system had evaporated".
- → scrutinize-rewritten-tests: the specific failure mode of an AI changing
  behaviour and updating hundreds of tests to match is called out by name.
- → explicit-intent-before-change: the demanded practice is being explicit about
  what a change should do before it is written.
- → maintain-system-mental-model: the durable, scarce skill is holding enough
  system context to see which behaviours are load-bearing and why past decisions
  were made.
- → explanation-before-code: passive delegation impairs skill formation far more
  than active, question-driven use of the same tool.
- → review-agent-diffs: AI output breaks the review-as-comprehension loop, since
  a junior can now generate faster than a senior can critically audit.
- Counter-evidence to note when writing patterns: tests and specs are both
  necessary and both insufficient — neither substitutes for a human
  understanding the change.

## Other-use-case material

- Organisational scope (flagged): the measurement gap where velocity, DORA and
  coverage all look immaculate while comprehension deficits are invisible to
  calibration committees; the assumption that reviewed code is understood code
  no longer holding, so liability is distributed silently; and a prediction that
  regulation will arrive for AI-generated code in healthcare, finance and
  government systems.
