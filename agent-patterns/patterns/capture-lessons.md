---
id: capture-lessons
title: Capture lessons as history, then mechanise them
type: pattern
status: adopted
durability: structural
scope: interactive
tools: both
category: compounding
verified: 2026-09-13
models: [claude-5, gpt-5.6]
confidence: high
sources: [willison-2026-aep, every-2026-05-29-compound-engineering-upgrade, cheapcode-2026, osmani-2026-intent-debt, every-2026-08-26-cloning-coworkers-skills, osmani-2026-agent-harness-engineering, every-2026-08-04-think-like-designer, lagomorph-2026-k8s-forensics]
related: [prefer-deterministic-controls, intent-ledger, skill-authoring, agents-md-hygiene]
aliases: []
---
# Capture lessons as history, then mechanise them

**Use when:** a session taught you something the next one would need — and,
separately, whenever enough captured sessions have piled up to look across them.

**Do:**
- Capture generously at session end: what failed, what you tried, the why behind
  expensive decisions. This is history, not a rulebook — volume is fine here.
- Treat one session's own recommendations as data, not a to-do list — unless a
  recommendation already *is* a mechanism, in which case ship it.
- Periodically mine the record for threads recurring *across* sessions; those are
  what is worth spending on.
- Convert each thread into the least ignorable mechanism available: a harness
  hook first, then a CI check or a linter — see
  [prefer-deterministic-controls](prefer-deterministic-controls.md).
- Send to prose only what genuinely cannot be mechanised, and keep that file tight.

**Why:** the record is what makes improvement possible at all — reading across
many sessions finds causes no single one can see. But it pays off only if the
output is a mechanism. Prose in an instructions file, an ADR or a skill can be
ignored by both the agent and the harness, accretes until it dilutes itself, and
is read differently by different models. A hook runs regardless.

**Don't / when not:** a one-off with no pattern behind it — record it and do
nothing. An unactionable lesson written up as a rule is pure token load.

**Evidence:**
- [willison-2026-aep] end each project by writing what you learned into the instructions the agent reads next.
- [every-2026-05-29-compound-engineering-upgrade] "compound" is the loop's most important step: each cycle should make the next easier.
- [osmani-2026-intent-debt] a session-end learnings file captures root causes and failed approaches that otherwise stay in your head.
- [osmani-2026-agent-harness-engineering] convert each agent mistake into an AGENTS.md line, hook, or reviewer check so it cannot recur.
- [every-2026-08-26-cloning-coworkers-skills] a self-improve skill interrogates the bad output and proposes a targeted edit to the operating instructions.
- [every-2026-08-04-think-like-designer] a correction made twice becomes a standing rule rather than a third correction.
- [cheapcode-2026] rules written in advance were necessary but not sufficient; the controls that sustained velocity were induced from failures visible only during the agentic work.
- [lagomorph-2026-k8s-forensics] capturing was load-bearing — a six-week forensic analysis was only possible because 45 retrospectives and a full run record had been kept. Emitting rules from them was not: those retros yielded 152 rule candidates and ~51 adopted rules with no measured reduction in the behaviours they targeted, and the fix was amending the retrospective skill to stop emitting rule files at all.
- [own] 2026-09-13 captured retrospectives are what made a six-week forensic analysis possible at all; what fails is only the remedy channel — instruction, ADR and skill edits get ignored — so threads mined from the accumulated record become CI checks, linters and harness hooks instead, and a retrospective's own recommendations are almost never adopted.
