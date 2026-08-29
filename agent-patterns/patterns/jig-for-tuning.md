---
id: jig-for-tuning
title: Ask for a jig, not a tweak
type: pattern
status: candidate
durability: structural
scope: interactive
tools: both
category: execution-loop
verified: 2026-08-29
models: [claude-5, gpt-5.6]
confidence: medium
sources: [every-2026-08-07-make-a-jig]
related: [polish-pass, agentic-manual-testing]
aliases: []
---
# Ask for a jig, not a tweak

**Use when:** you are iterating on a value rather than a behaviour — timings,
spacing, thresholds, opacity — and each round trip is a prompt, a rebuild and a
look.

**Do:**
- Stop prompting for individual adjustments and ask the agent to build you a
  control surface for the parameters: a panel embedded in the thing itself.
- Name the parameters you want exposed, and let the jig surface the ones buried
  in the code.
- Ask it to persist the settings so they survive a restart, and to require your
  approval before any adjustment goes into the published artifact.
- Prefer an off-the-shelf control kit when one fits; build a single-use jig when
  the parameters are specific to this artifact.

**Why:** chat is a coarse instrument for tuning. Direct, immediate, reversible
manipulation is what lets you discover what you actually want; describing it in
prose is slower and less precise, and the parameters are otherwise invisible
without reading the source.

**Don't / when not:** a single adjustment, or a change in behaviour rather than
in a value. The woodworker's test applies — build the jig when the job is hard
to do precisely or tedious to repeat.

**Evidence:**
- [every-2026-08-07-make-a-jig] asking the agent for an embedded control panel exposed parameters hidden in the code; one jig tuned 27 variables for a single section.
- [every-2026-08-07-make-a-jig] prompting to the same result "would've taken too long — if I was able to at all"; playing with sliders is what clarified the design.
- [every-2026-08-07-make-a-jig] the shared prompt asks the jig to persist settings and to ask before making any local adjustment public.
