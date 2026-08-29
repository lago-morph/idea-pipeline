---
id: checkpoint-commits
title: Commit small, commit often
type: pattern
status: adopted
durability: structural
scope: interactive
tools: both
category: version-control
verified: 2026-08-29
models: [claude-5, gpt-5.6]
confidence: medium
sources: [osmani-2026-ai-coding-workflow, willison-2026-aep]
related: [small-reviewable-steps]
aliases: []
---
# Commit small, commit often

**Use when:** an agent is making edits you may want to undo — any session that
changes more than one thing.

**Do:**
- Commit after every chunk that is finished *and* tested, so each commit is a save
  point you can revert to in one command.
- Write real messages: the history is also the brief you hand the agent later, and
  what `bisect` reads.
- Split work into separate commits even when it feels fussy — the agent does the Git
  work now.
- Hand messy history to the agent as a task ("clean up this branch"); rebase,
  reflog, and bisect are within its reach.
- Attach your own testing evidence to the commit or PR rather than the agent's claim
  of success.

**Why:** cheap generation is only safe with cheap undo. Frequent commits cap the cost
of a bad suggestion at one revert instead of an archaeology session, and a tidy
history lets you brief the agent with diffs.

**Don't, when not:** throwaway spikes in a scratch worktree you intend to delete.

**Evidence:**
- [osmani-2026-ai-coding-workflow] commit after each completed-and-tested chunk so a bad suggestion costs one revert, and history stays bisectable.
- [willison-2026-aep] keep everything in Git and treat history as an editable narrative; agents are fluent enough at rebase, reflog and bisect that history surgery is a viable prompt.
