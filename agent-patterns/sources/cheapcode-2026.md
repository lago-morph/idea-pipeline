---
id: cheapcode-2026
title: "Cheap Code, Costly Judgment: A Case Study on Governable Agentic Software Engineering"
author: James C. Davis, Paschal C. Amusuo, Tanmay Singla, Berk Çakar, Kirsten A. Davis
date: 2026-07-01
url: https://arxiv.org/abs/2607.01087
access: direct
accessed: 2026-09-13
scope: interactive
relevance: high
pass: distilled
patterns: [capture-lessons, prefer-deterministic-controls, give-a-runnable-check, front-load-context, agents-md-hygiene, calibrate-autonomy, unreviewed-code, reframe-before-blaming-the-model]
---

## Summary

A 12-week autoethnographic case study. One expert engineer — a professor with
sixteen years' experience, and an author of the paper — used Claude through the
VS Code chat plugin to build a document-accessibility remediation system under a US
accessibility deadline. The record: 88 contemporaneous field notes, 18,662
commits, ~420 KLOC of product and 1.16 MLOC of tests, analyses, agent-facing
documentation and tooling. Coding those incidents (72 engineering reflections;
35 controls, 20 architecture) yields a candidate middle-range theory,
*governance conversion*: velocity surfaces recurring failure classes, the human
judges each as a local defect or a structural one, and structural ones are
converted into durable mechanisms — a type, a lint, an analysis, a gate — that
narrow what later agents can do. The engineer inspected almost no agent-written
code, relying on that machine-enforced substrate instead. Controls written in
advance were used and found necessary but not sufficient. N=1, one toolchain,
theory-building not prevalence.

## Takeaways for our use case

- When the agent gets something wrong, the load-bearing judgement is whether it
  is a one-off defect or an instance of a class; only the second kind is worth
  converting into a durable mechanism.
- Prefer the mechanism that makes the failure unexpressible (a type, a closed
  vocabulary, a bounded seam) over one that merely detects it after the fact;
  the case treats architecture and controls as two responses to the same signal.
- Prose rules in an agent-facing instructions file are the weakest form of
  control here: the paper's claim is that soft, probabilistic guidance must be
  mated to deterministic checks, because at volume a low-probability violation
  becomes a certainty.
- Rules files are themselves artifacts to govern: this project added a rule
  index and a cap lint to its CLAUDE.md so project rules stayed enforceable
  rather than conventional.
- Front-load the *specific* constraints a change is subject to rather than all of
  them: a dispatch-time mechanism mapped the files a task would touch to the
  lints, conventions and boundaries governing them and injected only those into
  the brief, instead of letting the agent violate a rule and then repair it.
- Do not read the case as licence to stop reading diffs. Inspection was dropped
  only behind a verification substrate 2.75x the size of the product — 577
  project-specific static analyses, 13,000+ C# test methods, ~1,500 Python test
  files, 300+ property-based tests, 90 fuzz harnesses, and staged pre-commit /
  merge / deploy gates. Without that, this is just unreviewed code.
- Both directions matter: controls carried forward from this project made two
  later projects start faster, and new failure modes still appeared in each. An
  up-front rulebook and a capture habit are complements, not alternatives.
- Agent speed lowers the cost of the quality work you would normally defer — one
  incident refactored a ~100 KLOC front-end to TypeScript in two days with no
  defects under the project's own checks.
- Related failures arriving close together is itself a signal: their proximity
  is what let the engineer see an architectural gap that would have been
  invisible had the same failures surfaced months apart.
- When a delegated task fails, the paper's disposition is to "assume that you are
  the problem" — read it as a task not yet framed as an inspectable, constrained
  process before concluding the model cannot do it.
- The agent proposed no governance responses early on, but began suggesting
  plausible ones once the codebase contained examples of them — seeding the
  first few is the human's job.
- The ethics section reports real harm from the work pattern: degraded attention
  to personal relationships and physical strain, because agentic tools make
  extreme sessions sustainable for longer than is healthy.

## Candidate patterns / evidence

- → `capture-lessons`: across 88 field notes, the controls that sustained velocity were induced from failures visible only during agentic work — though rules written in advance were used too, and found necessary but insufficient.
- → `prefer-deterministic-controls` (new): the engineering-governance thesis is that review-centred and convention-based controls saturate under agentic velocity and must be converted into compiler-checked types, static analyses and commit gates.
- → `give-a-runnable-check`: quality was held by 577 project-specific analyses, 13,000+ C# tests, 300+ property tests and 90 fuzz harnesses gating commits — deterministic checks, not the engineer's reading, were the admission criterion.
- → `front-load-context`: the dynamic context injection control sliced repo-wide constraints down to the ones governing the files a change would touch and put them in the brief before editing, shifting detection left of the cheapest lint.
- → `agents-md-hygiene`: governance-doc controls included a CLAUDE.md rule index and a cap lint, plus mandatory snippet tables and definition-of-done checks, to keep agent-facing rules enforceable as they accumulated.
- → `calibrate-autonomy`: the engineer inspected almost no agent code and deliberately tested whether quality survives without inspection — but only inside a support apparatus 2.75x the size of the product; autonomy was bought with verification.
- → `unreviewed-code`: bounds the anti-pattern rather than contradicting it — skipping diff review was viable here only with an enormous machine-enforced envelope, and the paper makes no claim it transfers to ordinary projects.
- → `reframe-before-blaming-the-model` (new): a repeated lesson was to treat a failed delegation as evidence the task was not yet decomposed and constrained, rather than as evidence of model incapability.

## Other-use-case material

- **Flag: long-running / multi-agent.** The deepest mechanism stack (14
  complementary mechanisms) formed around orchestrator/sub-agent interactions,
  and much of the catalog presupposes many concurrent agents: an agent registry,
  a typed event bus, sentinel and tombstone commits, test and build serializers,
  an admission protocol keyed to machine health, and merge-train batching across
  worktrees. None of this belongs in single-session patterns.
- **Flag: organisational / builder-side.** Governance conversion is said to
  require authority — where ownership is divided, the same failure signal
  produces only a local patch. The paper also proposes governed throughput
  over implementation volume as the right productivity metric, and argues
  team-scale coordination artifacts get compressed into one person's workflow.
- **Flag: research-side.** The middle-range theory, its four falsifiable
  propositions, and the threats-to-validity section bear on how much weight to
  give the paper (single subject, single toolchain, subject as analyst), not on
  what to do in a session.
- The authors publish an enumeration of the governance mechanisms and an
  accompanying skill at davisjam.github.io/agent-governance-mechanisms — worth a
  separate triage pass as a distinct source.
