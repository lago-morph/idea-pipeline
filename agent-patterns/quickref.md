# quickref — generated 2026-08-29 · verified against: claude-5, gpt-5.6

GENERATED from adopted patterns by lint — edit `patterns/<id>.md`, not this file.

## Before starting

- Pack the context the task needs into the first prompt: files, constraints, approaches to avoid. [front-load-context]
- Write goal, non-goals, and boundaries before prompting; spec quality is the bottleneck. [spec-first]
- Explore and plan read-only first; iterate the plan until it's boring, then edit. [plan-before-code]
- Have a fresh session or model review the plan — a bad plan line costs hundreds of bad code lines. [review-plans-not-code]
- Write the done-condition (metric, invariants, stop rule) before the agent starts. [define-done-first]
- Hand the agent a runnable pass/fail check for its own work. [give-a-runnable-check]
- Keep AGENTS.md short: only non-discoverable rules, each earned by a real failure. [agents-md-hygiene]
- Pick the model by uncertainty and cost: frontier for unknowns, cheaper for routine. [match-model-to-task]
- Set autonomy by how fast you'd know it's wrong and how cleanly you can undo. [calibrate-autonomy]
- For a big delegated chunk: full brief up front, hands off, judge the artifact. [full-brief-up-front]

## While working

- Work in small reviewable steps; the unit of review is the unit of comprehension. [small-reviewable-steps]
- Commit small and often as save points; let the agent drive git. [checkpoint-commits]
- Compact context deliberately into progress files; stay inside the useful window. [context-compaction]
- Two failed corrections → reset with better steering; don't argue with a full context. [fresh-context-reset]
- Use subagents to keep search and noise out of the main context window. [subagents-for-context]
- Write your own expectation before reading the agent's answer. [form-your-own-take-first]
- Make the agent exercise the code like a human — CLI runs, curl, a real browser. [agentic-manual-testing]
- Take evidence (commands, output, screenshots), never the agent's narration. [demand-evidence-not-summary]

## Before finishing

- Review every diff yourself first; agent-written PR descriptions need review too. [review-agent-diffs]
- Tier review depth by blast radius; auth/payments/secrets get a human threat model. [tier-review-by-risk]
- Have a different model or fresh session review the result. [cross-model-review]
- Probe the failure paths: what must not work when the wrong caller tries it. [test-the-failure-paths]
- Final gate: open the running app and use it; checks passing isn't "good". [polish-pass]
- Turn this session's failures into standing instructions; quality compounds. [capture-lessons]
- Record the why — decisions, rejected options — where agents will re-read it. [intent-ledger]
- Repeated task? Turn it into a skill with steps and exit criteria, tested first. [skill-authoring]

## Watch out for

- Shipping agent output nobody read. [unreviewed-code]
- Accepting because it sounds right — polish is not correctness. [cognitive-surrender]
- A codebase nobody on the team understands anymore. [comprehension-debt]
- Prompts and skills tuned for last year's model quietly hurting this year's. [stale-scaffolding]
- Auto-generated AGENTS.md overviews — redundant at best, anchoring at worst. [auto-generated-agents-md]
