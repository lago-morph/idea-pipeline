---
id: every-2026-08-26-cloning-coworkers-skills
title: The Case for Cloning Your Coworkers
author: Laura Entis
date: 2026-08-26
url: (Gmail export, local mbox)
access: gmail
accessed: 2026-08-29
scope: interactive
relevance: high
pass: distilled
patterns: [self-improve-skill, capture-lessons, codify-failures-as-instructions, right-size-the-model]
---
## Summary

The section worth borrowing is a "self-improve" skill one operator runs against
her own agent. When the agent returns a wrong result she does two things: fix
the immediate problem, and stop it recurring. She feeds the agent an account of
where it fell short and what a better answer would have been, and once it has
the context she runs a skill that reviews the original output, interrogates what
went wrong, and proposes a targeted edit to the agent's operating instructions.
The worked example is an off-voice Slack draft, which yields a rule about
reading prior thread context before writing. She frames each misstep as data:
why didn't that work, and what does it teach about working with these tools. The
skill is published. The rest of the piece is organisational — packaging one
person's expertise (an editor's copyedits, a CEO's marketing instincts) into
skills the whole company can call — plus a note that the most capable model is
often not the right one, since most tasks get no gain from it while being slower
and dearer.

## Takeaways for our use case

- Treat every wrong agent output as two tasks: fix the artefact, then amend the
  instructions so the failure is less likely next time.
- Give the agent the specific gap — what it produced and what a better response
  would have been — before asking it to diagnose itself.
- Make the improvement step a named, repeatable skill rather than an ad-hoc
  "please remember this", so it runs the same way every time.
- The output should be a targeted edit to the operating rules, not a general
  apology; the example rule is narrow and behavioural.
- Feedback compounds when accepted-versus-rejected decisions are captured and
  fed back, not just the correction itself.
- Reach for the frontier model on genuinely ambitious work and something cheaper
  and faster for the rest — one heavy user reports no relative gain from the top
  model on roughly 80 percent of tasks.

## Candidate patterns / evidence

- → self-improve-skill: when the agent errs she supplies feedback, then runs a
  custom skill that "reviews the initial output, interrogates what went wrong,
  and suggests a targeted edit" to the agent's instructions; the skill is public.
- → capture-lessons: she treats missteps as data to funnel back — "Why didn't
  that work? And what can that teach me about working with these tools?"
- → codify-failures-as-instructions: the concrete outcome is a new operating
  rule (always read prior thread context before writing a message), the direct
  analogue of adding a line to CLAUDE.md / AGENTS.md after a bad session.
- → right-size-the-model: the most capable model is reported as slower and more
  expensive without being better on most knowledge work, with teams routing
  high-volume work to cheaper models.

## Other-use-case material

- Org-wide skill cloning: a copyediting skill trained on 30,000 historical edits
  that a whole team can call, with tracked-changes decisions fed back so it
  compounds, and a planned equivalent for a CEO's marketing judgment — builder /
  organisational scope, and the open question of which kinds of work have a
  clean enough dataset to be cloned this way.
- Model-of-the-week roster and open-weight-model market share — tool scope.
- The AI-mandatory hedge fund interview and the AI-bylines debate — meta.
