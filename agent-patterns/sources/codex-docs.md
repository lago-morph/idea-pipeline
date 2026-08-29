---
id: codex-docs
title: OpenAI Codex documentation — AGENTS.md, skills, product overview
author: OpenAI
date: n.d. (continuously updated; read 2026-08-29)
url: https://developers.openai.com/codex/ (pages: /codex/guides/agents-md, /codex/skills)
access: direct
accessed: 2026-08-29
scope: tool
relevance: high
pass: distilled
patterns: [agents-md-hygiene, cross-tool-portability, skill-authoring]
---
## Summary

Codex's two mechanisms for persistent, reusable instruction. **AGENTS.md**: Codex
rebuilds an instruction chain on every run (once per TUI session, no cache). It
reads the global scope first — `~/.codex/AGENTS.override.md` if present, else
`~/.codex/AGENTS.md`, first non-empty file only — then walks from the git root
down to the working directory, taking at most one file per directory, preferring
`AGENTS.override.md`, then `AGENTS.md`, then any name listed in
`project_doc_fallback_filenames`. Files are concatenated root-first, so the file
nearest your working directory lands last and wins. Empty files are skipped and
the chain stops at `project_doc_max_bytes` (32 KiB default), silently truncating
anything past it. **Skills**: a directory with `SKILL.md` requiring `name` and
`description`, built on the same open agent-skills standard Claude Code follows,
loaded by progressive disclosure — name and description first, full body only on
selection. The product-overview page is a link hub with little durable content.

## Takeaways for our use case

- Codex's override mechanism has no Claude Code equivalent: an `AGENTS.override.md`
  *suppresses* the sibling `AGENTS.md` in the same directory rather than adding to
  it. Useful for a temporary personal override; a hazard when you forget it exists
  (the docs list "look for an AGENTS.override.md higher in the tree" as the first
  troubleshooting step for wrong guidance).
- Precedence in both tools is "closest file wins by being read last", so a single
  AGENTS.md written for Codex behaves the way a CLAUDE.md would — this is what makes
  the one-file-two-tools bridge safe.
- The 32 KiB combined cap is a real constraint: past it, guidance is dropped without
  an error. Either raise `project_doc_max_bytes` or split across nested directories.
- `project_doc_fallback_filenames` lets an existing house file (`TEAM_GUIDE.md`) be
  treated as instructions without a rename — a migration path, not a place to live.
- Codex rebuilds the chain per run, so editing AGENTS.md mid-session means restarting
  Codex in the target directory; there is nothing to invalidate.
- To audit what actually loaded, ask Codex directly ("List the instruction sources
  you loaded") or enable a plaintext TUI log with `-c log_dir=./.codex-log`.
- Codex skills live in `.agents/skills` — repo, parent dirs up to the repo root,
  `$HOME/.agents/skills`, `/etc/codex/skills` — *not* `.claude/skills`. Same
  `SKILL.md` file format, different discovery path, so a shared skill needs either
  a symlink (supported, followed on both sides) or duplication.
- Same-named skills are not merged in Codex; both appear in the selector. Claude Code
  instead resolves by level. Unique names across the tree avoid the difference.
- The skills listing budget is ~2% of context (or 8,000 chars when unknown), and Codex
  shortens descriptions first, then omits skills entirely with a warning — the same
  pressure Claude Code documents, so front-loading trigger words in `description`
  pays off in both tools.
- `allow_implicit_invocation: false` in `agents/openai.yaml` is Codex's counterpart to
  Claude Code's `disable-model-invocation: true`: keep side-effecting skills manual.
- OpenAI's own skill-authoring advice is short and matches ours: one job per skill,
  instructions over scripts unless determinism is needed, imperative steps with
  explicit inputs and outputs, test the description for trigger behavior.

## Candidate patterns / evidence

- → `agents-md-hygiene`: documented discovery/merge order (global, then root-down,
  one file per directory, closest-last) plus a hard 32 KiB truncation limit that
  silently drops overflow.
- → `cross-tool-portability`: Codex reads AGENTS.md natively and Claude Code reaches
  the same file via a `@AGENTS.md` import, so one file serves both; the divergences
  to watch are the override file, the byte cap, and the skills directory path.
- → `skill-authoring`: both tools implement the same agentskills.io `SKILL.md` format
  and both do progressive disclosure with a capped description listing, so a skill
  written to the standard's minimal frontmatter is portable as-is.
- → `pin-instructions-to-scope`: "place overrides as close to specialized work as
  possible" — a nested `services/payments/AGENTS.override.md` swaps `npm test` for
  `make test-payments` without touching the root file.
- → `verify-what-loaded`: Codex's suggested check is to ask the agent to list its
  active instruction sources before trusting that a file took effect.

## Other-use-case material

- **builder-side**: plugins as the distribution channel for skills and connectors
  across ChatGPT and Codex; bundled MCP configuration; `agents/openai.yaml` display
  metadata; Record & Replay for drafting a skill from a demonstrated workflow.
- **long-running / cloud**: Codex cloud, GitLab support, scheduled tasks that fire on
  Gmail/Slack/GitHub events, GitHub code review with `## Code Review Rules` sections
  in the nearest AGENTS.md. Flagged, not adopted.
- The product-overview page (`codex-docs-home`) triaged low: marketing surface tour
  and a changelog feed, no durable practitioner content beyond the links above.
