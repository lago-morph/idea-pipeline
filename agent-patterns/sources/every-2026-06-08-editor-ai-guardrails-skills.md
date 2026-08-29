---
id: every-2026-06-08-editor-ai-guardrails-skills
title: My Editor Caught Me Sounding Like AI. Now AI Catches Me First.
author: Katie Parrott
date: 2026-06-08
url: (Gmail export, local mbox)
access: gmail
accessed: 2026-08-29
scope: interactive
relevance: high
pass: distilled
patterns: [staged-reviewer-skills, codify-failures-as-instructions, named-reviewer-personas, synthesize-conflicting-reviews, capture-lessons, iterate-skill-against-known-cases]
---
## Summary

After her editor listed the recurring weaknesses in her drafts, the author turned
that list into a skill — a Markdown file of standing instructions — called
`/guardrails`, and then built a family of similar reviewers. Each has a
deliberately memorable persona name and one job: one hunts for lost tension, one
checks whether a non-expert reader gets lost, one attacks the weakest reading of
the argument. She runs different reviewers at different stages: argument
pressure at the outline, line-level checks after each drafted section, whole-piece
reviews on the full draft, and a team checklist before handing off to a human.
A `/panel` command runs several reviewers in parallel and then has a synthesizer
read their outputs together, preserving disagreements rather than averaging them.
She frames the reviewers as protection from her own defaults as much as the
model's, and stresses continual updating.

## Takeaways for our use case

- Turn each piece of review feedback you receive into a line in a reusable
  reviewer skill instead of trying to remember it; the file is where the lesson
  lives.
- Split review into several narrow reviewers with one concern each, rather than
  one "review this" prompt — each asks a different question and they catch
  different things.
- Give reviewers names sticky enough that you reach for them under pressure; the
  author is explicit that clinical descriptors don't get invoked.
- Match the reviewer to the stage: structural pressure while the plan is still
  cheap to change, line-level checks per section as you go, whole-artifact review
  once complete, and a checklist sweep before handing to a human.
- Run line-level checks per section rather than only at the end, to catch drift
  while it is still local.
- When several reviewers run at once, add a synthesizer step that reports
  consensus, genuine tensions and the one open question — and keep the
  disagreement intact, because that is the decision you have to make.
- Re-run the reviewers after revision: the source notes that revisions reintroduce
  the same tells the earlier pass removed.
- Treat reviewer files as living: note what each one caught, missed and got wrong,
  and edit the skill file accordingly before running it again.

## Candidate patterns / evidence

- → staged-reviewer-skills: named reviewer skills are invoked at distinct stages —
  outline, per-section draft, full draft, final checklist — each with a different
  target.
- → codify-failures-as-instructions: the whole `/guardrails` skill began as the
  list of her own recurring failure modes, written down so they stop recurring.
- → named-reviewer-personas: personas with clear single jobs are used because
  memorable names get invoked, unlike "assess narrative momentum".
- → synthesize-conflicting-reviews: `/panel` runs reviewers in parallel and a
  synthesizer reconciles them into consensus findings, productive tensions and one
  hard question, leaving conflicts unresolved for the human.
- → capture-lessons: the author's standing habit is to bake anything newly learned
  into agent documentation, and to add new watch-items to old skills over time.
- → iterate-skill-against-known-cases: her onboarding instructions are to run one
  reviewer on a draft you know well, record hits and misses, update its SKILL.md,
  and repeat until the feedback is useful.

## Other-use-case material

- The domain is editorial writing, not code; the transferable object is the
  staged-reviewer mechanism, and the specific reviewer content (AI tells, hedges,
  house style) does not transfer.
- The author notes that defining standards precisely enough for a model to apply
  them is extra work that pays off in understanding your own standards — a claim
  about the human, not about the agent workflow.
- A public repo of her reviewer skills is linked from the newsletter; the skills
  themselves are not in this text.
