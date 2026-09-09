# agent instruction

**Log platform-mandated deviations from a spec when they happen.** "When session or platform rules override something a project spec mandates — branch naming, tooling, file placement — follow the platform rule and record the deviation and its reason in the project's log in the same working step, not at the end of the task."

*Grounded in: the session-mandated `claude/…` branch replacing SPEC's `feature/agent-patterns-mvp`, logged in `log.md` at Phase 0.*

# justification

The agent-patterns SPEC hard-coded `feature/agent-patterns-mvp` as the working branch; the remote session mandated `claude/agent-patterns-spec-th583c` and forbade pushing anywhere else. The platform rule wins — but a future reader of the SPEC will look for a branch that never existed, and a future agent might "fix" the discrepancy by creating it. One log entry written during Phase 0 ("branch deviation: session policy mandates…, same role") closed that trap for the cost of three lines. The same pattern covered renaming `agent-patterns-SPEC.md` to the spec's own `SPEC.md`. Deviations recorded at the moment they're made are accurate and cheap; deviations reconstructed at session end are guesses, and unrecorded ones become the next session's confusion.
