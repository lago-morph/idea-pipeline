---
id: every-2026-07-07-fable-unknowns
title: Use Fable Before You Know What to Ask
author: Katie Parrott
date: 2026-07-07
url: (Gmail export, local mbox)
access: gmail
accessed: 2026-08-29
scope: interactive
relevance: high
pass: distilled
patterns: [frontier-for-unknowns, cheap-model-instruction-manual, judge-tools-in-project-context]
---
## Summary

A newsletter issue on when an expensive frontier model earns its price. The
framing, drawn from an Anthropic engineer's field guide, is a gap between the
"map" (your prompt, skills, and context) and the "territory" (the actual
codebase and its constraints); the gaps are unknowns the model must decide
about without knowing what you would want. Unknown knowns are standards obvious
to you but never written down; unknown unknowns are questions you never
considered. Two examples: a book manuscript reviewed for unnamed omissions, and
five weeks of copy-editing experiments where the model found the team had been
optimising against a target nobody had validated. The recommendation is to
triage by uncertainty, not task size. Two shorter items cover having the
expensive model write an instruction manual a cheaper model can follow, and a
skill that forces tool advice to cite your project's own facts.

## Takeaways for our use case

- Choose the model by how settled the goal is, not by how big the task is: heavy execution against a clear plan is cheap-model work; an unsettled definition of "good" is where the expensive model pays.
- When the hard part is evaluation rather than execution, say so explicitly — ask the model to find what's missing or to reach its own conclusion, rather than to execute your plan.
- Expect the most valuable output to be a critique of the assignment itself (the wrong baseline, the unvalidated target), not the deliverable you asked for.
- After the expensive model succeeds at a job your everyday model fumbles, immediately have it write the method down: rule-based steps as scripts, judgment calls as a skill with examples, plus defined inputs, outputs, and quality checks.
- Feed the expensive model the failed attempts and the errors, not just the task, when asking it to produce that manual.
- Re-escalate to the expensive model only when the format changes or the written instructions fail in a new way.
- When asking an agent to assess a new library or tool, force it to cite a verified fact about your project (an existing dependency or integration point) plus an external source, and to check prior decisions and disconfirming evidence before it grades.
- A verdict scale (adopt / trial / hold / reject / not-our-problem) each with a follow-on action keeps tool evaluation from ending in vague enthusiasm.

## Candidate patterns / evidence

- → frontier-for-unknowns: reach for the expensive model when the map is incomplete — the goal, constraints, or definition of good are unsettled — and a cheaper one when they are settled.
- → cheap-model-instruction-manual: a recurring clipping job was fixed by having the expensive model document its method, save scripts and editorial instructions outside the chat, and hand the manual to the cheaper model next time.
- → judge-tools-in-project-context: an agent asked about a new library judges it in general and ignores your dependencies and prior decisions unless the workflow requires project-specific evidence before a verdict.
- → distrust-agent-self-report (supporting): the copy-editing example shows five weeks spent improving performance against a target nobody had validated — the premise, not the execution, was the defect.

## Other-use-case material

- Data point: a fine-tuned open model beat every frontier model tested on six financial tasks at 13.8x lower cost per task — evidence for cheap specialists on repeated, well-defined work, but a model-selection/economics point rather than an interactive-session pattern.
