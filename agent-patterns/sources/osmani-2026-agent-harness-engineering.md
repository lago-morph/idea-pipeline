---
id: osmani-2026-agent-harness-engineering
title: Agent Harness Engineering
author: Addy Osmani
date: 2026-04-19
url: https://addyosmani.com/blog/agent-harness-engineering/
access: direct
accessed: 2026-08-29
scope: mixed
relevance: high
pass: distilled
patterns: [harness-first-debugging, ratchet-rules-from-failures, agents-md-earn-each-line, hooks-as-enforcement, progressive-disclosure, offload-context-to-filesystem, prune-obsolete-scaffolding, done-condition-first]
---
## Summary

Osmani synthesises work by Viv Trivedy, HumanLayer, Anthropic and others around
one equation: an agent is a model plus a harness, where the harness is every
prompt, rule file, tool, sandbox, hook, subagent and feedback loop wrapped
around the model. His claim is that a decent model in a good harness beats a
good model in a bad one, supported by a Terminal Bench 2.0 result where a team
moved an agent from outside the top 30 into the top 5 by changing only the
harness. The practical consequence is a reframe: when an agent misbehaves, the
failure is usually a configuration failure you can fix today, not a model
limitation to wait out. He then walks the harness components — filesystem and
git as durable state, bash as the general-purpose tool, sandboxes, memory
files, context-rot countermeasures, planning and verification splits, hooks,
and AGENTS.md — and argues harnesses do not shrink as models improve, they
move, because each component encodes an assumption about what the model cannot
yet do alone.

## Takeaways for our use case

- When the agent does something dumb, debug your own scaffolding first: a
  missing convention in AGENTS.md, a rule written too loosely, a missing tool,
  or a context window full of junk.
- Treat every agent mistake as a permanent signal, not a bad run: convert it
  into an AGENTS.md line, a hook, or a reviewer check so it cannot recur.
- Every line in AGENTS.md should trace back to a specific failure or a hard
  external constraint; ratchet rules in from experience rather than
  brainstorming them up front.
- Keep the rule file short — HumanLayer keeps theirs under 60 lines — because
  every line competes for attention and more rules make each rule matter less.
- Hooks are the difference between telling the agent something and the system
  enforcing it: typecheck/lint/test after edits, block destructive bash,
  require approval before pushing.
- Design hook feedback so success is silent and failure is verbose — the error
  text gets injected back into the loop and the agent self-corrects for free.
- Fight context rot with compaction, offloading large tool outputs to files the
  agent reads on demand, and skills that disclose instructions only when a task
  calls for them.
- Prefer ten focused tools over fifty overlapping ones; tool names and
  descriptions are stamped into the prompt every request, and an untrusted MCP
  server's descriptions are prompt-injectable text.
- Remove scaffolding when a model upgrade makes it redundant — Osmani says the
  context-anxiety mitigations he wrote six months earlier became dead code.
- Write the done-condition before starting: he says this has caught more scope
  drift in his own workflows than any prompt change.
- Derive each harness piece from a behaviour you want; if you cannot name the
  behaviour a component delivers, it probably should not be there.

## Candidate patterns / evidence

- → harness-first-debugging: most agent failures are legible configuration
  problems ("it's not a model problem, it's a configuration problem"), and the
  same model scores very differently across harnesses on Terminal Bench 2.0.
- → ratchet-rules-from-failures: a merged PR with a commented-out test becomes
  an AGENTS.md rule, a pre-commit grep for `.skip(`, and a reviewer check.
- → agents-md-earn-each-line: keep the rulebook a pilot's checklist rather than
  a style guide, under ~60 lines, every line traceable to a real failure.
- → hooks-as-enforcement: hooks run at lifecycle points to run tests, block
  destructive commands, and gate pushes, with silent success and verbose
  failure.
- → progressive-disclosure: loading every tool and MCP at startup degrades
  performance before the first action; skills reveal instructions on demand.
- → offload-context-to-filesystem: the harness keeps head/tail of a large tool
  output and writes the rest to disk for the agent to read if needed.
- → prune-obsolete-scaffolding: every harness component encodes an assumption
  about what the model cannot do; when the model improves, the component should
  come out.
- → done-condition-first: writing the done-condition before starting caught
  more scope drift than any prompt change he has made.

## Other-use-case material

- Ralph-loop mechanics (a hook intercepts the model's exit and re-injects the
  original prompt into a fresh context window, with state carried between
  iterations through the filesystem) are a long-running/autonomous pattern.
- Planner / generator / evaluator splits and the "sprint contract" negotiated
  between generator and evaluator come from Anthropic's long-running harness
  work; the underlying principle (agents skew positive grading their own work)
  transfers, the multi-agent structure does not.
- Full context resets rebuilt from a compact hand-off file, and Harness-as-a-
  Service (Claude Agent SDK, Codex SDK) are builder-side concerns.
- Open problems named — many agents on a shared codebase, agents fixing their
  own harness from traces, just-in-time tool assembly — are orchestration
  research directions.
