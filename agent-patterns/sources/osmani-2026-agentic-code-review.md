---
id: osmani-2026-agentic-code-review
title: Agentic Code Review
author: Addy Osmani
date: 2026-06-15
url: https://addyosmani.com/blog/agentic-code-review/
access: direct
accessed: 2026-08-29
scope: interactive
relevance: high
pass: distilled
patterns: [review-agent-diffs, tier-review-by-risk, scrutinize-rewritten-tests, small-reviewable-steps, capture-agent-intent, heterogeneous-reviewers, agent-triage-first-pass, require-evidence-before-review, human-owns-the-merge, keep-deterministic-gates-strict]
---
## Summary

Osmani argues that agents made writing cheap while human reading speed stayed
flat, so the binding constraint moved to being confident a change is right.
He cites 2026 industry telemetry (churn, defect rate, review duration and
zero-review merges all sharply up; roughly 4x raw output for about 12% real
productivity gain) and notes vendor-funded framing where relevant. His central
claim is that how much review a change needs depends on three variables —
blast radius, how long the code lives, and how many people must understand it —
so advice written for an enterprise misfires on a solo project and vice versa.
Review's old job was checking an author's reasoning; an agent's reasoning is
usually discarded, leaving the reviewer to reconstruct intent that was never
written down. Fixes: capture the agent's intent, tier review by risk, run
heterogeneous automated reviewers, keep diffs small, and keep a human owning
the merge.

## Takeaways for our use case

- Set review depth by blast radius, code lifetime, and how many people must
  understand the change — not by a single fixed standard for every diff.
- Solo with no users is permission to defer review, not to skip verification;
  the deferred work is still owed, at a higher price.
- Have the agent state what it was trying to do and what it ruled out, and keep
  that with the change; it removes most of the intent-reconstruction cost.
- Use an agent as a first-pass risk triage over a queue of changes to allocate
  your attention, without letting its verdict become the merge decision.
- Treat any AI review as a sensor, not a verdict — a confident "looks good" from
  a model in a closed loop is borrowed confidence with nobody understanding.
- Read test-file changes before code changes: the signature agent failure is
  changing behaviour and then rewriting assertions to match it.
- Keep deterministic gates (CI, lint, coverage thresholds) strict, because they
  are the one check a confident paragraph cannot talk out of its verdict.
- Instruct the agent toward small commits; a readable diff is now a design
  constraint, since agent PRs run larger and large ones get rubber-stamped.
- Watch for untrusted input flowing into an LLM call — the vulnerability is
  latent in future data, not visible in the diff.

## Candidate patterns / evidence

- → review-agent-diffs: review must reconstruct intent an agent discarded, so the
  reviewer is often "the first human being to ever lay eyes on this code".
- → tier-review-by-risk: a config change earns a linter and a glance; a payments
  path earns types, tests, two AI reviewers, a human owner and a security pass.
- → capture-agent-intent: agents do reason visibly, but the reasoning is thrown
  away before the diff; capturing it as a decision log cuts review cost.
- → agent-triage-first-pass: Osmani points Claude Code or Codex at a batch of
  incoming PRs for a risk-sorted read, then spends human time on the flagged ones.
- → heterogeneous-reviewers: across 146 PRs and four reviewers, 93.4% of flagged
  locations were caught by exactly one tool and none by all four.
- → scrutinize-rewritten-tests: a green check over 200 edited tests means nothing
  until the edits are confirmed; mutation testing beats coverage here.
- → small-reviewable-steps: agent PRs averaged 51% larger, and large unreviewable
  changes get rejected outright or waved through.
- → require-evidence-before-review: refuse changes that arrive without a stated
  purpose, a readable diff, and proof the tests were actually run.
- → human-owns-the-merge: a model cannot be paged or held responsible, so whoever
  merges owns the outcome.
- → keep-deterministic-gates-strict: agents weaken CI to reach green as the
  cheapest path, so the gates must not be negotiable.
- → comprehension-debt: a change nobody understood becomes someone's future
  incident; "tests passed" is not "a person understands this".

## Other-use-case material

- Team/enterprise scope (flagged, not for quickref): treating review capacity as
  a measured resource, the senior-engineer review tax, and warnings against
  cutting headcount before closing the review gap.
- Long-running/builder scope: loop engineering, where an agent judge decides
  work is done and designs the reviewer out of the inner loop; and the solo
  builder running 20–30 parallel agents against detailed up-front plans with an
  automated merge gate — relevant to long-running agent setups, not to one
  interactive session.
