---
id: every-2026-04-16-youre-manager-now
title: You're the Manager Now
author: Laura Entis
date: 2026-04-16
url: (Gmail export, local mbox)
access: gmail
accessed: 2026-08-29
scope: interactive
relevance: high
pass: distilled
patterns: [confidence-check, prompt-at-higher-abstraction, track-token-spend]
---
## Summary

An Every "Context Window" digest arguing that the developer's job is shifting
from writing code to overseeing agents. It reports Anthropic's redesign of the
Claude Code desktop app (session sidebar, drag-and-drop panes, integrated
terminal and editor) as evidence that a pure CLI is no longer the right primary
surface once agents write the code — what a supervisor needs is parallel-session
management, visible git/task context, and above all a live preview of what is
being built. A second thread, attributed to Dan Shipper, argues that as models
improve you should raise the abstraction level of your prompts: describing a bug
in mechanical detail is a low frame; "there seems to be a problem, can you fix
it?" is a higher one that can surface a deeper architectural issue. The digest
also carries a concrete self-review workflow and a token-usage command.

## Takeaways for our use case

- Before accepting agent output, ask it to self-rate confidence 1–100; below 90,
  send it back with "find improvements and get to 90+" and repeat.
- Stop at 90 rather than chasing 100 — the source frames the last stretch as
  burning tokens for diminishing returns.
- The value of the confidence question is that it makes the agent surface edge
  cases and glossed-over assumptions it would not have volunteered.
- As models get stronger, deliberately loosen the prompt: state the goal or the
  symptom rather than the mechanism, so the agent has room to find a better
  problem than the one you named.
- The tradeoff of the higher frame is that your job becomes deciding which
  problem matters, not explaining how the problem works.
- `npx ccusage@latest monthly` reports Claude Code token usage; the source's
  reference point is ~2.2M tokens/month for non-engineering agentic work, well
  under a Max plan's allowance.
- Keep a running preview of the artifact next to the session; text-only
  supervision (diffs, logs, terminal output) is called out as a poor primary
  interface for agent-written code.

## Candidate patterns / evidence

- → confidence-check: Every's head of growth asks Claude Code "how confident are
  you in this, 1–100?" before any PR, and iterates until it clears 90; credited
  with changing output quality for a non-engineer.
- → prompt-at-higher-abstraction: as capability rises, the mechanical bug
  description is dominated by the vaguer high-frame prompt, which can find the
  same bug plus a larger architectural issue.
- → track-token-spend: a single command (`npx ccusage@latest monthly`) plus a
  published baseline makes budget a checkable number rather than a worry.
- → preview-alongside-session: the argued future coding UI centres on parallel
  work, git/task awareness, and a preview of what you are building.

## Other-use-case material

- The "Tact" OpenClaw plugin — a trained classifier that decides when a Slack
  agent should stay silent — is builder-side multi-agent hygiene, not
  single-session practice. Flag as `scope: builder`.
- The Claude Mythos framing dispute (autonomous vulnerability discovery vs.
  pointing a small model at known-buggy code) is `scope: long-running`
  background, useful only as context for capability claims.
