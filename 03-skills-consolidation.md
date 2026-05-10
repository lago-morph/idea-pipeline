# Spec: Skills Consolidation

**Phase 3 of the high-level plan (parallel with Phase 2)**
**Repos:** `lago-morph/ai-skills`, `lago-morph/skill-sharing`, `lago-morph/poc-github-ai-sandbox`

---

## What It Is

Skills are currently scattered across multiple repos in inconsistent states:

- `poc-github-ai-sandbox/skills/` — batch-job and task-dag as specs + Python helpers
- `poc-github-ai-sandbox/retrospective/` — 9 additional skill specs from session 1
- `ai-skills/skills/` — general skill content store (Python + HTML, sparse)
- `skill-sharing/` — distribution tooling (skillctl CLI, Iteration 0 scaffolding)

This project consolidates all skill content into a coherent, canonical library with
consistent format and clear ownership — and prepares that library for handoff to the
LiteLLM skill organizer service in Phase 6.

---

## Current State

- `skill-sharing` is at Iteration 0 (scaffolding works, smoke test passes); Iterations
  1–4 planned but not implemented
- `ai-skills` has a `skills/` directory but minimal documented content
- The `poc-github-ai-sandbox` retrospective contains 9 skill specs with README,
  SPEC.md, and excerpts.jsonl per skill — the most complete skill documentation in
  the portfolio
- The agentskills.io open standard format is referenced by skill-sharing; SKILL.md
  with YAML frontmatter + markdown content is the baseline format

---

## Recommended Changes / Additions

- **Designate `ai-skills` as the canonical content library** and `skill-sharing` as the
  distribution mechanism — clarify this split in both READMEs
- **Import the 9 retrospective skill specs** from poc-github-ai-sandbox into ai-skills
  as the first wave of content, converting them to production SKILL.md format
- **Add progressive disclosure structure** as a standard: every skill has a root SKILL.md
  (summary + trigger, ~100 tokens) with sub-pages for detail (protocol, examples,
  references, scripts) that load on demand
- **Tag skills by domain** (infrastructure, agent coordination, knowledge management,
  writing) to enable filtering by the LiteLLM skill organizer

---

## Open Questions

- Does `skill-sharing` continue as a separate distribution CLI, or does it become
  superseded by the LiteLLM skill organizer in Phase 6? If the latter, how much of
  Iterations 1–4 should still be built?
- Are the 9 retrospective skill specs ready to use as-is, or do they need significant
  additional work?
- What is the right canonical directory structure inside `ai-skills`?

---

## What Needs to Happen Next

1. Inventory: list all skill content across the three repos with current state and format
2. Define canonical SKILL.md format with progressive disclosure structure (aligns with
   Phase 1 output)
3. Convert the 9 retrospective specs from poc-github-ai-sandbox
4. Convert/import the batch-job and task-dag skills (from Phase 1)
5. Update `skill-sharing` README to clarify its role relative to `ai-skills`
6. Tag all skills by domain for Phase 6 handoff

---

## Dependencies

**Depends on:** Phase 1 (establishes canonical format), `poc-github-ai-sandbox` (source material)
**Enables:** Phase 5 (agent software factory needs a skills library to work with),
Phase 6 (skills management needs organized content to manage)
