# Project Dependencies Map

## Legend

- **→** hard dependency (cannot start without)
- **~~>** soft dependency (benefits from, but can proceed without)
- **[REPO]** existing GitHub repo
- **[NEW]** new project, no repo yet
- **[PIVOT]** existing repo with recommended direction change

---

## Phase-by-Phase Dependencies

```
Phase 1: Batch Job Skill [PIVOT: poc-github-ai-sandbox → ai-skills]
  → requires: poc-github-ai-sandbox (source material)
  → requires: ai-skills (target format)
  → enables: Phase 2, Phase 3, Phase 5

Phase 2: k8-platform Reset [REPO: k8-platform]
  → requires: Phase 1 (batch-job skill)
  → requires: poc-github-ai-sandbox (execution protocol)
  → enables: agent-os (infrastructure baseline)

Phase 3: Skills Consolidation [REPOS: ai-skills, skill-sharing, poc-github-ai-sandbox]
  → requires: Phase 1 (establishes canonical format)
  ~~> benefits from: poc-github-ai-sandbox retrospective specs
  → enables: Phase 5 (factory needs skills), Phase 6 (content to manage)

Phase 4: Ideas Pipeline [NEW]
  → requires: Phase 1 (execution substrate)
  ~~> benefits from: Phase 3 (skills for processing agents)
  ~~> fed by: Browser History Intelligence, Session Analyzer
  → enables: Phase 5 (work queue), dynamic scheduling after Phase 6

Phase 5: Agent Software Factory [NEW]
  → requires: Phase 1 (batch-job + task-dag skills)
  → requires: Phase 3 (skills library)
  → requires: Phase 4 (work queue)
  → enables: all post-Phase 6 implementation work

Phase 6: Structured Skills Management [NEW or extends skill-sharing]
  → requires: Phase 3 (consolidated content)
  → requires: Phase 5 (factory produces new skills)
  ~~> requires: k8-platform (runs LiteLLM)
  → enables: agent-os implementation, Tech Skill Builder publishing
```

---

## Post-Phase 6 Projects and Their Dependencies

```
Tech Skill Builder [NEW]
  → requires: Phase 6 (publishing layer)
  → requires: Phase 5 (factory builds and runs the pipeline)
  ~~> built on: conference-summaries (ingestion pattern)
  → enables: agent-os Knowledge Base, all technology-specific skills

conference-summaries Generalization [PIVOT: conference-summaries]
  → requires: Phase 3 (SKILL.md format)
  → requires: Phase 6 (publishing layer)
  ~~> should complete current Phase 1 first before pivoting
  → enables: Tech Skill Builder (becomes its ingestion layer),
             agent-os vendor doc companion project

agent-os [REPO: agent-os]
  → requires: k8-platform COMPLETE (infrastructure baseline)
  → requires: Phase 6 (skills management)
  → requires: Phase 5 (agent software factory for implementation)
  ~~> requires: conference-summaries generalization (vendor docs)
  ~~> requires: ai-skills + skill-sharing (skills layer)
  ~~> informed by: code-knowledge-base (Knowledge Base research)
  → enables: everything eventually runs on agent-os as Platform Agents

Browser History Intelligence [NEW]
  → requires: nothing (most independent project)
  → enables: Ideas Pipeline (input source), personal tech radar

Session Analyzer [NEW]
  → requires: nothing structural (can start data collection now)
  ~~> benefits from: Phase 3 (style file format)
  → enables: Ideas Pipeline (personal patterns source),
             all agent work (better alignment from the start)

Writing Assistant [NEW]
  → requires: Phase 6 (skills management)
  → requires: Tech Skill Builder (writing craft skill)
  ~~> better as: agent-os Platform Agent (post-agent-os)
  → enables: documentation for all other projects
```

---

## Full Dependency Graph (Simplified)

```
poc-github-ai-sandbox ──→ [Phase 1: Batch Job Skill]
                                    │
                    ┌───────────────┼───────────────┐
                    ↓               ↓               ↓
            [Phase 2:          [Phase 3:         enables
            k8-platform]       Skills             Phase 5
                │             Consol.]                │
                ↓               │                     │
            agent-os        [Phase 4:          [Phase 5:
            (baseline)      Ideas Pipeline]    Agent Factory]
                                    │               │
                                    └───────┬───────┘
                                            ↓
                                    [Phase 6: Skills Mgmt]
                                            │
                     ┌──────────────────────┼──────────────────────┐
                     ↓                      ↓                      ↓
              Tech Skill              conference-           agent-os
              Builder                 summaries             (implement)
                     │               Generalization
                     └──────────────────────┘
                                    ↓
                           agent-os Knowledge Base
                           + all technology skills

[standalone, can start anytime]
Browser History ──→ Ideas Pipeline
Session Analyzer ──→ agent-style.md → all agent work
```

---

## Recommended Pivots to Existing Projects

| Project | Current Direction | Recommended Pivot |
|---|---|---|
| `k8-platform` | Ad-hoc GitHub Actions for Terraform | Adopt batch-job skill for all privileged ops (Phase 2) |
| `conference-summaries` | KubeCon-specific extractor | Generalize to any source; output as SKILL.md, not just YAML |
| `ai-skills` | General skills store (sparse) | Canonical skills library; clear owner of content separate from distribution |
| `skill-sharing` | Distribution CLI for Codex | Clarify role: contributor tooling upstream of LiteLLM organizer |
| `code-knowledge-base` | Research only | Feed directly into agent-os Knowledge Base design; research is done |
| `musings` | Informal notes | First-class input to the ideas pipeline capture process |

---

## Dependency Invariants

These must hold for the plan to work:

1. **Phase 1 before Phase 2**: k8-platform cannot use the batch-job skill until the
   skill exists
2. **Phase 1 before Phase 3**: consolidation needs the canonical format Phase 1 establishes
3. **Phase 3 before Phase 5**: the factory needs a skills library to load from
4. **Phase 4 before Phase 5**: the factory needs a work queue to pull from
5. **k8-platform complete before agent-os implementation**: non-negotiable hard dependency
6. **Phase 6 before agent-os serious implementation**: agents need organized skills to
   work at the scale of 40+ components
7. **conference-summaries Phase 1 complete before pivoting**: don't abandon work mid-flight
