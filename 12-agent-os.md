# Spec: agent-os (Agentic Execution Platform)

**Post-Phase 6 project — treated as one project for dependency tracking**
**Repo:** `lago-morph/agent-os`
**Implementation detail:** will be broken down into components (40+) in a separate
spec-development effort after the prerequisite phases are complete.

---

## What It Is

A full agentic execution platform that runs AI agents as governed, observable,
policy-controlled Kubernetes workloads. Every LLM call, MCP call, A2A call, and
outbound HTTP flows through a single chokepoint (LiteLLM) with OPA policy enforcement,
audit to OpenSearch, and tracing to Langfuse. Agents are declared as Kubernetes CRDs,
sandboxed with gVisor or Kata, and their capabilities governed by a layered CapabilitySet
model. A self-management agent (HolmesGPT) and a self-improvement agent (Coach) run
on the platform.

The architecture is fully documented in `architecture-overview.md` (1,509 lines, 26
ADR candidates). This spec treats the entire platform as one project for dependency
purposes.

---

## Current State

- Architecture-only repository (2 commits)
- Complete architecture document with 6 workstreams, 40+ components, dependency graph
- Architecture backlog documents deferred design decisions, rejected alternatives,
  and evolution paths
- No implementation has started
- The document explicitly states: "Implementation will be done by AI agents. The agent
  topology is a separate conversation, taken up after this architecture is solid."

---

## What the Architecture Requires Before Implementation

1. **k8-platform complete** — the architecture's baseline assumptions (ArgoCD, Grafana,
   Keycloak, Crossplane v2, ESO, cert-manager) are exactly what k8-platform delivers.
   agent-os cannot be installed without this substrate.
2. **Skills management operational (Phase 6)** — agents implementing 40+ components
   need rich, organized skills for the technologies involved
3. **Agent software factory (Phase 5)** — the factory is the implementation machinery
4. **Vendor documentation companion project** — the architecture explicitly references
   this as a separate project; conference-summaries generalization fills this role

---

## Key Architectural Decisions (for dependency tracking)

- **Execution substrate**: every LLM/MCP/A2A call through LiteLLM; non-LiteLLM HTTP
  through Envoy egress proxy; no other paths to external services
- **Policy**: OPA is the policy engine (RBAC is floor; OPA may raise floor per-decision)
- **Agent lifecycle**: ARK operator manages agents declared as CRDs in Sandboxes
- **Memory**: Letta, declared via ARK Memory CRD, backed by Postgres + OpenSearch
- **Observability**: OTel → Tempo + Langfuse correlated by trace_id
- **CI/CD**: GitHub Actions only for v1.0; agent-platform CLI is the integration surface
- **Knowledge Base**: `platform-knowledge-base` RAGStore — separate primitive available
  to any agent; seeded by the vendor documentation companion project
- **Self-management**: HolmesGPT runs as a Platform Agent from day one
- **Self-improvement**: Coach Agent observes traces, proposes changes via PR

---

## First Components to Implement (no internal dependencies)

Per the architecture's dependency graph, these can start immediately once the substrate
and skills are in place:
- A11 (OpenSearch)
- A13 (Tempo + Mimir)
- A14 (HolmesGPT — installed early so it can observe the platform being built)
- A7 (OPA / Gatekeeper)
- B3 (OPA policy framework)

---

## Open Questions (from architecture backlog)

- CapabilitySet layering semantics (merge vs replace per field type)
- Multi-tenancy onboarding flow details
- LiteLLM skill organizer capabilities in OSS vs enterprise
- Specific agent profiles and compositions to ship in the profile library
- Agent topology for the implementation team (the factory)

---

## What Needs to Happen Next

1. Phases 1–6 of the high-level plan complete (substrate + factory + skills)
2. A separate spec-development effort breaks agent-os into implementable components
   with the agent software factory's spec-agent role
3. Implementation starts with foundation components (A11, A13, A14, A7, B3)
4. HolmesGPT goes in early to observe the rest of the build

---

## Dependencies

**Hard prerequisites:**
- `lago-morph/k8-platform` (infrastructure baseline — must be complete)
- Phase 6 (skills management — required before digging in)
- Phase 5 (agent software factory — required for efficient implementation)

**Companion projects:**
- `lago-morph/poc-github-ai-sandbox` (implementation execution protocol)
- `lago-morph/conference-summaries` (vendor documentation companion project)
- `lago-morph/ai-skills` + `lago-morph/skill-sharing` (skills layer)
- `lago-morph/code-knowledge-base` (Knowledge Base research)

**Enables:** everything — agent-os is the production platform on which the Platform
Agents for writing assistant, Tech Skill Builder, and all other projects eventually run
