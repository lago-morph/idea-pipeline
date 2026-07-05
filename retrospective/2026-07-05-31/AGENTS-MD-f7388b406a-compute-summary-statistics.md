# agent instruction

**Compute summary statistics, never estimate them.** "Any number a document claims about itself or its siblings ('exercises 17 distinct checks', '44 items', 'covers all five tiers') must come from a computation you just ran, not from memory of writing the content. If you cannot compute it, do not claim it."

*Grounded in: the regression suite's "17 distinct checks across all five tiers" claim; recomputing gave 24 across three tiers.*

# justification

The §R closing sentence in hardening/checks.md claimed the regression cases "exercise 17 distinct checks across all five tiers." A recount during the consistency pass gave 24 checks across three tiers — the number and the tier claim were both wrong, written from a stale mental tally mid-draft. The fix was one grep-and-count. Self-describing claims are exactly the ones readers trust without checking, so they rot silently; in this repo they are also exactly the defect class the hardening suite exists to catch in other people's specs, which makes shipping one in the suite itself doubly corrosive.
