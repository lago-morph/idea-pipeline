# Spec: `blind-rubric-profiling`

## Intent

When a task requires comparing several large artifacts (specs, RFCs, design
docs, codebases) to find what they have in common, the naive approaches both
fail: reading them serially in one context blows the context budget and lets
the first artifact anchor the reading of the rest; asking one agent to
"compare these four documents" produces mush. This skill fixes both by
dispatching one agent per artifact, each given the **identical rubric** and
**no visibility into the others' outputs**, then intersecting the results in
the parent context. Because the profiles are produced independently,
convergence across them is evidence, not echo.

Grounded in: this session profiled four ~2,000-line specs (three StrongDM
Attractor specs + OpenAI Symphony) with four parallel Explore agents against
a 14-dimension rubric. The profiles converged on 12 shared attributes and —
because one rubric dimension demanded weaknesses — surfaced real defects in
all four "gold" documents, which became the most reusable output of the whole
analysis.

## Trigger

- Direct: "compare these N documents/specs/designs", "what do these have in
  common?", "profile each of these against the same criteria".
- Proactive: any comparative-analysis task where the artifacts total more
  than ~3,000 lines or there are ≥3 of them.
- Negative: do NOT use for 2 short documents that fit comfortably in one
  context (just read both); do NOT use when the artifacts must be compared
  *interactively* (e.g., diffing two versions line-by-line).

## Inputs

- N artifact locations (files, URLs — fetch URLs to local files first so
  agents read identical bytes).
- The comparison question (what commonality/difference matters).
- Optionally: a hypothesis to test (kept OUT of the rubric wording to avoid
  leading the witnesses).

## Outputs

- N per-artifact profile files (markdown), uniform structure, every claim
  carrying evidence pointers (file:line).
- One synthesis document: commonalities (with per-artifact evidence),
  differences among *successful* artifacts (these identify non-necessary
  attributes), and residual defects found.

## Workflow

1. Fetch all artifacts to local files; record sizes (`wc -lc`). If any
   artifact exceeds ~2,000 lines, note in the brief that the agent must read
   it in chunks.
2. Write ONE rubric. Rules for a good rubric:
   - Dimensions ask about the artifact **as a document**, not a summary of
     its subject ("how are types specified?" not "what types exist?").
   - Every dimension demands (a) a 1–3 sentence assessment, (b) evidence
     with line numbers, (c) at most one short verbatim excerpt.
   - Include one adversarial dimension: "find the 2–3 places where this
     artifact is WEAKEST / least precise." This dimension reliably produces
     the highest-value material.
   - Include a quantitative-stats request (headings, tables, code blocks,
     checklist items) so profiles are comparable numerically.
3. Dispatch N agents in a single message (parallel), one per artifact. Each
   brief contains: the file path, the full rubric verbatim, and the closing
   contract: "Your final message IS the deliverable — return the full
   structured profile as markdown, no preamble." Do NOT tell any agent about
   the other artifacts' contents or your hypothesis.
4. On completion, save each profile verbatim to its own file (they are
   evidence; do not paraphrase them away).
5. Synthesize in the parent context: build the intersection (attributes in
   ALL profiles), the difference set (attributes varying across otherwise
   successful artifacts), and the defect roll-up from the adversarial
   dimension. Where profiles disagree on a seemingly-shared attribute, check
   the evidence pointers before claiming commonality.
6. Re-read the synthesis top-to-bottom once, checking every "all N" claim
   against the individual profiles — universal quantifiers are where drift
   creeps in.

## Concrete examples

**Example 1 (this session).** Four specs fetched via
`curl -sSL -o <name>.md https://raw.githubusercontent.com/strongdm/attractor/main/<name>.md`
(+ Symphony). Rubric: 14 dimensions including "AMBIGUITY AUDIT: find the 2–3
places where the spec is LEAST precise." Four Explore agents dispatched in
one message. Result: profiles converged on "binary DoD checklist framed as
'done when every box is checked'" (present in all four) while diverging on
RFC-2119 usage (Symphony: 26 MUST/50 SHOULD; StrongDM specs: 2–6 uppercase
keywords total) — proving keyword convention is not a necessary condition.
The synthesis's claim "all four specify backoff as an equation" failed the
step-6 reread: one spec delegates backoff to a companion document. Fixed
before commit.

**Example 2 (hypothetical).** "Why do our three most reliable services have
so few pages?" → fetch the three services' runbooks + alerting configs, rubric
dimensions on alert design, ownership clarity, failure-mode documentation,
each demanding line-number evidence, plus the adversarial dimension "where
would this runbook fail a 3am responder?" Three parallel agents → intersect →
the commonalities become the runbook standard; the adversarial findings
become the lint list.

## Anti-patterns

- **Letting agents see each other's outputs** (or summarizing artifact A in
  agent B's brief) — destroys independence, the whole point. (This session
  explicitly noted "independence matters: convergence is signal, not
  anchoring" in the published method section.)
- **Rubric asks for a summary of the subject** instead of properties of the
  document — you get N book reports that can't be intersected.
- **Skipping the adversarial dimension** — praise-only profiles of good
  artifacts produce nothing actionable; the defects in gold examples were
  this session's most reused output (checklist lint section, task-03
  regression corpus).
- **Paraphrasing profiles into the synthesis and discarding them** — the
  line-number evidence is what makes the synthesis auditable later; keep the
  profiles as files.
- **Universal claims without a per-profile check** — "all N do X" written
  from memory of the profiles, not verification against them.

## Acceptance criteria

- Every profile follows the same section structure and every claim has a
  file:line pointer.
- The synthesis contains a commonality list, a difference list, AND a defect
  list — all three, each citing profiles.
- No agent brief mentions another artifact's content or the hypothesis.
- Every "all N" claim in the synthesis has been re-verified against each
  profile before commit.

## Files this skill creates / modifies

- `<analysis-dir>/profiles/<artifact>-profile.md` — one per artifact,
  verbatim agent output.
- `<analysis-dir>/README.md` (or similar) — the synthesis with method note,
  commonality/difference/defect sections.
