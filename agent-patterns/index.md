# index

## How to use this (agent)

1. Find the task shape in *By task* below; open only the listed pattern files.
2. For browsing, use *By category*.
3. Statuses: only `adopted` patterns appear in `quickref.md`; `candidate` means
   evidence is thin — use with judgment.
4. Long-running / builder-scoped material lives only in source notes'
   "Other-use-case" sections; don't apply it to interactive sessions.
5. Learned something? One line in `inbox.md`.

## By task

| task shape | patterns |
|-|-|
| new feature, unfamiliar codebase | run-tests-first · front-load-context · plan-before-code · review-plans-not-code · small-reviewable-steps · review-agent-diffs |
| new feature, familiar codebase | spec-first · define-done-first · small-reviewable-steps · checkpoint-commits · review-agent-diffs |
| bug fix with repro | run-tests-first · red-green-tdd · small-reviewable-steps · fresh-context-reset |
| refactor | plan-before-code · small-reviewable-steps · checkpoint-commits · agentic-manual-testing · review-agent-diffs |
| spike / throwaway prototype | hoard-working-code · match-model-to-task · jig-for-tuning (review discipline relaxes only if it stays throwaway) |
| big delegated chunk | full-brief-up-front · define-done-first · calibrate-autonomy · demand-evidence-not-summary |
| reviewing a diff (agent's or someone else's) | review-agent-diffs · tier-review-by-risk · form-your-own-take-first · cross-model-review · test-the-failure-paths |
| UI / visual work | polish-pass · jig-for-tuning · agentic-manual-testing |
| stuck / session going badly | fresh-context-reset · match-model-to-task · context-compaction · form-your-own-take-first |
| dependency upgrade | run-tests-first · agentic-manual-testing · test-the-failure-paths · checkpoint-commits |
| session end | capture-lessons · intent-ledger · skill-authoring |
| new model release | stale-scaffolding · match-model-to-task |

## By category

### session-setup
- agents-md-hygiene — keep AGENTS.md short; every line earned by a real failure
- front-load-context — pack what the task needs into the first prompt
- give-a-runnable-check — hand the agent a way to verify its own work
- intent-ledger — record the why (ADRs, decision logs) agents can't reconstruct
- hoard-working-code *(candidate)* — keep proven examples; point at code, not prose
- run-tests-first *(candidate)* — open sessions on existing code by running the tests

### planning
- plan-before-code — explore and plan read-only before any edit
- spec-first — goal, non-goals, boundaries before the prompt
- review-plans-not-code — human leverage is highest at the plan
- define-done-first — write the done-condition before the agent starts

### execution-loop
- small-reviewable-steps — the unit of review is the unit of comprehension
- context-compaction — compact deliberately into files, not by default
- jig-for-tuning *(candidate)* — ask for a control panel, not one more tweak

### version-control
- checkpoint-commits — small frequent commits as save points; let the agent drive git

### delegation
- subagents-for-context — subagents protect the main context window
- match-model-to-task — frontier for unknowns, cheaper models for routine
- calibrate-autonomy — autonomy follows verification, not task name
- full-brief-up-front — for big chunks: whole brief, then judge the artifact

### review-quality
- review-agent-diffs — you review first, always
- tier-review-by-risk — depth by blast radius; humans threat-model the risky parts
- demand-evidence-not-summary — proof, not the agent's narration
- agentic-manual-testing — exercise the code like a human, beyond the suite
- form-your-own-take-first — write your expectation before reading output
- cross-model-review — a different model or fresh session as reviewer
- test-the-failure-paths — probe what must NOT work (auth, abuse, errors)
- polish-pass — final gate is using the running thing
- red-green-tdd *(candidate)* — the four-word prompt that enforces test-first

### debugging-recovery
- fresh-context-reset — restart with better steering instead of arguing

### compounding
- capture-lessons — failures become standing instructions; quality compounds
- skill-authoring — skills as tested process with exit criteria, not prose

### anti-pattern
- unreviewed-code — shipping agent output nobody read
- cognitive-surrender — accepting because it sounds right
- comprehension-debt — a system nobody on the team understands anymore
- stale-scaffolding — prompts/skills tuned for last year's model
- auto-generated-agents-md — /init overviews are redundant at best, anchoring at worst
- over-compressed-context *(candidate)* — token-shaving that raises total cost

## Status legend

`candidate` — proposed, thin evidence (single source) · `adopted` — in quickref ·
`deprecated` — don't use; kept for the record · `absorbed` — tools/models now
do this automatically.

## Recently changed

- 2026-08-29 — initial synthesis: 30 patterns + 6 anti-patterns from 49 source
  notes (see log.md, Phases 0–4).
