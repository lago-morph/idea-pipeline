---
id: anthropic-2025-ccbp
title: Best practices for Claude Code
author: Anthropic
date: 2025
url: https://www.anthropic.com/engineering/claude-code-best-practices
access: direct
accessed: 2026-08-29
scope: interactive
relevance: high
pass: distilled
patterns: [explore-plan-code, give-a-runnable-check, specific-prompt-context, agents-md-hygiene, guardrail-hooks, spec-first, course-correct-early, fresh-context-reset, context-compaction, subagents-for-context, review-agent-diffs]
---
## Summary

Anthropic's own guide to driving Claude Code, drawn from internal teams. It
hangs almost everything off one constraint: the context window fills fast and
quality degrades as it does, so context is the resource to manage. From that
follow the guide's main moves — give the agent a check it can run itself so it
stops on pass/fail rather than on "looks done"; separate explore, plan,
implement, commit using plan mode, but skip planning when you could describe
the diff in a sentence; write precise prompts naming files, scenarios, and
example patterns; keep CLAUDE.md short enough that its rules still bind; use
hooks where an action must be deterministic; clear context between unrelated
tasks; push research into subagents; and have a fresh-context reviewer check
the diff before calling it done. It closes by warning against treating any of
this as fixed rules rather than starting points.

## Takeaways for our use case

- Before starting, decide what pass/fail signal the agent can run itself — test suite, build exit code, linter, screenshot diff — because without one the human becomes the verification loop.
- Ask for evidence (the command run and its output) rather than an assertion of success; reviewing evidence is cheaper than re-running the check.
- Use plan mode when the approach is uncertain, several files change, or the code is unfamiliar; skip it when the diff is describable in one sentence, since planning has real overhead.
- Prompt with the file, the scenario, the constraint, and a pointer to an existing example of the pattern you want; vague prompts are for exploration only.
- Treat a second correction on the same issue as a signal to reset: clear context and re-prompt with what you learned, rather than continuing in a session polluted by failed approaches.
- Keep the persistent instruction file short — test each line by asking whether removing it would cause mistakes — and move sometimes-relevant knowledge into skills.
- Where a step must happen every time, encode it as a hook, not as advisory prose in CLAUDE.md.
- Delegate unscoped investigation to subagents so file reads land in their context, not yours.
- For a large feature, have the agent interview you and write a self-contained spec (files, interfaces, out-of-scope, end-to-end verification), then execute it in a fresh session.
- Have a reviewer in fresh context check the diff against the plan, and tell it to report only correctness/requirement gaps — a reviewer asked for findings will invent them.

## Candidate patterns / evidence

- → give-a-runnable-check: "Claude stops when the work looks done" unless a check it can run supplies a pass/fail signal; the guide grades checks from in-prompt, to a goal condition, to a Stop hook, to a second-opinion subagent.
- → explore-plan-code: names a four-phase explore → plan → implement → commit loop in plan mode, with explicit guidance on when planning is not worth its overhead.
- → specific-prompt-context: a before/after table showing scoped file+scenario+constraint prompts and pointers to existing code patterns cutting correction rounds.
- → agents-md-hygiene: bloated CLAUDE.md causes Claude to ignore actual instructions; prune with "would removing this cause mistakes?", push occasional knowledge to skills, emphasize at most one line.
- → guardrail-hooks: hooks are deterministic where CLAUDE.md instructions are advisory, so anything that must happen every time belongs in a hook.
- → spec-first: an interview prompt that ends in a written SPEC.md, then a fresh session to implement it; precision in the spec pays more than watching the implementation.
- → course-correct-early: Esc to interrupt, rewind/checkpoints to restore conversation or code, "undo that" — tight feedback loops beat one perfect attempt.
- → fresh-context-reset: after two failed corrections, clear and re-prompt; a clean session with a better prompt beats a long one carrying failed approaches.
- → context-compaction: auto-compaction plus `/compact <focus>`, summarize-from-here checkpoints, and CLAUDE.md instructions on what compaction must preserve.
- → subagents-for-context: research reads many files; subagents run in separate context windows and return summaries, fixing the "infinite exploration" failure.
- → review-agent-diffs: a subagent reviewing the diff in fresh context sees the result, not the reasoning that produced it — but must be told to flag only correctness/requirement gaps or it over-engineers.

## Other-use-case material

- Non-interactive `claude -p` in CI, pre-commit hooks, and pipelines, with JSON/stream-JSON output — builder scope.
- Fan-out across files (loop `claude -p` per file, or `/batch` splitting a change across 5–30 subagents in worktrees) — long-running scope.
- Parallel sessions, worktrees, cross-session messaging, agent view, and experimental agent teams — long-running scope, though the Writer/Reviewer two-session pattern is a cheap interactive variant of review-agent-diffs.
- Auto mode with a classifier reviewing commands for unattended runs — relevant mainly when stepping away from the session.
