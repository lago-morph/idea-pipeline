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
| new feature, unfamiliar codebase | run-tests-first · front-load-context · plan-before-code · review-plans-not-code · small-reviewable-steps · tier-review-by-risk |
| new feature, familiar codebase | spec-first · define-done-first · small-reviewable-steps · checkpoint-commits · give-a-runnable-check |
| bug fix with repro | run-tests-first · red-green-tdd · small-reviewable-steps · fresh-context-reset |
| refactor | plan-before-code · small-reviewable-steps · checkpoint-commits · agentic-manual-testing · tier-review-by-risk |
| spike / throwaway prototype | hoard-working-code · match-model-to-task · jig-for-tuning (review discipline relaxes only if it stays throwaway) |
| big delegated chunk | full-brief-up-front · define-done-first · calibrate-autonomy · demand-evidence-not-summary · verify-from-clean-state |
| reviewing a diff (agent's or someone else's) | tier-review-by-risk · form-your-own-take-first · cross-model-review · test-the-failure-paths · verify-from-clean-state |
| UI / visual work | polish-pass · jig-for-tuning · agentic-manual-testing |
| stuck / session going badly | fresh-context-reset · match-model-to-task · context-compaction · form-your-own-take-first |
| dependency upgrade | run-tests-first · agentic-manual-testing · test-the-failure-paths · checkpoint-commits |
| session end | capture-lessons · intent-ledger · skill-authoring · prefer-deterministic-controls |
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
- review-agent-diffs *(deprecated 2026-09-13)* — kept for the record; same disposition as unreviewed-code
- tier-review-by-risk — depth by blast radius; humans threat-model the risky parts
- demand-evidence-not-summary — proof, not the agent's narration
- agentic-manual-testing — exercise the code like a human, beyond the suite
- form-your-own-take-first — write your expectation before reading output
- cross-model-review — a different model or fresh session as reviewer
- test-the-failure-paths — probe what must NOT work (auth, abuse, errors)
- polish-pass — final gate is using the running thing
- verify-from-clean-state *(candidate)* — evidence from the committed artifact, in an environment nobody patched
- red-green-tdd *(candidate)* — the four-word prompt that enforces test-first

### debugging-recovery
- fresh-context-reset — restart with better steering instead of arguing

### compounding
- capture-lessons — capture sessions as history, then mine the pile into mechanisms
- refactor-skills-into-checks *(candidate, placeholder)* — move a skill's checkable steps into hooks and lints
- prefer-deterministic-controls — convert a recurring failure into a type, lint or gate, not a prose rule
- skill-authoring — skills as tested process with exit criteria, not prose

### anti-pattern
- unreviewed-code *(deprecated 2026-09-13)* — kept for the record; reviewing every line is no longer the working norm
- cognitive-surrender — accepting because it sounds right
- comprehension-debt — a system nobody on the team understands anymore
- stale-scaffolding — prompts/skills tuned for last year's model
- auto-generated-agents-md — /init overviews are redundant at best, anchoring at worst
- bloated-instruction-surface *(candidate)* — accreted AGENTS.md, skills and ADRs: context spent, contradictions unresolved
- no-progressive-disclosure *(candidate)* — reference material that can only be loaded whole
- over-compressed-context *(candidate)* — token-shaving that raises total session tokens

## Status legend

`candidate` — proposed, thin evidence (single source) · `adopted` — in quickref ·
`deprecated` — don't use; kept for the record · `absorbed` — tools/models now
do this automatically.

## Recently changed

- 2026-09-13 — `review-agent-diffs` deprecated alongside `unreviewed-code`; its
  surviving parts distributed to `tier-review-by-risk`,
  `demand-evidence-not-summary` and `prefer-deterministic-controls`.
  `capture-lessons` rewritten: capture as history, mechanise the threads. Two new
  anti-patterns (`bloated-instruction-surface`, `no-progressive-disclosure`) and a
  placeholder `refactor-skills-into-checks`. Source note extended with the
  now-complete session transcript.
- 2026-09-13 — ingested `lagomorph-2026-k8s-forensics` (own project, first-hand):
  12 evidence lines across existing pages, new candidate `verify-from-clean-state`,
  and `prefer-deterministic-controls` promoted to adopted at `confidence: high` —
  the wiki's first, since own experience plus a second independent source now back
  it. Carries counter-evidence against `capture-lessons`.
- 2026-09-13 — `unreviewed-code` deprecated on the owner's own experience: reading
  every line an agent writes is no longer the 2026 norm. Re-rated `compensation`;
  its surviving point (ship nothing that *nothing* has checked) absorbed into
  `prefer-deterministic-controls`. Removed from `quickref.md`.
- 2026-09-13 — new candidate `prefer-deterministic-controls` from `cheapcode-2026`;
  folded "a failed delegation is under-framing" into `fresh-context-reset`.
- 2026-09-13 — re-ingested the three arXiv sources that had been distilled from
  their abstracts (`dontvibe-2025`, `cheapcode-2026`, `beyondhumanreadable-2026`)
  from full text; corrected the four evidence lines citing them and narrowed
  `over-compressed-context`. Rewrote `skill/…/patterns-list.md` against a new
  row contract (SPEC §5.11) after 30 of its 36 triggers were found truncated.
- 2026-08-29 — initial synthesis: 30 patterns + 6 anti-patterns from 49 source
  notes (see log.md, Phases 0–4).
