# log

## 2026-08-29 — MVP build kickoff (Phase 0)

- Started the SPEC §9 build in a Claude Code remote session.
- Branch deviation: session policy mandates `claude/agent-patterns-spec-th583c`
  instead of SPEC's `feature/agent-patterns-mvp`; same role (feature branch off
  `main`, merge only at checkpoints on Jonathan's OK).
- Renamed `agent-patterns-SPEC.md` → `SPEC.md` to match SPEC §4.
- Moved `every.mbox` (committed by Jonathan — that resolves SPEC §11 open item 1,
  option (a)) out of git into `.cache/every.mbox`; SPEC §2 forbids committing
  newsletter bodies. 148 messages.
- §11 items resolved from the environment: default branch is `main` (item 2);
  model hierarchy approximated with subagent `model:` fields since `/model`
  phase-switching isn't available in a remote session (item 3). Items 4 (dogfood
  tasks), 5 (symlink OK), 6 (Osmani Substack) don't block Phases 0–4; raised at
  Checkpoint B.
- Scaffolded per SPEC §4: README, AGENTS.md, CLAUDE.md bridge, index, log,
  inbox, experiments, bibliography (seeded from §10), sources/_triage.md,
  .claude/agents/ subagents, .gitignore for .cache/.
