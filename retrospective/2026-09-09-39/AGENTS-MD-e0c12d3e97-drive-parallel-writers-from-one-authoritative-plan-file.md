# agent instruction

**Drive parallel writers from one authoritative plan file.** "When several subagents write files that must be mutually consistent — shared metadata fields, cross-references between files — put every per-file decision into one plan file they all read, and keep each agent's prompt to pointing at its section of the plan. Do not restate metadata inside each prompt: restated copies drift."

*Grounded in: `pattern-plan.md` driving five writer batches to 36 pages with zero metadata inconsistencies at lint.*

# justification

Phase 4 of the agent-patterns build needed 36 pattern pages from five parallel writers, where every page's `related:` links had to name slugs another writer was creating and every frontmatter field had to survive a strict lint. All of it — slug, title, type, category, status, durability, confidence, sources, related — went into one `pattern-plan.md`, and each writer prompt said only "write the pages in your batch section". The post-write lint found zero problems: no broken related-links across writers, no status or category drift, no id/filename mismatches. The failure mode this prevents was demonstrated in miniature by the same session's SPEC, whose prose and §10 table disagreed about its own filename. Writing the plan file costs the planning you were doing anyway; per-prompt restatement costs a reconciliation pass over every inconsistency two copies can develop.
