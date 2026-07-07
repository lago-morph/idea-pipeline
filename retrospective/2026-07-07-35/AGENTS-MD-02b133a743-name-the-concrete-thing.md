# agent instruction

**Name the concrete thing when surfacing a decision to a human.** When presenting a choice for the human owner to decide, never refer to work products or steps by a shorthand you coined mid-session ("the amendment", "staged", "the realignment"). Lead with the concrete thing — the actual file, the actual alternatives in plain words, the trade-off, and the cost of choosing wrong. The reader cannot see your internal labels.

*Grounded in: the owner's correction that "amendment" and "staged" were invented shorthand they could not read.*

# justification

When presenting the pre-implementation decisions, the response leaned on invented shorthand — framing a choice as "one amendment vs. staged" and naming decision topics as if they were documents the reader already knew. The owner's reaction was blunt: "what fucking do you mean about 'amendment'... you are making up your own language and communicating it to me without regard to the fact that I can't read your mind. 'staged' is not an alternative. It is a buzzword you made up." The whole decision batch had to be re-asked in plain language — real files named, alternatives spelled out, trade-off and rewind path stated — costing a full round-trip and eroding trust. This repo already ships a `human-scoped-deliverables` skill that says exactly this; the failure was not following it. The marginal cost of the rule is zero — it is *less* work to write "I rewrite all four files and you review one diff, or I do it in two rounds you review separately" than to write "one amendment vs. staged" and then explain both terms. The asymmetry is total: plain naming is cheaper to write *and* cheaper to read, and coined shorthand has no upside when the audience is a human who was not in your head when you coined it.
