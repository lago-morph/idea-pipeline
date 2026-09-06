# agent instruction

**Load human-scoped-deliverables before writing anything the owner will read.** Before drafting a summary, plan, index, or design document whose reader is Jonathan rather than another agent, invoke the `human-scoped-deliverables` skill and follow its vocabulary discipline. Its rule against invented jargon covers coined codes, coined labels, and any term not already in the corpus.

*Grounded in: the skill existed in this repository and was not loaded before the architecture documents were written.*

# justification

The `human-scoped-deliverables` skill sits in this repository's `.claude/skills/` and its description names exactly the failure that happened: invented jargon over corpus terms, cognitive load as a real resource. It was listed as available in every turn of the session and never invoked, because the documents were framed as design drafts rather than as summaries or primers. The result was the event-code rewrite described in the previous rule, which the skill's vocabulary rule would have prevented before the first draft. The cost of loading the skill is one tool call at the start of a writing task. The cost of not loading it was a twenty-file rewrite and a round-trip with the owner.
