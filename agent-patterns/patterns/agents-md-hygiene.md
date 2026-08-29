---
id: agents-md-hygiene
title: Keep AGENTS.md short and earned
type: pattern
status: adopted
durability: structural
scope: interactive
tools: both
category: session-setup
verified: 2026-08-29
models: [claude-5, gpt-5.6]
confidence: medium
sources: [osmani-2026-agents-md, anthropic-2025-ccbp, openhands-2026-ccbp, claude-code-docs, codex-docs, agentsmd-spec, osmani-2026-agent-harness-engineering]
related: [auto-generated-agents-md, capture-lessons, intent-ledger]
aliases: []
---
# Keep AGENTS.md short and earned

**Use when:** you are about to add a line to AGENTS.md / CLAUDE.md, or the agent is
ignoring rules already in it.

**Do:**
- Ask of every line: could the agent discover this by reading the code? If yes, cut it.
- Keep the unguessable and operationally significant — tooling gotchas, non-obvious
  conventions, do-not-touch warnings, commands you want run.
- Add entries after real mistakes, one at a time; each line should trace to a failure.
- Prune stale mentions; they bias every later prompt toward what you replaced.
- Move scoped rules into nested files, occasional knowledge into skills, must-happen
  steps into hooks.

**Why:** the file is context, not enforced configuration, and every line competes with
the task for attention — real rules buried among speculative ones are weighted equally
and followed none.

**Don't / when not:** don't cut listed test and lint commands; agents run those.

**Evidence:**
- [osmani-2026-agents-md] generated context files helped only once other repo docs were stripped; the cost is redundancy.
- [anthropic-2025-ccbp] a bloated CLAUDE.md makes Claude ignore real instructions; prune by "would removing this cause mistakes?".
- [openhands-2026-ccbp] start the file late; add entries one at a time as the agent errs.
- [claude-code-docs] under 200 lines is the stated target; conflicting nested rules resolve arbitrarily.
- [codex-docs] Codex concatenates root-first, closest last, and silently truncates past 32 KiB.
- [agentsmd-spec] no required fields, so hygiene is self-imposed; the test is "anything you'd tell a new teammate".
- [osmani-2026-agent-harness-engineering] HumanLayer keeps its rule file under ~60 lines, every line traceable to a real failure.

**Tool notes:** Claude Code: a `CLAUDE.md` containing `@AGENTS.md` bridges both tools;
`/context` shows what loaded. Codex: the chain rebuilds per run, so restart after
editing; `AGENTS.override.md` suppresses its sibling `AGENTS.md`.
