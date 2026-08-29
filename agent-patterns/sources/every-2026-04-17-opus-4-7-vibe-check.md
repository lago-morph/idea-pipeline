---
id: every-2026-04-17-opus-4-7-vibe-check
title: "Vibe Check: Opus 4.7 Stopped Reading Between the Lines"
author: Katie Parrott
date: 2026-04-17
url: (Gmail export, local mbox)
access: gmail
accessed: 2026-08-29
scope: interactive
relevance: high
pass: distilled
patterns: [retune-prompts-per-model, specify-tightly, dont-rely-on-gap-filling, rebaseline-at-model-release]
---
## Summary

Every's day-after read on Opus 4.7, based on two hours of live testing by five
testers plus an afternoon of internal discussion; the full review is linked, so
only the highlight bullets are available here. Their unifying claim is that
Anthropic tunes Claude's eagerness like a dial between releases, and that 4.7 is
a hard dial-back from 4.6's gap-filling intuition — the model is more literal and
more precise, and the review's own summary is that it "rewards people who write
tight prompts and frustrates everyone who doesn't." The reported results are
genuinely split: Kieran Klaassen called it the best coding model he had tested,
the first to complete a full e-commerce build including a custom product designer
and reliable cart; Dan Shipper saw it diagnose a messy codebase at
senior-engineer quality and then decline to execute the fix; Brandon Gell found
it missed a data error 4.6 had caught unprompted; Parrott preferred 4.6's prose.

## Takeaways for our use case

- Assume prompts tuned on a previous model are stale after a release, and budget
  time to rewrite them rather than concluding the new model is worse.
- With a more literal model, under-specification stops being cheap: gaps that a
  previous model quietly filled now come back unfilled or unexecuted.
- Do not rely on the model volunteering problems you did not ask about — the
  reported P&L regression is exactly an error the older model surfaced
  unprompted and the newer one did not.
- If the model diagnoses well but stops short of acting, treat that as a
  literalness symptom and ask explicitly for execution, not as a capability gap.
- Expect capability changes to be uneven across task types within a single
  release: the same model was called best-ever for a large coding build and worse
  than its predecessor for personal-essay prose in the same review.
- On a well-specified coding task this is the strongest model the reviewers had
  used; the win condition is the quality of your specification.
- Re-run your own representative tasks after a release rather than trusting a
  general verdict; this source's value is a method (five testers, fixed tasks,
  head-to-head against the predecessor) as much as a result.

## Candidate patterns / evidence

- → retune-prompts-per-model: the review states plainly that old Opus prompts
  will not deliver the results you are used to and need tweaking for 4.7.
- → specify-tightly: 4.7 is described as the best model tested on well-specified
  tasks, and as frustrating for those who do not write tight prompts.
- → dont-rely-on-gap-filling (anti-pattern): the "eagerness dial" was turned
  down, so implicit expectations — including catching an unmentioned data error —
  are no longer met.
- → rebaseline-at-model-release: five testers running fixed personal tasks
  head-to-head against the prior version produced a split verdict a single
  benchmark would have hidden.

## Other-use-case material

- Agentic-work results are mentioned as one of the tested categories but not
  detailed in the available text; the full article is the place to look for
  `scope: long-running` material.
