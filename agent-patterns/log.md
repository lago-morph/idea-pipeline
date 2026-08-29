# log

## 2026-08-29 — Phase 1: acquire

- Split `.cache/every.mbox` → 148 per-message text files in `.cache/every/`.
- Fetched 86 web items into `.cache/web/`: all 16 Willison AEP chapters + index +
  intro; Anthropic ccbp/bea/tools; Claude Code docs (sub-agents, memory, skills,
  hooks, common-workflows); Codex docs (home, agents-md, skills); agents.md;
  Tornhill; OpenHands; Karpathy llm-wiki gist; HumanLayer ACE + 12-factor README;
  Augment Code; 8 arXiv items (abstract pages for P3s, HTML for consensuslayer);
  Ng four agentic patterns (located: deeplearning.ai The Batch); beyond.addy.ie.
- All SPEC §10 URLs verified live, including anthropic-2025-ccbp at its original
  URL. Located at kickoff: codex docs → developers.openai.com/codex; ACE →
  github.com/humanlayer/advanced-context-engineering-for-coding-agents;
  ng-2024-agentic → deeplearning.ai/the-batch/how-agents-can-improve-llm-performance.
- Osmani: enumerated sitemap; 40 posts since 2025-03-01 plausibly about
  AI-assisted/agentic dev, all fetched. Blog is self-hosted and free — Substack
  question (§11 item 6) moot for now.
- Process note (80/20): Phase 2 triage will batch ~10–15 items per Sonnet
  subagent instead of one item per invocation — 234 items would make per-item
  invocations pure overhead. Same output contract per item.

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
