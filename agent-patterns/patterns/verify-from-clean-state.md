---
id: verify-from-clean-state
title: Verify from a clean state
type: pattern
status: candidate
durability: structural
scope: interactive
tools: both
category: review-quality
verified: 2026-09-13
models: [claude-5, gpt-5.6]
confidence: medium
sources: [lagomorph-2026-k8s-forensics]
related: [demand-evidence-not-summary, give-a-runnable-check, prefer-deterministic-controls]
aliases: []
---
# Verify from a clean state

**Use when:** you are about to accept evidence that something works — a green
check, a demo, a passing run — and the environment that produced it is one you or
the agent could have touched.

**Do:**
- Ask what the check ran against: the committed artifact, or a working copy that
  was patched until it passed.
- Make the clean path the default: build, deploy or run from committed source in
  an environment nobody hand-edited, before anything counts as done.
- When the clean run hasn't happened, say that instead of reporting done.
  "Pending clean-state verification" is a status; "done" is a claim.
- Where you can, remove the ability to hand-patch rather than forbidding it. A
  shortcut that stays available gets taken under deadline.

**Why:** a hand-fixed environment proves the mechanism and never the artifact.
The fix lives somewhere the next run won't have it, so the same gap returns
session after session while each individual verification still looks honest.

**Don't, when not:** exploratory work where you are deliberately poking a live
system to learn something — just don't let that session's output become the
evidence you ship on.

**Evidence:**
- [lagomorph-2026-k8s-forensics] across six weeks one project declared 6+ items done, proven or validated against 0 validated from a clean build, and re-fixed the same three gaps by hand across at least four runs because a nightly environment rotation erased each patch.
