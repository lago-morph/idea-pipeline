---
id: subagents-for-context
title: Use subagents to protect context
type: pattern
status: adopted
durability: compensation
scope: interactive
tools: both
category: delegation
verified: 2026-08-29
models: [claude-5, gpt-5.6]
confidence: medium
sources: [willison-2026-aep, claude-code-docs, horthy-2025-acefca, anthropic-2025-ccbp]
related: [context-compaction, match-model-to-task]
aliases: []
---
# Use subagents to protect context

**Use when:** a step will generate output you will never re-read — searching a large
tree, tracing control flow, digesting logs or JSON, running a noisy test suite,
fetching docs.

**Do:**
- Send that work to a subagent and ask for a short summary, so the raw reads land in
  its window and not yours.
- Scope the request tightly and say what the summary must contain; the summary is
  all you get.
- Keep a small set of subagents defined by *what output they absorb*, not by
  role-play job titles.

**Why:** the main window is the scarce resource and search traffic is the biggest
avoidable consumer of it. A subagent is a fresh window whose cost you pay once, in
compressed form.

**Don't, when not:** the task needs back-and-forth, or it depends on context the main
thread already holds — a non-forked subagent starts with no conversation history and
no files already read. Do not fragment into many specialists.

**Evidence:**
- [willison-2026-aep] subagents are framed primarily as context-limit management, with a warning against over-fragmenting into specialists.
- [claude-code-docs] Anthropic's stated primary use is isolating work that would flood the main conversation with search results, logs or file contents; only the summary returns.
- [horthy-2025-acefca] send file search, code-flow tracing and log digestion to subagents — the point is context control, not anthropomorphised roles.
- [anthropic-2025-ccbp] delegating unscoped investigation puts the file reads in the subagent's context and fixes the "infinite exploration" failure.

**Tool notes:** Claude Code: subagents are markdown files in `.claude/agents/` with
their own context window, tool allowlist and model; the built-in Explore subagent
does read-only investigation, and `/subtask` forks the current conversation while
keeping its tool calls out of your window.
