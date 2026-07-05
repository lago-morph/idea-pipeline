# Hardened Checks — Definitions

*Task-03 deliverable for [issue #22](https://github.com/lago-morph/idea-pipeline/issues/22).
The framework — tiers, escalation ladder, ID/output/failure conventions, Tier-L constraint
rules, constants, execution map, and the §3-item coverage table — is in
[README.md](README.md); read it first. Artifact IDs, traceability rules T1–T7, and the tag
grammar are [../artifact-model.md](../artifact-model.md); stages, defect classes, routing,
and record schemas are [../process.md](../process.md). Compiled 2026-07-05.*

Reading notes, applying to every block below:

- **Inputs** name artifact files (process §3.1 layout) for in-process runs; for a
  compiled or external spec, the same inventories come from `dist/spec.md` (tags survive
  compilation) or the §2.1 extraction path (untagged).
- **Metric** reuses process §9.2 names and formulas verbatim where they exist. Ratios
  are oriented so 1.0 is perfect. `(or N/A)` in a closure formula means an explicitly
  written N/A cell counts as filled — silence never does.
- **Output** is always the standard record (framework §3.2); the block lists only
  check-specific evidence fields.
- **Failure semantics** name the default defect class and routed stage per process
  §8.1; the Q-record vs. BD-record form follows framework §3.3 automatically, and the
  process's reclassification rule can override the default class at triage.
- Tier-D regex sketches build on the artifact-model §5 grep surface:
  `\[(#|realizes:|freedom:|checks:)\s*[A-Z]-[A-Z]{2}-[0-9]{3}` plus the per-artifact
  record schemas (process §4).

Contents: [§1 Deterministic checks](#1-deterministic-checks-d-01d-29) ·
[§2 Extraction and hybrid checks](#2-extraction-and-hybrid-checks) ·
[§3 Reader probes](#3-reader-probes-l-01l-09) ·
[§4 Gate-adequacy (mutation) checks](#4-gate-adequacy-mutation-checks-m-01m-02) ·
[§5 Human check](#5-human-check-h-01) ·
[§R Residual-defect regression suite](#r-residual-defect-regression-suite)

---

## 1. Deterministic checks (D-01…D-29)

### CHECK D-01 — Enum closure
- **Hardens:** C.2 (supports B.2)
- **Tier:** D (D+L on untagged specs, via EXT-1)
- **Inputs:** C-DM (enum declarations); all normative artifacts (enum-value references); A-VS dependency register (declared enum delegations)
- **Procedure:**
  1. Build the declaration set: every `ENUM` block in C-DM → `{enum, values[], delegated?}`; a delegation is valid only if it cites an A-VS register row with a discovery procedure.
  2. Build the reference set: every enum-typed field, transition label, gate box, or algorithm branch naming an enum value (grep value tokens; on tagged specs, values are declared under the enum's element ID).
  3. Referenced-but-undeclared enum, or referenced value missing from its declaration → open cell. Declared value never referenced anywhere and not marked `reserved` → unconsumed value (each is evidence: dead vocabulary or missing behavior — attractor's `Direction`).
  4. Emit per-enum evidence rows.
- **Metric:** `enum_closure` = fully-enumerated enums ÷ enums declared in C-DM (process §9.2), threshold 1.0; secondary `value_consumption` = values consumed-or-reserved ÷ values declared, threshold 1.0.
- **Output:** evidence rows `{enum, value?, direction: undeclared|missing|unconsumed, locus}`.
- **Failure semantics:** the contract's vocabulary is open — a builder must invent members or dead values hide unstated behavior. Class CONTRACT_GAP → S3 (undeclared/missing); unconsumed values default LINT → S6 with the reclassification rule alert.

### CHECK D-02 — State-machine transition closure
- **Hardens:** B.2
- **Tier:** D (D+L on untagged specs, via EXT-2)
- **Inputs:** C-BC (state machines); C-DM (state/event enums)
- **Procedure:**
  1. For each machine, take states `S` from its C-DM enum and events `E` from the declared trigger set.
  2. Build the `S × E` matrix from the transition table; a cell is filled by a target state, a self-loop, or a **declared impossibility** ("cannot occur because …").
  3. Any silent cell → open. Any transition citing a state/event outside `S`/`E` → reference defect (route to D-09).
  4. Verify every machine's initial state and terminal states are declared.
- **Metric:** `transition_closure` = (state, event) cells with a transition or declared impossibility ÷ Σ per machine (states × events) (process §9.2), threshold 1.0.
- **Output:** evidence rows `{machine, state, event}` per open cell.
- **Failure semantics:** an implementer facing an unlisted (state, event) pair invents semantics. Class CONTRACT_GAP → S3.

### CHECK D-03 — Operation × failure-class closure
- **Hardens:** F.1 (supports F.3)
- **Tier:** D (D+L on untagged specs, via EXT-2 + EXT-3)
- **Inputs:** C-BC (operation inventory); C-FM (failure taxonomy)
- **Procedure:**
  1. Rows: every C-BC operation obligation. Columns: every C-FM failure class, which must minimally cover {timeout, malformed input, missing resource, concurrent modification} — a taxonomy lacking one of the four minima is itself a FAIL (the classes the gold specs' defects cluster in).
  2. A cell is filled by defined behavior (C-FM text citing the operation, or an operation-level failure clause) or an explicit per-cell N/A.
  3. Failure mentions anywhere in the spec that name no C-FM class → unresolved failure reference (evidence).
- **Metric:** `failure_closure` = (operation, failure-class) cells with defined behavior or explicit N/A ÷ (C-BC operations × C-FM classes) (process §9.2), threshold 1.0.
- **Output:** evidence rows `{operation, failure_class}` per silent cell; `{locus}` per unresolved failure mention.
- **Failure semantics:** error paths are where generated code is chronically thin (README §4.1.5); a silent cell is behavior the builder will improvise. Class CONTRACT_GAP → S3.

### CHECK D-04 — Failure-class attribute closure
- **Hardens:** F.2, F.3
- **Tier:** D (D+L on untagged specs, via EXT-3)
- **Inputs:** C-FM
- **Procedure:**
  1. For every failure class: require a retryability cell ∈ {retryable, terminal, conditional(condition cited)} — table or per-class statement.
  2. Require a blast-radius cell: what halts vs. what degrades, phrased over C-BC behavioral units (run attempt, tick, dispatch…).
  3. Require the unknown/unclassified-failure default to be stated once (unified-llm's conservative default is the exemplar).
- **Metric:** `class_attr_closure` = classes with both cells filled ÷ classes, threshold 1.0; boolean `unknown_default_stated` (genuinely binary).
- **Output:** evidence rows `{class, missing: retryability|blast_radius}`.
- **Failure semantics:** a class without retryability yields divergent retry loops; without blast radius, divergent failure propagation. Class CONTRACT_GAP → S3.

### CHECK D-05 — Defaults closure
- **Hardens:** E.1
- **Tier:** D (D+L on untagged specs, via EXT-1 + EXT-4)
- **Inputs:** C-DM (configurable fields); R-CD (defaults); R-FR (declared open defaults)
- **Procedure:**
  1. Enumerate configurable C-DM fields (marked configurable on the field, or appearing as an R-CD knob).
  2. Each must have an R-CD default **at its point of definition** or a `[freedom:]` tag to a live R-FR entry.
  3. R-CD knob with no C-DM field → dangling default (symphony's defect inverted; route to D-07/D-09 territory, evidence here).
  4. Default values must be literals with units where the type has units (`ms`, bytes) — a unitless duration is an open cell.
- **Metric:** `defaults_closure` = configurable C-DM fields with an R-CD default or `[freedom:]` tag ÷ configurable fields (process §9.2), threshold 1.0.
- **Output:** evidence rows `{field, missing: default|field|unit}`.
- **Failure semantics:** every missing default is an arbitrary decision that diverges across builds (README §4.1.3). Class REALIZATION_GAP → S4 (a *deliberately* open default missing its R-FR entry reclassifies CONTRACT_GAP → S3).

### CHECK D-06 — Pseudocode helper closure
- **Hardens:** J.1 (supports B.1)
- **Tier:** D (D+L on untagged specs, via EXT-4)
- **Inputs:** R-RA (pseudocode); R-IS (surface definitions); C-BC (obligations); G-ST (script calls)
- **Procedure:**
  1. Parse every call-shaped token in R-RA pseudocode and G-ST script steps: `identifier(...)`.
  2. Each must resolve to: a definition in R-RA, a signature in R-IS, or a named C-BC obligation invoked abstractly (T6; the S4-X5 slice).
  3. Language keywords and A-GL-declared pseudocode primitives (declared once in the notation legend) are whitelisted; the whitelist is part of A-GL, not of this check.
- **Metric:** `helper_closure` = resolved invocations ÷ invocations, threshold 1.0.
- **Output:** evidence rows `{helper, locus}` (attractor's `execute_subgraph`, `steer_cooldown_elapsed`, `serialize_results`; coding-agent-loop's `validate_arguments`).
- **Failure semantics:** an undefined helper is behavior that exists nowhere — the single most audited defect shape in the corpus. Class REALIZATION_GAP → S4 (if the helper embodies uncontracted observable behavior, CONTRACT_GAP → S3).

### CHECK D-07 — Config-reference closure
- **Hardens:** J.2
- **Tier:** D (D+L on untagged specs, via EXT-4)
- **Inputs:** all normative artifacts (prose config references); C-DM; R-CD
- **Procedure:**
  1. Collect config-key references: backticked keys matching the R-CD key grammar, and prose phrases of the form "the configured X" / "the X setting".
  2. Each must resolve to a C-DM field **and** an R-CD default-or-freedom (D-05's pair).
  3. "The configured X" with no such key is a FAIL even when X is a plausible concept — plausibility is how symphony's "configured assignee" survived review.
- **Metric:** `config_ref_closure` = resolved references ÷ references, threshold 1.0.
- **Output:** evidence rows `{reference, locus}`.
- **Failure semantics:** the minimal fix decides the class (process §8.1 reclassification rule): typo → LINT → S6; missing field → CONTRACT_GAP → S3 (the symphony case).

### CHECK D-08 — Record-field access closure
- **Hardens:** J.3
- **Tier:** D (D+L on untagged specs, via EXT-4)
- **Inputs:** R-RA (field accesses); G-ST (ASSERT operands); C-DM (record definitions)
- **Procedure:**
  1. Parse every field access in pseudocode and G-ST ASSERTs: `receiver.field` (chase the receiver's declared type through signatures and local bindings; an untypeable receiver is itself evidence).
  2. Each accessed field must exist on the receiver's C-DM record (or the register-imported type's declared field list).
  3. Fields written but never declared, and comparisons against enum values not in the enum, are the same defect shape — include them.
- **Metric:** `field_access_closure` = resolving accesses ÷ accesses, threshold 1.0.
- **Output:** evidence rows `{record, field, locus}` (attractor's `c.score`/`c.id` on Outcome; its smoke test's `outcome.completed_nodes`).
- **Failure semantics:** an algorithm reading a phantom field means the data model or the algorithm is wrong — a human picks which at triage. Class REALIZATION_GAP → S4 (missing entity/field in Layer 1 reclassifies CONTRACT_GAP → S3).

### CHECK D-09 — Reference and tag closure
- **Hardens:** J.1, J.2, J.3 (their tag-level generalization; substrate for T1/T2/T5 checks)
- **Tier:** D (D+L on untagged specs, via EXT-1/4/5)
- **Inputs:** all artifacts; A-GL; A-VS register
- **Procedure:**
  1. Tag grammar: every occurrence matching the loose pattern `\[(#|realizes:|freedom:|checks:)` must fully match artifact-model §5's grammar; malformed → FAIL row.
  2. ID uniqueness: every `[#X-YY-NNN]` declared exactly once; citations resolve to a declared ID.
  3. Term closure (T6): every backticked or Capitalized-Term used normatively resolves to one definition in A-GL or C-DM (unified-llm's "stable conversation prefix" is the type case).
  4. External-name closure: every external system/document named in normative text resolves to an A-VS register row.
  5. Enum-value closure at the gate: every enum value a gate item references exists in its C-DM enum (coding-agent-loop's gate-legislated `"xhigh"`).
- **Metric:** `ref_tag_closure` = resolving references ÷ references (all five kinds pooled; per-kind counts as evidence), threshold 1.0.
- **Output:** evidence rows `{kind, reference, locus}`.
- **Failure semantics:** default LINT → S6, with the reclassification rule applied per row (a term that names missing behavior is CONTRACT_GAP → S3; a gate-legislated value is GATE_GAP → S5 under T4).

### CHECK D-10 — Realization grounding (T1)
- **Hardens:** H.1
- **Tier:** D (D+L on untagged specs, via EXT-2/4 against the contract inventory)
- **Inputs:** all Layer-2 artifacts; Layer-0/1 element inventory
- **Procedure:**
  1. Every Layer-2 element (R-AS component, R-IS surface element, R-RA algorithm, R-CD knob, R-FR entry) carries ≥1 `[realizes:]` citation to a live Layer-0/1 element (T1).
  2. Untagged path: for each realization element extracted, search the contract inventory for the obligation it discharges; none found → orphan.
- **Metric:** `t1_orphans` = Layer-2 elements with no citation (process §9.2), threshold 0.
- **Output:** evidence rows `{element, locus}`.
- **Failure semantics:** an orphan HOW is a decision that never passed through triage — a missing requirement **or** over-specification; the finding does not say which (artifact-model T1), so the routed stage dispositions it. Class REALIZATION_GAP → S4 (if the disposition is "missing requirement," it cascades CONTRACT_GAP → S3).

### CHECK D-11 — Contract closure (T2) and witness coverage
- **Hardens:** H.1, B.1 (supports I.5)
- **Tier:** D (D+L on untagged specs)
- **Inputs:** Layer-1 element inventory; Layer-2 citations; R-FR
- **Procedure:**
  1. Every Layer-1 element is cited by ≥1 Layer-2 element or by an R-FR entry (T2). Neither → dangling WHAT.
  2. Witness sub-slice: every C-BC **operation obligation** is cited by ≥1 R-RA algorithm (its determinism witness) or carries `[freedom:]` — the redundancy README §2.1-J observed (prose rule + pseudocode witness), made mandatory.
- **Metric:** `t2_dangling` = uncited Layer-1 elements (process §9.2), threshold 0; secondary `witness_coverage` = witnessed-or-free C-BC operations ÷ operations, threshold 1.0.
- **Output:** evidence rows `{element, kind: dangling|unwitnessed}`.
- **Failure semantics:** a dangling WHAT is a promise no realization or declared freedom accounts for (attractor's promised-but-unrealized cancellation). Class REALIZATION_GAP → S4; if the element *should* be open, the fix is an R-FR entry via scoped S3 re-entry (CONTRACT_GAP).

### CHECK D-12 — Hedge-word scan
- **Hardens:** J.5 (supports H.1)
- **Tier:** D
- **Inputs:** all normative artifacts (R-FR excluded by rule)
- **Procedure:**
  1. Case-insensitive scan with **HW-LEX v1** (the canonical lexicon; T7's list plus the corpus's audited hits): `appropriately, appropriate, reasonable, reasonably, sensible, leniently, lenient, gracefully, best effort, as needed, as expected, properly, robustly, common field names, if possible, where feasible`.
  2. Hits inside R-FR entries and inside X-DR are exempt (declared freedom and quarantined rationale respectively).
  3. Each hit is either fixed (precise wording) or converted to a declared freedom — the two legal dispositions per §3.J.5 and T7.
  4. Lexicon updates are versioned here; adding a word is a suite change, not a per-run choice.
- **Metric:** `hedge_hits` = HW-LEX matches outside R-FR/X-DR, threshold 0.
- **Output:** evidence rows `{word, locus, quote}` (symphony's "leniently").
- **Failure semantics:** a hedge is unregistered freedom in disguise (T7). Class LINT → S6; a hit whose precise rewrite would change behavior reclassifies CONTRACT_GAP → S3.

### CHECK D-13 — Dependency-register completeness
- **Hardens:** H.2
- **Tier:** D (D+L on untagged specs, via EXT-5)
- **Inputs:** A-VS (external-dependency register)
- **Procedure:**
  1. Every register row has all three cells: scope-of-reliance (which types/sections — "imports exactly these 10 types"), version pin **or** discovery procedure, and a conflict-resolution rule ("on conflict, X controls").
  2. Every external document/system named anywhere in normative text has a row (the D-09 external-name slice feeds this).
  3. Delegated enums/values (symphony's Codex enums) must cite the row's discovery procedure.
- **Metric:** `register_completeness` = filled cells ÷ (rows × 3), threshold 1.0.
- **Output:** evidence rows `{dependency, missing_cell}` (attractor's DOT subset carries no conflict clause).
- **Failure semantics:** an unmanaged dependency is scope leaking outward — conflicts get resolved silently by whichever document the builder happens to read. Class CONTRACT_GAP → S3 (register content is A-VS-owned; scope-level rows route S1 per §8.1's scope-level case).

### CHECK D-14 — Inspiration-only enforcement
- **Hardens:** H.3
- **Tier:** D (D+L on untagged specs, via EXT-5)
- **Inputs:** A-VS register (reference-implementation rows); all normative artifacts; G-AC/G-CM/G-ST
- **Procedure:**
  1. Every reference implementation in the register is marked exactly one of `inspiration-only` or `pinned-oracle` (pinned: version + scope + conflict rule per D-13).
  2. For each `inspiration-only` row: grep its name across C-/R-/G- artifacts; any hit inside an obligation (normative keyword in scope, gate box, `[checks:]`-cited text) is a violation — "mirror the structure of X" binding conformance to an unpinned repo is the signature defect.
- **Metric:** `inspiration_violations` = obligation-hits on inspiration-only names, threshold 0.
- **Output:** evidence rows `{reference, locus, quote}` (coding-agent-loop's mirror clauses).
- **Failure semantics:** conformance bound to a mutable external artifact is untestable and drifts. Class GATE_GAP → S5 when the binding is a gate item; CONTRACT_GAP → S3 when body text binds it (the behavior must be contracted locally or registered as a pinned oracle).

### CHECK D-15 — Scope-structure completeness
- **Hardens:** G.1, G.2, G.3
- **Tier:** D (D+L on untagged specs, via EXT-5)
- **Inputs:** A-VS
- **Procedure:**
  1. Goals: ≥1 goal; every goal carries a name and a principle statement (name token + prose; a bare feature list is not a principle set).
  2. Non-goals: a dedicated section exists with ≥1 entry, or an owner-signed waiver in the ledger states the spec genuinely excludes nothing (rare; the waiver is the evidence). Absence with no waiver = FAIL (unified-llm).
  3. Extension points: every non-goal names the extension point where it would attach, or declares "no attachment point" explicitly (coding-agent-loop §8 is the exemplar).
- **Metric:** `scope_structure` = (named goals + dispositioned non-goals + extension-pointed exclusions) ÷ (goals + non-goals + exclusions), threshold 1.0.
- **Output:** evidence rows `{kind, entry, missing}`.
- **Failure semantics:** missing non-goals invite scope wandering on long-horizon builds (README §4.1.4). Class INTENT_GAP (scope-level) → S1.

### CHECK D-16 — Contract purity and notation conformance
- **Hardens:** C.1, C.3 (nullability half); enforces T3 for all C-artifacts
- **Tier:** D (D+L on untagged specs, via EXT-1)
- **Inputs:** C-DM, C-BC, C-FM, C-QC; A-GL (notation legend)
- **Procedure:**
  1. Legend exists in A-GL and declares the full type grammar (base types, `List<T>`, `T | None`, `RECORD`/`ENUM`).
  2. Every C-DM field line parses against that grammar: `name : Type [constraint…]`. Unknown type token → FAIL row. Nullability is decidable per field from the notation alone (`| None` present or absent) — no field may leave it to prose.
  3. T3 purity sweep over all four C-artifacts: zero occurrences of R-element IDs, pseudocode fences, default-value assignments (`= literal` outside constraint grammar), wire literals (HTTP verbs + paths, status codes, JSON bodies), or signature syntax. (Attachment-rule fragments are exempt *in the compiled file* because they keep R-IDs and tags — the sweep keys on ownership tags, not position; artifact-model §6.2.)
- **Metric:** `typed_fields` = grammar-conforming fields ÷ fields, threshold 1.0; secondary `purity_violations` = Layer-2 vocabulary hits in C-artifacts, threshold 0.
- **Output:** evidence rows `{artifact, locus, kind: untyped|purity}`.
- **Failure semantics:** an untypeable field is an undecidable data model; a purity hit is WHAT-inside-HOW — the corpus's most defect-dense zone (artifact-model §11 finding 3). Class CONTRACT_GAP → S3 (pure notation slips: LINT → S6).

### CHECK D-17 — Signature grammar conformance
- **Hardens:** D.1
- **Tier:** D (D+L on untagged specs, via EXT-4)
- **Inputs:** R-IS; C-DM; A-VS register (imported types)
- **Procedure:**
  1. Every public interface element parses as: exact name, parameter list with `name : Type` per parameter, return type (or explicit `None`/`Unit`).
  2. Every type token resolves to C-DM, A-GL notation, or a register-imported type (the D-09 slice, scoped here to signatures).
  3. Prose-only surface ("provides a way to fetch…" with no signature) counts the element as non-conforming.
- **Metric:** `typed_signatures` = fully-parsed signatures ÷ public surface elements, threshold 1.0.
- **Output:** evidence rows `{element, missing: name|param_type|return|type_resolution}`.
- **Failure semantics:** a loose signature forces builders to invent the surface, which is exactly what cross-build divergence measures later — pay at S4 instead. Class REALIZATION_GAP → S4.

### CHECK D-18 — Tool/endpoint block completeness
- **Hardens:** D.2 (supports F.1)
- **Tier:** D (D+L on untagged specs, via EXT-4)
- **Inputs:** R-IS (tool/endpoint blocks); C-FM (failure classes)
- **Procedure:**
  1. Every tool/endpoint has all three block fields: `parameters` (each typed, marked required/optional, optional ⇒ default per D-05), `returns` (typed), `errors` (list).
  2. Every `errors` entry resolves to a C-FM class (per-method error contracts realize C-FM — artifact-model's R-IS→C-FM edge).
  3. An empty `errors` list must be the literal `errors: none` — silence is an open cell.
- **Metric:** `block_completeness` = filled cells ÷ (blocks × 3), threshold 1.0; secondary `error_ref_closure` = resolving error entries ÷ entries, threshold 1.0.
- **Output:** evidence rows `{block, missing_cell | unresolved_error}`.
- **Failure semantics:** a tool without an error contract fails unspecified — builders diverge on the most-executed path. Class REALIZATION_GAP → S4 (unresolved error naming a missing class: CONTRACT_GAP → S3).

### CHECK D-19 — Wire-surface completeness
- **Hardens:** D.3
- **Tier:** D (D+L on untagged specs, via EXT-4)
- **Inputs:** R-IS (wire sections); X-WE (payload examples)
- **Procedure:**
  1. Every route/message has: method, exact path (or message name), status/outcome codes enumerated, request body example (or explicit `no body`), response body example per declared status family.
  2. Every JSON/structured example parses (syntactic validity is free to check and the gold specs' payloads earn their keep by being pasteable).
  3. Field names appearing in wire examples must resolve to the mapping table or C-DM (D-08's spirit at the wire).
- **Metric:** `wire_completeness` = filled cells ÷ (routes × 5), threshold 1.0; secondary `example_parse_failures` = 0.
- **Output:** evidence rows `{route, missing_cell | parse_error}`.
- **Failure semantics:** wire gaps produce incompatible implementations that each pass their own reading. Class REALIZATION_GAP → S4.

### CHECK D-20 — Freedom-register entry completeness
- **Hardens:** E.3 (supports H.1); mechanizes S3-X4 / T7's field requirements
- **Tier:** D
- **Inputs:** R-FR; all artifacts (`implementation-defined` markers); R-CD
- **Procedure:**
  1. Every R-FR entry has all required fields non-empty: the open choice, the bounding-contract citation **resolving to a live C-element**, the documentation obligation, and `origin` (process §4.5).
  2. Every `Implementation-defined` / `implementation-defined` token anywhere carries `[freedom: R-FR-nnn]` to a live entry; every R-CD `implementation-defined` default likewise (R-CD→R-FR edge).
  3. Inverse: every R-FR entry is referenced by ≥1 `[freedom:]` tag (an entry nothing points at is dead or its subject is untagged).
- **Metric:** `rfr_completeness` = entries with all fields resolving ÷ entries, threshold 1.0; secondary `unregistered_markers` = 0.
- **Output:** evidence rows `{entry|marker, missing}` (attractor's bounded-but-undocumented freedoms; unified-llm's dangling bounding citation on auto-cache).
- **Failure semantics:** an entry without a bound is unbounded ambiguity wearing a register ID; a marker without an entry is a leak. Class CONTRACT_GAP → S3 (R-FR is S3-owned).

### CHECK D-21 — Derived-view freshness
- **Hardens:** E.4 (supports I.5)
- **Tier:** D (D+L on untagged specs, via EXT-4)
- **Inputs:** source artifacts; `dist/spec.md` derived views (config cheat-sheet, reference appendices, ToC)
- **Procedure:**
  1. Tagged path: regenerate every derived view from its source artifacts (artifact-model §6.3) and diff against the published view; any line differing → drift.
  2. Untagged path: extract the cheat-sheet/appendix entries and the body's point-of-definition entries; set-diff both directions — an entry in the body missing from the "complete" view is the attractor Appendix A defect; a view entry missing from the body is worse (view legislating).
  3. Existence: R-CD non-empty ⇒ a consolidated cheat-sheet view exists (E.4's core).
- **Metric:** `derived_view_drift` = differing entries, threshold 0; boolean `cheatsheet_exists`.
- **Output:** evidence rows `{view, entry, direction: missing_in_view|missing_in_body}`.
- **Failure semantics:** hand-maintained redundancy rots into a second source of truth (artifact-model §11 finding 10). Class LINT → S6 (a view entry with no body source reclassifies GATE_GAP/CONTRACT_GAP per what it legislates).

### CHECK D-22 — Gate coverage and framing
- **Hardens:** A.1; mechanizes T5a and S5-X1
- **Tier:** D (D+L on untagged specs, via EXT-6)
- **Inputs:** G-AC (+ G-CM cells); normative element inventory
- **Procedure:**
  1. G-AC exists; its framing line matches `done when every (item|box) is checked` (case-insensitive) — the gold specs' shared frame.
  2. Every box uses checkbox syntax and carries ≥1 `[checks:]` citation resolving to a live element (a box citing nothing is symphony's §17.7 CLI defect).
  3. Coverage direction: every normative element (grep all `[#…]` declarations in Layers 0–2) is cited by ≥1 G-AC box or G-CM cell.
- **Metric:** `gate_coverage` = normative elements cited by ≥1 `[checks:]` ÷ normative elements (process §9.2), threshold 1.0; secondary `box_citation` = boxes citing ≥1 live element ÷ boxes, threshold 1.0.
- **Output:** evidence rows `{element_uncovered | box_unanchored, locus}`.
- **Failure semantics:** an uncovered element is behavior the gate cannot fail — invisible to S7 grading; an unanchored box creates obligations, which gates never do (T4). Class GATE_GAP → S5.

### CHECK D-23 — Gate-box lexical checkability screen
- **Hardens:** A.2 (cheap screen; L-05 is the deciding instrument)
- **Tier:** D
- **Inputs:** G-AC boxes, G-CM cells, G-ST ASSERT lines
- **Procedure:**
  1. Scan gate text with **JW-LEX v1** (judgment lexicon): `mirrors, similar to, consistent with, the structure of, reasonable, appropriate, properly, correctly, robust, gracefully, as expected, high quality, idiomatic`.
  2. Any hit → the box is presumptively judgment-shaped (coding-agent-loop's "mirrors the … system prompt structure").
  3. Numeric-claim boxes ("token counts are accurate") must name the exact value source or formula; `accurate/correct` without one is a hit.
- **Metric:** `jw_hits` = judgment-lexicon matches in gate text, threshold 0.
- **Output:** evidence rows `{item, word, quote}`.
- **Failure semantics:** a judgment box is unverifiable, so it silently passes everything (T5b). Class GATE_GAP → S5 — and per the S5 resistance rule, the *claim* behind an unphrasable box routes onward to S3/S4 for rewrite.

### CHECK D-24 — Smoke-test structural completeness
- **Hardens:** A.3; mechanizes S5-X3 and S5-X5
- **Tier:** D (D+L on untagged specs, via EXT-6)
- **Inputs:** G-ST; R-IS; C-DM; X-WE
- **Procedure:**
  1. G-ST exists and is script-shaped: ordered executable steps, not prose claims that a test "can be run" (symphony's §17.8 fails here).
  2. Every scenario contains ≥1 `ASSERT`; every ASSERT compares against a concrete expected literal and carries `[checks:]`.
  3. Public-surface closure: every call in the script resolves to an R-IS surface element (no internal reach-ins, no phantom entry points — attractor's `run_pipeline`); every ASSERT operand passes D-08 field resolution (attractor's `outcome.completed_nodes`).
  4. Test vectors promoted from X-WE cite their source example (dashed G-ST→X-WE edge).
- **Metric:** `st_assert_coverage` = scenarios with ≥1 conforming ASSERT ÷ scenarios, threshold 1.0; secondary `st_public_closure` = resolving calls/operands ÷ calls/operands, threshold 1.0.
- **Output:** evidence rows `{scenario|assert, defect}`.
- **Failure semantics:** the smoke test is the oracle that bounds the one-shot search (README §4.1.1); a non-executable or phantom-referencing script is a broken oracle. Class GATE_GAP → S5.

### CHECK D-25 — Conformance-matrix and profile-tag completeness
- **Hardens:** A.4, A.5
- **Tier:** D (D+L on untagged specs, via EXT-6)
- **Inputs:** G-CM; A-VS/R-IS/R-FR (variation-axis declarations); ledger (waiver)
- **Procedure:**
  1. Trigger: a variation axis is declared (per-provider realization in R-IS, optional features in R-FR/A-VS, platform targets). If none: a logged G-CM waiver must exist (process S2/S5); waiver present → PASS-waived.
  2. If triggered: the matrix covers every axis value × every shared requirement — no empty cells; per-variant deltas are ordinary G-AC boxes (coding-agent-loop's §9.12/§9.2 division).
  3. Every cell/profile tag cites the axis-creating element and the requirement it crosses (G-CM's citation obligation).
  4. Profile totality: every gate item carries a profile tag or defaults to core by the declared lexical convention; the convention itself is declared (symphony's "If … is implemented" rule).
- **Metric:** `cm_completeness` = filled, cited cells ÷ (axis values × shared requirements), threshold 1.0; boolean `profile_totality`.
- **Output:** evidence rows `{cell|item, missing}`.
- **Failure semantics:** an empty cell is a variant × requirement combination no build will be graded on — parity holes surface as provider-specific bugs post-freeze. Class GATE_GAP → S5.

### CHECK D-26 — Worked-example coverage
- **Hardens:** I.1, I.2 (count half); mechanizes S4-X6
- **Tier:** D (D+L on untagged specs, via EXT-4 + EXT-6)
- **Inputs:** X-WE; R-IS (format surfaces)
- **Procedure:**
  1. Enumerate format surfaces: every R-IS grammar, wire format, file format, and structured-input parameter.
  2. Each surface has ≥1 complete, realistic, copy-pasteable sample input (not a fragment — completeness = parseable as a whole document per D-27).
  3. Each parsing boundary has ≥1 worked input→output pair ("Alice is 30" → `{"name":"Alice","age":30}`).
- **Metric:** `xwe_coverage` = surfaces with sample **and** boundary pairs ÷ surfaces, threshold 1.0.
- **Output:** evidence rows `{surface, missing: sample|io_pair}`.
- **Failure semantics:** examples cluster where prose is weakest (README §2.1-I); a surface without one is a parser the builder writes from prose alone. Class REALIZATION_GAP → S4.

### CHECK D-27 — Example parse validity
- **Hardens:** I.2 (validity half)
- **Tier:** D where the surface grammar is machine-readable; the residue escalates to an L-03 trace vector
- **Inputs:** X-WE samples; R-IS grammars
- **Procedure:**
  1. For each sample: if its surface has a formal grammar (BNF, JSON, declared file format), parse the sample against it; failure → FAIL row (either the sample or the grammar is wrong — T4 within Layer 2, attractor's `evaluate_clause` vs. its own §10.2 grammar is the shape).
  2. If the surface has no machine-readable grammar, emit a `needs_trace` row: the sample becomes a mandatory L-03 vector instead (checked by traced execution, not parsing).
- **Metric:** `example_validity` = samples parsing (or trace-passing) ÷ samples, threshold 1.0.
- **Output:** evidence rows `{sample, surface, error | needs_trace}`.
- **Failure semantics:** an example the spec's own grammar rejects poisons the strongest teaching instrument the spec has. Class LINT → S6 (sample typo) or REALIZATION_GAP → S4 (grammar wrong — reclassification rule).

### CHECK D-28 — Compilation order and ToC integrity
- **Hardens:** I.3
- **Tier:** D
- **Inputs:** `dist/spec.md`
- **Procedure:**
  1. Section order matches artifact-model §6.1's slot ordering (which encodes types-before-behavior and conformance-last); a section out of slot → violation.
  2. A linked ToC exists; every ToC link resolves to an anchor in the file; every H2 appears in the ToC.
  3. Derived views are marked derived (§6.3 rule — feeds D-21).
- **Metric:** `slot_order_violations` = 0; secondary `toc_broken_links` = 0.
- **Output:** evidence rows `{section|link, defect}`.
- **Failure semantics:** ordering is a retrieval feature for an agent reader (README §2.1-K); breakage is hygiene. Class LINT → S6.

### CHECK D-29 — Annex force check
- **Hardens:** I.4 (deterministic half; L-08 is the body-side classifier)
- **Tier:** D (D+L on untagged specs, via EXT-5's appendix classification)
- **Inputs:** X-DR, X-WE; A-GL (keyword regime)
- **Procedure:**
  1. Scan annex artifacts for the A-GL normative keywords (uppercase or declared-lowercase regime), obligation-declaring element IDs, and `[checks:]` tags — all must be absent (annex carries zero force, T4).
  2. Quote-fenced restatements of body text are exempt when they cite the body element they quote.
  3. Untagged path: classify appendices per EXT-5; a rationale appendix asserting a mandate is the coding-agent-loop Appendix C defect.
- **Metric:** `annex_force_hits` = 0 (mechanizes S6-X5).
- **Output:** evidence rows `{annex, locus, quote}`.
- **Failure semantics:** annex text amending a mandate is a latent contradiction with a defined loser (T4: the body wins) — but the conflict itself must still be fixed. Class LINT → S6; if body and annex genuinely disagree on behavior, CONTRACT_GAP → S3 (the byte-for-byte case).

## 2. Extraction and hybrid checks

### 2.1 Inventory extraction (EXT-1…EXT-6)

The framework §4 acquisition rule in executable form. On tagged specs every inventory
below is a grep/parse over the artifact files (the "Tagged source" column); on untagged
specs it is produced by `k_extract = 3` ephemeral sessions under the shared template,
canonicalized, and gated at `S_extract` pairwise agreement before any Tier-D
verification consumes it. All Tier-L constraint rules (framework §5) apply.

| ID | Inventory (JSON schema sketch) | Tagged source |
|---|---|---|
| EXT-1 | domain: `records[{name, fields[{name, type, nullable, constraints[], configurable}]}]`, `enums[{name, values[{value, semantics}], delegated_to?}]`, `terms[{term, definition_locus}]` | C-DM records/enums, A-GL terms |
| EXT-2 | behavior: `operations[{name, locus}]`, `machines[{name, states[], events[], transitions[{state, event, target\|impossible}]}]`, `precedence_rules[{name, criteria[], tiebreak?}]`, `numeric_claims[{claim, locus, formula?}]`, `order_idem[{operation, ordering?, idempotency?}]`, `invariants[{text, predicate?, locus}]`, `concurrency[{construct, guarantee?, mechanism?, cancellation?, result_order?}]` | C-BC element IDs by kind; C-QC concurrency elements |
| EXT-3 | failure: `classes[{name, retryability?, blast_radius?}]`, `failure_refs[{locus, class?}]`, `timeouts[{name, scope?, default?, expiry?}]`, `boundaries[{surface, case, behavior?}]` | C-FM; R-CD timeout knobs |
| EXT-4 | surface: `signatures[{name, params[{name,type}], returns, errors[]}]`, `blocks[{tool, params?, returns?, errors[]}]`, `routes[{method, path, statuses[], req_example?, resp_example?}]`, `grammars[{name, formal}]`, `config[{key, default?, locus, chain?}]`, `helpers_invoked[{name, locus}]`, `field_accesses[{record, field, locus}]`, `externals[{name, locus}]` | R-IS, R-RA, R-CD |
| EXT-5 | scope/freedom: `goals[{name?, text}]`, `non_goals[{text, extension_point?}]`, `boundary_notes[]`, `register[{name, scope?, pin_or_discovery?, conflict_rule?, kind}]`, `freedoms[{choice, bound_citation?, doc_obligation?, marker_locus}]`, `appendix_classes[{section, kind: rationale\|examples\|normative}]` | A-VS, R-FR, X-DR/X-WE |
| EXT-6 | gate: `boxes[{text, citations[], checkbox}]`, `framing_line?`, `matrix{axes[], rows[], cells[{axis, row, filled, citation?}]}`, `profiles[{name, convention}]`, `smoke{steps[], asserts[{text, expected?, citation?}], calls[]}` | G-AC, G-CM, G-ST |

**Shared extraction template** (pinned, v1 — the bracketed slots are filled verbatim
from the table row; nothing else varies):

> You are given a specification document (attached; your only context). Produce a JSON
> inventory of **[inventory description from the EXT row]**, conforming exactly to this
> schema: [schema from the EXT row]. Rules: enumerate exhaustively — include entries you
> consider obvious; copy identifiers verbatim (no normalization, no renaming); for every
> entry include the line number or quoted anchor where it is defined; leave a field null
> rather than guessing; do not deduplicate near-identical entries — list both. Output
> the JSON only.

Ingestion: canonicalize (sort keys, strip whitespace, case-fold nothing — identifiers
are case-significant), compute pairwise agreement over entry keys, apply the framework
§4 stability gate, proceed on the intersection with union-minus-intersection attached
as disputed-territory evidence.

### CHECK DL-01 — Precedence and resolution-chain totality
- **Hardens:** B.3, E.2
- **Tier:** D+L
- **Inputs:** EXT-2 `precedence_rules` (C-BC half, run at S3); EXT-4 `config[].chain` (R-CD half, run at S4)
- **Procedure:**
  1. *(L)* Extract every precedence/priority/resolution rule with its ordered criteria and tie-break.
  2. *(D)* Each rule has ≥1 criterion and an explicit final tie-break; the tie-break's key is declared unique in C-DM (id-like) or is a total lexical order — otherwise the order is partial.
  3. *(D)* No open-ended markers inside the criteria list (`etc.`, `and so on`, trailing `…`).
  4. *(D)* Config resolution chains: every source that can supply the knob appears exactly once in the chain (a source outside the chain is an unordered pair).
- **Metric:** `precedence_totality` = rules with a strict total order ÷ rules, threshold 1.0.
- **Why extraction is L:** recognizing that a prose passage *states* a priority scheme requires reading; the totality verdict over the extracted list is pure set arithmetic.
- **Output:** evidence rows `{rule, defect: no_tiebreak|nonunique_key|open_list|unordered_source}`.
- **Failure semantics:** two builders sorting the same candidates differently is observable divergence by construction (the §4.3 BLOCKER test). Class CONTRACT_GAP → S3 (C-BC rules) / REALIZATION_GAP → S4 (R-CD chains).

### CHECK DL-02 — Numeric-behavior formula closure
- **Hardens:** B.4
- **Tier:** D+L
- **Inputs:** EXT-2 `numeric_claims`
- **Procedure:**
  1. *(L)* Extract every claim that behavior varies with a number: backoff, limits, thresholds, quotas, sizes, estimates, sampling.
  2. *(D)* Each claim carries an exact formula (arithmetic over named C-DM/R-CD identifiers — parseable expression), an exact constant with units, or a `[freedom:]` tag.
  3. *(D)* Formula identifiers resolve (D-09); constants that configure resolve to R-CD (D-05).
  4. *(D)* Adjective-only quantification (`fast`, `small`, `a reasonable delay`) is an open cell — and a D-12 hit.
- **Metric:** `formula_closure` = claims with formula/constant/freedom ÷ claims, threshold 1.0.
- **Why extraction is L:** deciding that a sentence makes a numeric-behavioral commitment (vs. describing one) is semantic; the formula-presence verdict is a parse.
- **Output:** evidence rows `{claim, locus}` (unified-llm's `reasoning_tokens` "estimated" with no estimator).
- **Failure semantics:** un-formularized numbers diverge silently and are ungateable (the "accurate token counts" parity cell is unverifiable *because* the estimate has no formula). Class CONTRACT_GAP → S3 (observable-value formulas are C-BC per artifact-model §2.1 delta 4).

### CHECK DL-03 — Ordering and idempotency declaration closure
- **Hardens:** B.5
- **Tier:** D+L
- **Inputs:** EXT-2 `operations`, `order_idem`
- **Procedure:**
  1. *(L)* Extract the operation inventory and every stated ordering/idempotency clause.
  2. *(D)* Every operation has an idempotency cell ∈ {idempotent, not-idempotent, N/A + reason}.
  3. *(D)* Every operation pair that the extraction marks as interacting (shared state or declared sequence) has an ordering cell: an explicit "X before Y" / "unordered" declaration.
  4. *(D)* Parallel-execution constructs must declare result ordering (feeds DL-04's cell).
- **Metric:** `order_idem_closure` = filled cells ÷ cells, threshold 1.0.
- **Why extraction is L:** identifying which operations interact through shared state is a comprehension task; cell accounting is deterministic.
- **Output:** evidence rows `{operation(s), missing: idempotency|ordering}` (coding-agent-loop's unstated `AWAIT_ALL` result-ordering).
- **Failure semantics:** unordered interacting operations are a race the spec authorized by silence. Class CONTRACT_GAP → S3.

### CHECK DL-04 — Concurrency closure
- **Hardens:** B.6
- **Tier:** D+L
- **Inputs:** EXT-2 `concurrency`
- **Procedure:**
  1. *(L)* Extract every concurrency construct: parallel execution sites, shared mutable state, background loops, cancellation points, "single-authority"/serialization claims.
  2. *(D)* Per construct, four cells, each filled or explicit N/A: **guarantee** (what is serialized/atomic/isolated), **permitted mechanism** (named mechanism, or `[freedom:]` to an R-FR entry bounding it), **cancellation semantics** (who cancels, when observed, state after), **result ordering**.
  3. *(D)* A guarantee whose mechanism cell is empty and unregistered is exactly README §2.3 defect class 1 — flag with its own evidence kind.
- **Metric:** `concurrency_closure` = filled cells ÷ (constructs × 4), threshold 1.0.
- **Why extraction is L:** concurrency constructs hide in prose ("others may be cancelled"); no token pattern finds them reliably. The cell audit is deterministic.
- **Output:** evidence rows `{construct, empty_cell}` (attractor's parallel handler: mechanism, cancellation both empty; symphony's single-authority: mechanism empty and unregistered).
- **Failure semantics:** the corpus's #1 residual-defect zone. Class CONTRACT_GAP → S3 (guarantee/cancellation/ordering are contract; a mechanism deliberately left open must become an R-FR entry).

### CHECK DL-05 — Invariant checkability and gate linkage
- **Hardens:** B.7
- **Tier:** D+L
- **Inputs:** EXT-2 `invariants`; G-AC citations (gate half, run at S5)
- **Procedure:**
  1. *(L)* Extract every invariant: numbered lists plus prose "always/never/at most/exactly" claims.
  2. *(D)* Each invariant has a validation predicate over C-DM terms — an expression a test could evaluate (`cwd == workspace_path`; `LLM calls ≤ max_tool_rounds + 1`). Prose with no predicate → unverifiable invariant.
  3. *(D)* Each invariant is cited by ≥1 gate item (`[checks:]` — T5 over the invariant subset).
- **Metric:** `invariant_closure` = invariants with predicate **and** gate citation ÷ invariants, threshold 1.0.
- **Why extraction is L:** distinguishing an invariant from ordinary description is semantic; predicate-presence and citation lookup are deterministic.
- **Output:** evidence rows `{invariant, missing: predicate|gate}`.
- **Failure semantics:** an invariant with no predicate cannot fail a build; one with no gate box never gets asked. Class CONTRACT_GAP → S3 (predicate) / GATE_GAP → S5 (linkage).

### CHECK DL-06 — Constraint locality
- **Hardens:** C.3
- **Tier:** D+L
- **Inputs:** EXT-1 `records[].fields[].constraints`; EXT-2/EXT-4 (constraints asserted in behavior/interface prose)
- **Procedure:**
  1. *(L)* Extract every field constraint asserted anywhere outside the field's definition: ranges, formats, derivations, nullability claims, uniqueness.
  2. *(D)* Each remotely-asserted constraint also appears at the field's C-DM definition line (inline-with-the-field, §3.C.3's actual demand).
  3. *(D)* Two constraints on the same field that cannot both hold → contradiction evidence (feeds L-06 triage).
- **Metric:** `constraint_locality` = remotely-asserted constraints present at definition ÷ remotely-asserted constraints, threshold 1.0.
- **Why extraction is L:** finding constraint assertions buried in behavioral prose is a reading task; the co-location verdict is a lookup.
- **Output:** evidence rows `{field, constraint, remote_locus}`.
- **Failure semantics:** a constraint the builder only meets while reading a distant section is a constraint half the builds miss. Class CONTRACT_GAP → S3.

### CHECK DL-07 — Boundary-case coverage
- **Hardens:** F.4
- **Tier:** D+L
- **Inputs:** EXT-3 `boundaries`; EXT-4 (input surfaces)
- **Procedure:**
  1. *(L)* Extract the input surfaces (formats, collections, sizes, counts, identifiers) and every named boundary case with its behavior.
  2. *(D)* Per surface, a row per boundary class {empty, oversized, malformed, duplicate, zero/negative}: filled by named behavior — ideally with the motivating pathological input quoted — or explicit N/A.
  3. *(D)* A boundary case named without behavior ("watch out for huge lines") is an open cell, not coverage.
- **Metric:** `boundary_closure` = filled cells ÷ (surfaces × 5), threshold 1.0.
- **Why extraction is L:** what counts as an input surface, and which prose names a boundary case, requires comprehension; the grid audit is deterministic.
- **Output:** evidence rows `{surface, class}` (the gold exemplar cell: coding-agent-loop's "2-line file where each line is a 10MB CSV").
- **Failure semantics:** boundary silence turns into per-build improvisation at the exact inputs that break systems. Class CONTRACT_GAP → S3.

### CHECK DL-08 — Timeout closure
- **Hardens:** F.5
- **Tier:** D+L
- **Inputs:** EXT-3 `timeouts`; R-CD; C-FM
- **Procedure:**
  1. *(L)* Extract every timeout/deadline/stall mention.
  2. *(D)* The spec declares its timeout scope set (connect / request / stream-read / stall / custom, per its domain); every extracted timeout carries a scope from that set.
  3. *(D)* Per timeout, three cells: scope, default (resolves to R-CD — D-05's pair), and expiry semantics in C-FM (what expiry *means*, plus the kill-escalation sequence where a process is involved — SIGTERM → grace → SIGKILL is the exemplar shape).
- **Metric:** `timeout_closure` = filled cells ÷ (timeouts × 3), threshold 1.0.
- **Why extraction is L:** timeouts hide as "eventually", "hangs", "too long" in prose; the cell audit is deterministic.
- **Output:** evidence rows `{timeout, missing: scope|default|expiry}`.
- **Failure semantics:** an unscoped timeout gets attached to the wrong operation; a default-less one diverges; expiry without semantics leaks resources. Class CONTRACT_GAP → S3 (semantics) / REALIZATION_GAP → S4 (missing default).

## 3. Reader probes (L-01…L-09)

All blocks inherit the framework §5 constraint rules: ephemeral session, zero author
context, context = the named slice only, pinned template (v2 templates below supersede
process §4.7's v1 charters where one exists; ingestion and routing stay with
process.md), schema-validated output, k + aggregation as stated, evidence pointers
mandatory, reports archived verbatim under `probes/`.

### CHECK L-01 — Question-count probe (P-QCOUNT v2)
- **Hardens:** C.3, F.4 primarily; cross-cutting residual detector for every §3 section
- **Tier:** L
- **Context slice:** in-process (S3): current drafts of A-VS, A-GL, C-DM, C-BC, C-FM, C-QC, R-FR. Standalone grading: `dist/spec.md` (or the external spec file) only.
- **Template (pinned, v2 — prompt text identical to process §4.7 v1):**
  > You must implement the system described by the attached documents, alone, with no
  > ability to ask anyone anything. Read them, then list **every question you would
  > need answered** before you could implement with confidence that the result matches
  > the authors' intent. For each question give: (1) the question; (2) the passage or
  > element ID it concerns (quote if no ID); (3) why the documents as written cannot
  > answer it; (4) what you would do if forced to guess. Do not propose fixes, do not
  > summarize the documents, and do not stop early — an empty answer is only acceptable
  > if you could genuinely start implementing now.
- **Output schema:** rows `{question: string, locus: string (element ID or verbatim quote), why_unanswerable: string, forced_guess: string}`. Rows without a locus are dropped and counted (framework §5.6).
- **k / aggregation:** in-process, k = 1 per S3 iteration — replication is sequential via `D_dry = 2` (process §9.1). Standalone, `k_L = 3`, **union after dedupe** (dedupe key: same locus + same forced choice, process §4.2's duplicate rule).
- **Metric:** `new_q(sev)` per probe (process §9.2), severity graded at ingestion by the AUTHOR per §4.3 using `forced_guess` as evidence. Threshold, finished spec: new BLOCKER + MAJOR = 0. During S3: the §9.3 burn-down contract governs the trend (monotone decrease enforced by `stall-streak`, not by this check).
- **Failure semantics:** each surviving question is triaged normally (INTENT/ARBITRARY/DEFERRABLE); post-S3, any INTENT-shaped question is CONTRACT_GAP → S3 by the INTENT-after-S3 rule (process §8.2).
- **Why not Tier D:** whether a document answers an arbitrary implementation question is comprehension over an unbounded question space; there is no enumerable pattern for "a builder would need to ask here."

### CHECK L-02 — Scenario-divergence probe
- **Hardens:** G.4 primarily; B.5, B.6, F.3, J.4
- **Tier:** L (Tier-D comparison of Tier-L answers)
- **Context slice:** generation phase and answer phase both: `dist/spec.md` (or all normative artifact drafts) only.
- **Procedure:**
  1. *Generation (one session):* produce concrete scenario questions per `N_scenario` (≥1 per C-BC operation, ≥1 per C-FM failure class, plus a scope family for G.4), under this pinned template:
     > From the attached specification only, write concrete scenario questions of two
     > kinds. Kind BEHAVIOR: "Given <fully concrete initial state and input, with
     > literal values>, what observably happens?" — one per operation the spec defines,
     > one per failure class it names, each answerable from the spec if the spec is
     > complete. Kind SCOPE: "Is <concrete capability> in scope?" — ten candidates a
     > reasonable implementer might wonder about. For each question, name the
     > element/section it targets and the answer schema: the observable outcome as an
     > enum of the spec's own vocabulary or an exact value. Output JSON rows
     > `{kind, question, target, answer_schema}`.
  2. *Answering:* `k_L = 3` fresh sessions each answer every question from the spec alone, output `{question_id, answer, evidence_locus}`; answers must conform to the question's answer schema.
  3. *(D) Comparison:* per question, canonicalize answers; ≥2 materially distinct answers = divergent. A question the answerers expose as ill-posed (contradictory answer schemas) is INDETERMINATE for that row and evidence for the generator's target.
- **Metric:** `divergence_rate` = divergent questions ÷ questions; threshold: 0 for BEHAVIOR questions targeting contracted elements (an observed divergence *is* the §4.3 BLOCKER test passing empirically), 0 for SCOPE questions (each divergence = a missing A-VS boundary note).
- **Failure semantics:** BEHAVIOR divergence → CONTRACT_GAP → S3 at the question's target (the pre-build twin of S7's CONTRACTED_DIVERGENCE); SCOPE divergence → INTENT_GAP (scope-level) → S1.
- **Why not Tier D:** answering "what happens when X" from prose requires semantic entailment; only the answer comparison is mechanical.

### CHECK L-03 — Determinism trace
- **Hardens:** B.1, B.3, B.4, A.3; supports I.5, J.4
- **Tier:** L (Tier-D exact-match over Tier-L outputs)
- **Context slice:** the target R-RA algorithm (or G-ST script) + every artifact section it cites (`[realizes:]` targets, invoked R-IS signatures, relevant C-DM records) + A-GL. Nothing else.
- **Vectors:** per `N_trace` — ≥1 per R-RA algorithm, ≥2 where the algorithm branches on enum values (one per arm floor); vectors promoted from X-WE where available (cite the source example), else constructed as concrete literals and recorded with the check.
- **Template (pinned, v1):**
  > Execute the attached pseudocode algorithm by hand on the input below. Produce a
  > numbered trace: for every step, the step number, the concrete values of every
  > variable the step reads or writes, and any output/effect emitted. Use only the
  > attached documents to resolve any term or helper the pseudocode references; if a
  > step cannot be executed because something is undefined or ambiguous, stop and
  > report BLOCKED with the exact identifier and locus. Do not repair, assume, or
  > improvise. Input: [vector]. Output JSON: `{steps: [{n, reads, writes, emits}],
  > result, blocked: null | {identifier, locus, why}}`.
- **k / aggregation:** `k_L = 3` per vector; **exact match required** on `result` and on emitted observables (intermediate wording is free). Any mismatch = FAIL with the diff as evidence; any BLOCKED = FAIL with the identifier (this is how undefined helpers/fields manifest as behavior, not just as lint).
- **Metric:** `trace_match` = vectors with 3/3 identical results ÷ vectors, threshold 1.0.
- **Failure semantics:** mismatch = the pseudocode under-determines its own output — CONTRACT_GAP → S3 if the ambiguity is in the contracted rule, REALIZATION_GAP → S4 if in the witness; BLOCKED routes with the blocking identifier (usually joins a D-06/D-08 finding).
- **Why not Tier D:** the pseudocode's steps deliberately lean on prose-defined semantics (it is a spec, not code), so execution requires interpreting natural language; the equality check on outputs is Tier D.

### CHECK L-04 — Assumption probe (P-ASSUME v2)
- **Hardens:** G.1, G.2, G.4
- **Tier:** L
- **Context slice:** in-process (S1): `idea-record.md`; on re-probes within S1, plus the current A-VS draft (process §4.7's rationale). Standalone grading: the spec's A-VS (or overview/scope sections) withheld — the probe reads `idea-record.md`-equivalent intent material only, so the spec's scope fence can be graded against ignorant expectations.
- **Template (pinned, v2 — prompt text identical to process §4.7 v1):**
  > Here is an idea for a system. List everything you would assume is **included in
  > scope** if you were asked to build it — features, users, integrations, data
  > handled, qualities (performance, security, persistence), and operational surface
  > (deployment, configuration, monitoring). One assumption per row, categorized
  > {feature, user, integration, data, quality, operational}. Be exhaustive, and
  > include the assumptions you consider too obvious to state. Do not design the
  > system, and do not rank or filter — completeness is the deliverable.
- **Output schema:** rows `{assumption, category}`.
- **k / aggregation:** in-process, k = 1 per S1 pass (S1-X1's 1-clean-probe constant, process §9.1). Standalone, `k_L = 3`, union after dedupe (same-scope-item).
- **Mapping step (standalone):** a second-stage session (context: the assumption list + A-VS + R-FR) maps each assumption to {goal | non-goal | boundary note | R-FR entry | UNMAPPED}, k = 3, majority per row. `scope_closure` = mapped ÷ assumptions, threshold 1.0; every UNMAPPED row is a finding. In-process, mapping is the S1 owner disposition itself.
- **Failure semantics:** an unmapped assumption is scope the owner never dispositioned. Class INTENT_GAP (scope-level) → S1.
- **Why not Tier D:** enumerating what a reader would *assume unstated* is generative — the interesting rows are precisely the ones no text mentions.

### CHECK L-05 — Gate entailment and decidability
- **Hardens:** A.2 (the deciding instrument behind D-23's screen); supports A.3
- **Tier:** L
- **Context slice:** per gate item: the box/cell/ASSERT text + the full text of the elements it cites (`[checks:]` targets) + A-GL. Deliberately nothing else — a box that needs more context than its citations is exactly what this check exists to catch.
- **Template (pinned, v1):**
  > Below is one acceptance-checklist item from a specification, together with every
  > specification passage it cites. Answer three questions strictly from this material:
  > (1) DECIDABLE — could you write an automated test that asserts this item, using
  > only what is given? If yes, sketch the assertion (pseudocode, one block). If no,
  > name exactly what is missing. (2) ENTAILED — does the cited material actually
  > state the obligation this item checks, with the same strength and the same values?
  > If not, quote the mismatch. (3) EVIDENCE — the locus for each answer. Output JSON:
  > `{decidable: bool, assertion_sketch: string|null, missing: string|null,
  > entailed: bool, mismatch: string|null, loci: [string]}`.
- **k / aggregation:** `k_L = 3` per gate item, **majority** per verdict with agreement floor `A_min = 2/3`; below floor → INDETERMINATE (the item is unclear enough that verifiers disagree — itself a finding).
- **Metric:** `checkable_rate` = gate items decidable **and** entailed ÷ gate items (hardens process S5-X2's `checkable_rate`), threshold 1.0.
- **Failure semantics:** not-decidable → GATE_GAP → S5, and per the S5 resistance rule the underlying claim routes to S3/S4 for rewrite; not-entailed → GATE_GAP → S5 under T4 (the gate never creates obligations — coding-agent-loop's `"xhigh"` box, symphony's JSON-line-protocol box); missing-definition verdicts also join D-09's term findings (unified-llm's "stable conversation prefix").
- **Why not Tier D:** entailment between a checkbox and cited prose is a semantic judgment; D-23's lexicon catches only the flagrant cases.

### CHECK L-06 — Contradiction sweep
- **Hardens:** J.4; supports I.5 (redundant statements must agree)
- **Tier:** L
- **Context slice:** `dist/spec.md` (or all normative artifacts + annexes, labeled per artifact).
- **Template (pinned, v1):**
  > Read the attached specification looking for one thing only: pairs of passages that
  > cannot both be satisfied by a single implementation. Include: body vs. body, gate
  > vs. body, appendix/rationale vs. body, example vs. rule, and redundant restatements
  > that drifted apart. For each pair output: the two loci (quote each passage), why
  > they conflict (one sentence naming the observable behavior on which they disagree),
  > and which reading each of two reasonable implementers would take. Do not report
  > stylistic tension or redundancy that agrees. Output JSON rows:
  > `{locus_a, quote_a, locus_b, quote_b, conflict, reading_1, reading_2}`.
- **k / aggregation:** `k_L = 3`, **union after dedupe** (dedupe key: unordered locus pair). Each unioned finding is then confirmed at triage (AUTHOR verifies the two quotes actually conflict — a cheap human/Tier-D-ish confirmation that kills hallucinated pairs before routing).
- **Metric:** `confirmed_contradictions` = triage-confirmed pairs, threshold 0.
- **Failure semantics:** T4 with the precedence rule as triage (body > gate, normative > annex — the loser is the defect's locus, but the pair is fixed, not just re-ranked). Class per pair: gate-vs-body → GATE_GAP → S5; annex-vs-body → LINT → S6 or CONTRACT_GAP → S3 where behavior genuinely differs (byte-for-byte vs. behavioral-alignment); body-vs-body → CONTRACT_GAP → S3.
- **Why not Tier D:** contradictions rarely share tokens ("byte for byte" vs. "behavioral alignment" collide only in meaning); string comparison cannot see them.

### CHECK L-07 — Implementation probe (P-IMPL v2)
- **Hardens:** B.6, D.1, H.1 (the empirical detector for all three)
- **Tier:** L
- **Context slice:** all Layer-0–2 artifact drafts (A-VS, A-GL, C-*, R-*). Module selection: deterministic rule per process §4.7 (highest count of distinct `[realizes:]` C-BC citations; tie → primary-flow component, then lexical; iteration *j* probes the *j*-th ranked, wrapping).
- **Template (pinned, v2 — prompt text identical to process §4.7 v1):**
  > Implement the module named below, in a language of your choice, using only the
  > attached documents. Complete the implementation even where the documents are
  > silent — but keep an **invention log**: every decision you had to make that the
  > documents did not determine. For each: (1) the decision point; (2) the choice you
  > made; (3) an alternative another implementer might plausibly choose; (4) the
  > observable consequence if they did. Deliver the module and the log. The log is the
  > deliverable that matters; the code will be discarded.
- **Output schema:** invention rows `{decision_point, choice, plausible_alternative, observable_consequence, locus}` + the module (archived, discarded). The S7 BUILDER charter (process §4.7) reuses this invention-log schema verbatim, plus the G-ST self-run transcript it already requires.
- **k / aggregation:** in-process, k = 1 per S4 iteration (S4-X3's 1-clean-probe constant; successive iterations broaden module coverage). Standalone, 2 probes over the 2 highest-ranked modules, union of logs.
- **Metric:** `inventions(sev)` (process §9.2), severity at ingestion; threshold: BLOCKER inventions = 0 (S4-X3).
- **Failure semantics:** each invention triages normally (process S4 activity 5): ARBITRARY → owning R-artifact; DEFERRABLE → R-FR via scoped S3 re-entry; INTENT → escalate as CONTRACT_GAP evidence (§8.2's INTENT-after-S3 rule).
- **Why not Tier D:** the check *is* the act of generation — only an attempt to build reveals which decisions the documents fail to determine.

### CHECK L-08 — Rationale-leak classifier
- **Hardens:** I.4 (body half; D-29 is the annex half)
- **Tier:** L
- **Context slice:** normative artifacts only (C-*, R-*, G-*), labeled per artifact.
- **Template (pinned, v1):**
  > The attached documents are the normative body of a specification: every sentence
  > should prescribe or define. Flag passages that instead explain or persuade —
  > design rationale, rejected alternatives, historical notes, comparisons, "because"
  > justifications — i.e. text that could move to a non-normative appendix without
  > changing what a conforming implementation is. Quote each passage exactly, with its
  > locus, and classify it {rationale, history, comparison}. Do not flag definitions,
  > obligations, examples, or cross-references. Output JSON rows:
  > `{locus, quote, kind}`.
- **k / aggregation:** `k_L = 3`, union after dedupe (locus); each finding confirmed at S6's rationale sweep before the move (the move itself must be semantics-preserving or it reclassifies).
- **Metric:** `body_rationale_hits` (confirmed), threshold 0 at freeze-grade; advisory during iteration.
- **Failure semantics:** rationale in the body is a latent T4 contradiction (annex-force in the wrong direction: force where none belongs). Class LINT → S6 (the quarantine move is S6 activity 3); a passage whose removal would change obligations was never rationale — reclassify per §8.1.
- **Why not Tier D:** prescriptive-vs-explanatory is a linguistic classification; keyword lists ("because", "we chose") both over- and under-fire badly.

### CHECK L-09 — Freedom-width probe (T7)
- **Hardens:** E.3, H.1, A.4 (the width half of T7; D-20 is the fields half)
- **Tier:** L
- **Context slice:** per R-FR entry: the entry + its bounding-contract elements + every gate item citing those elements + G-ST. Nothing else.
- **Procedure:**
  1. *Construction (one session per entry):*
     > Below is a declared implementation freedom from a specification, with its
     > bounding contract and the acceptance checks that cite that contract. Construct
     > TWO resolutions of the freedom that are each fully compliant with the bounding
     > contract but as different from each other as you can make them — aim for the
     > extremes of the permitted space. Describe each resolution concretely (what an
     > implementation would observably do). Output JSON:
     > `{resolution_1, resolution_2, compliance_argument_1, compliance_argument_2}`.
  2. *Verdict (per resolution, `k_L = 3`, majority):* given one resolution + the same context slice: "Does an implementation behaving this way pass every attached acceptance item and smoke-test expectation? Answer per item: PASS/FAIL with the item quoted." Schema: `{items: [{item, verdict, why}], escapes_bound: bool}`.
  3. *(D) Comparison:* entry is too wide iff the two resolutions' per-item verdict vectors differ, or either `escapes_bound` (majority) is true.
- **Metric:** `width_violations` = entries whose extremes flip any gate outcome or escape the bound, threshold 0.
- **Failure semantics:** FREEDOM_T7 by definition (process §4.8) — the entry is narrowed. Class CONTRACT_GAP → S3 (symphony's Codex safety posture is the corpus case: bounded only by "MUST document" + a liveness invariant, wide enough to flip Real-Integration outcomes).
- **Why not Tier D:** constructing extreme-but-compliant resolutions is generative design work; only the verdict-vector comparison is mechanical.

## 4. Gate-adequacy (mutation) checks (M-01…M-02)

The strongest and most expensive probes. Everything in §1–§3 checks the *body*; these
check the *gate*: seed deliberate spec-violations and verify G-AC + G-ST catch each
one. A surviving mutant is a named hole in the gate. Shared **mutant taxonomy** (v1,
six classes — the divergence and defect shapes the corpus actually produced):
`wrong_default`, `skipped_ordering_guarantee`, `missing_failure_handling`,
`off_by_one_formula`, `violated_invariant`, `widened_freedom` (a freedom exercised
outside its R-FR bound). `N_mut` = ≥2 mutants per class, ≥12 total.

### CHECK M-01 — Mutation kill rate (cheap variant: behavior descriptions)
- **Hardens:** A.1, A.2, A.4, A.5, B.7
- **Tier:** L+D
- **Inputs:** `dist/spec.md`; its G-AC, G-CM, G-ST
- **Procedure:**
  1. *Generation (L, one session per class):*
     > Below is a specification and one violation class: [class + one-line definition].
     > Write [n] mutants. Each mutant is a description of an implementation that
     > satisfies the specification everywhere EXCEPT one seeded violation of this
     > class: name the element violated (ID or quote), state exactly what the mutant
     > implementation observably does instead, and keep everything else conforming.
     > Make the violations realistic — the mistake a hurried implementer would make,
     > not a caricature. Output JSON rows: `{class, mutated_element, mutant_behavior,
     > why_violates}`.
  2. *Validity screen (D + triage):* reject mutants whose `mutated_element` doesn't resolve (D-09) or whose violation restates another class; regenerate to quota.
  3. *Grading (L, `k_L = 3` per mutant, majority per gate item):* graders receive the gate sections + one mutant description: "Walk every acceptance item and smoke-test expectation against an implementation behaving as described. Output every item that FAILS, with the item quoted; if none fail, say SURVIVED." Schema: `{failed_items: [{item, why}], survived: bool}`.
  4. *(D) Scoring:* mutant killed iff ≥1 gate item fails by majority. Cross-check every survivor against `gate_coverage` (D-22): a survivor whose mutated element has no citing box is a confirmed T5 hole; a survivor *with* a citing box means the box is too weak — both are named holes.
- **Metric:** `kill_rate` = killed ÷ valid mutants; threshold `kill_min` = 1.0 at freeze-grade, 0.90 advisory during iteration.
- **Output:** evidence rows per survivor `{class, mutated_element, mutant_behavior, citing_boxes}`.
- **Failure semantics:** every survivor is GATE_GAP → S5 (add/strengthen the box citing the element); if the violated behavior turns out to be contracted nowhere, the body element is created first via S3/S4 — the gate never creates obligations (T4).
- **Why not Tier D:** inventing realistic violations is generative, and grading a described behavior against prose checkboxes is entailment; only scoring and the coverage cross-check are mechanical.

### CHECK M-02 — Mutation kill rate (full variant: real implementation)
- **Hardens:** A.1, A.3 (the executable half M-01 cannot reach)
- **Tier:** L+D
- **Inputs:** `dist/spec.md`; a conforming base implementation (an S7 build that passed, or for gold specs an OSS implementation, e.g. one of the attractor implementations); the grading harness from the ledger (S7-E2)
- **Procedure:**
  1. *Generation (L):* per taxonomy class, produce ≥2 code-level mutations of the base implementation — a minimal diff seeding exactly one violation; same realism rule and schema as M-01 plus `{diff}`.
  2. *Validity screen:* the mutant must build/start; a mutant dead on arrival is replaced (crashes are not gate kills — they are luck).
  3. *(D) Grading:* execute G-ST verbatim against each mutant; walk G-AC (mechanical boxes scripted; any box already flagged by L-05 as judgment-shaped is excluded from kill credit — a gate should not get credit for boxes only a human can fail).
  4. *(D) Scoring:* as M-01, including the D-22 cross-check.
- **Metric:** `kill_rate`, same thresholds as M-01.
- **Output:** as M-01, plus the surviving mutants' diffs.
- **Failure semantics:** as M-01. A mutant G-ST *should* catch but doesn't because the script never exercises the mutated path additionally routes as G-ST coverage GATE_GAP → S5.
- **Why not Tier D:** mutation generation requires understanding what the spec forbids well enough to violate it minimally; execution and scoring are Tier D — which is exactly why this variant is the strongest instrument the suite has.

## 5. Human check (H-01)

### CHECK H-01 — Owner behavior acceptance
- **Hardens:** G.1 (that the stated goals are the *owner's* goals, observed in behavior)
- **Tier:** H
- **Inputs:** S7 round summary: G-ST transcripts, divergence report, representative build outputs; the A-VS goals
- **Procedure:**
  1. At each S7 round review (process S7 activity 6), the OWNER is shown, per primary flow: what the passing builds observably do — transcripts and outputs, not descriptions.
  2. The owner answers one question per flow: "Is this what you want?" — with the standing instruction that "it passes all gates" is not evidence, since gate-passing-but-wrong is precisely what this check exists to catch.
  3. Each rejection is recorded verbatim with the behavior sample it rejects.
- **Metric:** `owner_rejections` per round, threshold 0 for freeze eligibility (S7-X1's clean-round requirement inherits this).
- **Output:** rejection rows `{flow, behavior_sample, owner_note}`.
- **Failure semantics:** always the pair (process §8.3): INTENT_GAP → S3 (contract the behavior the owner actually wants — scope-level cases → S1) **and** GATE_GAP → S5 (the gate had no box able to fail it). Fixing only the gate half leaves the next builder guessing again.
- **Why not Tier L:** the pass criterion is unstated intent — P4's limit: probes measure what the documents convey, and this check exists precisely for what the documents failed to encode; an LLM judging "what the owner wants" from the artifacts would be grading the spec against itself. **Why not Tier D:** same, a fortiori — there is no text to compute over.

## §R Residual-defect regression suite

The suite's own acceptance test, per the task definition: a hardened check suite that
would not have flagged the gold specs' audited defects is inadequate. Corpus: the
fourteen audited defects of artifact-model §9 (which subsume every dimension-13 finding
in the four [profiles](../profiles/)), pinned as named cases with **expected firings**.
FT-4 (framework §10) executes this table; a suite revision that stops catching any RD
row is rejected. RD rows are mandatory; the RX extension (beyond-audit defects,
artifact-model §9's second list) is informative but expected to fire as stated.

| Case | Spec — defect (artifact-model §9 row) | Expected firings | Expected class → route |
|---|---|---|---|
| RD-01 | attractor — parallel handler promises bounded concurrency + cancellation; pseudocode is sequential; `execute_subgraph` undefined (#1) | **DL-04** (guarantee/mechanism/cancellation cells), **D-06** (`execute_subgraph`), D-11 (cancellation dangling), L-06 (prose vs. pseudocode), L-03 (BLOCKED trace) | CONTRACT_GAP → S3; REALIZATION_GAP → S4 |
| RD-02 | attractor — manager loop invokes 4 undefined helpers, reads unregistered `context.stack.child.*` keys, narrative-only supervisor (#2) | **D-06** (helpers), **D-09** (unregistered keys), D-10 (pseudocode behavior citing no contract), DL-04 (supervisor mechanism cells) | REALIZATION_GAP → S4; CONTRACT_GAP → S3 |
| RD-03 | attractor — `heuristic_select` sorts on `c.score`/`c.id`, fields Outcome lacks; `serialize_results`, `llm_evaluate` undefined (#3) | **D-08** (phantom fields), **D-06** (helpers), L-03 (BLOCKED trace) | REALIZATION_GAP → S4 |
| RD-04 | coding-agent-loop — §3.1 "byte for byte" vs. Appendix C "behavioral alignment"; DoD tests the softer reading (#4) | **L-06** (annex vs. body), **D-29** (normative force in rationale appendix), L-05 (box not entailed at body strength) | CONTRACT_GAP → S3 (recast as R-FR entry) |
| RD-05 | coding-agent-loop — "mirror the … system prompt structure" DoD item; unpinned reference projects bind conformance (#5) | **D-23** (JW-LEX), **L-05** (not decidable), **D-14** (inspiration-only bound), D-20 (freedom without doc obligation) | GATE_GAP → S5; CONTRACT_GAP → S3 |
| RD-06 | coding-agent-loop — `validate_arguments` invoked, gated, never defined; AWAITING_INPUT trigger informal and unreachable; AWAIT_ALL ordering unstated (#6) | **D-06** (helper), **D-11** (validation obligation unrealized), L-03 (unreachable state in trace), DL-03 (result ordering cell) | REALIZATION_GAP → S4; CONTRACT_GAP → S3 |
| RD-07 | unified-llm — auto-cache "implementation-specific" vs. DoD demanding breakpoints on the undefined "stable conversation prefix" (#7) | **D-09** (term unresolved), **D-20** (bounding citation dangles), **L-05** (box undecidable) | GATE_GAP → S5; CONTRACT_GAP → S3 |
| RD-08 | unified-llm — `reasoning_tokens` "estimated" with no formula vs. parity cell "token counts are accurate" (#8) | **DL-02** (no estimator formula), **L-05** (cell not entailed/decidable), D-23 ("accurate" without value source) | CONTRACT_GAP → S3; GATE_GAP → S5 |
| RD-09 | unified-llm — tool-context injection via magic parameter names; mechanism and collision rules open; no gate box (#9) | **D-11** (mechanism unrealized/unregistered), **D-22** (element uncovered), L-07 (invention at the injection point) | CONTRACT_GAP → S3 |
| RD-10 | unified-llm — no Non-Goals section; content scattered (#10) | **D-15** (non-goals absent, no waiver), L-04 (unmapped scope assumptions) | INTENT_GAP (scope) → S1 |
| RD-11 | symphony — Codex policy enums delegated with discovery procedure, defaults `Implementation-defined` — conforming; residual: safety-posture freedom wide enough to flip Real-Integration outcomes (#11) | D-01, D-13, D-20 all **PASS** (negative control — the delegation pattern is the one the model prescribes); **L-09** fires on entry width | CONTRACT_GAP → S3 (narrow the entry) |
| RD-12 | symphony — eligibility references "the configured assignee"; no such config field exists (#12) | **D-07** (the check's type case), **D-22** (assignee routing uncovered by any gate bullet), L-02 (readers diverge on eligibility) | CONTRACT_GAP → S3 |
| RD-13 | symphony — "single-authority" concurrency mechanism unspecified; tokens extracted "leniently from common field names" (#13) | **DL-04** (mechanism cell empty, unregistered), **D-12** ("leniently", "common field names" ∈ HW-LEX), D-11 (unregistered freedoms), L-05 ("aggregation remains correct" undecidable) | CONTRACT_GAP → S3 |
| RD-14 | symphony — no executable smoke test; §17.8 only asserts one *can* be run (#14) | **D-24** (G-ST not script-shaped / absent) | GATE_GAP → S5 |

Extension set — the eleven beyond-audit defects (artifact-model §9, second list),
informative:

| Case | Defect | Expected firings |
|---|---|---|
| RX-01 | attractor — DoD requires `POST /run`/`GET /status`/`POST /answer`; §9.5 defines disjoint `/pipelines…` routes | L-05 (not entailed), L-06 |
| RX-02 | attractor — parity row "orphan node → warning" vs. lint rule `reachability` = ERROR | L-06 |
| RX-03 | attractor — smoke test asserts `outcome.completed_nodes` (field of Checkpoint, not Outcome) and calls `run_pipeline(...)`, defined nowhere | D-24 (`st_public_closure`), D-08, D-06 |
| RX-04 | attractor — `evaluate_clause` accepts a bare-key clause the §10.2 grammar cannot produce | L-03 (branch unreachable from grammar-conformant vectors), L-06 |
| RX-05 | attractor — grammar production `Direction` consumed by nothing (`rankdir` only in examples) | D-01 (unconsumed vocabulary, applied to grammar productions) |
| RX-06 | attractor — "Complete Attribute Reference" (Appendix A) omits every handler-local knob | D-21 |
| RX-07 | coding-agent-loop — DoD item legislates enum value `"xhigh"` found in no contract | D-09 (gate-cited enum value nonexistent), L-05 (not entailed) |
| RX-08 | coding-agent-loop — AWAITING_INPUT unreachable in the reference algorithm | L-03 (with RD-06) |
| RX-09 | symphony — DoD hardcodes "JSON line protocol" while the body delegates transport framing to Codex | L-05, L-06 |
| RX-10 | symphony — §16.5 passes `turn_number`/`max_turns` into prompt building; §12.1's input contract lists neither | D-08 (fields absent from the contracted input record), D-10 (witness quietly extends the contract) |
| RX-11 | symphony — §17.7 gates a CLI surface no body section specifies | D-22 (`box_citation` — unanchored boxes) |

Reading the table back against the coverage claim: the fourteen mandatory cases
exercise 24 distinct checks across the D, D+L, and L tiers (M and H are absent by
design — they test gate adequacy and owner intent, not existing text defects), and
RD-11 doubles as the suite's negative control — a well-formed delegation must **not**
fire the closure checks, or the suite is measuring pedantry rather than defects.




