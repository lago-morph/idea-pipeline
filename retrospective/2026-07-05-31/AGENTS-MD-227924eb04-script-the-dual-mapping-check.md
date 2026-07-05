# agent instruction

**Script the check on dual-maintained mappings.** "When the same mapping is maintained in two places (a coverage table and per-item fields, an index and its entries), verify it with a throwaway script that parses both sides and diffs them bidirectionally — before every commit that touches either side. Eyeballing is not verification."

*Grounded in: four coverage-table asymmetries found by script in PR #30.*

# justification

In PR #30 the coverage table in hardening/README.md and the per-check `Hardens:` fields in hardening/checks.md were written minutes apart by the same author — and still drifted in four places (D-03, D-20, L-03, L-05). A ~30-line Python snippet found all four in one run, plus a structural gap (L-08 missing from the S6 execution-map row) on the second pass in PR #31; visual review had caught none of them. Cost of the script: about two minutes, reusable verbatim on the next commit. Cost of shipping the drift: the deliverable's own acceptance property ("no check exists without a mapped item") would have been false in its first published revision — in a repo whose entire subject is checkable completeness.
