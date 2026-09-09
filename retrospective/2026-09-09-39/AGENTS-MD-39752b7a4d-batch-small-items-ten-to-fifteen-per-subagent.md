# agent instruction

**Batch small items ten to fifteen per subagent.** "When fanning classification or triage work out over a corpus of many small items, give each subagent a batch of 10–15 items rather than one item per invocation — per-item dispatch spends more tokens on prompt overhead than on the work itself. Keep the per-item output contract identical to the single-item design."

*Grounded in: 234 cached sources triaged in 16 batches instead of 234 invocations.*

# justification

Phase 2 of the agent-patterns build had 234 items to rate (148 newsletter emails plus 86 web fetches). The spec's one-item-per-invocation design would have meant 234 subagent dispatches, each paying the full prompt, role-file read, and return-envelope overhead to skim a file that is often two paragraphs of marketing. Batching 15 items per agent cut that to 16 dispatches with identical per-item output (one triage row each), and the whole phase finished in a few minutes of wall-clock. The rule's cost is nothing — the batch prompt is the single-item prompt with a file list. Its absence costs an order of magnitude in dispatch overhead, plus an orchestrator context flooded by 234 completion notifications.
