# Document Profile: Coding Agent Loop Specification

A 1,468-line language-agnostic engineering specification (StrongDM's `coding-agent-loop-spec.md`). Below, each dimension gives an assessment, evidence with line numbers, and (where useful) one short verbatim excerpt.

---

## Quantitative stats

| Metric | Count |
|---|---|
| Total headings (levels 1–4) | 83 |
| Level-1 (`#`) | 1 (title, line 1) |
| Level-2 (`##`) | 13 (9 numbered sections + ToC + 3 appendices; lines 9–1453) |
| Level-3 (`###`) | 62 (subsections like 2.1–2.10, plus appendix subsections) |
| Level-4 (`####`) | 7 (per-tool definitions: read_file, write_file, edit_file, shell, grep, glob, apply_patch) |
| Fenced code blocks | 44 (88 fence lines) |
| Tables | 8 |
| Checklist items (`- [ ]`) | 59 (Definition of Done §9.1–9.11) |
| Parity-matrix cells | 15 test cases × 3 providers = 45 additional checkboxes (§9.12) |
| Table rows (`\| …`) | 76 |

The 8 tables: reasoning effort (§2.7), output size limits (§5.2), line limits (§5.3), command timeouts (§5.4), project doc files (§6.5), cross-provider parity matrix (§9.12), tool-level errors (App B), session-level errors (App B).

---

## 1. Purpose & Scope
Specifies a **programmable coding-agent loop library** (not a CLI) that pairs an LLM with developer tools via an agentic loop (line 3). Goals are stated both as a narrative problem statement (§1.1, lines 25–29) and six design principles (§1.3, lines 46–58). Non-goals are **explicitly and separately enumerated** in a dedicated "Out of Scope" section (§8, lines 1133–1148): MCP, Skills, sandboxing, compaction, approval system, read-before-write guardrail — each with a note on where its extension point lives.

> "This spec defines a **library** -- a programmable agentic loop that a host application controls at every step." (line 35)

## 2. Document Structure
Clear, disciplined ordering that flows overview → behavior → data → interfaces → environment → prompts → composition → non-goals → acceptance → appendices. Full top-level inventory:
- ToC (9), §1 Overview and Goals (23), §2 Agentic Loop (124), §3 Provider-Aligned Toolsets (463), §4 Tool Execution Environment (722), §5 Tool Output and Context Management (850), §6 System Prompts and Environment Context (987), §7 Subagents (1060), §8 Out of Scope (1133), §9 Definition of Done (1151), Appendix A: apply_patch v4a (1315), Appendix B: Error Handling (1407), Appendix C: Design Decision Rationale (1453).

Ordering logic is discernible and consistent: each capability area presents the data model (RECORD/ENUM/INTERFACE) before its behavior, and acceptance criteria are deferred to a single consolidated §9. Appendices hold reference-grade detail (patch grammar) and rationale, keeping the main body prescriptive.

## 3. Data Model
Types are specified with a **language-neutral pseudocode notation** (`RECORD`, `ENUM`, `INTERFACE`, `Map<K,V>`, `List<T>`, `String | None`) — explicitly declared as such (line 58: "All code is pseudocode"). Fields are given as aligned tables with inline `-- comment` semantics, e.g. `Session` (131–143), `SessionConfig` (148–159, every field typed with a default), the five Turn types (189–212), `SessionEvent`/`EventKind` (412–434), `ToolDefinition`/`RegisteredTool`/`ToolRegistry` (690–707), `ExecResult`/`DirEntry` (757–768), subagent records (1101–1115). Enums are enumerated **completely** with per-value comments: `SessionState` (4 values, 164–169), `EventKind` (15 values, 418–434), `SubAgentStatus` (3 values, 1101–1104).

> `max_command_timeout_ms       : Integer = 600000  -- 10 minutes` (line 151)

## 4. Interfaces / API Surface
Public surfaces are given **exact names, typed parameters, and return types**. The `ProviderProfile` interface lists methods and capability flags (§3.2, 474–488); `ExecutionEnvironment` gives full method signatures including param types and returns (§4.1, 729–755). Every tool has a structured block with `parameters` (typed, marked required/optional with defaults), `returns`, and `errors` — e.g. `edit_file` (530–539), `shell` (548–556), `grep` (565–575). Host-facing methods `steer()`/`follow_up()` are given with behavioral contracts (§2.6, 371–380). Subagent tools (`spawn_agent`, `send_input`, `wait`, `close_agent`) fully specified (§7.2, 1069–1096). This is one of the spec's strongest dimensions — very little is loose.

## 5. Behavioral Semantics
Core behavior is given **deterministically as numbered pseudocode**, not left to inference. The centerpiece `process_input()` loop is a step-numbered algorithm (§2.5, 219–303) with explicit limit checks, request build, single-shot completion, tool execution, steering drain, and loop detection. Supporting functions are fully written out: `drain_steering`, `execute_tool_calls` (with parallel/sequential branch), `execute_single_tool` (lookup→validate→execute→truncate→emit→return), `detect_loop` (443–458), `truncate_output`/`truncate_lines` (859–944). State machine given as an explicit transition table (§2.3, 173–182). Stop conditions enumerated (§2.8). Most precise example — the loop-detection pattern scan:

> `FOR pattern_len IN [1, 2, 3]: IF window_size % pattern_len != 0: CONTINUE …` (lines 448–456)

Ordering guarantees are explicit (character truncation MUST precede line truncation, §5.3). Concurrency is bounded: parallel tool calls only when `supports_parallel_tool_calls` (317–320).

## 6. Defaults & Configuration
Nearly every knob carries an **explicit default value inline**. `SessionConfig` defaults are set at the type level: `max_turns = 0`, `default_command_timeout_ms = 10000`, `loop_detection_window = 10`, `max_subagent_depth = 1` (148–159). Per-tool defaults are tabulated: output char limits (§5.2), line limits (§5.3), timeouts (§5.4), read_file `limit` default 2000 (504). Provider-specific overrides are explicit (Anthropic shell default 120s overrides the 10s global, line 643). Defaults are framed as overridable floors, not ceilings (line 56: "prescribes defaults, not ceilings").

## 7. Error Handling & Edge Cases
Systematically covered, with a **dedicated appendix (B)** plus inline handling. Two decision tables map error type → recovery/retryability: tool-level (7 rows, 1413–1421) and session-level with a Retryable column (6 rows, 1427–1434). Tool errors become `is_error=true` results returned to the model (not exceptions); unknown-tool and validation failures handled explicitly in `execute_single_tool` (333–342). Timeout sequence is spelled out (SIGTERM → 2s → SIGKILL, 957–961) and repeated in graceful-shutdown (1440–1449). Boundary/pathological cases are called out by name: the "2 lines each 10MB CSV" case motivates truncation ordering (line 900, 946); context overflow → warning only, no compaction (§5.5). Malformed patch matching → fuzzy fallback (541, 1386).

## 8. Examples
Rich in worked examples. ~44 fenced code blocks total. Categories: an ASCII architecture diagram (62–95); ~15 pseudocode algorithm/type blocks; per-tool definition blocks; the apply_patch appendix has 6 concrete patch examples (Add/Delete/Update/Rename/multi-hunk, 1343–1403) plus a formal grammar block (1321–1338); and a full **end-to-end integration smoke test** with 7 numbered scenarios and `ASSERT` statements (§9.13, 1273–1311). Alternative environments are illustrated with command-mapping snippets (Docker/K8s/WASM/SSH, 794–824). Examples span both illustrative (sample patches) and executable-style (smoke test with assertions).

## 9. Acceptance Criteria / Conformance
Exceptionally strong — a full **Definition of Done** section (§9, lines 1151–1311). 59 checkbox items grouped into 11 themed subsections (Core Loop, Provider Profiles, Tool Execution, Execution Environment, Truncation, Steering, Reasoning Effort, System Prompts, Subagents, Events, Error Handling). Plus a **Cross-Provider Parity Matrix** (§9.12) of 15 test cases × 3 providers = 45 cells that "each … must pass," and a runnable integration smoke test (§9.13). Opening line: "An implementation is done when every item is checked off" (1153).

## 10. Normative Language
Does **not** systematically use RFC-2119 style. Hard `MUST` appears only ~2 times, both about truncation ordering (line 854: "it MUST be truncated"; line 900: "MUST always run first"). "should" (~11) carries most prescription, and "may" (~5) marks options. There is no MUST/SHOULD/MAY key or capitalization convention. Instead, prescription is conveyed largely through **imperative pseudocode and the DoD checklist**, which is arguably more testable than prose keywords. Prescription vs. suggestion is separated structurally (normative body + §9 checklist vs. Appendix C rationale and §1.5 "worth studying" references), but not lexically flagged.

## 11. Implementation Freedom
Freedom is **explicitly marked and bounded**. Language is free ("implementable … in any programming language," line 3; "All code is pseudocode," 58). Internal structure is free where behavior is pinned — e.g. system prompt *text* is left to the implementer while required *topics* are enumerated ("The spec does NOT prescribe full system prompt text … It specifies what topics the prompt must cover," 1010). Fuzzy matching is permitted ("the implementation may attempt fuzzy matching," 541). Notably, Appendix C **softens** an earlier hard constraint: §3.1 demands a "1:1 copy … byte for byte" (469) whereas C reframes the goal as "behavioral alignment … not a byte-for-byte copy" (1455) — a deliberate bounding of freedom that also creates an internal tension (see §13).

## 12. Self-Containedness
Mostly self-contained for the loop mechanics, but **explicitly depends on a companion document**: the Unified LLM Client Specification (`./unified-llm-spec.md`), imported for `Client`, `Request`, `Response`, `Message`, `Tool`, `ToolCall`, `ToolResult`, `StreamEvent`, `Usage`, `FinishReason` (§1.6, 109–120; also line 5). Retry/backoff behavior is delegated to that layer (1242, 1429–1433). It also references three external reference projects (codex-rs, pi-agent-core, gemini-cli, §1.5) — but frames them as "worth studying," not required. Assumed external knowledge: JSON Schema, regex, POSIX signals, git, ripgrep, Docker/K8s CLIs, the v4a patch format (though Appendix A defines it fully). An implementer could build the loop from this doc **only if** the unified-llm spec is also available.

## 13. Ambiguity Audit
Three least-precise areas:
1. **Byte-for-byte vs. behavioral alignment contradiction.** §3.1 (469) mandates "the exact same tool definitions, byte for byte," while Appendix C (1455) says "not a byte-for-byte copy … behavioral alignment." An implementer gets conflicting instructions on how literally to clone reference agents.
2. **System prompt content is deliberately underspecified.** Profiles must "mirror the codex-rs / Claude Code / gemini-cli system prompt structure" (622, 641, 663, 1004–1010) but no text or concrete acceptance test is given beyond "cover identity, tool usage, best practices" — the DoD item (1171) is subjective.
3. **`validate_arguments` / JSON-Schema validation depth** (339, 1179) is invoked but never defined — how strict, which drafts, coercion behavior are all open. Related soft spots: `AWAITING_INPUT` transition trigger ("model asks user a question (no tool calls, open-ended)," 177) has no detection algorithm; and the parallel-execution result-ordering guarantee vs. `AWAIT_ALL` isn't stated.

## 14. Distinctive Techniques
Several patterns a checklist-writer should capture:
- **Decision/mapping tables** as first-class spec artifacts: error→recovery and error→retryability tables (App B), reasoning-effort semantics table (§2.7), and the per-provider tool-mapping lists (§3.4–3.6).
- **Per-provider behavior differentiation** ("provider-aligned toolsets") — a whole design axis where OpenAI/Anthropic/Gemini get different tools, editing formats, and timeout defaults, then validated by a **3-column parity matrix** (§9.12).
- **Key-design-decision callouts** inline (e.g. line 436: TOOL_CALL_END carries full untruncated output while LLM sees truncated) plus a consolidated **rationale appendix** (C) answering "Why X?" for seven decisions.
- **Ordering invariants stated as rules** with a motivating pathological case ("character truncation MUST come first," §5.3, with the 10MB-line CSV justification).
- **Priority-ordered layering** for the system prompt ("later layers taking precedence," 991–1000) and project-doc precedence ("deeper = higher precedence," 1053).
- **Executable acceptance** — assertions and a smoke-test harness rather than prose ("done when every item is checked off").
- **Explicit extension-point mapping** in the Out-of-Scope section: each non-goal names exactly where in the architecture it would hook in (e.g. approval gate "between VALIDATE and EXECUTE," 1145).
