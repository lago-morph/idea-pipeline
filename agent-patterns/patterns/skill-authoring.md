---
id: skill-authoring
title: Author skills as tested process
type: pattern
status: adopted
durability: structural
scope: interactive
tools: both
category: compounding
verified: 2026-08-29
models: [claude-5, gpt-5.6]
confidence: medium
sources: [osmani-2026-agent-skills, every-2026-05-12-fallacy-16-hour-agent, claude-code-docs, every-2026-06-29-powerpoint-automation, every-2026-07-22-biggest-launch-ever, every-2026-06-08-editor-ai-guardrails-skills]
related: [capture-lessons, stale-scaffolding]
aliases: []
---
# Author skills as tested process

**Use when:** you are writing down a procedure you repeat — a review pass, a
release checklist, a pipeline you have run by hand.

**Do:**
- Write it as a workflow: steps, checkpoints, an exit criterion that produces
  evidence. Not a reference essay.
- Start from a task you already do and can judge; supervise a first run before
  saving anything as a reusable skill.
- Write 5–10 cases first, including negative ones it should not fire on; run it
  on a case you know well, record hits and misses, edit, repeat.
- Phrase the trigger the way you would actually ask for the thing.
- Test every line: would the agent get this wrong without it? If not, cut it.
- Spin each recurring failure out as its own small unit to iterate on alone.

**Why:** an essay gets summarised back at you; a workflow gets executed and can
be verified. Skill text costs context every time it loads, so lines must earn
their place.

**Evidence:**
- [osmani-2026-agent-skills] a skill is a workflow with checkpoints and a defined exit criterion, not reference documentation.
- [every-2026-05-12-fallacy-16-hour-agent] start with 5–10 eval cases including negatives; phrase triggers in user language; cut non-load-bearing lines.
- [every-2026-07-22-biggest-launch-ever] promote instructions to a saved skill only after supervising a first run the agent handled reliably.
- [every-2026-06-08-editor-ai-guardrails-skills] run the skill on a case you know, record hits and misses, edit the file, re-run.
- [every-2026-06-29-powerpoint-automation] recurring failures were spun out as separate small skills and iterated in isolation.
- [claude-code-docs] a skill body loads only when invoked, so procedures cost nothing until used.

**Tool notes:** Claude Code: a skill is a `SKILL.md` folder — keep it under 500
lines with reference material in sibling files, put the key use case first in
`description` (truncated at 1,536 chars), and set
`disable-model-invocation: true` for side-effecting skills. Malformed
frontmatter skips the file silently.
