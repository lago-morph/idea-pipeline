---
id: every-2026-04-23-gpt-5-5-vibe-check
title: "Vibe Check: GPT-5.5 Has It All"
author: Katie Parrott
date: 2026-04-23
url: (Gmail export, local mbox)
access: gmail
accessed: 2026-08-29
scope: interactive
relevance: high
pass: distilled
patterns: [plan-handoff-across-models, model-tiering, plan-before-code]
---
## Summary

The newsletter teaser for Every's Vibe Check of GPT-5.5 on release day; the full
review is behind a link, so only the summary bullets are available here. Every
reports GPT-5.5 scoring 62.5 against Opus 4.7's 33.5 on their Senior Engineer
Benchmark, which measures rewriting a messy production codebase the way a senior
engineer would — with humans still in the high 80s and low 90s. The finding they
call the twist: GPT-5.5's best run used a plan written by Opus. They characterise
GPT-5.5 as strongest when given a plan, an existing system, or a tight feedback
loop, and as unusually easy to settle into — fast, personable, assertive enough
to carry a plan through. Opus 4.7 is reported to retain advantages on one-shot
vibe coding, PowerPoint, Ruby, and some broad product-design work. Writing
quality is called the best from OpenAI in about a year.

## Takeaways for our use case

- Planning and execution are separable and can go to different models: the best
  result reported here came from an Opus-authored plan executed by GPT-5.5.
- Choose the model by task shape rather than by leaderboard position — the same
  release notes put one model ahead on structured refactoring and the other ahead
  on one-shot generation from a blank slate.
- If you are handing a task to GPT-5.5, invest in the plan, the existing
  structure, or the feedback loop first; it is reported to underperform its own
  ceiling without them.
- Reach for Opus 4.7 when there is no existing structure to work inside — one-shot
  builds, broad product-design questions, and (per this source) Ruby and slides.
- Treat even the strongest reported score as well short of human: 62.5 versus
  high-80s human performance on the same benchmark is a reason to keep reviewing
  refactors closely.
- Benchmark numbers here are Every's own internal benchmark on one release day;
  weight them as one team's hands-on read, not a settled result.

## Candidate patterns / evidence

- → plan-handoff-across-models: Every's single best Senior Engineer Benchmark run
  paired an Opus-written plan with GPT-5.5 execution.
- → model-tiering: the same review assigns structured refactoring to GPT-5.5 and
  one-shot vibe coding and broad design to Opus 4.7, i.e. route by task shape.
- → plan-before-code: GPT-5.5 is described as shining specifically with a plan,
  an existing system, or a tight feedback loop in place.
- → retune-prompts-per-model: the framing that frontier models each have slow
  spots you must learn — though GPT-5.5 is presented as unusually low-friction to
  adapt to.

## Other-use-case material

None; the available text is entirely about interactive model choice. Note that
the substantive detail (pricing, screenshots, switch/stay guidance) sits behind
the paywalled full article and is not represented here.
