---
id: every-2026-07-16-case-against-skills
title: The Case Against Skills
author: Laura Entis
date: 2026-07-16
url: (Gmail export, local mbox)
access: gmail
accessed: 2026-08-29
scope: interactive
relevance: high
pass: distilled
patterns: [skill-audit, stale-scaffolding, prove-the-skill-helps, cross-model-review]
---
## Summary

The argument is that most trending agent skills no longer help, because frontier
models have absorbed the capability those skills were written to patch. Extra
instructions then fight the model's training, invite mistakes, and inflate token
cost. The cited benchmark tested 49 public software-engineering skills: 39 had no
effect, three made results worse, only seven helped — and the ones that helped
supplied specialised knowledge the model could not have. The durable skills are
the ones carrying private context: your taste, your company's template, internal
data, or an exact required sequence. An audit is proposed (keep private-context
skills, retest compensating ones, retire the rest), plus a four-step method for
proving a skill works: golden examples, codify what's good, an LLM judge on one
narrow metric, and a with/without sanity check. A separate item describes a
review skill that hands an agent's diff to a different model until no findings
remain.

## Takeaways for our use case

- Assume any instruction you wrote to compensate for a model quirk has a shelf life, and retest it at each model release rather than carrying it forward.
- Keep only instructions carrying information the model could not know — your preferences, private data, a required sequence, a specific template.
- Prove a skill earns its place before keeping it: run the same input with and without it and compare.
- Build the comparison on a golden set of real examples of good output, then codify what you like about them into the instructions and re-run the same input to check you are moving toward the set.
- Break a subjective "does it look right" judgement into one narrow measurable metric at a time and delegate that grading to a model judge trained on good and bad examples.
- Skill text is not free: the benchmark found many skills increased compute without improving results, the worst by 451 percent.
- Have a second, different model review the diff before merge, then let the first model verify each finding against the code, fix only what the change introduced, rerun tests, and repeat until no actionable findings remain.
- Constrain that review loop: tell it to stop and ask before any fix that would expand the original task.
- Third-party skills are only worth adopting if their author actively updates and prunes them.

## Candidate patterns / evidence

- → skill-audit: keep skills that supply private context or a company workflow, retest those compensating for a model weakness, retire those that don't demonstrably improve results.
- → stale-scaffolding (anti-pattern): skills the previous model needed to avoid mistakes actually harmed the newer model's performance — compared to 2023-era prompt hacks that became unnecessary a model generation later.
- → prove-the-skill-helps: golden data set of 15–20 real good outputs, narrow LLM-judge metric (letter spacing), and a with/without sanity check.
- → cross-model-review: an agent's changes are packaged and sent to a different model for review, and the loop repeats over hours until no snags remain, replacing the human's bug-hunting pass.
- → distrust-agent-self-report (supporting): the value of the review skill is that a separate model, not the author of the code, finds the problems.

## Other-use-case material

- The nine-hour overnight run in which one model built a feature across a back end and three clients, self-reviewing via the review skill until it produced a mergeable PR, is a long-running-agent story; flag as `scope: long-running`. The review-loop mechanic itself transfers to an interactive session.
