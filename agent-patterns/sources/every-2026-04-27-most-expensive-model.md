---
id: every-2026-04-27-most-expensive-model
title: You Are the Most Expensive Model
author: Mike Taylor
date: 2026-04-27
url: (Gmail export, local mbox)
access: gmail
accessed: 2026-08-29
scope: interactive
relevance: medium
pass: distilled
patterns: [incremental-determinism, model-tiering, session-to-skill-file]
---
## Summary

Taylor argues the binding cost in an AI workflow is your attention, not tokens,
and that most people get the balance wrong in both directions — overpaying
frontier models for trivial steps while underusing AI where it would free up
their own time. His illustration is that no one asks the McDonald's CEO to work
the grill, and that paying Opus rates to check a to-do list runs to roughly
$1,095 a month. His proposed process is "incremental determinism": each time you
repeat a task, push it further toward a fixed procedure — first by writing a
skill file, then by separating which steps genuinely need the most capable model
from those a cheaper one can do, then by converting the parts that repeat often
enough into ordinary code. The name comes from determinism in programming; the
stated tradeoff is upfront systematisation effort. The email is paywalled partway
through Level 1, so only the framework's shape and its first level are legible.

## Takeaways for our use case

- Ask of each step, not each task, how much intelligence it actually needs — the
  answer is claimed to be usually less than you would assume.
- The first move on any repeated task is to capture it as a skill file: a plain
  text description of how the task is done, applied every time it recurs.
- Write the skill file at the end of the session that figured the task out, while
  the working approach is still in front of you.
- Decompose before downgrading: split a task into steps so the expensive model
  handles only the steps that need it, rather than downgrading the whole task.
- Steps that repeat often enough should stop being model calls at all and become
  code — faster, cheaper, and reliably identical output for identical input.
- Systematising has a real upfront cost, so spend it in proportion to how often
  the task actually recurs; the first pass through a task is meant to be
  exploratory.
- Delegation quality is framed as the fourth lever: the point of the cost work is
  to protect your own attention for what needs you.

## Candidate patterns / evidence

- → incremental-determinism: the source's named framework — each repetition of a
  task justifies nailing down more of it, moving the workflow toward deterministic
  steps that are faster, cheaper, and more reliable.
- → model-tiering: explicit instruction to identify which parts of a process need
  the most expensive model and which can be delegated to cheaper ones, with a
  worked cost figure for the naive default.
- → session-to-skill-file: Level 1 is turning the back-and-forth of a finished
  session into a reusable skill file so later runs need less improvisation.
- → promote-repeats-to-code: tasks that repeat often enough are meant to graduate
  out of the model entirely into ordinary code.

## Other-use-case material

- Levels 2–4 are behind the paywall. The teased contents — testing skills against
  gold-standard examples, a tool for checking whether an older model suffices for
  a task, and decomposing a deck-building task for cost — are all likely relevant
  and worth revisiting if paid access ever appears. Not distilled here.
- Organisation-wide cost control across many people's AI use is `scope: builder`
  material and out of scope for the interactive quickref.
