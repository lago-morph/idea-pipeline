---
id: claude-code-docs
title: Claude Code documentation — subagents, memory, skills, hooks, common workflows
author: Anthropic
date: n.d. (continuously updated; read 2026-08-29)
url: https://code.claude.com/docs/en/sub-agents (siblings: /memory, /skills, /hooks, /common-workflows)
access: direct
accessed: 2026-08-29
scope: tool
relevance: high
pass: distilled
patterns: [subagents-for-context, claude-md-imports, skill-authoring, guardrail-hooks, cross-tool-portability, agents-md-hygiene]
---
## Summary

Five reference pages covering the four mechanisms a single user has for shaping
one Claude Code session. **Memory**: CLAUDE.md files load at every session start,
concatenated from filesystem root down to the working directory so the closest
file is read last; they are context, not enforced configuration. `@path` imports
expand at launch (max four hops). **Skills**: a `SKILL.md` directory whose body
loads only when invoked, so procedures and long reference material cost nothing
until used. **Subagents**: markdown-plus-frontmatter workers with their own
context window, tool allowlist, model, and permission mode; verbose work happens
in their context and only a summary returns. **Hooks**: shell commands (or HTTP
endpoints, prompts, subagents) fired at named lifecycle events; exit code 2 on a
blocking event is the deterministic enforcement layer that instructions are not.
The common-workflows page adds prompt recipes, plan mode, worktrees, and resume.

## Takeaways for our use case

- Anthropic states plainly that CLAUDE.md is context, not configuration: "no
  guarantee of strict compliance" — anything that must happen at a fixed point
  belongs in a hook, not in an instructions file.
- Target under 200 lines per CLAUDE.md; longer files consume context and measurably
  reduce adherence, and a file over 4 MiB is skipped entirely.
- Instructions should be concrete enough to verify ("use 2-space indentation",
  "run `npm test` before committing") rather than aspirational.
- Contradictory instructions across nested CLAUDE.md files make Claude pick one
  arbitrarily — periodic pruning is part of maintaining the file, not optional.
- `@path` imports organize but do not save context: imported files load at launch
  anyway. Only path-scoped rules (`.claude/rules/*.md` with `paths:` frontmatter)
  and skills actually defer their cost.
- The cross-tool bridge is a one-line `CLAUDE.md` containing `@AGENTS.md`, with any
  Claude-specific lines appended below; a symlink also works but breaks on Windows.
- Decision rule for where a piece of knowledge goes: a fact needed every session →
  CLAUDE.md; a multi-step procedure or long reference → skill; a rule for one part
  of the tree → path-scoped rule; a thing that must happen deterministically → hook.
- Subagents are for isolating high-volume output (test runs, log processing, doc
  fetching) and for enforcing tool restrictions; they are the wrong choice when the
  task needs back-and-forth or shares heavy context with the main thread.
- A non-fork subagent starts fresh: it sees no conversation history, no files already
  read, and no auto memory. It does inherit the CLAUDE.md hierarchy — except the
  built-in Explore and Plan agents, which skip it deliberately for speed.
- A fork (`/subtask`) is the opposite trade: it inherits the whole conversation so
  you needn't re-explain, while its tool calls still stay out of your context.
- Keep subagent `description` fields short — combined descriptions over 15,000 tokens
  trigger a startup warning; detail belongs in the system prompt, which loads lazily.
- Skill body content persists in context across turns once invoked and is not re-read,
  so write standing instructions, not one-time steps; keep `SKILL.md` under 500 lines
  and push reference material into sibling files.
- `disable-model-invocation: true` is the guard for side-effecting skills (deploy,
  commit, send): you don't want the model deciding the code looks ready to ship.
- Hook events worth knowing for a solo session: `PreToolUse` (blocks a call),
  `UserPromptSubmit` (blocks/augments a prompt), `PostToolUse` (feedback after),
  `Stop` (refuses to let the turn end), `SessionStart`, `InstructionsLoaded`
  (debug what actually loaded).
- Exit code 1 does *not* block — it is treated as a non-blocking error and the action
  proceeds. Policy enforcement must use exit 2 or a JSON `permissionDecision`.
- Hooks defined in a project `.claude/settings.json` are committable and so travel
  with the repo; `settings.local.json` stays personal.
- Debugging adherence: `/context` shows which memory files actually loaded, `/memory`
  opens them, `--debug` surfaces frontmatter parse errors that silently skip a file.
- Skill and subagent files with malformed or absent frontmatter are skipped *silently*
  in the session — a real failure mode when hand-authoring.

## Candidate patterns / evidence

- → `subagents-for-context`: Anthropic's stated primary use is isolating work that
  "would flood your main conversation with search results, logs, or file contents
  you won't reference again"; only the summary returns to the main thread.
- → `claude-md-imports`: `@path` syntax expands at launch with a four-hop depth limit,
  resolving relative to the importing file; imports organize but do not reduce context.
- → `agents-md-hygiene`: explicit size target of <200 lines, a "specific enough to
  verify" test for each line, and a warning that conflicting rules across files are
  resolved arbitrarily.
- → `skill-authoring`: `SKILL.md` under 500 lines with supporting files loaded on
  demand; `description` is the trigger surface and gets truncated at 1,536 chars, so
  the key use case goes first.
- → `guardrail-hooks`: hooks "apply regardless of what Claude decides"; the docs route
  every must-happen-at-this-point instruction out of CLAUDE.md and into a hook.
- → `cross-tool-portability`: the documented AGENTS.md interop path is a `CLAUDE.md`
  whose whole content is `@AGENTS.md`, optionally plus Claude-specific lines below.
- → `plan-before-code`: plan mode (`--permission-mode plan`, or Shift+Tab) reads and
  proposes but makes no edits until approved; a dedicated read-only Plan subagent
  gathers the context.
- → `delegate-verbose-output`: the recipe "use a subagent to run the test suite and
  report only the failing tests" is given as the canonical context-saving move.

## Other-use-case material

- **long-running / multi-session**: agent teams, background agents with a monitoring
  view, cross-session messaging, `SendMessage` resume of finished subagents,
  concurrent-subagent limits (default 20) and spawn-depth limits (default 3).
  Out of scope for one human driving one session.
- **builder-side**: the Agent SDK, `--agents` JSON for ephemeral session-scoped
  subagents, plugins/marketplaces as a distribution channel, HTTP and MCP hook
  handlers, `--append-subagent-system-prompt`.
- **org/enterprise**: managed-policy CLAUDE.md, `claudeMd` in managed settings,
  `claudeMdExcludes` for monorepos, `allowManagedHooksOnly`,
  `strictPluginOnlyCustomization`. Flagged only; not our use case.
- **automation**: Routines, desktop scheduled tasks, GitHub Actions, `/loop`, and
  piping `claude -p` into scripts — adjacent to interactive work but a different
  operating mode.
