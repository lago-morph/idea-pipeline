# agent-patterns

A small, agent-maintained wiki of practitioner patterns for **single-human /
single-agent interactive software development** — one person working in one
Claude Code or Codex session. The primary consumer and updater is an AI agent;
the human is the second reader.

**Two jobs:**

1. **Inject** — [`quickref.md`](quickref.md) (≤ 60 lines, generated) loads into
   any coding session so the agent works the way the best available guidance
   says it should. Packaged as a skill in [`skill/agent-patterns/`](skill/agent-patterns/).
2. **Advise** — given a task description, an agent reads [`index.md`](index.md),
   picks the relevant patterns, and proposes a strategy for that task.

Everything else ([`sources/`](sources/), [`bibliography.md`](bibliography.md),
[`log.md`](log.md), lint) exists only to keep those two jobs accurate.

**How to work here:** read [`AGENTS.md`](AGENTS.md) (the operating manual) and
[`SPEC.md`](SPEC.md) (frozen intent). Patterns live flat in
[`patterns/`](patterns/), one file per pattern, category as a tag.

> **80/20. Usable this week. Good-enough decisions.**
> This is an MVP that is meant to be used, found wrong, and fixed while in use.
> Do not add ceremony. If a rule does not help an AI agent (or Jonathan) get
> better results in a coding session, drop the rule and log that you dropped it.
> The only decisions worth agonizing over are the ones that would be expensive
> to reverse later. Everything else: pick, log, move on.
