---
id: osmani-2026-dont-outsource-learning
title: Don't Outsource the Learning
author: Addy Osmani
date: 2026-05-16
url: https://addyosmani.com/blog/dont-outsource-learning/
access: direct
accessed: 2026-08-29
scope: interactive
relevance: high
pass: distilled
patterns: [hypothesis-before-prompting, explanation-before-code, learning-mode-when-out-of-depth, re-derive-by-hand, ask-agent-to-teach, review-agent-diffs, cognitive-surrender, ship-and-learn-metrics]
---
## Summary

This is the solo counterpart to Osmani's cognitive-surrender piece: just you and
a model, where the model is faster so you stop competing on comprehension. He
summarises converging research — an Anthropic RCT where AI-assisted learners
matched the control group on speed but scored 50% vs 67% on comprehension, with
copy-paste users under 40% and conceptual-question users above 65%; MIT's EEG
study where 83% of LLM users could not quote a line they had just produced; and
a CHI 2026 finding that having the LLM available at the start anchored the whole
problem framing and worsened decisions even when the human did the rest. His
diagnosis is that tools default to closing tasks, and the friction they removed
was where the learning lived. Delegation is fine for boilerplate and throwaway
scripts, but breaks down when something fails, when the model is confidently
wrong, when foundations change, and away from well-trodden problems.

## Takeaways for our use case

- Write two or three sentences on what you think the problem is before asking,
  then use the model's answer to test that theory rather than replace it.
- In unfamiliar territory make your first prompt "explain how this works, the
  alternatives, and the tradeoffs", and ask for code only after the concepts.
- Order of operations matters: reaching for the model first lets it frame the
  problem, and that anchoring degrades decisions even if you do the rest.
- Turn on a Socratic/learning mode when out of your depth — it feels slower, and
  that is the point; it is not only a feature for students.
- Delegate freely where the answer is disposable (boilerplate, glue code, a CI
  script you will never reopen) and reserve the deliberate posture for code you
  will have to debug, migrate, or defend.
- Occasionally re-derive by hand a piece the model wrote, as a calibration check
  on how much capability you have quietly lost.
- After the agent does something clever, ask what concepts it used and what you
  would need to read; one extra prompt changes what the session leaves you with.
- Treat agent output like a junior's PR — read it, critique it, push back — and
  do not merge on green tests alone.
- End sessions with an honest question: did I learn anything, or just close
  issues? Ship and learn are two separate metrics and only one gets asked about.

## Candidate patterns / evidence

- → hypothesis-before-prompting: form and write a hypothesis before requesting a
  fix, and use the model to test it; supported by the CHI finding that early LLM
  access anchors the problem framing and measurably worsens decisions.
- → explanation-before-code: ask for explanation, alternatives and tradeoffs
  first; within the same AI group, conceptual-question users scored above 65%
  while copy-paste users scored under 40%.
- → learning-mode-when-out-of-depth: Socratic modes that stop and ask you to
  write code exist across vendors and are dismissed as student features; Osmani
  says use them for real work when learning.
- → re-derive-by-hand: recreating from scratch something the model wrote is
  offered as the calibration check on retained skill.
- → ask-agent-to-teach: one follow-up prompt asking what concepts were used and
  what to read converts a closed task into retained understanding.
- → review-agent-diffs: same standard as a junior engineer's PR — read, critique,
  push back, and don't merge just because tests pass.
- → cognitive-surrender: this piece is explicitly framed as the solo version of
  that loop, where the model's output replaces your own view.
- → ship-and-learn-metrics: closing a session by asking whether you learned
  anything, and treating months of "just closed issues" as accruing debt.

## Other-use-case material

None — the piece is entirely about a single human working with a single model.
