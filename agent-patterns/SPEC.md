# agent-patterns — MVP spec

Status: v0 draft, 2026-08-29. Written in claude.ai chat; execution happens in Claude Code.
Location: `idea-pipeline/agent-patterns/` — this file lives at `agent-patterns/SPEC.md`.

> \*\*80/20. Usable this week. Good-enough decisions.\*\*
> This is an MVP that is meant to be used, found wrong, and fixed while in use.
> Do not add ceremony. If a rule in this spec does not help an AI agent (or Jonathan)
> get better results in a coding session, drop the rule and log that you dropped it.
> The only decisions worth agonizing over are the ones that would be expensive to
> reverse later (listed in §3). Everything else: pick, log, move on.

\---

## 1\. What this is

A small, agent-maintained wiki of **practitioner patterns for single-human /
single-agent interactive software development** — Jonathan working in one
Claude Code session (personal projects) or one Codex session (work). The
primary *consumer* and *updater* is an AI agent; Jonathan is the second reader.

Two jobs:

1. **Inject** — a one-page `quickref.md` (and a SKILL.md wrapper) that can be
loaded into any coding session so the agent works the way the best available
guidance says it should.
2. **Advise** — an agent, given a task description, reads `index.md`, picks the
relevant patterns, and proposes a strategy for *that* task.

Everything else (sources, bibliography, log, lint) exists only to keep those two
jobs accurate as Jonathan's experience grows and as models change.

Not in scope: building agent systems, long-running autonomous agents, agent
frameworks, org-level governance. Lessons from those worlds may be *linked* but
must be flagged as a different use case (see §6).

Inspiration, not requirement: Karpathy's LLM-wiki pattern (raw sources → a wiki the
agent rewrites → an index; operations ingest / query / lint). GoF/Alexander pattern
*form* is used only where it helps an agent apply the pattern; no forces essays.

\---

## 2\. Hard constraints (do not violate)

* **Everything lives under `agent-patterns/`.** No files, configs, or side effects
anywhere else in the repo. It may be moved later; use relative links only, no
absolute paths inside content.
* **Branching:** work on `feature/agent-patterns-mvp` off the default branch
(`main` — confirm). Merge to `main` at the checkpoints in §9, after Jonathan says go.
* **Sources are stored as summaries + links only.** Never commit article text,
newsletter bodies, or exports. Raw material goes in `agent-patterns/.cache/`
(gitignored) for multi-pass work.
* **Access rules for material:**

  * Use only what you can fetch directly.
  * Free-with-signup → add to `bibliography.md` with `access: signup`, note it in
`log.md`, move on. Jonathan will batch these.
  * Paid → out of scope. If it is in training knowledge, only broad, certain strokes;
mark `confidence: low` and `access: paid`. When unsure, leave it out.
* **No hallucinated evidence.** Every `Evidence` line in a pattern points at a
source note that exists in `sources/` (or to `\[own]` experience with a date).
Paraphrase; at most one short attributed phrase per source; no pasted passages.
* **Cross-tool by default.** Claude Code and Codex converge on each other; write
patterns tool-neutral, and put tool-specific mechanics in a clearly marked line
(`Claude Code:` / `Codex:`). `tools: both` unless there is a concrete reason.

\---

## 3\. Decisions (made — reversible unless marked)

|#|Decision|Why|Reversible?|
|-|-|-|-|
|D1|Plain Markdown + YAML frontmatter. No database, no site generator, no build step.|Agents read Markdown natively; Git is the sync.|Yes|
|D2|**Flat `patterns/` directory; category is a frontmatter tag, not a folder.**|Categories will change; moving files breaks links.|**Hard to reverse — keep flat.**|
|D3|**Stable slugs as IDs (pattern ids, bibliography ids). Never reuse a slug. Rename = new file + `aliases:` entry in the old one.**|Links and `Evidence` lines depend on ids.|**Hard to reverse — do it from day one.**|
|D4|Pattern body ≤ \~250 words, fixed section headings (§5.1).|An agent will read 5–8 of these per task.|Yes|
|D5|`quickref.md` is **generated** from adopted patterns by `lint`. Edit patterns, not the quickref.|Single source of truth.|Yes|
|D6|Injection = a skill folder (`skill/agent-patterns/`) that both Claude Code and Codex can load, plus optional `@`-import / path pointer (§7).|Both tools use the same SKILL.md layout as of Aug 2026.|Yes|
|D7|Model hierarchy for the build: Sonnet-class subagents for triage, Opus-class subagents for distillation, Opus main session for execution, Fable for planning and checkpoint reviews.|Jonathan's direction; keeps orchestrator context small.|Yes|
|D8|**No beads for the MVP build.** Track build tasks in `log.md` + the tool's own task list.|`.beads/` would land outside the subdirectory or need config; one linear pass doesn't need it. Revisit when Jonathan adopts beads.|Yes|
|D9|Source notes only for items with relevance ≥ medium. Everything triaged gets one row in `sources/\_triage.md`.|\~200 Every emails; most won't earn a file.|Yes|
|D10|Durability rating on every pattern: `structural` / `compensation` / `unknown` (§6).|Compensation patterns die when models improve; must be findable and re-checkable.|Yes|
|D11|Every pattern carries `verified: <date>` and the set of model families it was last judged against.|Enables cheap staleness checks at each model release.|Yes|
|D12|Experiments on structure/process are allowed without asking, provided they are logged in `experiments.md` with a success criterion and a revisit date.|Malleability is the point.|Yes|

> 80/20: if a future decision isn't in this table and isn't obviously irreversible,
> just make it and write one line in `log.md`.

\---

## 4\. Directory layout

```
agent-patterns/
├── SPEC.md                  # this file; frozen intent; change sparingly, log changes
├── README.md                # one screen: what/why/how; the 80/20 charter
├── AGENTS.md                # agent operating manual: schema + workflows (cross-tool)
├── CLAUDE.md                # first line only: @AGENTS.md   (Claude Code bridge)
├── index.md                 # router: by task → patterns; by category; legend
├── quickref.md              # GENERATED ≤ \~60 lines; the injectable checklist
├── bibliography.md          # id → title/author/date/url/access/status (table)
├── log.md                   # append-only, dated: decisions, ingests, lints, experiments
├── inbox.md                 # quick capture from real sessions; consumed by lint
├── experiments.md           # active / closed experiments on structure \& process
├── patterns/<slug>.md       # one file per pattern or anti-pattern
├── sources/<bib-id>.md      # one note per source with relevance ≥ medium
├── sources/\_triage.md       # one row per triaged item (all of them)
├── skill/agent-patterns/    # SKILL.md + synced copies of quickref.md and a patterns list
├── .claude/agents/          # build/maintenance subagents (Claude Code only)
│   ├── source-triage.md     # model: sonnet
│   └── source-distill.md    # model: opus
├── .gitignore               # .cache/
└── .cache/                  # gitignored raw material
```

Run Claude Code with `agent-patterns/` as the working directory during the build so
its `.claude/` and `CLAUDE.md` are the project scope (verify with `/agents`).

\---

## 5\. File formats

### 5.1 Pattern page — `patterns/<slug>.md`

```markdown
---
id: plan-before-code            # == filename slug; never changes
title: Plan before code
type: pattern                   # pattern | anti-pattern
status: adopted                 # candidate | adopted | deprecated | absorbed
durability: structural          # structural | compensation | unknown
scope: interactive              # interactive | long-running | both
tools: both                     # both | claude-code | codex
category: planning              # see §5.6 (tag, not folder)
verified: 2026-09-01            # last judged against current models
models: \[claude-5, gpt-5.6]     # families it was judged against
confidence: medium              # high | medium | low
sources: \[openhands-2026-ccbp, willison-2026-aep]
related: \[small-reviewable-steps, checkpoint-commits]
aliases: \[]                     # old ids, if renamed
---
# Plan before code

\*\*Use when:\*\* the task touches more than one file, or you can't state the acceptance
test in one sentence.

\*\*Do:\*\*
- Have the agent explore read-only and write a short plan (bullets, not prose) before
  any edit. Claude Code: plan mode. Codex: ask for a plan and a stop.
- Put open questions in the plan; answer them; iterate until the plan is boring.
- For high-stakes changes, have a fresh session or model review the plan.
- Only then switch to editing.

\*\*Why:\*\* editing is cheap now; wrong direction is the expensive part. A plan is the
cheapest checkpoint and the easiest thing to review on a phone.

\*\*Don't / when not:\*\* trivial single-file changes; exploratory spikes you intend to
throw away.

\*\*Evidence:\*\*
- \[openhands-2026-ccbp] plan mode, iterating a planning file, fresh-model plan review.
- \[willison-2026-aep] (chapter list) — TO CONFIRM after distillation.
- \[own] 2026-09-xx: …

\*\*Tool notes:\*\* Claude Code: `--permission-mode plan`, Shift+Tab. Codex: — (to verify).
```

Rules: keep the six headings in that order; drop a heading rather than pad it;
≤ \~250 words below the frontmatter; imperatives in **Do**; one line per evidence item.
The example above is *illustrative* — its evidence lines must be regenerated from
real source notes.

### 5.2 Source note — `sources/<bib-id>.md`

```markdown
---
id: willison-2026-aep
title: Agentic Engineering Patterns
author: Simon Willison
date: 2026-02-23 (ongoing)
url: https://simonwillison.net/guides/agentic-engineering-patterns/
access: direct                  # direct | signup | paid | gmail
accessed: 2026-09-01
scope: interactive              # interactive | long-running | builder | mixed
relevance: high                 # high | medium | low | none
pass: distilled                 # triage | distilled
patterns: \[red-green-tdd, ...]  # best-effort back-links
---
## Summary            (≤ 150 words, own words)
## Takeaways for our use case   (bullets, each one usable sentence)
## Candidate patterns / evidence   (bullets: "→ <slug>: <one line>")
## Other-use-case material     (long-running / builder-side items worth linking, flagged)
```

Bibliography ids: `<author-or-org>-<yyyy>-<short>`; Every newsletters:
`every-<yyyy-mm-dd>-<slug>`. Lowercase, hyphens, no spaces.

### 5.3 `sources/\_triage.md`

One table, one row per item seen:
`id | date | title/author | relevance | scope | note-exists? | one-line takeaway`.
This is the only file the orchestrator reads to choose what to distill.

### 5.4 `bibliography.md`

Table generated/maintained by `lint` from source-note frontmatter plus items that have
no note (signup/paid/none): `id | title | author | date | url | access | relevance | note`.

### 5.5 `index.md`

1. *How to use this (agent)* — 5 lines.
2. *By task* — table: task shape → pattern ids (e.g. "new feature in unfamiliar
codebase", "bug fix with repro", "refactor", "spike/prototype", "dependency
upgrade", "review someone else's diff").
3. *By category* — lists of `id — one line`.
4. *Status legend* and *recently changed* (from `log.md`).

### 5.6 Initial categories (expected to change; tag only)

`session-setup` · `planning` · `execution-loop` · `review-quality` ·
`version-control` · `delegation` (subagents, parallelism, model choice inside an
interactive session) · `debugging-recovery` · `anti-pattern`.

### 5.7 `quickref.md` (generated)

≤ \~60 lines. Adopted patterns only, grouped **before starting / while working /
before finishing**, one line each ending with the pattern id in brackets so an agent
can drill down. Header line states the generation date and the model families it was
verified against.

### 5.8 `log.md`, `inbox.md`, `experiments.md`

* `log.md`: `## 2026-09-01 — <what>` entries, newest first; 1–5 lines each.
* `inbox.md`: raw bullets captured at session end: `- 2026-09-01 \[project] lesson…`.
Lint empties it into patterns (new candidate, new evidence line, or discard) and
logs what it did.
* `experiments.md`: `### <name> — status` with hypothesis, change made, success
criterion, revisit date, outcome.

### 5.9 `AGENTS.md` outline

1. Charter (the 80/20 box from the top of this file, verbatim).
2. Schema summary (link to §5 here; keep AGENTS.md self-sufficient anyway — 30 lines).
3. Workflows (§8), each as a numbered procedure an agent can follow cold.
4. Guardrails (§2, short form).
5. Permission to experiment (D12) and the cadence for lint.
6. Tool notes: Claude Code (`@AGENTS.md` bridge, subagents in `.claude/agents/`,
skills path) and Codex (`AGENTS.md` native, skills path, custom agents are TOML
under `.codex/agents/` — do not maintain those for the MVP).

### 5.10 `skill/agent-patterns/SKILL.md`

```markdown
---
name: agent-patterns
description: Practitioner patterns for interactive coding sessions. Use at the start of any non-trivial task, when choosing a strategy, and at session end to capture lessons.
---
1. Read `quickref.md` (in this folder) before starting a non-trivial task.
2. For a strategy question, read `patterns-list.md` here, then open the relevant
   pattern files in the full wiki at <path configured at install> if available.
3. At session end, append 1–3 one-line lessons to the wiki's `inbox.md`
   (or tell the user what to add if the wiki isn't reachable).
```

`lint` copies `quickref.md` and a generated `patterns-list.md` (id — title — one line)
into this folder so the skill is self-contained when symlinked into
`\~/.claude/skills/` and `\~/.codex/skills/`.

\---

## 6\. Relevance and durability (Aug 2026)

> 80/20: rate, don't research. A rating with a one-line reason beats an essay.

**Model families to judge against (verify at kickoff; third-party sources):**
Anthropic — Claude Fable 5, Opus 5, Sonnet 5. OpenAI — GPT-5.6 Sol (Codex default
since July 2026) and variants; GPT-5.4 still available. Record the families actually
checked in `models:`.

**Durability test.** Ask: *if the model got twice as good at X, would this still
matter?*

* `structural` — comes from the shape of the work: delegation, verification,
irreversibility, human attention as the scarce resource, context as a budget, git
as memory, tests as specification.
* `compensation` — works around a current model weakness (forgetting instructions,
weak self-verification, mid-context degradation, overconfidence). Keep it, mark it,
re-check at each major model release.
* `unknown` — say so.

**Confidence.** high = multiple independent sources *and* own experience; medium =
multiple sources or one strong source; low = single weak source, or training-only
knowledge.

**Other-use-case flag.** Anything about long-running agents, agent frameworks,
multi-agent systems, or building agent products gets `scope: long-running` or
`scope: builder` and a first-line note in the page: *"Primarily applies to
<other use case>; kept because <reason>."* It never appears in `quickref.md`.

**Absorbed.** When a pattern becomes unnecessary because the tools/models now do it
(e.g. automatic context compaction), set `status: absorbed`, keep the file, note when
and why.

\---

## 7\. Injection into real sessions

Primary: the skill folder (D6). Symlink `agent-patterns/skill/agent-patterns` into
`\~/.claude/skills/` and `\~/.codex/skills/` (Codex path to verify at kickoff).

Secondary (Claude Code only): add `@<abs path>/agent-patterns/quickref.md` to
`\~/.claude/CLAUDE.md`. Codex has no import; a line in `\~/.codex/AGENTS.md` telling it
to read the quickref path is the equivalent.

Fallback: paste `quickref.md` into a project's `AGENTS.md`.

Reality check: the injected artifact must stay short. If `quickref.md` grows past a
screen, lint should trim it, not the user.

\---

## 8\. Workflows (procedures for the maintaining agent — put in `AGENTS.md`)

> 80/20: each of these should take an agent minutes, not an hour. If one doesn't,
> simplify the workflow, not the data.

**advise** (query): read `index.md`; pick 3–7 patterns by task shape; read only those
files; return a ≤ 15-line strategy with pattern ids; if the task reveals a gap, add a
line to `inbox.md`.

**ingest** (new source): fetch → `.cache/`; triage (Sonnet subagent, §9 template); if
relevance ≥ medium, distill (Opus subagent) into `sources/<id>.md`; add/extend
patterns (`status: candidate` for new ones; new `Evidence` line for existing); append
row to `\_triage.md`; log.

**retro** (end of a real session): append 1–3 lessons to `inbox.md`. No structure, no
polish. This is the only workflow Jonathan is expected to trigger by habit.

**lint** (cadence: after every ingest batch; otherwise monthly or at any major model
release): empty `inbox.md` into patterns; merge duplicates; promote candidates with ≥ 2
evidence lines to `adopted` (ask if unsure); flag pages whose `verified` is older than
the latest model release; re-rate durability where a model change plausibly matters;
regenerate `quickref.md`, `bibliography.md`, `skill/…/patterns-list.md`, and the
"recently changed" block in `index.md`; log a 3–5 line summary.

**experiment**: propose a change to structure/process; write it in `experiments.md`
with hypothesis, success criterion, revisit date; do it; on revisit, keep or revert
and record the outcome. Allowed without asking; log it.

**release**: merge feature branch to `main` at a checkpoint after Jonathan's OK.

\---

## 9\. Execution plan for Claude Code

> 80/20: the goal of the first working session is a usable `quickref.md`, not a
> complete wiki. Coverage comes later, incrementally, via `ingest`.

### Roles and subagents

* **Main session**: Opus 5 for execution. Switch to Fable 5 (if selectable via
`/model`) for phase planning and checkpoint reviews; otherwise stay on Opus.
* **`.claude/agents/source-triage.md`** — `model: sonnet`, read-only tools plus
Write restricted to `sources/\_triage.md` and `.cache/`. Input: one cached item.
Output (≤ 200 words, fixed template): `id | relevance | scope | takeaways (≤ 5) | other-use-case flag | why`. Appends its row to `\_triage.md`; returns only the row to
the orchestrator.
* **`.claude/agents/source-distill.md`** — `model: opus`. Input: one item with
relevance ≥ medium. Output: writes `sources/<id>.md` (§5.2) and returns a ≤ 10-line
digest: candidate pattern slugs + one-line evidence each.
* Fan out triage in parallel batches (5–10 at a time; background subagents). The
orchestrator reads `\_triage.md`, never the raw material.

### Phases

**Phase 0 — scaffold (≤ 30 min).** Branch; directories; `.gitignore` (`.cache/`);
`README.md`, `AGENTS.md`, `CLAUDE.md` (`@AGENTS.md`), empty `index.md`, `log.md`,
`inbox.md`, `experiments.md`, `bibliography.md` seeded from §10; the two subagent
files; commit. Log the start.

**Phase 1 — acquire.** Verify every §10 URL; fetch what is direct into `.cache/`
(scripts, batched; convert HTML → text/markdown locally; never into git). Osmani:
enumerate posts since 2025-03-01 from the site feed/sitemap, keep only titles that
plausibly concern AI-assisted or agentic development. Every: depends on the access
path Jonathan chooses (§11); if an mbox lands in `.cache/`, split it with Python's
`mailbox` module into one text file per message. Write the `\_triage.md` skeleton.
Commit (notes only — check `git status` shows nothing from `.cache/`).

**Phase 2 — triage.** Sonnet subagents over everything in `.cache/`. Willison
chapters are all "examine" by direction — triage them anyway for consistency, then
distill all of them.

**Phase 3 — select + distill.** Orchestrator picks \~15–30 items: all `high`, plus
`medium` items with an angle nothing else covers. Opus subagents distill. Everything
else stays as a triage row.

**Phase 4 — synthesize (Opus; Fable to review).** Cluster candidate patterns → aim for
15–25 patterns + 5–10 anti-patterns. Write pages, rate durability/confidence/tools,
build `index.md`, generate `quickref.md`, `bibliography.md`, the skill folder. Commit.
**Checkpoint B — Jonathan reviews the pattern list and `quickref.md`.** Merge to
`main` on OK.

**Phase 5 — dogfood.** Run `advise` on three real task descriptions from Jonathan
(§11); fix what's wrong; open the first experiment; symlink the skill; log.
**Checkpoint C.** Merge.

**Checkpoint A** (optional, after Phase 0/1): Jonathan glances at the scaffold and the
source list; don't block on it.

### What "done" means for the MVP

`quickref.md` exists, is ≤ 60 lines, every line traces to a pattern page, every pattern
page traces to ≥ 1 source note, and the skill loads in Claude Code and Codex. Nothing
else is required for v0.

\---

## 10\. Seed bibliography (priority and access as of 2026-08-29)

P1 = distill for MVP; P2 = triage, distill if high; P3 = triage only / link.
Access: direct / signup / paid / gmail. Verify every URL at kickoff; mark dead ones.

|id|what|url|access|P|scope|
|-|-|-|-|-|-|
|willison-2026-aep|Simon Willison, *Agentic Engineering Patterns* guide (all chapters)|https://simonwillison.net/guides/agentic-engineering-patterns/|direct|P1|interactive|
|willison-2026-aep-intro|Launch post (framing: agentic engineering vs vibe coding; GoF-inspired format)|https://simonwillison.net/2026/Feb/23/agentic-engineering-patterns/|direct|P1|interactive|
|anthropic-2025-ccbp|Anthropic, Claude Code best practices (agentic coding)|https://www.anthropic.com/engineering/claude-code-best-practices — verify; may have moved under code.claude.com docs|direct|P1|interactive|
|claude-code-docs|Claude Code docs: sub-agents, memory/CLAUDE.md, skills, hooks|https://code.claude.com/docs/en/sub-agents (+ sibling pages via docs map https://docs.anthropic.com/en/docs/claude-code/claude\_code\_docs\_map.md)|direct|P1|tool|
|codex-docs|OpenAI Codex docs: AGENTS.md, skills, models|locate at kickoff (developers.openai.com/codex or learn.chatgpt.com)|direct|P1|tool|
|agentsmd-spec|AGENTS.md format (Agentic AI Foundation); Claude Code bridge is `@AGENTS.md`|https://agents.md — verify|direct|P2|tool|
|every-gmail|Every (every.to) newsletters — \~200 threads in Gmail; Jonathan's main influence|via Gmail (§11)|gmail|P1|mixed|
|osmani-blog|Addy Osmani blog posts since 2025-03-01, AI/agentic-dev only|https://addyosmani.com/blog/ (feed/sitemap; Substack if free, else flag)|direct|P2|interactive|
|osmani-2025-bvc-site|Companion site to *Beyond Vibe Coding* (book itself is paid — out of scope)|https://beyond.addy.ie/|direct|P2|interactive|
|tornhill-2026-codescene|Adam Tornhill, "Agentic AI Coding: Best Practice Patterns for Speed with Quality" (vendor-tinged)|https://codescene.com/blog/agentic-ai-coding-best-practice-patterns-for-speed-with-quality|direct|P2|interactive|
|horthy-2025-acefca|HumanLayer, Advanced Context Engineering for Coding Agents (research → plan → implement; context budget)|locate at kickoff (GitHub, humanlayer)|direct|P2|interactive|
|openhands-2026-ccbp|OpenHands, "10 Claude Code best practices" (secondary; derivative of Anthropic guide)|https://www.openhands.dev/blog/claude-code-best-practices-agentic-coding|direct|P3|interactive|
|dontvibe-2025|"Professional Software Developers Don't Vibe, They Control" — empirical study of agent use; notes no rigorous best practices exist|https://arxiv.org/pdf/2512.14012|direct|P2|interactive|
|beyondhumanreadable-2026|"Beyond Human-Readable: Rethinking SE Conventions for the Agentic Development Era"|https://arxiv.org/pdf/2604.07502|direct|P3|interactive|
|cheapcode-2026|"Cheap Code, Costly Judgment" — governable agentic SE case study|https://arxiv.org/pdf/2607.01087|direct|P3|mixed|
|karpathy-2026-llmwiki|Karpathy, llm-wiki gist (structural model for this repo)|https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f|direct|P1|meta|
|anthropic-2024-bea|Anthropic, "Building effective agents" — builder-side; mine only: start simple, orchestrator-workers, evaluator-optimizer as a review loop, tool/ACI design|https://www.anthropic.com/engineering/building-effective-agents|direct|P2|builder|
|anthropic-2025-tools|Anthropic, "Writing effective tools for AI agents"|https://www.anthropic.com/engineering/writing-tools-for-agents|direct|P3|builder|
|anthropic-ebook-bea|Anthropic eBook, Building Effective AI Agents|https://resources.anthropic.com/building-effective-ai-agents|**signup**|flag|builder|
|horthy-2025-12fa|12-Factor Agents (repo last pushed Sept 2025)|https://github.com/humanlayer/12-factor-agents|direct|P3|builder|
|white-2023-ppc|White et al., prompt pattern catalog (PLoP 2023; GoF form; chat-era)|https://arxiv.org/abs/2302.11382|direct|P3|historical|
|liu-2024-catalogue|Liu et al. (CSIRO), agent design pattern catalogue|https://arxiv.org/abs/2405.10467|direct|P3|builder|
|augmentcode-2026|Augment Code, 26-pattern catalog with anti-patterns (vendor)|https://www.augmentcode.com/guides/agentic-design-patterns|direct|P3|builder|
|ng-2024-agentic|Andrew Ng, four agentic patterns (The Batch)|locate at kickoff (deeplearning.ai)|direct|P3|builder|
|consensuslayer-2026|"Scaling Human-AI Coding Collaboration Requires a Governable Consensus Layer"|https://arxiv.org/html/2604.17883v1|direct|P3|governance|
|agentic-communities-2026|"Architecting Agentic Communities using Design Patterns"|https://arxiv.org/abs/2601.03624|direct|P3|governance|
|zou-2025-hac-survey|ACL 2026 survey, LLM-based human-agent collaboration systems|https://arxiv.org/abs/2505.00753|direct|P3|research|
|gulli-2025-adp|Gulli, *Agentic Design Patterns* (Springer, 21 patterns)|https://link.springer.com/book/10.1007/978-3-032-01402-3|**paid**|skip|builder|

Not listed on purpose: framework docs (LangGraph, CrewAI, ADK), "N patterns for 2026"
listicles. Add later via `ingest` only if a real session shows a gap.

\---

## 11\. Open items — Jonathan decides before/at kickoff

1. **Every access path.** Options: (a) Gmail label `every` on `from:every.to`, Google
Takeout export of that label as mbox → drop into `agent-patterns/.cache/every.mbox`
(recommended; no MCP needed, fully local); (b) Gmail MCP configured in Claude Code;
(c) defer Every to v0.1 and ship v0 from web sources. Choose one.
2. **Default branch name** (`main`?) and confirmation that the build runs with
`agent-patterns/` as the working directory.
3. **Fable 5 in Claude Code** — is it selectable via `/model`? If not, Opus does the
planning/review too.
4. **Three real task descriptions** for the Phase 5 dogfood (one personal/Claude Code,
one work-shaped/Codex, one bug-fix).
5. **Skill install**: OK to symlink the skill folder into `\~/.claude/skills/` and
`\~/.codex/skills/`? (Later: distribute via the skill-registry-manager.)
6. **Osmani Substack**: include if free to read; flag as `signup` otherwise.

\---

## 12\. Kickoff prompt (paste into Claude Code, cwd = `agent-patterns/`)

```
You are building the agent-patterns MVP described in SPEC.md. Read SPEC.md completely
before doing anything.

Working principles, in priority order:
1. 80/20. Usable quickly. Good-enough decisions, logged in log.md. The first session's
   goal is a usable quickref.md, not a complete wiki.
2. Never touch anything outside agent-patterns/. Relative links only.
3. Sources: summaries + links only in git; raw material in .cache/ (gitignored).
   Only use material you can fetch directly; flag signup-gated items; skip paid.
4. No evidence line without a source note behind it. Paraphrase; no pasted text.
5. Cross-tool: Claude Code and Codex both matter; write tool-neutral, note mechanics.
6. Long-running-agent / builder-side material is flagged as a different use case and
   never enters quickref.md.

Execution:
- Branch feature/agent-patterns-mvp off the default branch.
- Phase 0: scaffold per SPEC §4/§5, including .claude/agents/source-triage.md
  (model: sonnet) and .claude/agents/source-distill.md (model: opus). Commit.
- Phase 1: verify SPEC §10 URLs, fetch direct sources into .cache/, enumerate Osmani
  posts since 2025-03-01, build sources/\_triage.md skeleton. Commit.
- Phase 2: triage everything with source-triage subagents, in parallel batches; read
  only \_triage.md yourself.
- Phase 3: select \~15–30 items (all high + unique mediums); distill with
  source-distill subagents.
- Phase 4: synthesize 15–25 patterns + 5–10 anti-patterns, index.md, quickref.md,
  bibliography.md, skill folder. Commit. Stop for Checkpoint B and ask for review.
- Do not merge to main without an explicit OK.

Before starting Phase 0, list the SPEC §11 open items that are still unresolved and
ask for them in one message. Then proceed.
```

\---

## 13\. Things we are deliberately not doing (yet)

No site generator, no database, no Obsidian requirement, no formal "forces" essays,
no exhaustive coverage of builder-side catalogs, no beads for the build, no automated
tests for the wiki, no scripts unless a workflow proves too slow by hand. Every one of
these can be added later by an `experiment` if a real session shows the need.

> Last reminder: if you find yourself polishing instead of shipping, stop, commit,
> and write what you were about to do into `inbox.md` for later.

