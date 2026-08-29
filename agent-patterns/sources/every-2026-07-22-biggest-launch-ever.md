---
id: every-2026-07-22-biggest-launch-ever
title: How Every's Team Used AI to Ship Its Biggest Launch Ever
author: Laura Entis
date: 2026-07-22
url: (Gmail export, local mbox)
access: gmail
accessed: 2026-08-29
scope: interactive
relevance: high
pass: distilled
patterns: [supervise-first-run, delegate-to-cheaper-subagent, frame-and-review-only, codify-your-process-first]
---
## Summary

A newsletter issue rounding up how a small team worked with agents during a
product launch. The reusable core is a Codex playbook from OpenAI staff: pick a
task you already do every week or month, give the agent the files you normally
use plus one example of a finished result, the steps and rules you follow, and
any checklist you use to catch mistakes; supervise the first run; and only once
the agent handles part of the process reliably, save those instructions as a
reusable skill. A second item reports a nine-hour autonomous run that produced
ten mergeable pull requests but burned roughly 20 million tokens for ~5,000
lines changed, much of it on reading context, coordination, and research. The
fix on the next run was one line of instruction telling the model to pick an
appropriate lower-power model and run implementation in a subagent — keeping the
expensive model as, in one participant's phrase, "the CEO of the run."

## Takeaways for our use case

- Start automation from a task you already do repeatedly and can judge, not from a novel one.
- Hand over the same four things you would give a new colleague: the working files, a finished example, the rules and steps, and the checklist you use to catch your own mistakes.
- Watch the first run end to end; only promote the instructions to a saved, reusable skill after the agent has handled that part reliably.
- Add a standing instruction to delegate implementation to a cheaper model in a subagent, chosen by the orchestrating model itself, and keep the expensive model on planning, delegation, and review.
- Expect the token bill to be dominated by context reading, coordination, research, and self-checking rather than by writing code — those are the parts worth pushing down a tier.
- Position yourself at the two ends of the work: frame the problem and review the output, and delegate the middle.
- A screenshot of the relevant conversation plus "can you do this?" is often enough of a brief when the context is all in that thread.
- Do the metacognition first — articulate how you think about the task and what your process is — because agents run well with a codified process and poorly without one.

## Candidate patterns / evidence

- → supervise-first-run: the playbook explicitly puts human supervision on the first run before any part of the procedure is saved as a reusable skill.
- → delegate-to-cheaper-subagent: adding "for all coding tasks use your judgment to decide an appropriate lower-power model and run that in a subagent" cut expensive-model token use, with the model picking different tiers per job.
- → frame-and-review-only: the described ideal is being the top and bottom of the sandwich — frame the problem, review the output, delegate everything in between.
- → codify-your-process-first: agents can run with a process once you've done the upfront work of figuring out how you think about the problem.
- → promote-proven-run-to-skill: instructions become a saved skill only after the agent demonstrates it can follow them reliably (may merge into supervise-first-run).

## Other-use-case material

- The nine-hour unattended run over ~20 changes producing ten PRs is a long-running-agent case; the delegation instruction that fixed its cost applies to interactive sessions too. Flag the run itself as `scope: long-running`.
- A "daily driver" roster of which model each team member uses at which effort level is useful colour on model selection but is not a pattern; it also dates quickly.
