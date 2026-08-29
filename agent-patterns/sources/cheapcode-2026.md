---
id: cheapcode-2026
title: "Cheap Code, Costly Judgment: A Case Study on Governable Agentic Software Engineering"
author: James C. Davis, Paschal C. Amusuo, Tanmay Singla, Berk Çakar, Kirsten A. Davis
date: 2026-07-01
url: https://arxiv.org/abs/2607.01087
access: direct
accessed: 2026-08-29
scope: interactive
relevance: high
pass: distilled
patterns: [governance-conversion, capture-lessons, keep-work-inspectable]
---

## Summary

**Abstract page only — the PDF/HTML full text was not read.** Everything below
comes from the arXiv abstract, so treat the mechanism as stated-but-unverified
and the details as unknown.

The authors argue that generative AI moves software engineering from a practice
built around scarce implementation effort to one built around abundant cheap
code, which relocates the hard problem: not whether an agent can write useful
code, but whether the architecture, tooling, evidence and feedback loops keep
AI-mediated development inspectable, correctable and maintainable. Evidence is a
first-person case study — one expert engineer, 12 weeks, frontier coding agents,
building a document accessibility remediation system — recorded as 88
contemporaneous field notes plus 420 KLOC of production code and 1.16 MLOC of
tests, lints, docs and agent tooling. From it they propose a middle-range theory
they call *governance conversion*: agentic velocity surfaces recurring
structural failure classes, and engineering judgment sustains velocity by
converting those failures into durable governance mechanisms. Unlike governance
models that derive controls from known obligations, controls here are discovered
from failures only visible during agentic work.

## Takeaways for our use case

- The scarce resource in an agent-driven session is judgment, not code, so
  spend the human's attention on what makes the work checkable rather than on
  producing more output.
- Treat a recurring failure in agent output as a signal to build a durable
  control (a lint, a test, a standing rule), not as a one-off correction.
- Expect the controls you actually need to be undiscoverable up front: they
  emerge from working with the agent at speed, which is an argument for a
  capture habit rather than an up-front rulebook.
- Study shape matches ours closely (single expert engineer + frontier agents on
  a real system over weeks), so its claims are worth citing — but a single
  first-person case study with a proposed theory is weak evidence for any
  specific practice.
- **Can claim from the abstract:** the governance-conversion framing, the study
  design and scale, the direction of the argument.
  **Cannot claim:** any concrete practice, tool, prompt, guardrail, metric or
  failure taxonomy — the abstract names none. Anything specific needs the full
  text before it becomes an Evidence line.

## Candidate patterns / evidence

- → `governance-conversion`: names the process by which failure classes surfaced
  by fast agentic implementation get converted into durable governance
  mechanisms that then sustain velocity.
- → `capture-lessons`: the paper's controls are *discovered from failures*
  during agentic work rather than derived from known obligations, which is the
  research-side case for a retro/inbox habit.
- → `keep-work-inspectable`: frames the central engineering problem as
  organizing architecture, tools, evidence and feedback loops so AI-mediated
  development stays inspectable, correctable and maintainable.

## Other-use-case material

- The paper is pitched partly at software-engineering *research* and at
  organizational governance models; that framing is out of scope here and only
  the practitioner-side conversion loop transfers.
