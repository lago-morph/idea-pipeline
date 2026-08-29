---
id: every-2026-08-07-make-a-jig
title: "Designing With AI? Make a Jig."
author: Jack Cheng
date: 2026-08-07
url: (Gmail export, local mbox)
access: gmail
accessed: 2026-08-29
scope: interactive
relevance: high
pass: distilled
patterns: [jig-for-tuning, ask-for-a-tool-not-a-tweak, pause-before-irreversible-actions]
---
## Summary

Cheng borrows a woodworking term: a jig is a tool you build to make another
thing easier or more precise. Producing an interactive article with a coding
agent, he found it tedious to prompt the agent repeatedly to speed up, slow, or
thin a particle animation, so he asked it to build a control panel embedded in
the page exposing the parameters buried in the code — proximity to text blocks,
size and opacity ranges. Playing with the sliders, rather than describing what
he wanted, is what clarified the design. He built further jigs for text
placement and drop caps; the largest tuned 27 variables for a single section.
The argument for why prompting alone is not enough is that chat is a coarse
instrument compared with direct, visible, reversible manipulation, and designers
are rediscovering this. Jigs range from single-use hacks to reusable kits
(DialKit, Toolcraft) and are now shipping inside tools (Codex browser annotation
mode, Figma Motion). The piece ends with a reusable prompt for asking Codex or
Claude Code to build one.

## Takeaways for our use case

- When you are iterating on a value rather than a behaviour, stop prompting and
  ask the agent to build you a control surface for that value.
- Jigs make visible the parameters that are otherwise hidden in the code — you
  would otherwise have to read the source or interrogate the agent for them.
- Tight, immediate feedback is what lets you discover what you want; a prompt
  round-trip is too coarse and too slow for that kind of exploration.
- The cost is worth it when a job is hard to do precisely or tedious to repeat —
  the same test a woodworker applies before making a jig.
- Ask the jig to persist its settings so it survives restarts and disconnects,
  and to require your approval before any local adjustment goes public.
- Prefer an off-the-shelf control kit when one fits; build a single-use jig when
  the parameters are specific to this artefact.

## Candidate patterns / evidence

- → jig-for-tuning: "I asked the agent to make me a control panel, embedded on
  the page, that would allow me to adjust all the parameters hidden in the code
  itself"; one jig exposed 27 visual variables for a single story section.
- → ask-for-a-tool-not-a-tweak: it "would've taken too long to prompt my way
  there — if I was able to at all", so the agent's job became building the tool
  rather than making each change.
- → pause-before-irreversible-actions: the shared prompt ends with "ask me
  before making any local adjustments public", keeping a human gate between
  experimentation and the published artefact.

## Other-use-case material

- The survey of prebuilt jig kits (DialKit, Toolcraft) and platform features
  (Codex annotation mode, Figma Motion, Google Flow) — tool-landscape material
  that will date quickly.
- Wattenberger's speculation that agents will auto-generate a playground with
  adjustable panels at the start of a session — forward-looking, not a practice
  to adopt today.
