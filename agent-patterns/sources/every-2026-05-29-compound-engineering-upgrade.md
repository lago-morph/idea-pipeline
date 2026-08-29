---
id: every-2026-05-29-compound-engineering-upgrade
title: Compound Engineering Gets an Upgrade
author: Kieran Klaassen
date: 2026-05-29
url: (Gmail export, local mbox)
access: gmail
accessed: 2026-08-29
scope: interactive
relevance: high
pass: distilled
patterns: [compound-engineering, human-at-both-ends, capture-lessons, polish-after-review]
---
## Summary

The author, who coined "compound engineering" roughly a year earlier, reports
that his original loop — brainstorm, work, review, compound, repeat — no longer
describes where his attention goes. With capable models and a good plan, the
work phase has become uneventful: the agent writes the code, runs the tests and
fixes the obvious problems. What is left for the human sits at the two ends. At
the front he decides what is worth building and understands the user and the
edge cases; at the back he clicks around, reads the copy and asks whether the
experience is actually good, because a build can pass review and still be bad.
He expands the loop to ideate → brainstorm → plan → work → review → polish →
compound → repeat, keeping compound as the most important step, and argues the
shape generalises beyond engineering. (The email's own subtitle says "four steps
to eight"; the listed loop names seven steps plus repeat.)

## Takeaways for our use case

- Spend your effort at the front and back of a session: deciding what is worth
  doing and judging the finished thing, not supervising the middle.
- Add an explicit ideate/brainstorm stage before planning — the plan is not the
  first step, and a bad choice of work survives a good plan.
- Add an explicit polish stage after review: "passes review" and "is good" are
  different states, and the second one is a human judgement about feel, copy and
  design.
- Keep a compound step at the end of every loop — feed the lessons back so the
  next feature is easier; the author calls this the point of the whole exercise.
- Use the sandwich framing as a session-design check: if you are in the middle
  doing the work, either the plan or the context handed to the agent was thin.

## Candidate patterns / evidence

- → compound-engineering: the source is the primary statement of the loop and its
  expansion to ideate → brainstorm → plan → work → review → polish → compound.
- → human-at-both-ends: the "AI sandwich" — human bread at either end, agent in
  the middle — is the article's organising claim about where attention belongs.
- → capture-lessons: compound remains the most important step because each cycle
  should make the next feature easier; feedback is folded back rather than
  re-taught.
- → polish-after-review: a distinct post-review pass for design, copy and
  experience, on the grounds that everything can technically work and the product
  still not be good.

## Other-use-case material

- The author generalises the pattern to knowledge work broadly ("the middle of a
  lot of work will get automated") — a `meta` framing claim, not evidence for a
  coding practice.
- The full compound engineering guide and the compound engineering plugin are
  linked but not reproduced; the newsletter is a short announcement, so the
  step-by-step mechanics of each stage are not in this text.
