# Spec: Ideas Pipeline

**Phase 4 of the high-level plan**
**Repo:** new — to be created

---

## What It Is

A system for capturing ideas from many sources, tracking them through lifecycle stages
(idea → research → spec → implementation → done), and producing a prioritized work queue
that the agent software factory can pull from. The pipeline replaces ad-hoc planning
with a structured, queryable backlog of everything worth doing.

This session's brainstorm is early input. Full idea capture has not happened yet — that
is itself the first step of this project.

---

## Current State

- Does not exist as a system
- Ideas are currently scattered: in this session's transcript, in musings and shadow-it-research
  repos, in browser bookmarks, in various AI session histories
- There is no common format, no stages, no queue
- The conference-summaries project has a similar staging concept (4-task pipeline) that
  could inform the design

---

## Recommended Design Directions (not prescriptive — needs discovery)

- **GitHub-native first**: GitHub Issues as work items, labels as stages, milestones as
  themes — this costs nothing to set up and integrates naturally with poc-github-ai-sandbox's
  batch-job protocol
- **Multiple capture sources**: voice notes, browser history (Browser History Intelligence),
  AI session exports (Session Analyzer), direct entry, imported from existing repos'
  READMEs and issue trackers
- **Progressive enrichment**: an idea starts as a title + one-line description; an agent
  can interview the owner, produce a research brief, then a full spec — without human
  intervention at each step
- **Agent-queryable**: the pipeline should be queryable by the agent software factory —
  "give me the next ready-to-implement item in the infrastructure domain"
- **Connected to source repos**: each item links to its GitHub repo (if it has one),
  its spec documents, and its implementation history

---

## Open Questions

- What are all the idea sources? This session covered many but the user has not finished
  capturing everything.
- What is the right granularity for a work item — project-level, feature-level, or
  task-level? Probably all three, with parent/child relationships.
- How does the pipeline handle ideas that are too vague to act on vs ideas ready for
  implementation? What does "ready" mean?
- How does prioritization work — manual, AI-suggested, or both?
- Should this be a standalone tool or built on top of GitHub Projects + Issues?
- How does it handle personal vs work projects (separate instances vs one with tagging)?

---

## What Needs to Happen Next

1. **Finish capturing ideas** — dedicated session to dump everything not yet documented
   into a raw list (this is a prerequisite before system design)
2. Research existing tools (GitHub Projects, Linear, Notion) to understand what to build
   vs adopt
3. Design the data model: what fields does a work item have at each stage?
4. Design the capture flows: how does an idea get in from each source?
5. Prototype with GitHub Issues + labels before committing to a custom tool

---

## Dependencies

**Depends on:** Phase 1 (execution substrate), Phase 3 (skills for the agents that
process ideas), Browser History Intelligence (source of ideas), Session Analyzer
(source of patterns)
**Enables:** Phase 5 (agent software factory needs a queue to pull from), dynamic
scheduling of all future work after Phase 6
