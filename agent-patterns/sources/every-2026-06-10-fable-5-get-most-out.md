---
id: every-2026-06-10-fable-5-get-most-out
title: How to Get the Most Out of Fable 5
author: Laura Entis
date: 2026-06-10
url: (Gmail export, local mbox)
access: gmail
accessed: 2026-08-29
scope: mixed
relevance: high
pass: distilled
patterns: [delegate-with-definition-of-done, frontload-context, match-model-to-task, plan-before-build, verify-in-real-environment, batch-related-changes, build-tools-for-cheaper-models]
---
## Summary

A playbook for using a high-capability, slow, expensive model well. The framing:
stop prompting it like a smart-but-literal model and start briefing it like a
capable colleague — organised context, a well-defined goal, a clear definition of
done, and a way to verify — then step aside and review the finished result rather
than iterating turn by turn. A task qualifies only if you can supply all four and
the stakes justify the cost. Four worked examples with copyable prompts follow:
diagnosing why a Claude Code skill kept failing and building a CLI tool so cheaper
models can do the job afterwards; producing a go-to-market analysis that tests
assumptions against data instead of summarising internal consensus; batching two
days of Slack feedback into thirty non-conflicting product fixes; and rebuilding a
product from its original spec. Cost and latency mean quick edits and
brainstorming still belong to faster models.

## Takeaways for our use case

- Only delegate a whole task when you can give the agent organised context, one
  clear goal, and an explicit statement of what "done" and "good" look like —
  otherwise stay in a tighter loop with a cheaper model.
- With a strong model the failure mode shifts: because you are no longer correcting
  every turn, wrong or stale context and conflicting goals propagate all the way to
  the wrong conclusion.
- Ask for a specific artifact and shape (a ranked list of ten, evidence per
  recommendation, flagged assumptions) rather than "make a plan"; the vague ask
  gets you a summary of what you already agreed.
- Ask the agent to flag source conflicts, stale rules and single-source conclusions
  it wants you to verify before you act on them.
- Say "make a plan first, then build" in the prompt — all the worked prompts open
  that way.
- Make it verify in the environment where the thing actually runs: the stuck bug
  was only fixed once the model was told to run the app locally and watch it,
  after a code-only reading produced a confident wrong fix.
- Batch related fixes into one run and ask the agent to check they don't conflict,
  instead of shepherding ten small tasks separately.
- Point the expensive model at your session logs to diagnose why a workflow keeps
  failing, then have it build the tool or skill that fixes it — and let cheaper
  models use that tooling from then on.
- Ask for a close-out report: what changed, what was skipped, what needs review,
  and how the work was verified.
- Match the model to the task — the source is explicit that quick edits, small
  bugs and back-and-forth brainstorming remain better on faster, cheaper models.

## Candidate patterns / evidence

- → delegate-with-definition-of-done: good candidate tasks are defined as those
  with deep context, a well-defined goal, and a clear definition of what done
  looks like — plus stakes that justify the cost.
- → frontload-context: the reframing is that work moves from iterating mid-task to
  assembling context and directives up front, then reviewing only at the end.
- → match-model-to-task: explicit guidance that the slow expensive model suits
  large delegable jobs, while small edits and brainstorming stay on cheaper models.
- → plan-before-build: every published prompt in the piece instructs the model to
  make a plan first and then build.
- → verify-in-real-environment: the genogram bug resisted a code-only fix and was
  solved once the model ran the app locally and observed it; prompts ask for
  testing in the environment where it will be used.
- → batch-related-changes: thirty fixes made in one batch with the agent checking
  the changes did not interfere, instead of ten separate review cycles.
- → build-tools-for-cheaper-models: diagnosing the PowerPoint skill's root cause
  produced a CLI tool for targeted edits, explicitly so cheaper models could use
  the infrastructure later.

## Other-use-case material

- The podcast highlights (Mike Krieger) are about overnight, unattended runs —
  briefing the model at the end of the day, the model writing workarounds when a
  service goes down — `scope: long-running`, not interactive.
- Krieger's verification stack for delegated work (regression tests on known
  workflows, video captures so the model can catch animation glitches, mock
  backends for what can't be tested live, bug-to-PR from Slack) is builder/
  long-running practice but worth linking from any verification pattern.
- Kieran's next layer — an agent pulling Slack feedback on a schedule, scoring it
  against a vision document and personas, and presenting candidates for approval —
  is a scheduled long-running loop.
- Model-specific pricing and availability claims are dated to June 2026 and should
  not be carried into a pattern page.
