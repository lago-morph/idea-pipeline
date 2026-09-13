---
id: lagomorph-2026-k8s-forensics
title: "k8s-platform: LESSONS.md and the two-round forensic analysis"
author: lago-morph (wiki owner's own project; the documents are agent-authored about agent behaviour)
date: 2026-06-10
url: "(own repo: github.com/lago-morph/k8s-platform — ai/LESSONS.md and forensics/)"
access: direct
accessed: 2026-09-13
scope: interactive
relevance: high
pass: distilled
patterns: [prefer-deterministic-controls, verify-from-clean-state, capture-lessons, agents-md-hygiene, demand-evidence-not-summary, define-done-first, spec-first, give-a-runnable-check, comprehension-debt, intent-ledger, stale-scaffolding, agentic-manual-testing, calibrate-autonomy]
---

## Summary

First-hand record from the wiki owner's own project: a Kubernetes platform built
with coding agents (722 commits, 214 PRs in 38 days) that never reached a clean
build from committed source, plus the two-round forensic analysis that followed.
The forensics name four reinforcing structures. Verification was self-certified —
no automatic gate ever built the platform from committed source, so "done" meant
the agent said so. The agent held admin credentials on a throwaway cloud account,
which made patching the live environment always cheaper than fixing committed
code, and nightly account rotation erased the patch so the same gap was re-fixed
by hand. The founding spec hand-waved exactly the layer boundaries where that work
accumulated. And the standard remedy for behavioural failure was more instruction
text: 152 proposed rules, a rulebook peaking at 1,347 lines. Agent-authored,
single project, several conclusions self-flagged as inference — strong on
mechanism, weak on base rates.

## Takeaways for our use case

- The load-bearing finding: failure classes wired to a fail-closed mechanism
  stopped recurring; classes answered with a written rule did not. Eight of twelve
  tracked recurrence classes recurred *after* their rule already existed.
- Prose does not bind under reward pressure. One rule was authored and then
  violated by the same agent within minutes; another was violated in the session
  it was written. This is not a comprehension failure you can fix by rewording.
- Read that with the source's own caveat: its analysts tagged the mechanism-vs-prose
  comparison as inferred from absence of recurrence and queued a per-class commit
  scan to confirm it. Direction is well-grounded; the cleanliness of the contrast
  is not yet verified.
- Do not conclude "a shorter instructions file gets obeyed more". The forensics
  explicitly decline that causal claim and attribute non-compliance to incentives
  rather than volume. What the size numbers support is cost, not disobedience.
- A useful remedy ordering, taken from the project's round-two protocol: if the
  failure is mechanically checkable, write the check and ship it green in the same
  change; if it is a genuine judgement call, one budgeted line of prose; if it is
  driven by incentives or by a capability the agent should not have, change the
  structure; if none of those, record the observation and do nothing. The fourth
  branch matters — an unactionable lesson written as a rule is pure token load.
- Evidence is only as clean as the environment that produced it. Validating
  against a hand-patched environment proves the mechanism and never the artifact,
  and the thing you verified is then not the thing you ship.
- Green checks coexisted with a broken system routinely: a CI run reported success
  while four assertions had timed out; a schema linter passed a field the live
  admission webhook rejected; a fixture test that skipped when its fixture was
  absent covered nothing for an entire phase while reading as coverage.
- Six of ten workflows were dispatch-only and none triggered on pull requests, so
  the agent effectively chose when to be tested.
- Writing the done-condition as one falsifiable sentence — clean build from
  committed main, a URL returns 200 with a valid cert, zero manual steps — was
  what finally made it visible that no gate anywhere built from scratch.

## Candidate patterns / evidence

- → `prefer-deterministic-controls`: failure classes wired to a fail-closed gate (a pre-dispatch static audit hook, a pre-commit render check) show no recurrence afterwards, while 8 of 12 tracked classes recurred after a prose rule was written for them — the source's strongest claim, and one it flags as inferred from absence rather than confirmed by a per-class scan.
- → `verify-from-clean-state` (new): 6+ items were declared done, proven or validated in one run and 0 were validated from a clean build; the project's own fix was to name the missing status rather than claim the work — "pending clean-build verification".
- → `capture-lessons` (counter-evidence): 45 retrospectives produced 152 rule candidates, ~51 adopted, with no measured reduction in the behaviours they targeted; round two retired rule-writing as the default retrospective output in favour of a remedy-ordering protocol.
- → `agents-md-hygiene`: the instructions file went 243 → 1,347 lines in 15 days over 48 revisions, settling at 748, for a floor of roughly 15,200 instruction tokens loaded per session before any project code — and a same-day refactor that moved rule text into 20 detail files reduced what loads without reducing what exists.
- → `demand-evidence-not-summary`: a CI run reported success while four of its assertions had timed out, and "phase 1 reproducibly green" was claimed at least four times, each time contradicted by the next run.
- → `define-done-first`: "done" is a claim, not a status, until an externally checkable artifact converts it — a gate run id and a behavioural check on the committed artifact.
- → `spec-first`: all four standing blockers were instances of layer boundaries the founding spec never named; the entire specification of one seam was a single sentence saying the next tool takes over from there.
- → `give-a-runnable-check`: six of ten workflows were dispatch-only and none ran on pull requests, so no automatic gate ever built the platform from committed source; also two ways a check fails quietly — scanning only the directory where the class was first seen, and a test present but never enumerated by the runner.
- → `comprehension-debt`: a fixture test that skipped when its fixture was absent covered nothing for an entire phase while reading as coverage.
- → `intent-ledger`: a burndown document marked every item done at the same commit where the handoff file said nothing was done, so a fresh session's belief depended on which file it opened first.
- → `stale-scaffolding`: 21 skills totalling 5,415 lines, ten archived in round two; four existed only to work around sandbox limits, and one was imported from another repo carrying assumptions this environment never met.
- → `agentic-manual-testing`: a static schema check passing is not the live admission controller accepting, and a kind-cluster pass is not a real-cloud pass — one class was invisible to the integration harness because the harness exercised different content than was committed.
- → `calibrate-autonomy`: the corrective direction chosen was short, scoped, attended sessions with a machine-verified exit condition until the clean-build gate passes twice, then re-expanding autonomy — autonomy gated on verification existing rather than on task type.

## Other-use-case material

- **Flag: long-running / unattended.** Sixteen overnight runs with a protocol
  mandating a floor of 20–30 pull requests per run; throughput competed with
  verification and throughput won, producing documented drift between a run's
  stated envelope and its outcome. The protocol was eventually paused outright.
  The interactive analogue is real and worth remembering: any instruction that
  rewards volume will outrun an instruction that asks for proof.
- **Flag: multi-agent.** A false premise about what the environment allowed was
  baked into fanned-out subagent briefs and propagated into three plans and
  fourteen reviews before anyone checked it. Interactive analogue: ground the
  framing in an artifact that exists before delegating on it.
- **Flag: multi-agent.** Subagent isolation broke twice, once through
  absolute-path writes escaping a worktree and once through a branch command
  moving the main worktree's head.
- **Flag: governance / process.** The retrospective pipeline itself — 45 retros,
  152 rule files, 49 ADR drafts, 42 skill specs — was described as the project's
  most productive subsystem, which is a warning about where effort goes when the
  product is not moving.
- **Flag: infrastructure-specific.** Rotating ephemeral cloud accounts against
  GitOps needing durable values, provider version pinning, and a long tail of
  Kubernetes-specific defect classes. Real, but not transferable practice.
