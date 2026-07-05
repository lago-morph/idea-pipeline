# agent instruction

**Give every regression suite a negative control.** "When pinning expected-failure cases for a checker (lint suite, validation harness, mutation set), include at least one conforming case that must NOT fire, and say so in the suite — a checker validated only on positives will happily flag correct patterns as defects."

*Grounded in: RD-11 in hardening/checks.md §R — symphony's conforming enum delegation pinned as must-PASS.*

# justification

The residual-defect suite pins fourteen gold-spec defects as expected check firings; RD-11 is deliberately different. Symphony's Codex-enum delegation is the exact pattern the artifact model prescribes, so the closure checks are required NOT to fire on it — only the freedom-width probe may. Without that row, a future check revision could "improve" recall by firing on every delegation, and the suite would score the regression as progress. The control costs one table row; it is the difference between measuring defects and measuring pedantry — the suite's own phrasing.
