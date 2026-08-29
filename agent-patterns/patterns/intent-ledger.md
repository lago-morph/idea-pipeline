---
id: intent-ledger
title: Keep an intent ledger
type: pattern
status: adopted
durability: structural
scope: interactive
tools: both
category: session-setup
verified: 2026-08-29
models: [claude-5, gpt-5.6]
confidence: medium
sources: [osmani-2026-intent-debt, osmani-2026-agents-md]
related: [capture-lessons, agents-md-hygiene]
aliases: []
---
# Keep an intent ledger

**Use when:** a decision, constraint, or "we don't do it that way because…" exists only in
your head, and the next session will start cold without it.

**Do:**
- Write down the why behind decisions that would be expensive to get wrong — goals,
  constraints, non-negotiables, what done means beyond "functionally correct".
- Record the rationale at the moment you decide, not later; a short decision log is enough.
- Mark load-bearing code as load-bearing, so a guard clause nobody can justify does not get
  refactored away.
- Treat the instructions file as a ledger of intent, not a description of the code.
- End the session by writing back what you tried and why it failed.

**Why:** an agent can pay down technical and comprehension debt, but it cannot generate
intent — asked why a constraint exists, it invents a confident reason. Every cold session
re-pays unwritten rationale.

**Don't / when not:** you cannot capture all intent; skip the routine and obvious, and don't
let the ledger grow into a codebase overview.

**Evidence:**
- [osmani-2026-intent-debt] agents can refactor code and re-explain systems, but intent must originate with a human, so a model asked why a 300ms debounce exists invents a reason.
- [osmani-2026-intent-debt] "treat AGENTS.md as your intent ledger, not your config"; lightweight decision records are pure intent-debt paydown.
- [osmani-2026-intent-debt] the failure case is an agent removing a guard clause because nothing ever recorded whether it was load-bearing.
- [osmani-2026-agents-md] what earns a line is the unguessable — do-not-touch warnings and non-obvious conventions — not what the code already shows.
