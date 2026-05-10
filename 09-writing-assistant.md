# Spec: Writing Assistant

**Post-Phase 6 project (enters ideas pipeline queue)**
**Repo:** new — to be created

---

## What It Is

An AI-assisted writing tool that helps with idea generation, research, outlining, and
structure — but does not write the piece. The goal is to get to a granular, manipulable
extended outline (with each section, argument, and supporting point independently
movable) before the author writes. The assistant does the scaffolding; the author does
the writing. The output retains the author's voice because the author writes all the
prose.

This applies to blog posts, technical documentation, articles, talks, and READMEs.

---

## Current State

- Does not exist
- In the agent-os model, this is a Platform Agent with a writing-specific CapabilitySet:
  research MCP servers, RAG over writing resources, skills for outline generation
- The knowledge layer (good writing techniques, course syllabi, textbooks, style guides)
  needs to be ingested — the Tech Skill Builder would produce a "writing craft" skill
  from these sources

---

## Recommended Design

**Workflow:**
1. **Idea stage**: author describes a topic; assistant asks clarifying questions,
   suggests angles, identifies the audience
2. **Research stage**: assistant finds relevant sources, summarizes key points,
   identifies gaps and controversies
3. **Outline stage**: assistant produces a high-level structure with multiple alternatives
4. **Extended outline stage**: each section is broken into paragraphs with bullet
   points for each argument, example, and transition — all independently manipulable
5. **Pre-write review**: author moves items around, kills sections, adds new ones;
   assistant helps restructure without rewriting

**Knowledge sources for the assistant:**
- Classic writing guides (Elements of Style, On Writing Well, Bird by Bird)
- Technical writing courses and syllabi
- Blog posts on writing for developers
- The author's own previous writing (style reference)

---

## Open Questions

- What is the output format for the extended outline — markdown, a structured document,
  or something interactive (a web UI)?
- How does the assistant handle the author's voice — by reading previous writing, by
  style preferences explicitly stated, or both?
- Should this be a standalone tool or a Platform Agent exposed through LibreChat (once
  agent-os is running)?

---

## What Needs to Happen Next

1. After Phase 6, enter this into the ideas pipeline for proper spec development
2. As a prerequisite: have the Tech Skill Builder produce a "writing craft" skill
3. Design the extended outline format — this is the core UI/UX decision

---

## Dependencies

**Depends on:** Phase 6 (skills management), Tech Skill Builder (writing craft skill),
agent-os (if implemented as a Platform Agent)
**Enables:** documentation for all other projects, blog posts, READMEs
