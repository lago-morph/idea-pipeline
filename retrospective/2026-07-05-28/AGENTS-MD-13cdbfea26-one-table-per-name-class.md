# agent instruction

**One table per name class.** When a document defines named things used across sections — constants, metric names, criterion labels, statuses — define each name class in exactly one table and use the names verbatim everywhere else. Consistency then becomes a grep sweep (every use resolves to one definition; every definition is used) instead of a judgment call.

*Grounded in: process.md's §9.1 constants and §9.2 metrics tables, which let one grep pass verify 7 constants, 40 criterion labels, and 24 metric names.*

# justification

process.md carries three name classes (7 gate constants, 24 metric names, 40 entry/exit criterion labels) used across eight stage cards, a routing table, and a pressure-test appendix. Because each class was defined in exactly one table and used verbatim, the final consistency check was a 20-second grep loop that mechanically proved every name resolves — across ~1,500 lines. The counter-case is visible in the gold-spec audits this repo studies: symphony's "configured assignee" — a name used in prose that resolves to no definition anywhere — survived review and became a canonical defect example. Tabling names first costs nothing at authoring time; it converts an unbounded proofreading problem into a bounded mechanical one.
