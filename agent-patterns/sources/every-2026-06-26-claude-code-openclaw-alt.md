---
id: every-2026-06-26-claude-code-openclaw-alt
title: Claude Code Is the OpenClaw Alternative You Already Have
author: Nityesh Agarwal
date: 2026-06-26
url: (Gmail export, local mbox)
access: gmail
accessed: 2026-08-29
scope: mixed
relevance: high
pass: distilled
patterns: [plain-text-memory, one-thread-one-session, portable-skills, prefer-debuggable-simplicity, scope-the-agents-context-deliberately]
---
## Summary

An argument that Claude Code is a harness — the layer deciding what context a
model sees, which tools it has, how it remembers and how it reaches the outside
world — and that it already does what made the viral assistant OpenClaw exciting.
The comparison is the useful part. Claude Code's memory is three plain layers: a
CLAUDE.md file read at startup, a built-in memory that saves and recalls
observations, and (optionally) a local index over logs and documents. Skills are
an Anthropic standard, so a skill written for one tool runs in the other
unchanged. Sessions are per-thread, each starting from baseline instructions plus
CLAUDE.md, with automatic compaction when a thread grows. OpenClaw, by contrast,
keeps one long-lived session that accumulates cost, and spreads memory across
eight bootstrap files, a consolidation process, several search paths and a
storage layer — so when it misremembers, the cause is undiagnosable.

## Takeaways for our use case

- Prefer memory you can open and read: when the agent behaves oddly, the fix is to
  open the CLAUDE.md or memory file and see exactly what it has been told —
  debugging is editing a text file.
- Start a new thread for a new task. One thread is one session, so a fresh thread
  gives a clean context window seeded only with baseline instructions and
  CLAUDE.md; carrying one session all day accumulates tokens and cost for no gain.
- Keep CLAUDE.md small enough to be standing context, not an archive — the source
  puts a working CLAUDE.md at roughly 2,000–5,000 tokens.
- Skills are portable across harnesses with no conversion, so write them as
  reusable assets rather than tool-specific configuration.
- Be deliberate about how much of your filesystem the agent can see: running inside
  one project folder is a choice, and widening it changes what the agent can do —
  and what it can damage.
- Be sceptical of layered memory machinery: the source's diagnosis is that each
  layer exists to patch a weakness in the one beneath it, and every layer adds a
  place where things go wrong without adding a way to tell which one did.
- Claude Code: `--dangerously-skip-permissions` removes the per-action approval
  prompt. The source recommends the default approval behaviour for professional
  work and offers the flag only when you want full autonomy.

## Candidate patterns / evidence

- → plain-text-memory: Claude Code memory is Markdown you can open in any editor,
  which the author contrasts with OpenClaw's half-dozen opaque stores where a
  misremembered fact has no traceable origin.
- → one-thread-one-session: per-thread sessions start clean from baseline plus
  CLAUDE.md and compact automatically; the counter-example is a single endless
  thread that billed ~50,000 tokens for a message saying "hi".
- → portable-skills: skills are an Anthropic standard — a skill written for one
  harness runs in the other as is, no changes needed.
- → prefer-debuggable-simplicity: the stated reason to choose one harness over the
  other is that sophistication that cannot be inspected costs more than it saves.
- → scope-the-agents-context-deliberately: the tool "feels like a coding tool" only
  because people run it in one project folder; context breadth is a deliberate
  choice with real consequences.

## Other-use-case material

- The main worked example, Claudie — a 24/7 AI employee on a Mac Mini running the
  consulting back office from Slack — is a long-running/builder use case
  (`scope: long-running`), including its ~1,100 lines of Python Slack glue, its
  scheduled morning briefings and inbox triage, and its connections to Google
  Workspace, Asana and a CRM.
- Headless mode plus cron as the mechanism for scheduled unattended runs (the
  author notes OpenClaw's "heartbeat" is a cron job underneath): long-running.
- The reported maintenance split for such an agent — roughly 5 percent keeping it
  running, 30 percent managing memory, 65 percent building skills and deciding
  what to automate — is a useful long-running-ops datapoint.
- The observation that the hard part is deciding what to hand off and how, not
  getting the technology running, is a `meta` framing claim.
