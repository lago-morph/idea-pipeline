---
id: spec-first
title: Write the spec before the prompt
type: pattern
status: adopted
durability: structural
scope: interactive
tools: both
category: planning
verified: 2026-08-29
models: [claude-5, gpt-5.6]
confidence: medium
sources: [osmani-2026-good-spec, every-2026-08-04-think-like-designer, osmani-2026-agentic-engineering, osmani-2026-new-sdlc-vibe-coding]
related: [plan-before-code, define-done-first, intent-ledger]
aliases: []
---
# Write the spec before the prompt

**Use when:** building a feature rather than making an edit — anything an agent could
plausibly interpret two ways.

**Do:**
- Start from a short brief, have the agent draft the spec, then correct it yourself
  before any code exists.
- Cover commands, testing, structure, code style, git workflow, and boundaries in
  three tiers (Always / Ask first / Never).
- Write the non-goals and failure modes explicitly — that is where your context gets
  encoded.
- Add what the model cannot infer: schema quirks, library pitfalls, version
  workarounds.
- Keep the spec in version control; update it when a decision changes.
- Size the detail to the task; a full PRD for a one-line change adds confusion.

**Why:** implementation has compressed while requirements, architecture and
verification have not, so spec quality is the bottleneck. An agent left to guess
decides silently, and its guess becomes the code.

**Don't, when not:** throwaway prototypes and spikes you intend to discard.

**Evidence:**
- [osmani-2026-good-spec] The spec is the source of truth across sessions; GitHub's analysis of 2,500+ agent config files found effective ones cover six areas.
- [every-2026-08-04-think-like-designer] A worked spec with overview, hero scenario, requirements, behavioral rules, non-goals and failure modes — nearly every line encoding what the model could not know.
- [osmani-2026-agentic-engineering] Agentic engineering "starts with a plan": a design doc written before any prompting, and that is the step people skip.
- [osmani-2026-new-sdlc-vibe-coding] Spec quality is the bottleneck because implementation drops to hours while requirements and architecture stay slow judgment work.

**Tool notes:** Claude Code: draft the spec in read-only Plan Mode so nothing is written while it is still wrong.
