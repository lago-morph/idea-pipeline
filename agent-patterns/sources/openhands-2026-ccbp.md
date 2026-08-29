---
id: openhands-2026-ccbp
title: "10 Claude Code Best Practices for Agentic Coding: A 2026 Guide"
author: OpenHands Team
date: 2026-07-02
url: https://www.openhands.dev/blog/claude-code-best-practices-agentic-coding
access: direct
accessed: 2026-08-29
scope: interactive
relevance: high
pass: distilled
patterns: [explore-plan-code, review-plans-not-code, small-reviewable-steps, specific-prompt-context, give-a-runnable-check, agents-md-hygiene, guardrail-hooks, subagents-for-context, context-compaction, fresh-context-reset]
---
## Summary

A ten-item practitioner list for solo Claude Code sessions. The first half is
substantially derivative of Anthropic's own best-practices guide — it cites
that guide directly, and repeats its verification ladder, prompting advice,
CLAUDE.md guidance, and the five named failure patterns nearly one-for-one —
so treat it as corroboration rather than independent evidence. What it adds is
sharper operational detail on a few points: writing the agent's open questions
into a planning.md and iterating until the plan is right; having a fresh model
review the plan on high-stakes changes; asking for one function at a time (or
stubs first, filled in one by one) to stop drift; committing in clean
revertible steps rather than letting the agent auto-commit; starting CLAUDE.md
late and adding entries only as the agent makes mistakes; and using /clear
rather than /compact when context holds a wrong assumption. The back half is a
product pitch.

## Takeaways for our use case

- Review the plan before any code is written; capture the agent's open questions in a planning.md, answer them, and iterate — a good plan usually means implementation lands in one pass.
- On a high-stakes change, have a fresh model review the plan, since it catches wrong turns the original reasoning already baked in.
- Once the plan is approved, ask for one function at a time, or have the agent stub the functions and fill them in one by one, rather than requesting the whole change.
- Stage and commit at logical checkpoints yourself instead of letting the agent auto-commit, so reverting a bad step is one command rather than archaeology; scan the diff for security issues before each commit.
- Put one issue per prompt — a single prompt listing every problem in a block of flawed code does worse than working through them separately.
- Layer verification light to strict: in-prompt check, goal condition re-evaluated each turn, Stop hook blocking the turn, second-opinion subagent that tries to refute the result.
- Add one line telling the agent to fix the root cause rather than suppress the error, to head off bare exceptions and fake fallback data.
- Start the persistent instruction file late — once you know what the agent actually gets wrong — and add entries one at a time as mistakes occur; push domain rules into subdirectories rather than growing the root file.
- Prefer deny-by-default permissions with a tight allowlist plus explicit denies for risky operations such as network calls.
- When the context holds an assumption the model keeps reverting to, /compact is the wrong tool because it preserves the assumption; clear and restart with a sharper prompt.

## Candidate patterns / evidence

- → explore-plan-code: plan mode as read-only exploration first, entered at startup, by Shift+Tab, or /plan; asking for careful reasoning up front on thorny architecture "saves backtracking later".
- → review-plans-not-code: the plan gets reviewed before a line of code, via a planning.md of open questions and, for high-stakes work, a fresh model reviewing the plan.
- → small-reviewable-steps: one function per request or stub-then-fill to prevent drift, plus staging and committing at logical checkpoints so any step is revertible.
- → specific-prompt-context: most failed sessions trace to the prompt, not the model; scope tightly, point at an existing example file, describe bugs by symptom/location/fix, one issue per prompt.
- → give-a-runnable-check: a four-rung verification ladder (in-prompt, goal condition, Stop hook, second-opinion subagent) plus "show the command and its output".
- → agents-md-hygiene: start the file late and add entries one at a time as the agent errs; real rules buried under speculative ones get weighted equally and followed none.
- → guardrail-hooks: deny-by-default permissions with a tight allowlist, and hooks firing pre-tool, post-tool, and on stop, each able to allow, warn, or block by exit code.
- → subagents-for-context: hand heavy research to a subagent that returns a short summary so exploration never touches the main window.
- → context-compaction: /compact with a focus instruction for a long but coherent session, keeping the part of the task you care about and dropping noise.
- → fresh-context-reset: when corrections pile up, dump progress to a file, clear, and restart with a sharper prompt; /compact preserves the bad assumption and so makes it worse.

## Other-use-case material

- The back half is an OpenHands product pitch — Agent Canvas, Agent Control Plane, OpenHands Cloud, Large Codebase SDK, scheduled and event-driven automations, the vulnerability-fixer bot — all builder/long-running scope and not evidence for interactive practice. Sections 8 and 9 in particular pivot mid-section from Claude Code guidance to the product.
- Spotify's background coding agent (deterministic verifiers before a PR opens, then an LLM judge vetoing roughly a quarter of sessions) — long-running scope; the article itself flags it as one company's internal system, not a benchmark.
