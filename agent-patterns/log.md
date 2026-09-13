# log

## 2026-09-13 — `prefer-deterministic-controls` and `bloated-instruction-surface` paired

- Jonathan: deterministic controls are not free, just a better trade than the
  alternative. Both pages now say so and point at each other — two sides of one
  problem, what to do with a failure you have seen before. A mechanism costs
  design time and binds indiscriminately; prose costs context and binds nothing.
  Prefer the mechanism because the trade is better, not because it is cheap.
- Checkpoint reached: Jonathan gave the OK to merge to `main` (SPEC §8 `release`).

## 2026-09-13 — completed transcript folded in; `review-agent-diffs` deprecated; `capture-lessons` rewritten

- The `2026-06-10-218` transcript is complete (3,426 → 8,914 words) and back in
  scope. Its own redo note supersedes the fidelity caveat the first version
  carried: it was rebuilt from the full session log by a deterministic script,
  with no compaction, so the sections holding Jonathan's own statements are
  verbatim rather than summary. That upgrades the source.
- **Two corrections it forced on the existing note.** The instruction-file refactor
  moved rule text into 47 detail files, not 20; and the full instruction ceiling is
  ~73,000 tokens against the ~15,200 floor already recorded. Both propagated to
  `agents-md-hygiene`.
- **The `capture-lessons` counter-evidence framing was wrong** and is fixed. The
  transcript shows capture was load-bearing — the entire forensic analysis exists
  only because 45 retrospectives and a full run record had been kept. What failed
  was *emitting rules from* the captures. Framed as counter-evidence it read as an
  argument against retrospectives, which this source does not support.
- `capture-lessons` rewritten to Jonathan's model and retitled "Capture lessons as
  history, then mechanise them" (id unchanged per D3): capture generously, treat a
  single retro's recommendations as data rather than a to-do list *unless one is
  already a mechanism*, mine the accumulated record for cross-session threads, and
  convert those into a harness hook, CI check or linter — prose only for what can't
  be mechanised. `confidence: high` (many independent sources plus `[own]`).
- `review-agent-diffs` deprecated on the same reasons and disposition as
  `unreviewed-code`, at Jonathan's instruction. `compensation`, kept for the
  record, removed from `quickref.md` (45 lines) and rerouted out of four rows of
  the index task table. Surviving parts distributed rather than deleted: depth by
  blast radius stays in `tier-review-by-risk`; "the PR description is narration
  too" absorbed into `demand-evidence-not-summary`; the replacement for attention
  is `prefer-deterministic-controls` and `verify-from-clean-state`. Both
  deprecation notes now name where the function went — without that the wiki would
  drop a function without recording its successor.
- Supporting the deprecation, from the transcript: across six merged pull requests
  there is no instance of Jonathan reading a diff, and neither defect that
  surfaced — an agent claiming an artifact it had never produced, and a validator
  pinned to the wrong release — was the kind a diff read would have caught.
- Two new anti-patterns at his direction: `bloated-instruction-surface` (accreted
  AGENTS.md, skills and ADRs — context spent at best, unresolvable contradictions
  at worst) and `no-progressive-disclosure` (reference material that can only be
  loaded whole). Both `candidate`, both `confidence: medium`.
- **Sourcing point worth remembering:** `lagomorph-2026-k8s-forensics` is
  Jonathan's own project, so it and an `[own]` line are the *same* practitioner and
  do not corroborate each other. Those two anti-patterns therefore stay `candidate`
  despite carrying two evidence lines each. `prefer-deterministic-controls` is
  unaffected — `cheapcode-2026` is genuinely independent of him.
- `prefer-deterministic-controls` gained the cost side his position omits: a new
  check usually needs false positives fixed and pre-existing findings triaged
  before it can gate, gates bind indiscriminately, and two hooks obstructed correct
  work — scope an exemption with a removal trigger rather than widening the gate.
- Placeholder page `refactor-skills-into-checks` created at his request, marked
  "direction stated, evidence pending", `confidence: low`, excluded from quickref.
  `inbox.md` carries the reminder to ask him for real-project evidence.
- Also in `inbox.md`: a candidate slug `adversarial-self-review` (evidence parked on
  `cross-model-review` for now), and the ADR nuance — the transcript shows an ADR
  that *was* ratified, implemented and shipped with a contract lint, so "ADR edits
  get ignored" is too broad; the cut that holds is behavioural prose remedy versus
  design decision plus enforcement.

## 2026-09-13 — ingest: `lagomorph-2026-k8s-forensics` (own project, first-hand)

- Jonathan's own `lago-morph/k8s-platform`: `ai/LESSONS.md` plus the whole
  `forensics/` tree, cloned to /tmp (never into git). **Excluded at his
  instruction: `retrospective/2026-06-10-218-transcript.md`, which is incomplete.**
  Three Opus readers mined ~31k words in parallel and returned findings only; the
  source note is composed here, so it stays one coherent note.
- The finding he asked about is confirmed and then some: failure classes wired to
  a fail-closed gate stopped recurring, while 8 of 12 tracked classes recurred
  *after* a prose rule had been written for them; one rule was violated within
  minutes by the agent that wrote it. **`prefer-deterministic-controls` promoted
  `candidate` → `adopted`** on two independent sources (`cheapcode-2026` plus this)
  and **`confidence: high`** — the wiki's first, since SPEC §6 reserves `high` for
  multiple sources *and* own experience, which this now supplies. It enters
  `quickref.md` (46 lines).
- Recorded honestly rather than over-claimed: the source's own analysts tag the
  mechanism-vs-prose comparison as inferred from absence of recurrence, with a
  per-class scan still queued, and they explicitly decline the claim that a shorter
  instructions file gets obeyed more. Both caveats are in the note and the evidence
  lines.
- 12 evidence lines added across existing pages: agents-md-hygiene,
  demand-evidence-not-summary, define-done-first, spec-first, give-a-runnable-check,
  comprehension-debt, intent-ledger, stale-scaffolding, agentic-manual-testing,
  calibrate-autonomy, prefer-deterministic-controls, and capture-lessons.
- New candidate `verify-from-clean-state` (one strong first-hand source →
  `confidence: medium`): evidence must come from the committed artifact in an
  environment nobody hand-patched. Three readers independently proposed this idea
  under three different names; merged into one page rather than three.
- **Open, and the most important thing here: `capture-lessons` now carries
  counter-evidence from this source** — 45 retrospectives, 152 rule candidates,
  ~51 adopted, no measured reduction in the targeted behaviours; the project
  retired rule-writing as its default retrospective output. The page still says
  quality compounds by turning failures into standing instructions. Evidence line
  added; the page's claim is left for Jonathan, since rewriting it changes
  `quickref.md`.
- Lint rule tightened in AGENTS.md and SPEC §8: promotion needs ≥ 2 **independent
  sources**, not ≥ 2 evidence lines. Phase 4 already worked that way (hoard-working-code,
  jig-for-tuning and run-tests-first each hold 2–3 lines from a single source and
  correctly stayed candidate), but the written rule said "lines", which invites
  clearing the bar by splitting one finding in two.
- Long-running, multi-agent and infrastructure material from the source is flagged
  in the note's other-use-case section and kept out of the patterns entirely.

## 2026-09-13 — `unreviewed-code` deprecated (owner's own experience)

- Jonathan rejected the anti-pattern outright: in 2026 very few people review all
  the code an agent writes; that was necessary a year ago and is not now. He chose
  deprecation over re-rating or a cluster rewrite. This is `[own]` experience and
  under SPEC §6 it outranks the page's sources, all of which predate the judgement.
- `patterns/unreviewed-code.md`: `status: deprecated`, `durability: structural` →
  `compensation` (it was working around a model weakness that has eased),
  `verified: 2026-09-13`, and a deprecation note at the top of the body. File kept
  per the status legend; sources and evidence lines left unedited, since they still
  record what those sources said.
- Absorbed the surviving point into `prefer-deterministic-controls`: the failure is
  not "nobody read it" but "nobody read it and nothing checked it" — before shipping
  something you didn't read, name what did check it.
- Removed from `quickref.md` (adopted-only), which is now 45 lines; skill copy
  re-synced. `index.md` and the skill's `patterns-list.md` mark it deprecated.
- SPEC §5.11 and AGENTS.md §2 extended: the patterns-list row label now shows any
  non-adopted status — `(candidate)`, `(deprecated)`, `(absorbed)` — and a page
  that is no longer to be applied keeps its row but says so in place of a trigger,
  so an agent meeting a stale reference learns it from the router.
- Still unresolved and raised with Jonathan: `review-agent-diffs` is `adopted` and
  its quickref line still says to review every diff yourself, which is the same
  claim he rejected. Left untouched — he chose deprecation, not the cluster rewrite.

## 2026-09-13 — orphan slugs resolved; Jonathan rejects the review anti-pattern

- New page `prefer-deterministic-controls` (candidate, confidence low, single
  source `cheapcode-2026`): convert a recurring failure into a type, lint or gate
  rather than another prose rule. Deliberately ONE evidence line despite the
  source supporting two — two lines from one source would trip lint's
  ≥2-evidence promotion rule, same reasoning as `over-compressed-context`.
- `reframe-before-blaming-the-model` folded into `fresh-context-reset` as a Do
  bullet plus an evidence line, rather than getting its own page: it is a
  disposition, not a procedure.
- `agent-legible-code` parked in `inbox.md`, not written — single source, no
  experiment, and repo-design rather than session practice.
- Could not triage the agent-governance mechanism catalogue cited by
  `cheapcode-2026`: davisjam.github.io is live but the cited path 404s. Recorded
  in `inbox.md` rather than invented as a triage row with a guessed relevance.
- **Open and unresolved: Jonathan does not accept `unreviewed-code` as written**
  — "in 2026 very few people review all the code an AI agent writes; that was
  necessary a year ago." Captured in `inbox.md`. This implicates the whole review
  cluster (`unreviewed-code`, `review-agent-diffs`, `tier-review-by-risk`), all
  currently `durability: structural`; if he is right they are `compensation` for
  a model weakness that has eased. No page changed yet — the scope of the
  rewrite is his call, and it moves `quickref.md`, the injectable artifact.
- Word-limit cleanup deferred by Jonathan; the new page was still written to
  the limit rather than adding to the backlog. Skill install path left as is.

## 2026-09-13 — ingest step 4: new evidence lines from the three re-read papers

- Added 12 evidence lines across 10 pattern pages, completing the `ingest`
  workflow's step 4 for the re-ingested sources: `dontvibe-2025` to
  small-reviewable-steps, front-load-context, tier-review-by-risk,
  agentic-manual-testing, plan-before-code and review-agent-diffs;
  `cheapcode-2026` to calibrate-autonomy, give-a-runnable-check,
  front-load-context, agents-md-hygiene and comprehension-debt;
  `beyondhumanreadable-2026` to comprehension-debt, marked "(argument, not
  result)" because it comes from that paper's limitations section.
- Dropped one proposed line: `dontvibe-2025` → stale-scaffolding ("agents did
  more than asked", 8 of 13). It is real in the paper but it is an argument for
  small units and cheap rollback, not for scaffolding going stale; wrong page.
- No status or confidence changes. None of the pages gaining lines is a
  candidate, so the ≥2-evidence promotion rule was not triggered; `high`
  confidence still requires own experience (SPEC §6), which waits on Phase 5.
  `verified:` untouched — adding a source is not a re-judgement against models.
- Checked: every `sources:` id has an evidence line and vice versa on all 36
  pages; no dangling source refs. Side effect worth naming: pages over the ~250
  word body limit went 26 → 27 of 36 (plan-before-code crossed). The limit is
  a pre-existing Phase 4 problem, now slightly worse.
- Source notes' `patterns:` back-links remain broader than the pages that cite
  them (e.g. the `dontvibe-2025` note lists 12 slugs, 8 pages cite it). SPEC
  §5.2 calls these best-effort, so they are left as the distillers wrote them.

## 2026-09-13 — re-ingest abstract-only sources; patterns-list contract + regeneration

- **Data.** The three arXiv items distilled from their abstract pages in Phase 3
  (`dontvibe-2025`, `cheapcode-2026`, `beyondhumanreadable-2026`) were re-fetched
  in full (HTML → text in `.cache/arxiv/`, gitignored) and re-distilled by three
  Opus subagents. No "abstract only" marker remains anywhere in `sources/` or
  `patterns/`. The other degraded notes are the six paywall-truncated Every
  emails; SPEC §2 puts paid content out of scope, so those caveats stand.
- **Corrections the full texts forced.** `cheapcode-2026` was the worst: the
  abstract-only note framed it as "controls can't be derived up front", but the
  paper uses ex-ante controls and calls them necessary-but-not-sufficient, and
  its engineer inspected almost no agent code behind a verification substrate
  2.75x the product's size — "inspectable" there means machine-checkable, not
  human-read. `beyondhumanreadable-2026`'s 17%/67% result turns out to be four
  single sessions on one model with no repeats or statistics, measuring session
  *tokens* and wall-clock, not cost or quality (correctness was 5/5 in every
  condition). `dontvibe-2025` narrowed: implementation control was universal
  (13/13) but design control was 11/13, and three participants working outside
  their expertise did not read the generated code at all.
- Four evidence lines rewritten (`calibrate-autonomy`, `cognitive-surrender`,
  `capture-lessons`, `over-compressed-context`). `over-compressed-context` also
  had its **Use when**, one **Do instead** bullet and **Don't, when not** narrowed
  to what the paper actually measured; `verified: 2026-09-13`. It **stays
  `candidate`** — the full text is more detail on the same single finding, not a
  second independent source, so the ≥2-evidence rule is not met. `confidence: low`
  is right and unchanged.
- **Contract.** `skill/agent-patterns/patterns-list.md` had no format spec beyond
  "(id — title — one line)", so Phase 4 generated it by regex-pulling the first
  *physical* line after `**Use when:**`. Pages are hard-wrapped, so 30 of 36 rows
  were cut mid-sentence and the one page using a heading variant got an empty
  trigger — the skill's router, degraded to bare pattern names. Added SPEC §5.11
  (row format; the trigger says *when you would reach for the page*, is authored
  not extracted, one sentence ≤ ~120 chars ending in a period) and §5.11.1 (read
  generated files back; check for empty fields, truncated rows, and every heading
  variant). Mirrored into AGENTS.md §2 and a new lint step 5.
- All 36 triggers rewritten by hand from the full **Use when:** paragraphs and
  checked mechanically against §5.11.1: 36 rows, ids match the page set and are
  sorted, none empty, none over 120 chars, none merely restating the title, all
  status labels agree with frontmatter.
- Not done here: Phase 5 (dogfood) — still blocked on SPEC §11 items 4 and 5.
  Deliberately left for Jonathan: (a) new candidate slugs surfaced with no page —
  `prefer-deterministic-controls`, `reframe-before-blaming-the-model`,
  `agent-legible-code`; (b) `cheapcode-2026` is a published counter-case to
  `unreviewed-code` and the note frames it as a boundary condition; (c) a new
  triage candidate, davisjam.github.io/agent-governance-mechanisms; (d) 26 of 36
  pattern pages exceed the ~250-word body limit (pre-existing, from Phase 4).

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
