---
id: osmani-2026-good-spec
title: How to write a good spec for AI agents
author: Addy Osmani
date: 2026-01-13
url: https://addyosmani.com/blog/good-spec/
access: direct
accessed: 2026-08-29
scope: mixed
relevance: high
pass: distilled
patterns: [spec-first, plan-before-code, spec-six-core-areas, three-tier-boundaries, small-reviewable-steps, scoped-context-per-task, self-verification-checklist, spec-as-living-document, right-size-the-spec, tests-as-safety-net]
---
## Summary

A five-principle framework for writing specs that coding agents can actually
act on. Start from a short goal statement and let the agent expand it into a
detailed spec you then correct — using a read-only planning mode so nothing
gets written until the plan is unambiguous. Structure the result like a PRD
covering six areas that a GitHub study of 2,500+ agent files found to matter:
commands, testing, project structure, code style, git workflow, and
boundaries. Keep prompts modular: feeding everything at once triggers the
"curse of instructions", where more directives means worse adherence to each,
so hand the agent one section and one task at a time and refresh context
between features. Build quality control into the spec itself via three-tier
Always/Ask-first/Never boundaries, self-check instructions, and explicit
success criteria. Then iterate — the spec is a living, version-controlled
artifact, not a one-time contract.

## Takeaways for our use case

- Open with a short product brief and have the agent draft the detailed spec;
  review and correct it before any code exists.
- Use a read-only plan mode (Claude Code's Plan Mode) so the agent explores
  and drafts without editing, and ask it to question you about ambiguities.
- Check any spec against the six areas: commands (with flags), testing,
  project structure, code style (one real snippet beats three paragraphs),
  git workflow, and boundaries.
- Write boundaries in three tiers — Always (proceed unasked), Ask first
  (high-impact: schema changes, new dependencies, CI config), Never (secrets,
  vendor dirs, deleting failing tests).
- Give the agent one section of the spec per task; don't mix auth work with
  schema work in one prompt, and start a fresh session between major features.
- For a long spec, have the agent build a summarised table of contents to keep
  in context, pulling full sections in only on demand.
- Instruct the agent to compare its output against the requirement list and
  report which items it did not address.
- Put in what only you know: many-to-many relationships, library pitfalls,
  version-specific workarounds — the agent will not infer these.
- Match spec detail to task complexity; a full PRD for "center this div" adds
  confusion, but an OAuth flow needs one.
- Update the spec whenever a decision changes and re-sync the agent with the
  new version; keep it in version control alongside the code.
- Named pitfalls: vague prompts, dumping unsummarised context, skipping human
  review, and confusing prototyping with production work.

## Candidate patterns / evidence

- → spec-first: the spec becomes the persistent source of truth that anchors
  the agent across sessions and restarts.
- → plan-before-code: Plan Mode restricts the agent to read-only analysis
  until the plan leaves "no room for misinterpretation".
- → spec-six-core-areas: GitHub's analysis of 2,500+ agent config files found
  effective ones cover commands, testing, structure, style, git, boundaries.
- → three-tier-boundaries: Always / Ask first / Never is more effective than a
  flat list of don'ts; "never commit secrets" was the single most common
  helpful constraint in that study.
- → small-reviewable-steps: the four-phase Specify→Plan→Tasks→Implement flow
  breaks work into chunks each implementable and testable in isolation.
- → scoped-context-per-task: the "curse of instructions" means adherence drops
  as directives accumulate, so feed only the relevant spec slice per task.
- → self-verification-checklist: append "review the requirements above and
  mark any not satisfied" so the model audits its own output before you run it.
- → spec-as-living-document: reflect changed decisions back into the spec so
  it stays ground truth rather than drifting into fiction.
- → right-size-the-spec: don't under-spec a hard problem or over-spec a
  trivial one; detail should track task complexity.
- → tests-as-safety-net: success criteria and conformance cases in the spec
  define "done" and give the agent something to iterate against.

## Other-use-case material

- Splitting a spec across specialised subagents (database, API, frontend),
  each with its own context window — builder/multi-agent territory.
- Running 2-3 parallel agents on non-overlapping tasks with shared memory via
  vector DBs and orchestration frameworks — long-running/builder scope.
- LLM-as-a-Judge review agents and RAG-based spec retrieval for very large
  specs.
