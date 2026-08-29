# log

## 2026-08-29 — Phase 4: synthesize → Checkpoint B

- Clustered ~90 candidate slugs into 30 patterns + 6 anti-patterns (5 Opus
  writer subagents; plan preserved in session scratchpad). Over the spec's
  15–25 aim on purpose: distinct, well-evidenced patterns beat forced merges;
  prune candidates welcome at Checkpoint B.
- Status: 31 adopted / 5 candidate (single-source pages stay candidate per the
  ≥2-evidence rule: run-tests-first, hoard-working-code, red-green-tdd,
  jig-for-tuning, over-compressed-context). Durability: 31 structural /
  3 compensation / 2 unknown. Confidence capped at medium everywhere — "high"
  requires own experience (§6), which starts accruing in Phase 5.
- Added category `compounding` (capture-lessons, skill-authoring) to §5.6's
  initial set.
- Lint pass: all 36 pages have id==filename, valid frontmatter, existing
  sources and related links. Generated quickref.md (46 lines, adopted only),
  index.md (task router + categories), bibliography.md (62 rows), skill folder
  (SKILL.md, quickref copy, patterns-list.md).
- STOPPED at Checkpoint B: Jonathan reviews the pattern list and quickref.md
  on the PR before any merge to main. §11 items still open: three dogfood task
  descriptions (item 4) and skill-symlink OK (item 5).

## 2026-08-29 — Phase 3: distill

- 11 Opus subagents wrote 49 source notes in `sources/` (20 Every essays,
  15 Osmani posts, Willison AEP consolidated, Claude Code + Codex docs
  consolidated, agents.md spec, Anthropic ccbp + bea, OpenHands, Tornhill,
  HumanLayer ACE, Karpathy llm-wiki, 3 arXiv items and 2 more).
- arXiv notes are abstract-only and say so; paywalled Every content marked
  in-note; `claude-code-docs`, `codex-docs`, `willison-2026-aep` have no
  direct `_triage.md` rows (their component pages were triaged individually).
- `note-exists?` flipped to yes on 46 triage rows.
- ~90 candidate pattern slugs collected from distiller digests; heavy
  convergence on review-agent-diffs, small-reviewable-steps, spec-first,
  plan-before-code, agents-md-hygiene, skill-authoring, capture-lessons,
  context management, and verification-evidence themes → Phase 4 clustering.

## 2026-08-29 — Phase 2: triage

- 16 Sonnet subagent batches triaged all 234 cached items (148 Every emails,
  86 web items); fragments merged into `sources/_triage.md`.
- Distribution: ~50 high, ~60 medium, ~70 low, ~55 none (mostly Every
  marketing/onboarding sends).
- Selection for Phase 3 (80/20 consolidation, since highs alone exceed the
  spec's ~15–30 estimate): all highs, with the 16 Willison AEP chapters
  distilling into the single `willison-2026-aep` note, Claude Code doc pages
  into `claude-code-docs`, Codex doc pages into `codex-docs` (matching SPEC §10
  bib ids); plus unique-angle mediums `beyondhumanreadable-2026`,
  `osmani-2026-agentic-autonomy-levels`, `every-2026-04-27-most-expensive-model`.
  ≈ 45 source notes via 11 Opus distill subagents.

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
