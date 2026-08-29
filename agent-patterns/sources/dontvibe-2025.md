---
id: dontvibe-2025
title: "Professional Software Developers Don't Vibe, They Control: AI Agent Use for Coding in 2025"
author: Ruanqianqian Huang, Avery Reyna, Sorin Lerner, Haijun Xia, Brian Hempel
date: 2025-12-16
url: https://arxiv.org/abs/2512.14012
access: direct
accessed: 2026-08-29
scope: interactive
relevance: high
pass: distilled
patterns: [control-not-vibe, match-task-to-agent, keep-engineering-standards]
---

## Summary

**Abstract page only — the PDF/HTML full text was not read.** The findings below
are as the authors summarize them; none of the underlying observations, quotes
or counts behind them were available.

An empirical study of how experienced professional developers actually use
coding agents, combining field observations (N=13) with qualitative surveys
(N=99). Against the promise that agents let developers delegate wholesale and
build software purely from natural language, the authors find that experienced
developers value agents as a productivity boost but deliberately keep their own
agency over software design and implementation. The stated reason is insistence
on fundamental software quality attributes; they use their expertise to run
strategies that control agent behaviour. They also report enjoying agents as a
source of *collaboration* rather than complete delegation, and they exercise
judgment about which tasks an agent is suited to. The authors draw out
implications for the value of ordinary software engineering best practices when
working with agents, for task suitability, and for future agentic interfaces and
usage guidelines. Version 2 (Aug 2026) revises the December 2025 original.

## Takeaways for our use case

- The default posture of experienced practitioners is control, not delegation:
  design and implementation decisions stay with the human even when the agent
  writes the code.
- Deciding *whether this task suits an agent at all* is itself a reported skill,
  not a fixed answer — worth making an explicit step before handing work over.
- Existing engineering standards (quality attributes, review discipline,
  established practice) are what make agent use effective, so they are not
  overhead to be dropped for speed.
- Framing the session as collaboration rather than handoff matches what people
  who do this professionally actually report doing.
- **Can claim from the abstract:** the study design (N=13 field, N=99 survey),
  the top-level finding that developers retain agency, that they employ control
  strategies, and that task suitability is judged.
  **Cannot claim:** what the control strategies concretely are, which task types
  were judged suitable or unsuitable, any percentages, or the sentiment detail.
  Those need the full text before becoming Evidence lines for a specific
  practice.

## Candidate patterns / evidence

- → `control-not-vibe`: the paper's headline finding — experienced developers
  retain agency in design and implementation and employ strategies to control
  agent behaviour rather than delegating fully.
- → `match-task-to-agent`: developers exercise judgment about task suitability
  and treat agents as collaborators for some work and not others.
- → `keep-engineering-standards`: control is motivated by insistence on
  fundamental software quality attributes; the authors present ordinary best
  practices as an enabler of effective agent use.

## Other-use-case material

- Implications for "better agentic interfaces" are tool-builder-facing (how
  agent UIs should expose control), not something a single user can act on in a
  session; worth flagging if we ever review agent-harness design.
