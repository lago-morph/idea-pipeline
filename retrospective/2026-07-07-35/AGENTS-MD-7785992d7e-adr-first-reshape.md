# agent instruction

**Pin owner decisions as ADRs before a multi-file reshape.** When a review or design conversation produces binding decisions that will drive edits across more than one document, record each decision as an ADR (via the `adr` skill) *before* editing the documents. Treat the ADRs as the source of truth the edits are checked against, not as after-the-fact documentation.

*Grounded in: recording ADRs 0001–0005 before rewriting the four spec-completeness documents.*

# justification

This session's reshape touched four interdependent documents (`artifact-model.md`, `process.md`, `README.md`, `hardening/`) plus 55 executable checks, against five owner decisions accumulated over many feedback rounds. Recording the decisions as ADRs 0001–0005 *first* — before touching any of the four documents — meant every subsequent edit had a stable, citable target: each rewritten section could point at the ADR it implemented, and the owner approved the decisions once, at the ADR stage, rather than re-litigating them inside four separate diffs. The alternative — carrying the decisions only in conversation and editing directly — would have left the rationale spread across chat history that truncates, with no way for a later session (or the owner) to answer "why does this section say this?" without replaying the whole review. The marginal cost is small and front-loaded: five short ADR files and one `adr` link-check run. The payoff compounds across every document the decisions touch and every future session that needs to understand them. When decisions will drive edits in exactly one file, skip the ceremony; the rule is specifically for the multi-file case where drift between documents is the real risk.
