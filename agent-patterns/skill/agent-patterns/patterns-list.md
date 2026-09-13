# patterns-list — generated 2026-09-13

Router for this skill. One row per page: `id — type/status — title — when it applies`.
The last field says *when you would reach for the page*, not what it advises — for the
advice read `quickref.md`; for the full page read `agent-patterns/patterns/<id>.md`
(`agent-patterns/index.md` routes by task shape).

- `agentic-manual-testing` — pattern — Have the agent test like a human — The suite is green and you are about to believe it.
- `agents-md-hygiene` — pattern — Keep AGENTS.md short and earned — You are about to add a line to AGENTS.md / CLAUDE.md, or the agent is ignoring rules already in it.
- `auto-generated-agents-md` — anti-pattern — Auto-generated AGENTS.md — Setting up a repo for agent work and reaching for the generate-my-context-file command first.
- `calibrate-autonomy` — pattern — Calibrate autonomy to verification — Deciding, per task, how far to let the agent run before you look at what it did.
- `capture-lessons` — pattern — Capture lessons into instructions — You corrected an agent mistake, or a session taught you something the next one would need.
- `checkpoint-commits` — pattern — Commit small, commit often — An agent is making edits you may want to undo — any session that changes more than one thing.
- `cognitive-surrender` — anti-pattern — Cognitive surrender — You are ratifying a long diff rather than reviewing it, or shipping a fix to a stack trace you never read.
- `comprehension-debt` — anti-pattern — Comprehension debt — The codebase is growing faster than your model of it, and nothing feels wrong because the suite is green.
- `context-compaction` — pattern — Compact context deliberately — A long session is still on the right track, with research, verified phases or heavy tool output behind it.
- `cross-model-review` — pattern — Review with a different model — Before shipping anything with an auth, payment, data or public-endpoint surface, or any high-stakes change.
- `define-done-first` — pattern — Define done before starting — Always, and especially before handing over a task you will not watch turn by turn.
- `demand-evidence-not-summary` — pattern — Demand evidence, not summaries — Any time an agent reports that a task is finished.
- `form-your-own-take-first` — pattern — Form your own take first — The task turns on a judgement you will have to defend: a design choice, a diagnosis, a fix in your code.
- `fresh-context-reset` — pattern — Reset instead of arguing — You have corrected the same mistake twice, or the session is full of failed approaches.
- `front-load-context` — pattern — Front-load the context the task needs — Starting any task bigger than a one-sentence diff, especially with a model you won't babysit.
- `full-brief-up-front` — pattern — Full brief up front, then hands off — Giving a slow, high-capability model a substantial job you are willing to review only at the end.
- `give-a-runnable-check` — pattern — Give the agent a runnable check — Starting a task where "looks done" and "is done" could differ — which is most of them.
- `hoard-working-code` — pattern (candidate) — Hoard working code and point at it — The task resembles something already solved, and you would otherwise describe the behaviour in prose.
- `intent-ledger` — pattern — Keep an intent ledger — A decision or constraint exists only in your head, and the next session will start cold without it.
- `jig-for-tuning` — pattern (candidate) — Ask for a jig, not a tweak — You are iterating on a value rather than a behaviour: timings, spacing, thresholds, opacity.
- `match-model-to-task` — pattern — Match the model to the task — Starting a task, or handing off between phases of one.
- `over-compressed-context` — anti-pattern (candidate) — Over-compressed context — You are shrinking something the agent must read and interpret, judging the change by the tokens it saves.
- `plan-before-code` — pattern — Plan before code — The change spans several files, the codebase is unfamiliar, or the approach is still uncertain.
- `polish-pass` — pattern — Polish with the running app open — The change has a surface a person experiences — UI, copy, output formatting — and the checks are green.
- `prefer-deterministic-controls` — pattern — Prefer deterministic controls to prose rules — You are about to write a rule into an instructions file to stop a failure you have seen twice.
- `red-green-tdd` — pattern (candidate) — Prompt for red/green TDD — The change has a statable behaviour and the project has a test suite the agent can run.
- `review-agent-diffs` — pattern — Review every agent diff yourself — Before you merge, push, or open a PR containing anything an agent wrote.
- `review-plans-not-code` — pattern — Review plans, not just code — The agent produced research or a plan and you are deciding where to spend your own attention.
- `run-tests-first` — pattern (candidate) — Open the session by running the tests — Starting work in an existing repo, especially one you or the agent have not touched recently.
- `skill-authoring` — pattern — Author skills as tested process — You are writing down a procedure you repeat: a review pass, a release checklist, a manual pipeline.
- `small-reviewable-steps` — pattern — Work in small reviewable steps — The agent is editing code — almost always, and especially once a plan exists to cut into steps.
- `spec-first` — pattern — Write the spec before the prompt — Building a feature rather than making an edit — anything an agent could plausibly read two ways.
- `stale-scaffolding` — anti-pattern — Stale scaffolding — A model release just landed, or you are carrying skills and prompts written for an older weakness.
- `subagents-for-context` — pattern — Use subagents to protect context — A step will generate output you will never re-read: a big search, noisy logs, fetched docs.
- `test-the-failure-paths` — pattern — Test the failure paths — The change exposes a surface someone else can reach: an endpoint, a login, a payment, untrusted input.
- `tier-review-by-risk` — pattern — Tier review depth by risk — Deciding how much of your attention a change deserves — which is every change, once diffs outrun you.
- `unreviewed-code` — anti-pattern (deprecated) — Shipping unreviewed agent code — Deprecated; do not apply — see prefer-deterministic-controls and tier-review-by-risk instead.
- `verify-from-clean-state` — pattern (candidate) — Verify from a clean state — You are about to accept a green check or a demo produced in an environment you or the agent could have patched.
