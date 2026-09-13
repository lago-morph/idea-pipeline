# inbox

Quick capture from real sessions; consumed by lint. Format:
`- YYYY-MM-DD [project] lesson…`

- 2026-09-13 [agent-patterns] Jonathan: does not accept the `unreviewed-code`
  anti-pattern as written. In 2026 very few people review all the code an agent
  writes; reviewing all of it was necessary a year ago and is not now. Treat the
  review cluster (unreviewed-code, review-agent-diffs, tier-review-by-risk) as
  due for re-rating — currently all `durability: structural`.
- 2026-09-13 [agent-patterns] Candidate pattern parked, not written:
  `agent-legible-code` (naming and semantic density rise in value when agents are
  a primary reader of the code). Single source, `beyondhumanreadable-2026`, no
  experiment behind it, and it is repo-design rather than session practice.
  Write it if a second, independent source turns up.
- 2026-09-13 [agent-patterns] Wanted source, could not fetch: the agent-governance
  mechanism catalogue cited by `cheapcode-2026` at
  davisjam.github.io/agent-governance-mechanisms/index.html — the lab site is live
  but that path 404s as of today. Retry later or ask the authors.

- 2026-09-13 [agent-patterns] ASK JONATHAN LATER: `refactor-skills-into-checks` is
  a placeholder page with `[own]` direction but no demonstration. He offered
  evidence from real projects at a future date. Do not promote past `candidate`
  until that lands.
- 2026-09-13 [agent-patterns] Candidate slug not written: `adversarial-self-review`
  — dispatch reviewers grounded in the actual tree, told to falsify your own draft,
  before you act on it. Distinct from `cross-model-review` (different model, before
  shipping) in that it targets your own unratified plan and its claims. Evidence
  added to `cross-model-review` for now; ask whether it deserves its own page.
- 2026-09-13 [agent-patterns] Nuance to check with Jonathan: his position is that
  edits to AGENTS.md, ADRs *and* skills get ignored. The transcript complicates the
  ADR half — an ADR there was ratified, implemented, and shipped with a contract
  lint. The cut that holds is behavioural-prose-remedy vs design-decision-plus-
  enforcement, not document type. `prefer-deterministic-controls` currently states
  it the broad way.

