# agent instruction

**Dedupe retro proposals against prior retros.** Before proposing agents-file rules or skills in a retrospective, list what earlier retros already proposed (`ls retrospective/*/AGENTS-MD-*.md retrospective/*/SKILL-SPEC-*.md`) and read the rule names; drop any candidate an existing rule already covers, and cite the prior rule instead if the session re-confirmed it.

*Grounded in: this session nearly re-proposing grep-before-re-edit and jq-the-saved-result, both already filed by the PR-26 retrospective.*

# justification

Two of this session's strongest workaround candidates — grep the file before re-Editing aged text, and jq the saved result file for oversized MCP outputs — turned out to already exist verbatim in the PR-26 retrospective's sibling directory, discovered only because a pre-write `ls` of prior AGENTS-MD files happened as a formatting check. Re-proposing them would have produced two near-identical rules with different hashes for the downstream assembler to reconcile, and diluted the review signal of the genuinely new rules. The dedupe costs one ls plus a minute of reading names; the alternative grows the rule set superlinearly with session count while adding nothing. Re-confirmation is still signal — note it in the narrative ("the rule fired in anger"), not as a duplicate proposal.
