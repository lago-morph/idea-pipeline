# Document Profile: Attractor Specification

**Document under review:** `attractor-spec.md` — 2,090 lines. StrongDM's "Attractor," a DOT-digraph workflow-orchestration engine for multi-stage AI pipelines. This profile assesses the SPEC AS A DOCUMENT.

## Quantitative Stats (measured)

| Metric | Count |
|--------|-------|
| Total lines | 2,090 |
| H1 headings | 1 (title, line 1) |
| H2 headings (`##`) | 16 (ToC + 11 numbered sections + 4 appendices A–D) |
| H3 headings (`###`) | 85 numbered subsections (e.g. 1.1–1.4, 2.1–2.13, 11.1–11.13) |
| H4 headings (`####`) | 1 (line 711, "CodergenBackend Interface") |
| Markdown tables | 22 (counted by header-separator rows) |
| Fenced code blocks | ~59 (118 fence lines / 2) |
| DoD checklist items (`- [ ]`) | 76 (sections 11.1–11.11) |
| Parity-matrix checkbox cells (`\| [ ] \|`) | 22 (section 11.12) — total ~98 checkable items |
| RFC-2119 uppercase keywords | 3 total (lines 985–987: 2×MUST, 1×SHOULD NOT) |

---

## 1. Purpose & Scope
**Assessment:** Clearly scoped. Specifies a headless, DOT-graph-driven orchestration engine for chained AI/LLM workflows with conditional routing, human-in-the-loop gates, parallelism, and checkpoint/resume. Goals AND non-goals are both stated explicitly — unusually good for a spec.
**Evidence:** Problem statement and design principles at lines 25–52. Explicit out-of-scope carve-out at lines 54–60: the spec defines orchestration only and disclaims any specific LLM integration.
**Excerpt (lines 56–58):**
> "It does NOT require any specific LLM integration. The codergen handler (Section 4.5) needs a way to call an LLM and get a response -- how you provide that is up to you."

## 2. Document Structure
**Assessment:** Strong, discernible ordering: format/DSL → engine behavior → handlers → state → HITL → validation → styling → extensibility → expression language → acceptance, capped by four reference appendices. This is a textbook data-model-then-behavior-then-interfaces-then-conformance progression.
**Evidence — top-level inventory:** ToC (7–20); §1 Overview/Goals (23); §2 DOT DSL Schema (64); §3 Execution Engine (318); §4 Node Handlers (581); §5 State and Context (991); §6 Human-in-the-Loop (1240); §7 Validation/Linting (1371); §8 Model Stylesheet (1445); §9 Transforms/Extensibility (1525); §10 Condition Expression Language (1661); §11 Definition of Done (1783); Appendix A Attribute Reference (1984); Appendix B Shape mapping (2037); Appendix C Status File Contract (2053); Appendix D Error Categories (2082).
**Note:** Appendices A/B duplicate content from §2.5–2.8/§2.8 as consolidated quick-reference — deliberate redundancy.

## 3. Data Model
**Assessment:** Highly systematic. Entities are given as language-neutral pseudo-struct blocks with typed fields, backed by exhaustive attribute tables with Type/Default/Description columns. Enums are enumerated completely.
**Evidence:** Value-type table (122–128); Graph/Node/Edge attribute tables (134–177, re-consolidated in Appendix A 1988–2033); Outcome struct (1076–1084); StageStatus enum fully enumerated (1088–1094); FidelityMode enum (1141–1147); Context/Checkpoint/ArtifactStore/ArtifactInfo structs (997–1046, 1100–1125, 1181–1218); Question/Answer/QuestionType/AnswerValue models (1255–1289).
**Excerpt (line 1078):** `status : StageStatus  -- SUCCESS, FAIL, PARTIAL_SUCCESS, RETRY, SKIPPED` — the five values are then given their own semantic table (1088–1094).

## 4. Interfaces / API Surface
**Assessment:** Public interfaces are given exact names, parameters, and return types in pseudo-signature form (language-neutral but precise). HTTP surface is fully tabulated with methods and paths.
**Evidence:** `Handler.execute(node, context, graph, logs_root) -> Outcome` (588–599); `CodergenBackend.run(node, prompt, context) -> String | Outcome` (714–716); `Interviewer` triad ask/ask_multiple/inform (1247–1251); `Transform.apply(graph) -> Graph` (1532–1535); `LintRule` (1436–1439); HTTP endpoint table with 9 routes (1595–1605); `validate()`/`validate_or_raise()` signatures (1413–1429). Reserved-word guidance at 166 (external `type` vs internal `node_type`).

## 5. Behavioral Semantics
**Assessment:** The engine's core behavior is specified deterministically as step-by-step pseudocode, not left to inference. This is the spec's strongest dimension. Lifecycle, edge-selection priority, retry/backoff math, goal-gate enforcement, and concurrency rules are all given as executable-grade algorithms.
**Evidence:** 6-phase lifecycle (324–333); full `run()` loop (339–404); 5-step edge-selection priority both as prose AND pseudocode (406–459); goal-gate algorithm (470–478); `execute_with_retry` (491–523); exact backoff formula (543–549); single-threaded concurrency rule with branch-context isolation (573–577).
**Most precise example — deterministic tiebreak (lines 456–458):**
> `FUNCTION best_by_weight_then_lexical(edges): SORT edges BY (weight DESCENDING, to_node ASCENDING); RETURN edges[0]`

The spec even nails a subtle resume edge case: `full` fidelity must degrade to `summary:high` for exactly one hop after resume because in-memory LLM sessions can't be serialized (line 1134).

## 6. Defaults & Configuration
**Assessment:** Nearly every configurable knob carries an explicit default in a dedicated column; the few "inherited"/"unset" cases have their resolution chains spelled out. Excellent.
**Evidence:** Default columns throughout attribute tables (134–177, 1988–2033). Concrete numeric defaults: BackoffConfig `initial_delay_ms=200, backoff_factor=2.0, max_delay_ms=60000, jitter=true` (534–537); `max_parallel="4"`, `join_policy="wait_all"` (814–815); `manager.poll_interval="45s"`, `manager.max_cycles="1000"` (925–926); artifact file-backing threshold 100KB (1220); `reasoning_effort` default `"high"` (162). Where a default is contextual it is stated: fidelity "Default when unset: `compact`" (1164), and 5 named preset retry policies with exact delay sequences (554–560).

## 7. Error Handling & Edge Cases
**Assessment:** Covered systematically at multiple layers: a retryable/terminal predicate, backoff math, per-handler failure returns, a dedicated failure-routing order, and an error-taxonomy appendix. Boundary conditions (empty edge lists, missing results, timeouts) are handled in nearly every handler.
**Evidence:** `should_retry` predicate enumerates retryable vs non-retryable by HTTP code (562); failure-routing 4-step order (564–571); Appendix D three-category error taxonomy (2082–2090); handler guards e.g. "No outgoing edges for human gate" (738), "No parallel results to evaluate" (863), "No tool_command specified" (903); timeout/skip handling in human gate (753–762); missing-key comparison rule "Missing keys compare as empty strings" (1686).

## 8. Examples
**Assessment:** Rich with worked, copy-pasteable examples: complete DOT files, per-node resolution walkthroughs, and one end-to-end integration test with assertions. ~59 fenced blocks total (mix of grammar, pseudocode, and DOT samples).
**Evidence:** 3 minimal DOT workflows (linear/branching/human-gate, 253–314); subgraph inheritance example with narration (218–228); full stylesheet DOT + bullet-by-bullet resolution explanation (1494–1521); condition-expression cookbook of 5 labeled cases (1750–1767); §11.13 end-to-end smoke test with an embedded DOT pipeline and ~15 ASSERT statements (1929–1980).

## 9. Acceptance Criteria / Conformance
**Assessment:** Exceptional — a whole numbered section (§11, "Definition of Done") functions as a conformance suite. Combines a granular checklist, a cross-feature parity matrix, and an executable smoke test. Rare and valuable.
**Evidence:** 76 `- [ ]` checklist items across 11 feature groups (11.1–11.11, lines 1789–1894); a 22-row "Cross-Feature Parity Matrix" where "each cell must pass" (1896–1923); executable integration test with concrete assertions (1925–1980). Framing at line 1785: "An implementation is done when every item is checked off."

## 10. Normative Language
**Assessment:** The spec is prescriptive in tone but does NOT systematically use RFC-2119 uppercase keywords — only 3 uppercase instances exist, all in one "Handler contract" bullet list. Prescription is instead carried by lowercase "must," imperative pseudocode, and Default/Required table columns. Prescription vs. suggestion is reasonably separable via ERROR/WARNING severities and an explicit "Future" section, but not via consistent MUST/SHOULD/MAY tagging.
**Evidence:** Only uppercase normatives at lines 985–987 (2×MUST, 1×SHOULD NOT). Elsewhere prescription is lowercase: "must have exactly one" (185–186), "The engine must refuse to execute" (1375). Suggestion is quarantined in §10.7 "Extended Operators (Future)" (1769–1779) and WARNING-severity lint rules (1404–1408).
**Excerpt (line 986):** `Handler panics/exceptions MUST be caught by the engine and converted to FAIL outcomes.`

## 11. Implementation Freedom
**Assessment:** Explicitly and repeatedly marks what the implementer may choose (LLM backend, language, internal field names, extra handlers/transforms/lint rules, HTTP mode) while bounding freedom via interfaces and "externally visible behavior must remain identical" clauses.
**Evidence:** Backend freedom (56–58, 718: "How you implement this interface is up to you"); reserved-word / internal-naming latitude bounded by external-behavior invariant (166); custom handlers/transforms/lint rules via registration (966–988, 1431–1441, 1565–1573); HTTP mode gated as "Implementations may expose…" (1589); pseudocode disclaimed as language-neutral (337, "The following pseudocode defines…"). Freedom is bounded by named interfaces (Handler, CodergenBackend, Interviewer, Transform, LintRule).

## 12. Self-Containedness
**Assessment:** Largely self-contained for the orchestration core — an implementer could build the engine, parser, router, and validators from this document alone. It assumes general knowledge of Graphviz DOT, JSON, HTTP/SSE, and LLM APIs. It references companion specs but only for the optional backend, which it explicitly makes pluggable, so those references are not hard dependencies.
**Evidence:** External references: Graphviz DOT lang spec URL (40); two companion specs `coding-agent-loop-spec.md` and `unified-llm-spec.md` (58) — but framed as one option among several. The DOT subset is redefined locally via BNF (72–109) rather than deferring to Graphviz, reinforcing self-containedness. Assumed-but-unspecified: JSON serialization format, SSE mechanics, the LLM API itself.

## 13. Ambiguity Audit
Three least-precise areas:
1. **Parallel handler concurrency is under-specified vs. its own claims.** The pseudocode iterates branches sequentially ("FOR EACH branch … branch_outcome = execute_subgraph(...)", 819–821) despite prose promising bounded concurrency and `max_parallel`; `first_success` says "Others may be cancelled" (851) but no cancellation mechanism is defined. `execute_subgraph` is invoked but never specified anywhere.
2. **Manager-loop handler leans on undefined context keys and helpers.** `steer_cooldown_elapsed()`, `ingest_child_telemetry()`, `steer_child()`, and keys like `context.stack.child.status` (939–956) are named but never defined; how child telemetry reaches the parent context is left to inference. The steer/guard "supervisor architecture" (961–965) is described narratively, not algorithmically.
3. **Fan-in candidate model is loosely typed.** `heuristic_select` sorts by `c.score` and `c.id` (886–889), but the parallel results serialized at line 825 (`serialize_results`) never define a `score` or `id` field on branch outcomes, and `llm_evaluate` (867) is a black box. The Outcome struct (1076–1084) has no `score`/`id`, so the fan-in contract is internally inconsistent.

## 14. Distinctive Techniques
**Assessment:** Several reusable patterns a checklist-writer should capture:
- **Priority-ordered rule lists stated twice** (prose numbering + pseudocode) — edge selection (406–459), fidelity resolution (1158–1164), thread resolution (1165–1174), handler resolution (603–630), model-property resolution (1483–1492). Each precedence chain is explicit and total.
- **Decision/mapping tables as normative artifacts:** shape→handler table (183–194), join-policy table (846–851), accelerator-key parsing patterns (781–786), CSS specificity table (1466–1471), preset retry policies with computed delay sequences (554–560).
- **Namespace-convention table** for context keys (`context.*`, `internal.*`, `parallel.*`, etc., 1062–1070) — an invariant/convention registry.
- **Status-file contract as an inversion-of-control mechanism** (709, Appendix C 2053–2078): external agents communicate outcomes back to the engine by writing `status.json`.
- **Built-in-implementations catalogue** (5 Interviewer variants, 1291–1357) doubling as a test-doubles guide (Auto/Queue/Recording for testing).
- **Executable conformance section** (§11) combining checklist + parity matrix + assertion-based smoke test — the single most distinctive feature.
- **Explicit "Future" fence** (§10.7, 1769–1779) that separates speculative operators from the normative grammar and forbids adding them without updating the grammar.

**Overall:** This is an unusually implementation-ready spec — deterministic core algorithms, exhaustive typed tables with defaults, an interface-bounded extensibility story, and a built-in definition-of-done. Its weak spots are concentrated in the concurrency (parallel/fan-in) and supervisor (manager-loop) handlers, where prose ambitions outrun the pseudocode and several referenced helpers/fields are undefined.
