---
id: osmani-2026-intent-debt
title: The Intent Debt
author: Addy Osmani
date: 2026-06-05
url: https://addyosmani.com/blog/intent-debt/
access: direct
accessed: 2026-08-29
scope: interactive
relevance: high
pass: distilled
patterns: [intent-ledger, decision-logs, spec-first, record-load-bearing-why, learnings-writeback, agents-md-hygiene]
---
## Summary

Building on Storey's Triple Debt Model, Osmani separates three debts:
technical debt lives in the code, cognitive (comprehension) debt lives in
people's heads, and intent debt lives in artifacts — the externalised goals,
constraints, and rationale explaining why the system is as it is. They are
independent: you can understand a system perfectly yourself while its intent
exists nowhere outside your skull. His central claim is that agents can pay
down the first two — they refactor tangled code and re-explain systems you've
lost the model of — but cannot generate intent, because intent is the one
input that must originate with a human. Asked why a 300ms debounce exists, a
model invents a confident-sounding reason. Agents also make the cost compound:
each starts cold with no tacit history, so unwritten rationale is re-paid every
session rather than once at onboarding. The remedy is externalising the why.

## Takeaways for our use case

- Distinguish the three debts before reaching for a fix: refactoring helps
  technical debt, asking the agent to explain helps comprehension debt, and
  neither touches missing rationale.
- Assume every session starts cold. Anything you haven't written into a file
  the agent can read, it does not have, and it will fill the gap with a
  plausible guess rather than admitting ignorance.
- You cannot capture all intent, but that is no licence to capture none —
  write down the why behind decisions that would be expensive to get wrong.
- Write the spec for the intent, not the implementation: goals, constraints,
  non-negotiables, and an explicit definition of done that goes beyond
  "functionally correct" (fast, accessible, secure).
- Treat AGENTS.md as an intent ledger rather than configuration: conventions,
  "we don't do it this way because…", constraints invisible in any one file.
- Record decisions at the moment you make them; agents have made logging cheap
  enough that the old excuse for skipping ADRs is gone.
- End sessions by writing lessons back into a learnings file — every "we tried
  X and it failed because Y" is intent that would otherwise live only in your
  memory of a bad afternoon.
- Watch for the symptoms: an agent deleting a guard clause nobody can justify,
  a clean-looking refactor that changed behaviour because tests encoded the
  old behaviour rather than the intent, and "an agent suggested it and it
  seemed fine" as an architecture rationale.

## Candidate patterns / evidence

- → intent-ledger: "Treat AGENTS.md as your intent ledger, not your config" —
  an auto-generated file describes what the code is, an intent file describes
  what you mean.
- → decision-logs: lightweight ADRs are "pure intent-debt paydown"; recording
  why at decision time costs almost nothing versus reconstructing it months
  later.
- → spec-first: a good spec carries the goals, constraints, and explicit
  definition of done that the code itself cannot carry.
- → record-load-bearing-why: the failure case is an agent removing a guard
  clause because no doc or commit message ever recorded whether it was
  load-bearing.
- → learnings-writeback: a session-end learnings file run as an "intent-debt
  pump in reverse", capturing root causes and failed approaches.
- → agents-md-hygiene: reinforces the companion argument against `/init` —
  what belongs in the file is the un-inferable why, not a codebase description.

## Other-use-case material

- The "orchestration tax" of running many parallel agents is framed as partly
  an intent-debt tax — much of what makes managing them exhausting is
  re-supplying rationale that was never written down. Multi-agent scope, but
  the underlying mechanism is the same one a solo session hits at session
  boundaries.
