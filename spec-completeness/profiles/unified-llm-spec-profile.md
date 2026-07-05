# Document Profile: Unified LLM Client Specification

Document analyzed: StrongDM's `unified-llm-spec.md` (2,169 lines).

## Quantitative Stats (at a glance)

| Metric | Count |
|---|---|
| Top-level (H1) | 1 (title) |
| H2 sections | 12 (8 numbered + Table of Contents + 3 appendices) |
| H3 subsections | 81 |
| H4 sub-subsections | 33 |
| Markdown tables | ~22 |
| Fenced code blocks | ~87 (174 fence lines) |
| Definition-of-Done checklist items (`- [ ]`) | 71 |
| Cross-provider parity matrix cells | 45 (15 rows × 3 providers) |
| Bullet-list lines | 148 |
| Numbered-list items | 44 |
| Uppercase RFC-2119 terms | MUST ×4, REQUIRED ×1, SHOULD ×1, SHALL ×0, uppercase MAY ×0 |
| Lowercase modal verbs | must ×38, should ×18, required ×19, may ×14 |

---

## 1. Purpose & Scope
Specifies a **language-agnostic unified client library** presenting one interface across multiple LLM providers (OpenAI, Anthropic, Gemini, +others), explicitly intended to be implementable from scratch "in any programming language" (lines 3, 24-26). Goals are stated as five named **Design Principles** (lines 28-38: provider-agnostic, minimal surface area, streaming-first, composable, escape-hatches-over-false-abstractions). Non-goals are *implied rather than sectioned* — e.g. "The library does not invent its own model namespace" (line 120), "does not use [rate-limit info] for proactive throttling" (line 735) — but there is **no dedicated "Out of Scope / Non-Goals" heading**. That is the single most notable structural omission.

## 2. Document Structure
Clear ordering logic that flows **architecture → data model → behavior → interfaces → conformance**, with a hyperlinked Table of Contents (lines 7-17). Top-level inventory:
- L20 §1 Overview and Goals; L52 §2 Architecture; L346 §3 Data Model; L796 §4 Generation and Streaming; L1052 §5 Tool Calling; L1283 §6 Error Handling and Retry; L1479 §7 Provider Adapter Contract; L1796 Appendix A (Conversation Examples); L1866 Appendix B (High-Level API Usage); L1952 Appendix C (Design Decision Rationale); L1982 §8 Definition of Done.

The progression is deliberate: types (§3) precede the operations that consume them (§4-5), errors (§6) precede the adapter contract that raises them (§7), and everything precedes the acceptance checklist (§8). Rationale is deferred to an appendix (§C) so it doesn't interrupt normative flow.

## 3. Data Model
Highly systematic. §3 opens with an explicit **type-notation legend** (lines 348-358: `String`, `List<T>`, `T | None`, `T | U`, etc.), then defines every entity as a `RECORD`/`ENUM` block with per-field inline comments. Enums are fully enumerated: `Role` (5 values, lines 398-404), `ContentKind` (8 values, 439-448), `StreamEventType` (13 values, 770-784), `FinishReason` (6 unified values, 624-631). Types are **language-neutral pseudo-structs**, not native signatures. Representative field-table style:
```
RECORD Usage:
    input_tokens        : Integer
    reasoning_tokens    : Integer | None
    cache_read_tokens   : Integer | None
```
Enumerated types are frequently paired with **provider-mapping tables** (role mapping L408-414; finish-reason mapping L635-649; usage-field mapping L677-683).

## 4. Interfaces / API Surface
Public surface is given with **exact names, typed parameters, and return types**. The `ProviderAdapter` interface is stated verbatim (lines 164-172) with required `complete()`/`stream()` and optional `close()`/`initialize()`/`supports_tool_choice()` (182-191). The high-level `generate()` signature lists all 20 parameters with types and defaults (lines 851-872), e.g. `max_tool_rounds : Integer = 1`. Catalog lookups (`get_model_info`, `list_models`, `get_latest_model`) are given signatures at lines 314-323. Some surface is looser — `StreamResult` mixes a prose "ASYNC ITERATOR over StreamEvent" with typed members (939-944).

## 5. Behavioral Semantics
Core algorithms are given as **deterministic step-by-step pseudocode**, not left to inference. The most precise example is the multi-step tool loop (lines 1187-1227), a complete control-flow listing with explicit break conditions:
```
IF tool_calls AND response.finish_reason.reason == "tool_calls" AND round_num < max_tool_rounds:
    tool_results = execute_all_tools(tools, tool_calls)  -- concurrent
```
Other precisely-specified behaviors: middleware onion ordering ("request: registration order, response: reverse order", line 139), the streaming start/delta/end lifecycle (786-792), parallel-tool-execution as a 5-rule ordered list (1231-1237), `max_tool_rounds` arithmetic ("total number of LLM calls is at most `max_tool_rounds + 1`", 879), and backoff math (1420-1423). Concurrency rules are stated (Client holds no mutable state, adapters must be concurrency-safe; 204-208).

## 6. Defaults & Configuration
Most knobs carry explicit defaults, often inline in the type. `RetryPolicy` defaults every field (lines 1406-1413: `max_retries=2, base_delay=1.0, max_delay=60.0, backoff_multiplier=2.0, jitter=true`). `AdapterTimeout` gives connect=10s / request=120s / stream_read=30s (1044-1048). Other explicit defaults: `max_tool_rounds=1`, `max_retries=2` on `generate()` (858, 868); Anthropic `max_tokens` "Default to 4096" (1573); `media_type` defaults to `"image/png"` (475); `tool_choice` "defaults to AUTO if tools present" (557); `strict` default false (713). A few knobs are policy-deferred rather than defaulted — Anthropic auto-cache breakpoint placement is "implementation-specific" (340).

## 7. Error Handling & Edge Cases
The most rigorously covered dimension. A full **error class hierarchy** is drawn as a tree (lines 1298-1317, 17 error types), with anti-shadowing naming rationale (1319). Retryability is specified via two explicit tables (non-retryable 1339-1349, retryable 1353-1358) plus HTTP-status→error mapping (1368-1379) and a **gRPC-code mapping for Gemini** (1383-1392) and message-string fallback classification (1398-1401). Edge cases handled explicitly: unknown errors default retryable (1360), `Retry-After` exceeding `max_delay` ⇒ do NOT retry (1440), streaming does not retry after partial delivery (1447), unknown tool calls return error-results not exceptions (1267), partial tool-batch failures (1237), Gemini's missing tool-call IDs (519, 1595). Timeouts split into three scopes (connect/request/stream_read).

## 8. Examples
Example-rich: ~87 fenced blocks. Categories: (a) inline API-usage snippets throughout §2-§6; (b) **Appendix A** — 4 fully-populated `Message` literal examples incl. multimodal and thinking-block round-trip (1796-1862); (c) **Appendix B** — 6 high-level usage walkthroughs incl. a provider-fallback try/catch (1924-1931); (d) **§8.10 Integration Smoke Test** — a 6-part end-to-end script with concrete `ASSERT` statements and expected values (`result.output.age == 30`, lines 2109-2167). Worked input→output pairs appear (e.g. `generate_object` "Alice is 30" → `{"name":"Alice","age":30}`, 966-981). Most blocks are illustrative pseudocode rather than compilable code.

## 9. Acceptance Criteria / Conformance
Unusually strong. §8 "Definition of Done" is an explicit **71-item checkbox checklist** across 9 themed groups (8.1-8.8), stated as testable assertions ("`generate()` rejects when both `prompt` and `messages` are provided", 2026). §8.9 adds a **15×3 cross-provider parity matrix** (45 checkboxes, 2087-2103). §8.10 provides a runnable smoke-test with assertions. The doc frames done-ness as binary: "An implementation is considered done when every item is checked off" (1984), "If all items in this section are checked off, the unified LLM library is complete" (2169).

## 10. Normative Language
Prescription is carried **overwhelmingly by lowercase modal verbs, not RFC-2119 uppercase**. Uppercase keywords are rare and unsystematic: only 4 `MUST` (L212, 332, 338, 1231), 1 `SHOULD` (338), 1 `REQUIRED` (690); zero `SHALL`, zero uppercase `MAY`. Lowercase equivalents dominate: must ×38, should ×18, required ×19, may ×14. There is **no keywords/conformance-language section** defining these terms, so prescription-vs-suggestion is separated only by word choice and context, not by formal convention. The uppercase ones are reserved for the highest-stakes rules (native-API mandate, caching mandate, parallel-tool correctness).

## 11. Implementation Freedom
Freedom is explicitly marked and bounded. Language choice is open ("any programming language", line 3). Internal structure is bounded by the four-layer architecture (54-74) and the stable Layer-1 contract. Notable freedom clauses: typed languages "may model `provider_options` as provider-specific typed fields... so long as the serialized request behavior is equivalent" (587); sync/async spelling is left to the host language ("regardless of whether the host language spells it sync or async", 206); Anthropic auto-cache heuristic is implementation-specific but "adapters should document their heuristic and provide an escape hatch" (340). Reference OSS projects are explicitly "not dependencies; implementors may take inspiration" (42).

## 12. Self-Containedness
Mostly self-contained for the **abstraction layer**, but **assumes substantial external provider-API knowledge** for adapters. The mapping tables encode a lot (endpoints, field names, SSE event names, auth schemes — see the 20-row Provider Quirks table, 1745-1765), yet an implementer still needs live provider docs for exact request/response schemas, current beta-header strings, and evolving model IDs. The spec acknowledges this: model catalog "should be shipped as a data file... Consider auto-generating it from provider documentation" (328). External references are advisory only (3 OSS projects, lines 44-48) — no hard dependency on another document.

## 13. Ambiguity Audit (least-precise spots)
1. **Anthropic automatic cache-breakpoint placement** — the "recommended" auto-injection heuristic is explicitly "implementation-specific" (line 340) yet DoD 8.6 demands breakpoints "on the system prompt, tool definitions, and stable conversation prefix using a documented heuristic" (2049). What counts as the "stable prefix" is undefined.
2. **`reasoning_tokens` for Anthropic** — specified as an *estimate* "from the token lengths of thinking blocks" (697) with no estimation formula, making DoD parity for "token counts are accurate" (2101) unverifiable for Anthropic.
3. **Tool-context injection** — "The library inspects the handler's signature and injects recognized keyword arguments" (1108) lists three magic names (`messages`, `abort_signal`, `tool_call_id`) but leaves the injection/reflection mechanism and name-collision rules to the implementer. Related: `arguments : Dict | String` (515) and `content : String | Dict | List` (525) union types push parsing decisions onto the implementer.

## 14. Distinctive Techniques (worth capturing in a checklist)
- **Per-provider mapping tables as the dominant spec instrument** — ~22 tables systematically translate every unified concept (roles, finish reasons, usage fields, tool choice, tool defs, image formats, streaming events) into all three providers' native shapes.
- **Dual-representation types** preserving both unified and native values: `FinishReason{reason, raw}` (617-620), pervasive `raw : Dict | None` escape fields.
- **Explicit escape-hatch design pattern** — `provider_options` (568-587) with the stated "90%/10%" doctrine (252) and an honesty clause: "Code that uses `provider_options` is explicitly not portable" (585).
- **A dedicated Design-Decision-Rationale appendix** (§C, 1952-1978) answering "why" for ~11 decisions — unusual and valuable for an implementer making language-idiomatic tradeoffs.
- **Invariants stated inline**: `max_tool_rounds + 1` LLM-call bound (879); tool-result ordering must match call ordering (1236); thinking blocks "must round-trip verbatim" (447, 543).
- **Layered stability contract** — Layer 1 "changes rarely and only with explicit versioning... A new provider is added by implementing this interface, not by modifying it" (68).
- **Audience-aware framing** — repeatedly justifies features by their value to a downstream *AI coding agent* (326, 1256, 1958), including the catalog-to-prevent-hallucination argument.
- **Conformance-as-matrix** — the 15×3 parity grid (§8.9) plus a runnable end-to-end smoke test (§8.10) give a concrete, gradable definition of done.
