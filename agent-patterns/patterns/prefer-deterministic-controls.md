---
id: prefer-deterministic-controls
title: Prefer deterministic controls to prose rules
type: pattern
status: adopted
durability: structural
scope: interactive
tools: both
category: compounding
verified: 2026-09-13
models: [claude-5, gpt-5.6]
confidence: high
sources: [cheapcode-2026, lagomorph-2026-k8s-forensics]
related: [capture-lessons, give-a-runnable-check, agents-md-hygiene, unreviewed-code]
aliases: []
---
# Prefer deterministic controls to prose rules

**Use when:** you are about to write a rule into AGENTS.md / CLAUDE.md to stop a
failure you have seen more than once.

**Do:**
- Decide first whether it is a local defect or an instance of a class. Only a class
  earns a mechanism; that judgement stays yours.
- For a class, prefer the mechanism that makes the failure unexpressible — a type, a
  closed vocabulary, a narrowed interface — over one that catches it after.
- Where you can't eliminate it, automate detection: a lint, a test, a check on the
  commit path, so it runs without anyone remembering to.
- Keep the prose rule as a pointer to the mechanism, not as the enforcement.
- Before shipping something you did not read, name what did check it. "Nobody read
  it" is survivable; "nobody read it and nothing checked it" is the actual failure.

**Why:** a written rule is probabilistic guidance. At the volume an agent produces, a
rule followed most of the time is broken routinely, and the violations arrive faster
than anyone reads them. A mechanism fails closed; a rule fails silently.

**Don't, when not:** the failure is local, the mechanism costs more than the
failures it prevents, or you can't yet state the rule precisely enough to encode
it. Budget for the mechanism's own cost: a new check usually needs its false
positives fixed and its pre-existing findings triaged before it can gate
anything, and a gate binds indiscriminately — when it fires on correct work,
scope an exemption with a documented removal trigger rather than widening it.

**Evidence:**
- [cheapcode-2026] a 12-week single-engineer case study argues review- and convention-based controls saturate under agentic velocity and must become types, static analyses and commit gates; of its coded incidents, 35 added detection, 20 removed a class by construction.
- [lagomorph-2026-k8s-forensics] on one six-week project, failure classes wired to a fail-closed gate stopped recurring while 8 of 12 tracked classes recurred after a prose rule had been written for them — the source's own analysts flag this as inferred from absence rather than confirmed per class.
- [lagomorph-2026-k8s-forensics] the cost side, from the same project: a fail-closed gate went red two hours after being written over an unrelated comment edit, one lint needed false-positive fixes plus triage of 26 pre-existing findings before it could gate, and two hooks obstructed correct work.
- [own] 2026-09-13 prose in AGENTS.md, skills and ADRs accretes and loses effectiveness, and different models interpret the same prose differently; deterministic checks are more stable and more effective once you are past casual agent use.
**Tool notes:** Claude Code / Codex: a hook or pre-commit gate runs whether or not the
agent cooperates; a rule in the instructions file relies on it obeying that file.
