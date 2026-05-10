# Spec: Structured Skills Management

**Phase 6 of the high-level plan**
**Repo:** new or extends `lago-morph/skill-sharing`

---

## What It Is

Integration of the LiteLLM skill organizer service as the managed layer for the full
skills library. By Phase 6, the library will contain skills from: the batch-job protocol
(Phase 1), the skills consolidation (Phase 3), and ongoing output from the agent software
factory (Phase 5) and Tech Skill Builder (post-Phase 6). Agents need to discover,
load, and compose skills without context window bloat — the skill organizer provides
this capability at scale.

This is a prerequisite for serious `agent-os` implementation. The agent-os architecture
explicitly states skills are managed by LiteLLM's skill gateway, stored in Git. Phase 6
operationalizes that design decision.

---

## Current State

- LiteLLM has a skill gateway that manages skills stored in Git — this is the target
  infrastructure
- `skill-sharing` has distribution tooling (skillctl) at Iteration 0; its role relative
  to the LiteLLM organizer needs to be clarified
- `ai-skills` will have consolidated content after Phase 3 and ongoing additions from
  the factory
- The agentskills.io open standard format is the common format across all skill content

---

## Recommended Design

- **LiteLLM skill gateway** is the runtime: agents query it, it serves skills based on
  relevance to the current task, loading only what's needed
- **`ai-skills` Git repo** is the source of truth for skill content — the gateway
  reads from it
- **Progressive disclosure** is enforced at the format level: root SKILL.md is the
  100-token summary; sub-pages load on demand; no skill fully inflates the context
  window unless the agent explicitly asks for detail
- **`skill-sharing` / skillctl** may evolve into a contributor tool: developers write
  skills, skillctl validates format and pushes to ai-skills, the gateway picks them up
- **Domain tagging**: skills are tagged by domain (infrastructure, agent coordination,
  knowledge management, writing, language-specific) for routing and relevance filtering

---

## Open Questions

- What exactly is the "LiteLLM skill organizer service" — is this the LiteLLM skill
  gateway as documented in agent-os, a separate standalone service, or a specific
  LiteLLM configuration? This needs to be confirmed before Phase 6 begins.
- What happens to `skill-sharing`'s Iterations 1–4 (not yet built)? Should they be
  built, or does the LiteLLM gateway supersede them?
- How are skills versioned and promoted across environments (dev → staging → prod)?
  This is listed as a deferred decision in the agent-os backlog.
- How does the factory's "skills harvesting" (automatic extraction of reusable patterns)
  feed into the gateway? Does it auto-publish or propose for human review?

---

## What Needs to Happen Next

1. Confirm what the LiteLLM skill organizer service is and what it provides out of the box
2. Design the Git → gateway sync pipeline (likely ArgoCD-driven per agent-os architecture)
3. Define the versioning and promotion model
4. Set up the gateway with the consolidated skills library from Phase 3
5. Validate with a real agent task: agent loads skills from the gateway, completes work,
   skills harvesting extracts a new skill, skill gets published, future agents can use it

---

## Dependencies

**Depends on:** Phase 3 (consolidated skills library), Phase 5 (factory produces new skills),
`lago-morph/k8-platform` (runs LiteLLM as part of agent-os baseline)
**Enables:** `lago-morph/agent-os` implementation (skills management is a prerequisite),
Tech Skill Builder (needs a managed layer to publish into)
