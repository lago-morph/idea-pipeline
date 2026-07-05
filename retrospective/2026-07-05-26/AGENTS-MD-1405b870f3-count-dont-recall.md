# agent instruction

**Count, don't recall.** Any numeric claim in a document about a structure that exists in the same document (edges in a graph, rows in a table, items in a list) must be derived by counting the structure at write time — grep/wc or explicit enumeration — never written from memory. Re-verify every such claim after editing the structure.

*Grounded in: the artifact-model DAG paragraph claiming "three intra-layer edges" while listing four, with the true count being seven.*

# justification

The Mermaid graph, the edge-justification table, and the prose acyclicity argument were all in one file, and the prose still contradicted the graph it sat next to — written from a stale mental snapshot two edits earlier. It survived until a mandated full re-read (PR #26, re-read iteration 1). The rule costs one grep per claim; the failure mode ships a self-contradicting document whose whole point is teaching others to avoid self-contradiction.
