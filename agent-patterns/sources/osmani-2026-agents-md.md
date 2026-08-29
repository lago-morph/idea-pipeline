---
id: osmani-2026-agents-md
title: Stop Using /init for AGENTS.md
author: Addy Osmani
date: 2026-02-23
url: https://addyosmani.com/blog/agents-md/
access: direct
accessed: 2026-08-29
scope: interactive
relevance: high
pass: distilled
patterns: [no-auto-generated-agents-md, agents-md-hygiene, non-discoverable-only, fix-the-codebase-not-the-context, prune-stale-instructions, scoped-context-files, agents-md-as-friction-log]
---
## Summary

Osmani argues the near-universal ritual of running `/init` to generate an
AGENTS.md produces mostly noise. He reads two early-2026 studies against each
other: Lulla et al. (ICSE JAWs 2026, 124 paired PRs) found a human-maintained
AGENTS.md cut median runtime 28.6% and output tokens 16.6%, while an ETH
Zurich study found LLM-generated context files reduced task success 2-3% while
raising cost over 20%, and developer-written ones raised success ~4%. The
reconciling finding: when all other docs were stripped from the repos,
generated files started helping — they are redundant, not useless. He adds the
"pink elephant" problem, where a passing mention of a legacy dependency biases
every later prompt, and the static-file problem, where a monolithic file
loads identically regardless of task. His filter: if the agent can discover it
by reading the code, delete the line. What remains is landmines — tooling
gotchas, non-obvious conventions, do-not-touch warnings.

## Takeaways for our use case

- Don't run `/init`; auto-generated codebase overviews duplicate what the
  agent finds by listing directories and reading the README, adding
  reconciliation work and cost for the same outcome.
- Apply one filter before adding any line: can the agent discover this by
  reading the code? If yes, don't write it.
- What earns a line is operationally significant and unguessable — "use `uv`,
  not pip", "run tests with --no-cache or fixtures give false positives",
  "don't refactor the auth middleware", "legacy/ is deprecated but three
  production modules import it".
- Mentioning something anchors the model on it for every prompt, so a stale
  reference to a replaced dependency actively biases the agent toward the
  wrong pattern; prune aggressively.
- Blanket rules ("always run the full test suite") misfire on tasks they were
  never meant for, like a docs-only change — a flat file cannot condition on
  task type.
- Prefer scoped context: a thin root protocol file (what personas, skills, and
  MCP connections exist, plus the few undiscoverable repo facts) with focused
  files loaded per task, rather than one monolith.
- When the agent repeatedly gets something wrong, treat it as a codebase
  problem first — reorganise the directory, add a lint rule, fix the build
  pipeline — and only then add a context line.
- One technique: start nearly empty with a single instruction telling the
  agent to flag anything surprising, then fix what it flags instead of
  keeping the note.
- Expect instructions to expire as models improve at codebase navigation;
  re-audit rather than accumulate.

## Candidate patterns / evidence

- → no-auto-generated-agents-md: 100% of Sonnet 4.5's and 99% of GPT-5.2's
  auto-generated context files contained codebase overviews — exactly the
  content the agent can discover itself.
- → non-discoverable-only: when a developer-written file mentioned `uv`,
  agents used it ~1.6 times per task versus under 0.01 when unmentioned;
  repo-specific tools showed the same pattern.
- → agents-md-hygiene: the ETH Zurich result flipped positive only once all
  other repo documentation was removed, showing the cost is redundancy, and
  every added line competes for attention with the actual task.
- → prune-stale-instructions: the "pink elephant" effect — a passing mention
  of tRPC keeps it in context for every prompt even if it survives only in
  legacy endpoints.
- → fix-the-codebase-not-the-context: an agent repeatedly misplacing files is
  a signal the directory structure is confusing; fix that and delete the line.
- → agents-md-as-friction-log: treat the file as "a living list of codebase
  smells you haven't fixed yet", a diagnostic tool rather than permanent
  configuration.
- → scoped-context-files: a root routing/protocol file plus per-task persona
  or skill files keeps total context bounded; one root file is insufficient
  for any codebase of real complexity.

## Other-use-case material

- A maintenance subagent whose only job is keeping the protocol file accurate
  as the codebase evolves — plausible but no tool exposes the lifecycle hooks
  to build it cleanly yet.
- Automated prompt-learning loops (Arize AI) that optimise CLAUDE.md against
  evaluated runs, reporting +5.19% cross-repo and +10.87% in-repo accuracy —
  builder-side tooling, but the implication that authors misjudge what helps
  the model is worth carrying into manual editing.
- The 15-20% context-file cost overhead compounding across CI/CD or automated
  review pipelines at scale.
- Caveats worth honouring: the Lulla study measured only efficiency, never
  correctness; neither paper tested a hierarchical, dynamically-loaded setup.
