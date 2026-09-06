# agent instruction

**Mark every recorded conclusion as owner-stated or proposed.** When capturing a discussion into files, keep a decisions log in which each conclusion is labeled with who settled it: the owner in conversation, or the agent as a proposal awaiting the owner's word. Never present an agent's inference as settled. A merge is not ratification.

*Grounded in: `architecture-ideas/decisions-log.md`, which carried 37 labeled conclusions from one session.*

# justification

The session produced dozens of conclusions across six hours of discussion, and roughly a third of them were the owner's and two thirds were proposals. Without a label, a future session would read the proposals as settled and build on them, which is the exact failure agent-method's own lessons record under "label AI-inferred intent as unratified". The decisions log made the split explicit: each row says owner, proposed, or owner-agreed, and the open questions are listed separately. It cost one table. It is also what let the objectives document say "inferred" honestly and what let the subagents' judgment calls be logged as proposals rather than facts. The marginal cost is one column; the alternative is a document set whose provenance cannot be recovered.
