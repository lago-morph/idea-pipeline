---
id: every-2026-06-29-powerpoint-automation
title: AI Could Do Anything. Then It Met PowerPoint.
author: Mike Taylor
date: 2026-06-29
url: (Gmail export, local mbox)
access: gmail
accessed: 2026-08-29
scope: mixed
relevance: high
pass: distilled
patterns: [skill-authoring, blueprint-then-approve, context-rot, prefer-formats-the-model-knows, distrust-agent-self-report, isolate-failures-into-skills, automate-only-at-volume]
---
## Summary

Every's head of tech consulting recounts a months-long attempt to automate slide
production, first with Anthropic's official pptx skill and then with skills of
their own. The model is good at slides as a layout problem — the author argues it
is fluent in HTML and treats a slide the same way — but goes wrong the moment a
company template, brand style, or an edit to an existing deck is involved,
because .pptx is XML the model cannot mentally render. Their first real win was a
blueprint step: the agent drafts a slide plan with visual direction notes from
call-note-derived inputs and waits for human approval in Slack before generating.
Scaling that to a client doing 25 decks a week took three weeks of debugging into
a 24-skill, 11-phase plugin. The closing judgment is that full automation only
pays at high volume and near-zero defect rates.

## Takeaways for our use case

- Have the agent produce a plan/blueprint with explicit intent per unit of work and approve it before it generates the artifact; this caught shallow work and avoided wasted tokens.
- Watch the context budget: the piece puts the onset of "context rot" — the model getting confused and making dumb mistakes — past roughly 200k tokens of loaded material.
- Prefer a representation the model is fluent in (HTML here) over one it is not (XML/.pptx); the model cannot predict how the format it cannot render will actually look.
- Never accept the agent's own claim that its output is good: here it wrote content-only evaluation code, never looked at the rendered decks, and declared its version better while slides were visibly broken.
- Split each recurring failure out as its own small unit and iterate on it in isolation rather than re-running the whole hour-long pipeline.
- Where an output must be deterministic (colors, fonts), have the agent write a script instead of leaving it to generation.
- An 80-percent-right artifact can be worse than none, because reviewing a polished-looking wrong result is harder than doing it yourself.
- Below a real volume threshold, don't automate — wait for the next model or a better published tool.

## Candidate patterns / evidence

- → skill-authoring: an "outrageous amount of work writing, testing, and orchestrating skill.md files" was needed before automation was genuinely useful; Anthropic's own pptx skill is 59 files and ~7,000 words.
- → blueprint-then-approve: the biggest single improvement was making the agent write a slide-by-slide plan and wait for approval in Slack before producing the deck.
- → context-rot: piling more than ~200,000 tokens of research into one session makes the model start making dumb mistakes.
- → prefer-formats-the-model-knows: the model lays out decks well because a slide is a layout problem like HTML, but struggles with .pptx XML it cannot mentally render.
- → distrust-agent-self-report: after eight self-graded rounds the agent declared success without ever opening a deck; its self-written metrics checked content, not appearance.
- → isolate-failures-into-skills: every recurring failure was spun out as its own skill and A/B tested until it disappeared, avoiding hour-long full pipeline reruns.
- → automate-only-at-volume: fully automating this isn't worth it unless you do hundreds of similar artifacts a month; otherwise automate what you can and wait for the next model.

## Other-use-case material

- Builder-scale: the client pipeline is 24 skills, 11 phases, 18 Python scripts, 28.9M tokens and $62 per deck — an economics and orchestration story, not an interactive-session pattern. Flag as `scope: builder`.
- Long-running: an always-on assistant on an office Mac Mini producing decks while the human is offline/travelling, with feedback given asynchronously in Slack. Flag as `scope: long-running`.
- Skill chaining as orchestration (one skill hands off to the next, with parallel and sequential phases) is builder-side pipeline design.
