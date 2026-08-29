---
id: every-2026-05-12-fallacy-16-hour-agent
title: The Fallacy of the 16-hour Agent
author: Katie Parrott
date: 2026-05-12
url: (Gmail export, local mbox)
access: gmail
accessed: 2026-08-29
scope: mixed
relevance: high
pass: distilled
patterns: [evals-before-skills, skill-authoring, trigger-phrasing-in-user-language, instructions-as-principles, codify-failures-as-instructions, cut-non-load-bearing-lines]
---
## Summary

A Context Window issue with three unrelated segments. The lead unpacks METR's
updated long-horizon reliability numbers: a preview of Anthropic's next model
tops the 16-hour end of METR's task suite at a 50 percent success rate, but at
80 percent reliability the same model handles tasks that take a human a little
over three hours — and METR's "duration" is a proxy for task difficulty, not
model runtime. The second segment relays Perplexity's published methodology for
writing agent skills that keep working: start with evals, phrase triggers in
user language, write bodies as principles, fold production failures back into
the file, and cut any line that isn't load-bearing. A third segment describes
building a live "watcher" coach (MIDI keyboard into a coding agent) — a
build-your-own-tool pattern, not a coding-session one.

## Takeaways for our use case

- Before editing a skill file, write 5–10 test cases from real queries, known
  failures and edge cases — and include negative cases the skill should *not*
  fire on; the gap between current behaviour and those cases is the work list.
- Write skill trigger lines the way you would actually ask for the thing ("watch
  CI", "make sure this lands"), not in tidy technical nouns, so the skill loads
  without you remembering a magic command.
- Write skill bodies as principles and intent rather than step-by-step
  procedure — the model already knows the commands; it needs to know what
  outcome to preserve.
- After a session where the agent got something wrong, add that failure mode to
  the skill file as a standing instruction rather than re-explaining it next time.
- Apply an edit test to every added line: would the agent get this wrong without
  it? If not, delete it — the source frames each extra line as context cost.
- Treat headline benchmark hours sceptically: the source notes benchmarks measure
  capability *after* a human found a prompt that surfaces it, so reliability
  targets (80 percent) matter more than the top-line number.

## Candidate patterns / evidence

- → evals-before-skills: Perplexity's central lesson is to start with the tests,
  not the skill — 5–10 cases including negative examples, run against the current
  skill to produce a backlog.
- → skill-authoring: the piece is a compact methodology for writing skills that
  don't rot in production, covering triggers, body style, maintenance and length.
- → trigger-phrasing-in-user-language: "Load when…" plus the user's own phrasing
  ("babysit a PR") instead of a clinical descriptor like "monitors pull requests".
- → instructions-as-principles: recommended body style is direction such as
  cherry-pick onto a clean branch and resolve conflicts preserving intent, rather
  than an enumerated command sequence.
- → codify-failures-as-instructions: each production failure gets written into
  the skill file so the mistake becomes a standing guard.
- → cut-non-load-bearing-lines: every candidate line is tested with "would the
  agent get this wrong without this?"; if not, cut it.

## Other-use-case material

- METR long-horizon reliability data and the framing of duration-as-difficulty:
  context for autonomous / overnight agent runs (`scope: long-running`), not for
  interactive sessions. The 16-hour figure is a 50-percent-success measure; at 80
  percent the horizon is roughly three hours.
- The suggested diagnostics for overnight loops — how long did it run, with what
  guardrails, against what feedback signal, at what verified accuracy — belong to
  long-running-agent practice.
- New `/goals`-style commands in Codex and Claude Code that let an agent pursue an
  objective across turns without checking in: mentioned only in passing, no
  usage detail in the newsletter text.
- Building a live watcher/coach app (MIDI in, feedback out; generalises to screen
  capture or camera) is a builder-side use case.
