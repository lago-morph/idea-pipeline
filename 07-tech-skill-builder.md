# Spec: Tech Skill Builder

**Post-Phase 6 project (enters ideas pipeline queue)**
**Repo:** new — to be created

---

## What It Is

An agent pipeline that ingests official documentation, web content (tips, sample code,
use cases, forum discussions), and community resources for any technology, then distills
that into a hierarchical SKILL.md with progressive disclosure. The result is a rich,
up-to-date skill an agent can load progressively as it works with that technology —
only loading the depth it needs, when it needs it.

This solves a core problem with agentic coding: agents know general programming patterns
but not the specific idioms, gotchas, and best practices of a particular library or
platform version.

---

## Current State

- Does not exist as a system
- The ingestion pipeline shape is proven by `conference-summaries`: multi-source
  discovery → extraction → AI processing → structured output
- The output format (progressive SKILL.md) is defined by the Phase 1/3 skills work
- `code-knowledge-base` contains research on knowledge base design that applies here
- The agent-os architecture references this as "the vendor documentation companion
  project" (Workstream F3) — the Tech Skill Builder is the generalized version of that

---

## Recommended Design

**Input sources per technology:**
- Official documentation website (crawled and versioned)
- GitHub repo README and docs/ directory
- Stack Overflow and community forums (top-voted Q&A)
- Conference talks (conference-summaries pipeline)
- Blog posts and tutorials from recognized practitioners

**Processing pipeline:**
1. Discovery agent: find and rank sources for a given technology
2. Ingestion agent: extract content, normalize format, strip noise
3. Distillation agent: identify core concepts, common patterns, gotchas, best practices
4. Skill builder agent: structure into progressive SKILL.md (root summary + detail pages)
5. Review gate: human or automated review before publishing to ai-skills

**Output:** SKILL.md with structure:
- Root: 100-token summary + trigger description
- Quickstart: common patterns and minimal working examples
- Reference: API/config details on demand
- Gotchas: known issues, version-specific behaviors
- Integration: how this technology connects to other tools in the stack

---

## Open Questions

- How is the technology list maintained — manual, auto-detected from repos, or both?
- How often are skills refreshed when a technology releases a new version?
- How does the pipeline handle technologies with rapidly changing APIs vs stable ones?
- Should skills be generated on demand (an agent requests a skill) or proactively
  for a curated list of technologies?

---

## Recommended Additions

- **Version tracking**: each skill is tagged with the technology version it covers;
  the pipeline detects new versions and triggers re-generation
- **Quality scoring**: after a skill is used by agents, feedback (did the agent succeed,
  did it ask follow-up questions that should have been in the skill?) feeds back into
  skill improvement
- **Confluence with conference-summaries**: technologies appearing prominently in
  conference talks get skills automatically generated — the conference data signals
  what's worth building skills for

---

## What Needs to Happen Next

1. Define the target technology list (start with the stack in agent-os: LiteLLM, ARK,
   Crossplane, Knative, OPA, Langfuse, etc.)
2. Adapt the conference-summaries ingestion pipeline as the base
3. Build the distillation agent (the hardest part — converting raw docs to a good skill)
4. Pilot with one technology end-to-end before building the full pipeline

---

## Dependencies

**Depends on:** Phase 6 (skills management layer to publish into), Phase 5 (factory
builds and runs the pipeline), conference-summaries (ingestion pattern)
**Enables:** `agent-os` (vendor doc Knowledge Base), every other project (richer agent skills)
