# Spec: Batch Job Skill

**Phase 1 of the high-level plan**
**Source repo:** `lago-morph/poc-github-ai-sandbox`
**Output repo:** `lago-morph/ai-skills`

---

## What It Is

A production-grade SKILL.md (with supporting files) that teaches any AI agent how to
use the GitHub-native batch job protocol. The protocol lets an agent submit privileged
work to GitHub Actions runners using only the GitHub MCP server as transport — no direct
cloud credentials, no shell access required. Results come back structured, the job is
restart-safe, and every operation is auditable.

Two skills are in scope:

- **batch-job** — submit one job, poll for results, acknowledge completion
- **task-dag** — claim an issue, plan subagents, schedule successors, merge results

Both exist as implementation-grade specs in `poc-github-ai-sandbox/retrospective/`. This
project converts them into deployable SKILL.md files with progressive disclosure.

---

## Current State

- Protocol is fully specified in `poc-github-ai-sandbox/SPEC.md` (with live-correction annotations)
- Live-validated across 11 of 15 scenarios; 446 tests at ~93% coverage
- `skills/batch-job/` and `skills/task-dag/` exist as directories with SKILL.md specs and Python helpers
- `retrospective/` contains 9 additional skill specs harvested from session 1
- The skills exist but are not yet in the canonical format used by `ai-skills` and `skill-sharing`

---

## Recommended Changes / Additions

- Add a **k8s-infra** command variant to the batch-job command registry (Terraform plan,
  apply, destroy; kubectl apply; Helm install/upgrade) — this makes the skill immediately
  usable for k8-platform Phase 2
- Document **progressive disclosure structure** explicitly: root SKILL.md has summary +
  trigger description; sub-pages for protocol detail, command registry, error handling,
  and examples load on demand
- Add a **health-check skill** derived from the existing `lock-and-sweep` mechanism —
  lets an agent verify the protocol is working before submitting real jobs
- Package the 9 retrospective skill specs into the same format in a single pass

---

## Open Questions

- Should batch-job and task-dag be one skill (loaded together) or two separate skills
  that can be loaded independently? Task-dag implies batch-job, but the reverse isn't true.
- Which of the 9 retrospective skills are immediately usable vs need more work?
- Does the skill need a TypeScript variant (for Codex CLI) or Python-only for now?
- How are secrets (AWS credentials, kubeconfig) referenced in the batch-job command
  registry? Needs to be documented for the k8-platform use case.

---

## What Needs to Happen Next

1. Audit the existing `skills/batch-job/` and `skills/task-dag/` directories against the
   canonical SKILL.md format used in `ai-skills`
2. Write the production SKILL.md for batch-job with progressive disclosure structure
3. Write the production SKILL.md for task-dag
4. Add the k8s-infra command variant to the poc-github-ai-sandbox command registry
5. Copy finalized skills into `ai-skills/skills/` as the canonical location
6. Smoke-test by having an agent use the skill to submit a simple Terraform plan

---

## Dependencies

**Depends on:** `poc-github-ai-sandbox` (source material), `ai-skills` (target format)
**Enables:** k8-platform reset (Phase 2), skills consolidation (Phase 3), agent software
factory (Phase 5)
