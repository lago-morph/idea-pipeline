# Lagomorph Labs — High-Level Execution Plan

## Intent

Six phases of foundational work, then dynamic replanning via the idea pipeline. Each phase
delivers something that makes the next phase more capable. Phases 1–3 have parallel tracks.
After phase 6, the idea pipeline drives scheduling — this document becomes an input artifact,
not the authority.

---

## Phase 1 — Batch Job Skill (Execution Substrate)

Formalize the `poc-github-ai-sandbox` batch-job protocol as a production SKILL.md with
progressive disclosure. This gives any agent a standardized, reusable way to submit
privileged work (Terraform, k8s operations, cloud provisioning) to GitHub Actions runners
and receive structured results — without needing direct cloud access or stored credentials.

This is the mechanical layer everything else stands on.

**Repo:** `lago-morph/poc-github-ai-sandbox` → output to `lago-morph/ai-skills`

---

## Phase 2 — k8-platform Remaining Iterations (2–6)

Replan and execute k8-platform iterations 2–6 using the batch-job skill. The protocol
replaces the ad-hoc GitHub Actions approach used in iterations 0–1. Agents handle the
logic; the skill handles privileged execution.

Delivers the infrastructure substrate that `agent-os` requires as its baseline.

**Repo:** `lago-morph/k8-platform`
**Depends on:** Phase 1

---

## Phase 3 — Skills Consolidation (parallel with Phase 2)

Inventory all skill content scattered across repos: the retrospective skill specs in
`poc-github-ai-sandbox`, content in `ai-skills`, distribution tooling in `skill-sharing`.
Consolidate into a canonical, consistently formatted, discoverable library. The LiteLLM
skill organizer service (Phase 6) will manage this library at scale; Phase 3 prepares
the content for that handoff.

**Repos:** `lago-morph/ai-skills`, `lago-morph/skill-sharing`, `lago-morph/poc-github-ai-sandbox`

---

## Phase 4 — Ideas Pipeline

Design and build the system for capturing, staging, and scheduling all work. The ideas
captured in this session are early input; full idea capture and system design happen in
this phase. The pipeline becomes the scheduling backbone for everything after Phase 5 —
replacing ad-hoc planning with a queue that the agent factory can pull from.

**Repo:** new — to be created
**Depends on:** Phase 3 (skills to work with), Phase 1 (execution substrate)

---

## Phase 5 — Agent Software Factory

Build the multi-agent development pipeline: work item in → agents spec, prototype,
implement, test, and iterate → working software out. Feedback loops return results to
the idea pipeline. Human intervention is minimal and explicit (approval gates, not
constant hand-holding).

This is what makes the rest of the portfolio feasible within real-world token and
time constraints. Without it, every project requires manual coordination of every session.

**Repo:** new — to be created
**Depends on:** Phases 1, 3, 4

---

## Phase 6 — Structured Skills Management

Integrate the LiteLLM skill organizer service as the managed layer for the growing skills
library. This is required before serious `agent-os` implementation — agents need
discoverable, well-organized, progressively disclosed skills to work effectively at scale.
The output of the Tech Skill Builder and the Agent Software Factory feed into this layer.

**Repo:** new or extends `lago-morph/skill-sharing`
**Depends on:** Phases 3, 5

---

## After Phase 6

Replan using idea pipeline output. Dynamic scheduling takes over from this document.
`agent-os` implementation, Tech Skill Builder, conference-summaries generalization,
browser history intelligence, writing assistant, session analyzer, and all other
identified projects enter the queue and are executed by the agent software factory.
