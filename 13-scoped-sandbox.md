# Scoped Sandboxes

**Source:** handwritten notes, 2026-09-12

---

## Raw transcription

Scoped Sandboxes                                        2026-09-12

Idea:

  When working with AI agents, introduce a concept of scoped
  sandboxes.

  What this means is for every large task, during planning an
  explicit input/output interface is defined.

  This is not for security, it is to focus attention.   (!!)

  Each task has, as input, definition of the following:

  - Files
      - Git
      - Ephemeral working

  - AI files (skills, agents.md, harness config)

  - Resources + Credentials

      Database
      MCP
      Git
      Cloud

  - Network rules

  - Tools

      Programs able to use w/ knowledge

  Every item is tagged

    - CRUD permissions          <- [margin note, arrow pointing at this
                                   line] Must be explicit recipe or
                                   positive statement nove [last word
                                   not confidently read; letterforms read
                                   n-o-v-e, matching the pointed "v" of
                                   "positive" in the same annotation;
                                   "none" is the plausible intended word
                                   but the third glyph is not the writer's
                                   "n"]
    - If it is easily recreated (and how)
    - Expected concurrency
    - Expected use (with details in prompt)

  There is deterministic linting at end
      for information, to improve process,
      NOT for security or automated
      remediation.

  The driving use case is for organizing
  the work of AI agents, with some
  combination of the following attributes

  - Subagents for parallelization or to
    preserve orchestrator agent context

  - Repeatability for controlled experiments

      How context affects tasks
      Comparing models, harnesses, skills
        experiments when 1 variable changes

  - Reducing accidental context
    pollution

  - As a clarification mechanism to
    define tasks well for both humans and
    agents

  - Explicit scope/change definition to
    reduce complexity for both humans and
    agents.

  Enabling technologies

    Dynamically scoped credentials

      - Create tightly scoped access tokens/keys
        as needed for specific tasks

    Beads
    Sparse GIT worktrees
