# agent instruction

**Read a source before citing it.** "An evidence or citation line may be written only after reading the cited source in this session, and may claim only what that source actually supports. When delegating writing, instruct subagents to drop or narrow unsupported citations from both the text and any metadata list, and to report every drop or narrowing back."

*Grounded in: page writers scoping the `openhands-2026-ccbp` citation on `cross-model-review` down to fresh-model plan review.*

# justification

The agent-patterns wiki's value rests on its no-hallucinated-evidence rule (SPEC §2), and the Phase 4 writers were the point of maximum risk: 36 pages, ~140 evidence lines, written from a plan that merely asserted which sources supported which patterns. Because every writer prompt required reading the cited note first and licensed dropping or narrowing, the discipline caught real errors: one writer scoped the OpenHands citation on `cross-model-review` to fresh-model *plan* review (the note doesn't support different-model *code* review), another confined an abstract-only arXiv note to what an abstract can claim, and a third recorded that `osmani-2026-code-review-ai` supports the threat-model tier rather than failure-path testing per se. Each of those would otherwise be a fabricated citation sitting in a wiki whose whole premise is traceability. Cost: the writer reads notes it was going to need anyway. The report-back line makes the drops auditable instead of silent.
