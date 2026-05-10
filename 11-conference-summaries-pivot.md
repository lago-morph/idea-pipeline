# Spec: conference-summaries Generalization (Recommended Pivot)

**Post-Phase 6 project (enters ideas pipeline queue)**
**Repo:** `lago-morph/conference-summaries` (pivot of existing project)

---

## What It Is

A pivot of the existing conference-summaries project from a KubeCon-specific data
extraction tool into a general-purpose technology intelligence pipeline. The generalized
system ingests from a wide variety of sources, processes content with AI, and packages
the results as complex, well-organized agent skills with progressive disclosure —
making the output directly consumable by agents rather than just human-readable.

This project becomes the practical implementation of the Tech Skill Builder's ingestion
layer, and the vendor documentation companion project referenced in agent-os (Workstream F3).

---

## Current State

- KubeCon-specific scraper working and validated at scale (KubeCon 2025 North America)
- 67 commits; requirements complete; 4-task architecture (discovery, extraction, AI
  processing, issue resolution) well-designed and documented
- Uses Python with yt_dlp, multi-search-engine discovery, YAML storage
- AGENTS.md and CLAUDE.md exist; uses GitHub Issues for error handling
- JavaScript and Python mix; multi-tool (Kiro, Claude Code, web search)
- Prototype validated; ready for Phase 1 (core extraction) implementation

---

## The Pivot

**From:** Extract KubeCon talk metadata, transcripts, and slides; analyze for trends

**To:** General-purpose technology intelligence pipeline that:
1. Accepts any source type: conference talks, official docs, blog posts, GitHub repos,
   forum threads, YouTube tutorials, academic papers
2. Processes content with AI to extract technology-specific knowledge
3. Packages output as SKILL.md files with progressive disclosure (not just YAML datasets)
4. Publishes directly to `ai-skills` via the LiteLLM skill organizer (Phase 6)
5. Supports the agent-os Knowledge Base (`platform-knowledge-base` RAGStore) as the
   vendor documentation companion project

---

## Recommended Changes to Architecture

- **Add a source adapter layer**: each source type (Sched.com conferences, docs.sometech.io,
  GitHub repos, YouTube channels) has its own adapter; the core pipeline is source-agnostic
- **Change the output format**: instead of YAML datasets, produce SKILL.md files structured
  with progressive disclosure — summary, quickstart, patterns, gotchas, integration examples
- **Add a skill quality gate**: before publishing to ai-skills, a review step checks
  skill coherence, progressive disclosure quality, and trigger description accuracy
- **Add version awareness**: track technology versions and trigger re-generation on
  major/minor releases
- **Keep the existing KubeCon extractor** as one adapter — it's already working and
  demonstrates the pattern

---

## Open Questions

- What source types should be prioritized after conferences? Likely official docs first
  (most authoritative), then GitHub README + docs/, then community content
- How does the pipeline handle content that changes frequently (blog posts) vs
  content that is stable (foundational textbooks)?
- Should the output SKILL.md files be in the same repo as the pipeline, or is `ai-skills`
  always the output destination?
- How does this relate to the Tech Skill Builder spec? They overlap significantly —
  should they be the same project?

---

## Relationship to Tech Skill Builder

These two projects are converging. The distinction is:
- **conference-summaries** is the existing, proven ingestion and processing pipeline
- **Tech Skill Builder** is the broader vision including distillation into skills

The recommended path is to generalize conference-summaries first (it has existing code),
then have it absorb the Tech Skill Builder's distillation layer — making conference-summaries
the unified pipeline rather than creating a separate project.

---

## What Needs to Happen Next

1. Complete the current Phase 1 (core extraction) as planned — don't pivot mid-flight
2. After Phase 1: design the source adapter layer (this is the core architectural change)
3. Design the SKILL.md output format alongside Phase 1/3 of the high-level plan
4. Add the first non-conference adapter (official docs for one technology used in agent-os)
5. Validate the skill quality gate with a human review before automating

---

## Dependencies

**Depends on:** Phase 3 (SKILL.md canonical format), Phase 6 (skills management layer
for publishing), `ai-skills` (output destination)
**Enables:** Tech Skill Builder (generalizes this pipeline), agent-os Knowledge Base
(vendor doc companion project), every project that needs technology-specific skills
