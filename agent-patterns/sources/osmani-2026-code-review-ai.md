---
id: osmani-2026-code-review-ai
title: AI writes code faster. Your job is still to prove it works.
author: Addy Osmani
date: 2026-01-07
url: https://addyosmani.com/blog/code-review-ai/
access: direct
accessed: 2026-08-29
scope: interactive
relevance: high
pass: distilled
patterns: [pr-contract, human-threat-model-review, require-evidence-before-review, small-reviewable-steps, review-agent-diffs, human-owns-the-merge, explain-what-you-merge, manual-exercise-the-feature]
---
## Summary

Osmani's position is that AI did not remove code review, it made the burden of
proof explicit: a change ships with evidence that it works, and review is then
spent on risk, intent and accountability. He contrasts two situations. A solo
developer ships at inference speed, reads only key parts, and leans on strong
automated tests plus hands-on manual exercise of the feature as the backstop —
which only works if the tests were built first. A team faces a volume problem:
larger PRs, more incidents per PR, higher change-failure rates, and review as
the rate limiter. The concrete artefact is a "PR Contract" — what/why, proof it
works, risk tier and which parts were AI-written, and one or two areas where
human input is wanted. Security is the hard line: anything touching auth,
payments, secrets or untrusted input needs a human threat-model review plus a
security tool pass.

## Takeaways for our use case

- Ship changes with evidence attached (tests run, logs, screenshots, a demo),
  not with a promise that it works; no change goes up without one or the other.
- Fill out a four-part contract for your own changes: what/why, proof it works,
  risk tier plus which parts the agent wrote, and where you want scrutiny. If
  you cannot fill it out, you do not understand the change well enough yet.
- Treat auth, payments, secrets, and untrusted-input paths as a category that
  always gets a human threat-model pass and a security scanner, regardless of
  how confident the agent or its tests are.
- Use AI review as a first-pass advisory — closer to spellcheck than an editor —
  and keep the fix decisions with yourself.
- Aim human attention at what the model misses: duplicated existing code,
  maintainability of the approach, and security holes.
- Prompt the agent to actually execute code and run tests after generating, so
  the evidence exists before you look.
- Keep work incremental: small self-contained commits with clear messages act as
  checkpoints, and never commit code you cannot explain.
- Even at high velocity, run the app yourself and click through the feature; if
  you have not seen the code do the right thing, it does not work.
- Skipping review does not remove work, it defers it — build the verification
  system first, then go fast.

## Candidate patterns / evidence

- → pr-contract: the four-item contract (what/why, proof it works, risk + AI
  role, review focus) is framed as a forcing function for author accountability.
- → human-threat-model-review: explicit rule that auth/payments/secrets/untrusted
  input require a human threat model plus a security tool pass before merge,
  with cited rates of security flaws and elevated XSS/logic errors in AI code.
- → require-evidence-before-review: "insist on proof, not promises" — no PR
  without new tests or a demonstration of the change working.
- → small-reviewable-steps: teams enforce smaller, stackable PRs even when the
  agent could do the giant change at once; a 13,000-line AI PR was rejected
  because nobody had bandwidth to review it.
- → review-agent-diffs: reviewing an AI change increasingly means reviewing the
  plan or conversation behind it as much as the diff.
- → explain-what-you-merge: if the author cannot explain why the code works, the
  on-call debugging path is broken; never commit code you can't explain.
- → manual-exercise-the-feature: solo devs still run the app and use the feature
  themselves as the final check on top of tests.
- → human-owns-the-merge: a computer can never be held accountable, so a human
  signs off no matter how much the AI contributed.

## Other-use-case material

- Team/organisational scope (flagged): review as knowledge transfer across a
  team, AI-contribution governance policies, emergent "AI code auditor" roles,
  and tuning shared AI review bots (sensitivity, opt-in/opt-out) to stop their
  output being dismissed as noise.
