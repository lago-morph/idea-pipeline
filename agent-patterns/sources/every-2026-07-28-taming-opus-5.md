---
id: every-2026-07-28-taming-opus-5
title: Taming Opus 5
author: Katie Parrott
date: 2026-07-28
url: (Gmail export, local mbox)
access: gmail
accessed: 2026-08-29
scope: interactive
relevance: high
pass: distilled
patterns: [full-brief-up-front, judge-the-artifact, concise-output-style, skill-audit-on-model-release, model-switching-on-stuck]
---
## Summary

A newsletter round-up of how the Every team adapted to Claude Opus 5 in its
first week. The complaints are consistent: the model needs repeated prompting
to keep answers simple, narrates as if talking to another agent rather than a
person, and is blunt to the point of rudeness. What the team converged on is a
working style rather than a fix — hand Opus a substantial job with a clear
finish line, state up front that you are stepping away and it should batch its
work and surface only blocking questions, then leave it alone; Anthropic's own
prompting guide gives the same advice. Judge what comes back by the artifact,
not by the running commentary. For unreadable narration, push conciseness rules
into Claude Code output styles (or a shared skill) instead of correcting the
tone turn by turn. The author remains unconvinced, getting a better deck from a
different model on the same inputs. The section on whether an older skill or the
new model is at fault is cut off by the paywall.

## Takeaways for our use case

- On a new frontier model, put the whole brief in the first prompt and let it
  run to a clear finish line rather than steering it step by step.
- Telling the agent you are away, and asking it to batch work and raise only
  blocking questions, produced good results for three separate people.
- Evaluate the finished artifact on its own terms; the model's account of how it
  got there is not the deliverable and can mislead.
- If the model's tone or verbosity is the problem, encode the fix once (output
  style, skill, rules file) instead of repeating "I don't understand you".
- A model release can invalidate prompts and agent instructions built for the
  previous model; expect to re-tune them rather than assume regression.
- When a model is a bad fit for your kind of work, the honest option is to use a
  different one — the author got a usable deck from GPT-5.6 Sol on identical
  inputs.

## Candidate patterns / evidence

- → full-brief-up-front: two team leads independently "handed Opus a
  substantial job with a clear finish line, then left it alone" and got good
  results; a third told it he was stepping away so it should batch work and only
  ask blocking questions.
- → judge-the-artifact: the advice is to evaluate the output on its own without
  getting bogged down in the model's narration of its process.
- → concise-output-style: conciseness and action-orientation rules were moved
  into Claude Code output styles so they filter every response automatically.
- → skill-audit-on-model-release: the piece flags a workflow for checking
  whether skills built for an older model now get in the new one's way, and
  Anthropic's own note that prompts and agent instructions may need revisiting.
- → model-switching-on-stuck: same presentation inputs produced an unusable
  draft from Opus 5 and a presentable one from another model.

## Other-use-case material

- A reusable image-workflow "Technique" (extract visual rules from a reference,
  fan out three concepts, package for teammates) — builder / non-coding scope.
- The full "is it the skill or the model?" debugging workflow is behind the
  paywall; only the framing of the question survives in this email.
