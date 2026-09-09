# agent instruction

**Spot-check generated files for empty extracted fields.** "After generating a file by regex-extracting sections from other documents, grep the output for empty fields and verify the extractor against every heading variant the source documents were allowed to use. An extractor written against the common case silently drops the variants."

*Grounded in: `patterns-list.md` losing its one-liner for the one page using the `**Use when (at risk of it):**` heading variant.*

# justification

The agent-patterns build generated `skill/agent-patterns/patterns-list.md` by regex-pulling each page's `**Use when:**` line. The writer subagents had been explicitly allowed a variant for anti-patterns — `**Use when (at risk of it):**` — and the extractor's `\*\*Use when:?\*\*` pattern missed it, leaving one entry's one-liner empty. The gap was caught only because the generated output was read back before committing; nothing errored. In a generated file that agents will consume as their index into the wiki, an empty description is a quiet routing failure. The check costs one grep for empty-looking rows plus comparing the regex against the variants you yourself authorized; the alternative is shipping generated artifacts whose gaps surface only when a future consumer misbehaves.
