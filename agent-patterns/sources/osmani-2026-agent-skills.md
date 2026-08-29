---
id: osmani-2026-agent-skills
title: Agent Skills
author: Addy Osmani
date: 2026-05-03
url: https://addyosmani.com/blog/agent-skills/
access: direct
accessed: 2026-08-29
scope: interactive
relevance: high
pass: distilled
patterns: [process-over-prose, skill-authoring, anti-rationalization-table, verification-exit-criteria, progressive-disclosure, touch-only-whats-asked, surface-assumptions-first]
---
## Summary

Osmani explains the design behind his Agent Skills repo, and argues the
generalisable lesson is independent of the repo itself. Coding agents default
to the shortest path to "done" and skip the senior-engineer work that never
shows up in a diff: surfacing assumptions, writing the spec, sizing the change
for a reviewer, leaving evidence that it works. Skills are his attempt to make
that scaffolding non-optional. The central distinction is that a skill is a
workflow with checkpoints and an exit criterion, not reference documentation —
an essay on testing gets read and paraphrased, a workflow gets executed and can
be verified. He names five load-bearing principles (process over prose,
anti-rationalization tables, non-negotiable verification, progressive
disclosure, scope discipline), maps the skills onto documented Google
engineering practice, and closes with five non-negotiables he would put in any
AGENTS.md tomorrow.

## Takeaways for our use case

- Write instruction files as workflows with steps, checkpoints and a defined
  exit criterion, not as reference essays; an essay gets summarised back at you
  while a workflow gets run.
- Any long "how we approach X" document is reference material in disguise —
  convert it to a short workflow with checkpoints and it shrinks substantially.
- Pair each shortcut the agent might rationalise with a written rebuttal in the
  instruction file ("I'll write tests later" → later is the load-bearing word;
  write the failing test first). Models are good at producing plausible reasons
  why this particular task is the exception.
- Make producing evidence the exit step of every task: a green test run, a
  screenshot, a log, a review approval. "Seems right" never closes the loop.
- Passing tests are evidence, not proof — also check the runtime, check
  user-visible behaviour, and have a human read the diff.
- Don't load the whole rulebook at session start; keep a small router that
  points at the right small chapter for the current task.
- Scope discipline ("touch only what you're asked to touch") is, in his view,
  the single biggest determinant of whether an agent's PR is mergeable or has
  to be unwound.
- Five non-negotiables worth copying into AGENTS.md: surface assumptions before
  building, stop and ask when requirements conflict, push back when warranted,
  prefer the boring obvious solution, touch only what you were asked to touch.
- Concrete review/quality norms he encodes: ~100-line PR sizing,
  Critical/Nit/Optional/FYI comment severity labels, DAMP over DRY in tests,
  Chesterton's Fence before deleting code.
- A model has read about a practice in training data but will not apply it
  unprompted at 3am; scaffolding is what makes it actually happen.
- The skill format is portable markdown-with-frontmatter — the same file works
  across Claude Code, Cursor rules, Gemini CLI, Codex and anything else that
  accepts system-prompt content.

## Candidate patterns / evidence

- → process-over-prose: "Process over prose. Workflows over reference. Steps
  with exit criteria over essays without them" is named as the distinction that
  separates a useful skill from a pretty markdown file.
- → skill-authoring: a skill is a workflow — sequence of steps, checkpoints
  producing evidence, defined exit criterion — routed to by a small meta-skill,
  scaled to the actual scope (a bug fix might use three skills, a feature
  eleven).
- → anti-rationalization-table: pre-written rebuttals to excuses the agent has
  not yet made, because LLMs are excellent at rationalising skipped steps.
- → verification-exit-criteria: every skill terminates in concrete evidence;
  the agent is a generator, so you need a separate signal that work is done.
- → progressive-disclosure: activate skills by phase rather than loading twenty
  at startup, since every token loaded degrades performance somewhere.
- → touch-only-whats-asked: agents will decide that fixing one bug requires
  modernising three unrelated files; scope discipline decides mergeability.
- → surface-assumptions-first: wrong assumptions held silently are named as the
  most common failure mode; stop and ask rather than guess when requirements
  conflict.

## Other-use-case material

- He notes skills matter more for long-running agents than chat-style ones,
  because a skipped test in a 30-hour run becomes debugging archaeology; the
  argument that discipline must be enforced rather than suggested scales with
  run length.
- Installation via the Claude Code plugin marketplace is tool mechanics rather
  than a pattern.
