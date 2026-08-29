---
id: agentsmd-spec
title: AGENTS.md — a simple, open format for guiding coding agents
author: Agentic AI Foundation (Linux Foundation); originated with OpenAI Codex, Amp, Jules, Cursor, Factory
date: n.d. (read 2026-08-29)
url: https://agents.md
access: direct
accessed: 2026-08-29
scope: tool
relevance: high
pass: distilled
patterns: [agents-md-hygiene, cross-tool-portability]
---
## Summary

The canonical site for AGENTS.md, framed as "a README for agents": a predictable,
agent-addressed place for the build steps, test commands, and conventions that
would clutter a human README. It is plain Markdown with **no required fields and
no reserved headings** — the agent simply parses whatever text is there. Two
rules carry all the semantics: the AGENTS.md nearest the edited file wins, and an
explicit prompt from the user overrides every file. Nesting is the scaling
answer — a monorepo puts one AGENTS.md per package (OpenAI's own repo is cited as
having 88), each agent reading the closest. Commands listed in the file are
treated as things to actually run: agents will execute the programmatic checks
and fix failures before finishing. The format is stewarded by the Agentic AI
Foundation under the Linux Foundation, claims 60k+ public repos, and lists
roughly two dozen adopting tools including Codex, Cursor, Aider, Gemini CLI,
Copilot, Jules, Zed, and Warp.

## Takeaways for our use case

- The suggested contents are a short, stable list: project overview, build and test
  commands, code style, testing instructions, security considerations — plus commit
  and PR conventions, gotchas, and deployment steps.
- The best one-line editorial test the site offers: "anything you'd tell a new
  teammate belongs here too." That is a usable filter for what to add and what to cut.
- Because there are no required fields, hygiene is entirely self-imposed — nothing in
  the format stops the file from becoming a dumping ground.
- Conflict resolution is worth internalizing: closest file wins, and your chat prompt
  beats the file. So a file rule you keep overriding in chat is a rule to rewrite.
- Listing test/lint commands is not passive documentation — it is a commitment that
  the agent will run them and iterate until green. Only list commands you want run.
- Nesting is the intended answer to a long root file: push package-specific rules
  down into the package rather than growing the root.
- "Treat AGENTS.md as living documentation" — the site expects revision, which is
  consistent with our retro→inbox→lint loop.
- Migration is a rename plus a compatibility symlink
  (`mv AGENT.md AGENTS.md && ln -s AGENTS.md AGENT.md`); the same shape works for
  bridging other tools' filenames.
- Tools that don't read it natively can usually be pointed at it by config rather
  than by duplicating content — the site gives Aider (`read: AGENTS.md` in
  `.aider.conf.yml`) and Gemini CLI (`context.fileName` in `.gemini/settings.json`)
  as worked examples. This is the same move as Claude Code's `@AGENTS.md` import.

## Candidate patterns / evidence

- → `agents-md-hygiene`: the format supplies structure but no constraints — the site's
  own guidance is a contents checklist plus a "new teammate" inclusion test, so
  discipline about size and staleness has to come from the author.
- → `cross-tool-portability`: one AGENTS.md is read natively by roughly two dozen
  agents, and the remainder can be configured or symlinked to it — the strongest
  available argument for writing tool-neutral instructions by default.
- → `pin-instructions-to-scope`: nested per-package AGENTS.md files with
  nearest-file-wins resolution are the documented way to scale instructions in a
  monorepo without inflating the root file.
- → `list-only-commands-you-want-run`: the FAQ confirms agents will execute the
  programmatic checks found in the file and fix failures before finishing.
- → `human-prompt-overrides-file`: explicit chat instructions override everything in
  the file, which makes the file a default rather than a constraint — the same
  "context, not enforced configuration" caveat Anthropic states for CLAUDE.md.

## Other-use-case material

None specific. The site is tool-neutral and single-repository in framing; there is
no long-running-agent or builder-side material beyond the adopters list and the
Linux Foundation governance note.
