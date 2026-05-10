# Spec: Agent Software Factory

**Phase 5 of the high-level plan**
**Repo:** new — to be created

---

## What It Is

A multi-agent development pipeline that takes a work item from the ideas pipeline and
drives it from specification through implementation and testing with minimal human
intervention. Agents do the coding; humans set direction, make key decisions, and
approve at defined gates. The factory is what makes the rest of the portfolio feasible
within real-world token budget and five-hour session constraints.

The pipeline covers: spec → prototype → implementation → testing with simulated usage
→ feedback loop → iteration. At each stage, the appropriate agent (or team of agents)
does the work and hands off results.

---

## Current State

- Does not exist as a system
- The closest existing artifact is the task-dag skill in poc-github-ai-sandbox: a primary
  agent claims an issue, plans subagents, each works on a branch, results merge, successors
  schedule. This is the execution coordination layer the factory builds on.
- The batch-job skill (Phase 1) provides the privileged execution substrate
- The ideas pipeline (Phase 4) provides the work queue

---

## Recommended Design Directions

**Execution substrate:** built on poc-github-ai-sandbox's batch-job + task-dag skills.
Every piece of work the factory does that requires privileged access (running tests,
building containers, deploying to a cluster) goes through the batch-job protocol.

**Agent roles:** at minimum —
- **Spec agent**: interviews the work item, asks clarifying questions, produces a
  structured spec (SPEC.md format from poc-github-ai-sandbox conventions)
- **Implementation agent(s)**: write code against the spec, working on branches
- **Test agent**: runs tests, generates simulated usage scenarios, reports failures
- **Review agent**: checks implementation against spec, flags gaps
- **Integration agent**: merges branches, resolves conflicts, updates the ideas pipeline

**Human gates:** the factory pauses for human input at: spec approval, architecture
decisions above a defined complexity threshold, and final merge. Everything else runs.

**Token budget awareness:** agents track their token usage and checkpoint work before
hitting limits. The task-dag skill's restart-safety handles session interruptions.

**Feedback loop:** test failures and review findings go back to implementation agents,
not to the human — the factory resolves them autonomously up to a configurable depth.

---

## Open Questions

- What is the right primary agent SDK to use? The agent-os architecture chose Langchain
  Deep Agents for v1.0, but the factory may be built before agent-os is deployed.
- How are agent roles coordinated — sequential pipeline, parallel DAG, or dynamic based
  on work item type?
- How does the factory handle work items that span multiple repos?
- What does "simulated usage testing" look like in practice — synthetic prompts, property
  tests, or actual end-to-end scenarios?
- How does the factory decide when a work item is "done enough" to close vs needs more
  iteration?
- What is the human approval UX — GitHub PR review, a simple comment pattern, or
  something in the ideas pipeline UI?

---

## Recommended Additions

- **Stress-testing agent**: after implementation, a separate agent probes completed
  projects for weaknesses, extension opportunities, and integration gaps — feeds findings
  back to the ideas pipeline as new work items
- **Documentation agent**: generates READMEs, blog posts, and tutorial outlines that
  preserve the user's voice rather than sounding AI-generated
- **Skills harvesting**: as the factory implements projects, it automatically extracts
  reusable patterns and proposes new SKILL.md additions to `ai-skills`

---

## What Needs to Happen Next

1. Formalize the task-dag skill (Phase 1/3) — this is the factory's coordination layer
2. Design the agent role taxonomy and handoff protocol
3. Define the human gate interface (what format, what triggers review)
4. Build a minimal version: spec agent + implementation agent + human gate, no test
   or review agents yet
5. Run the factory on a small, self-contained work item from the ideas pipeline as
   the first proof-of-concept

---

## Dependencies

**Depends on:** Phase 1 (batch-job + task-dag skills), Phase 3 (skills library),
Phase 4 (ideas pipeline provides the work queue)
**Enables:** all post-Phase 6 work — agent-os, Tech Skill Builder, conference-summaries
generalization, and every other queued project
