# agent instruction

**Persist subagent results to a scratchpad ledger as they arrive.** "When collecting results from many background subagents, append each returned digest to a single scratchpad ledger file the moment its completion notification arrives. Later phases then rebuild from disk instead of relying on conversation context that may be summarized away."

*Grounded in: the `digests.md` ledger accumulating 11 distiller digests during the agent-patterns build.*

# justification

The agent-patterns Phase 3 fan-out returned 11 distiller digests — roughly 90 candidate pattern slugs with one-line evidence each — that Phase 4's clustering depended on completely. Those digests arrived as conversation messages, exactly the material a long session's context summarization compresses first, and the build still had two heavy phases to go. Appending each digest to `scratchpad/digests.md` on arrival cost one small Bash call per notification; it turned the synthesis input from "whatever survives in context" into a file that could be re-read verbatim at any point. Without the ledger, losing those digests would have meant re-reading 49 source notes to reconstruct the slug inventory — the single most expensive artifact of the session to recompute.
