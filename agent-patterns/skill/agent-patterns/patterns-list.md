# patterns-list — generated 2026-08-29

id — type/status — title — one line. Full pages: agent-patterns/patterns/<id>.md

- `agentic-manual-testing` — pattern — Have the agent test like a human — the suite is green and you are about to believe it.
- `agents-md-hygiene` — pattern — Keep AGENTS.md short and earned — you are about to add a line to AGENTS.md / CLAUDE.md, or the agent is
- `auto-generated-agents-md` — anti-pattern — Auto-generated AGENTS.md — setting up a repo for agent work and reaching for the
- `calibrate-autonomy` — pattern — Calibrate autonomy to verification — deciding, per task, how far to let the agent run before you look.
- `capture-lessons` — pattern — Capture lessons into instructions — the agent got something wrong and you corrected it, or a session
- `checkpoint-commits` — pattern — Commit small, commit often — an agent is making edits you may want to undo — any session that
- `cognitive-surrender` — anti-pattern — Cognitive surrender — you are at risk of this — ratifying a long diff rather than
- `comprehension-debt` — anti-pattern — Comprehension debt — you are at risk of this — the codebase is growing faster than your
- `context-compaction` — pattern — Compact context deliberately — a session is long but still on the right track — research, several
- `cross-model-review` — pattern — Review with a different model — before shipping anything with an auth, payment, data, or public-endpoint surface — and on any high-stakes chan
- `define-done-first` — pattern — Define done before starting — always, and especially before handing over a task you will not watch
- `demand-evidence-not-summary` — pattern — Demand evidence, not summaries — any time an agent reports that a task is finished.
- `form-your-own-take-first` — pattern — Form your own take first — the task involves a judgement you will have to defend — a design
- `fresh-context-reset` — pattern — Reset instead of arguing — you have corrected the same mistake twice, the agent keeps reverting to
- `front-load-context` — pattern — Front-load the context the task needs — starting any task bigger than a one-sentence diff, especially with a slow,
- `full-brief-up-front` — pattern — Full brief up front, then hands off — giving a slow, high-capability model a substantial job you are willing
- `give-a-runnable-check` — pattern — Give the agent a runnable check — starting any task where "looks done" and "is done" could differ — which is
- `hoard-working-code` — pattern (candidate) — Hoard working code and point at it — the task resembles something you or someone else has already solved, and you
- `intent-ledger` — pattern — Keep an intent ledger — a decision, constraint, or "we don't do it that way because…" exists only in
- `jig-for-tuning` — pattern (candidate) — Ask for a jig, not a tweak — you are iterating on a value rather than a behaviour — timings,
- `match-model-to-task` — pattern — Match the model to the task — starting a task, or handing off between phases of one.
- `over-compressed-context` — anti-pattern (candidate) — Over-compressed context — 
- `plan-before-code` — pattern — Plan before code — the change spans several files, the codebase is unfamiliar, or the
- `polish-pass` — pattern — Polish with the running app open — the change has a surface a person experiences — UI, copy, output formatting — and the checks are already green
- `red-green-tdd` — pattern (candidate) — Prompt for red/green TDD — the change has a statable behaviour and the project has a test suite the agent can run.
- `review-agent-diffs` — pattern — Review every agent diff yourself — before you merge, push, or open a PR containing anything an agent wrote.
- `review-plans-not-code` — pattern — Review plans, not just code — the agent has produced research or a plan and you are deciding where to
- `run-tests-first` — pattern (candidate) — Open the session by running the tests — starting work in an existing repo, especially one the agent (or you) has not
- `skill-authoring` — pattern — Author skills as tested process — you are writing down a procedure you repeat — a review pass, a
- `small-reviewable-steps` — pattern — Work in small reviewable steps — the agent is editing code — i.e. almost always, and especially once a
- `spec-first` — pattern — Write the spec before the prompt — building a feature rather than making an edit — anything an agent could
- `stale-scaffolding` — anti-pattern — Stale scaffolding — you are at risk of this — a model release just landed, or you are
- `subagents-for-context` — pattern — Use subagents to protect context — a step will generate output you will never re-read — searching a large
- `test-the-failure-paths` — pattern — Test the failure paths — the change exposes a surface someone else can reach — an endpoint, a connector, a login, a payment, anything h
- `tier-review-by-risk` — pattern — Tier review depth by risk — deciding how much of your attention a given change deserves — which is every change, once the agent produces m
- `unreviewed-code` — anti-pattern — Shipping unreviewed agent code — you are at risk of this — the tests are green, the diff is large
