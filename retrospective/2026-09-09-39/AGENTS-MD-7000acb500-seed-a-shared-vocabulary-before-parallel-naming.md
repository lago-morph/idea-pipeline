# agent instruction

**Seed a shared vocabulary before parallel naming.** "When multiple parallel subagents will coin identifiers (slugs, ids, filenames) that must later be merged, give every prompt the same seed list of preferred identifiers plus the convention for coining new ones. Independent agents then converge instead of inventing synonyms that need manual reconciliation."

*Grounded in: three page-writer batches independently converging on `give-a-runnable-check` from shared seed-slug lists.*

# justification

The agent-patterns build's distill and writer fan-outs all coined pattern slugs that had to merge into one flat namespace (SPEC D3 makes slugs permanent ids). Every distiller prompt carried the same seed-slug list plus the coining convention (lowercase-hyphenated, imperative). The payoff was visible: separate batches independently produced `give-a-runnable-check`, `specific-prompt-context`, and `course-correct-early` for the same underlying ideas — the W3 writer even reported the convergence unprompted. Without the seed list, ~90 candidate slugs from 16 independent agents would have arrived as ~90 near-synonyms (`runnable-check` vs `self-verification-tool` vs `verify-tool`), and deduplicating them is exactly the judgment-heavy merge work fan-outs are supposed to save. Cost: one reused paragraph per prompt.
