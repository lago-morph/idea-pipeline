# agent instruction

**Give parallel writers private fragment files.** "When several concurrent subagents must each contribute rows or entries to one shared file, have each write its own fragment file (for example `.cache/<job>/<batch>.md`) and merge the fragments in the orchestrator afterward. Never instruct two concurrent agents to append to the same file."

*Grounded in: 16 parallel triage batches merged conflict-free into `sources/_triage.md` in the agent-patterns build.*

# justification

The agent-patterns SPEC designed its triage subagent to append rows directly to `sources/_triage.md` — fine for one-at-a-time ingest, but the Phase 2 build ran 16 triage subagents concurrently. Concurrent appends to one file interleave and clobber: rows land mid-row, or one agent's read-modify-write erases another's rows, and the corruption is silent until a later phase reads garbage. The build instead gave each batch a private fragment under `.cache/triage/` and merged with a three-line shell loop; 234 rows landed intact on the first try. The marginal cost is one merge step the orchestrator was going to do anyway; the avoided cost is re-running an entire fan-out (dozens of subagent invocations) to recover rows nobody can prove are missing.
