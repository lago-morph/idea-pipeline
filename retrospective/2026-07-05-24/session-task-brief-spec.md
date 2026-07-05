# Spec: `session-task-brief`

## Intent

When work is too large or too distinct for one session, it must be split into
session-sized units coordinated through files, not memory — the next session
starts with zero context. A task brief that says "implement the artifact
model we discussed" is worthless to a fresh session; a brief that inlines
everything is bloated and goes stale. This skill produces task-definition
files calibrated to the actual consumer: a fresh-context agent that can read
repo files but knows nothing about the originating conversation.

Grounded in: this session ended with the owner requesting "one task file for
each of the three ideas… complete enough with enough context for a new
session to use one of these task definitions as a prompt and produce good
work." The three files written (`spec-completeness/tasks/task-0{1,2,3}-*.md`)
plus an index are the reference implementation.

## Trigger

- Direct: "write task definitions", "split this into sessions", "create a
  work queue", "make this something a fresh session can pick up".
- Proactive: when a session has designed multi-part work whose parts each
  deserve dedicated context (offer, don't assume — task granularity is an
  intent decision; see Anti-patterns).
- Negative: do NOT use for subtasks executed within the current session
  (that's a subagent brief, a different artifact); do NOT use when the user
  asked you to do the work now.

## Inputs

- The design conversation / analysis that motivated the work.
- The decomposition unit **confirmed by the user** (how many tasks, cut
  where).
- Knowledge of which repo files a fresh session can rely on existing.

## Outputs

- One `tasks/task-NN-<slug>.md` per unit.
- A `tasks/README.md` index: table of task → deliverable → depends-on, plus
  recommended execution order and parallelism notes.

## Workflow

Each task file gets these sections, in order:

1. **Header**: status, depends-on (other tasks, marked hard/soft), feeds
   (what consumes this task's output).
2. **Why this task exists**: 1–2 paragraphs of motivation including the
   *user's own requirements in their words* — the fresh session must know
   what the human actually asked for, not just the technical goal.
3. **Context to load**: an ordered reading list of repo files (with what to
   take from each) and external URLs. Point at files rather than inlining
   them — files stay current, inlined copies rot. Inline only what exists
   nowhere else.
4. **Objective**: the deliverable in one tight statement, with exact output
   paths.
5. **Design direction**: the originating session's design thinking,
   compressed and **explicitly labeled a hypothesis** ("refine or
   restructure with stated reasons — not settled"). This transfers value
   without anchoring. Include known tensions/open questions the design
   didn't resolve.
6. **Validation requirement**: how the fresh session knows its deliverable
   is right — ideally grounded in checkable evidence that already exists
   (e.g., "every defect listed in the profiles' ambiguity audits must
   reappear as a model violation; if one is invisible to your model, the
   model has a hole").
7. **Deliverables**: exact file paths, including required cross-reference
   edits to existing docs.
8. **Task acceptance checklist**: 6–10 checkboxes — a Definition of Done for
   the task itself. Include one "re-read the doc top-to-bottom for internal
   consistency" item.
9. **Out of scope**: what the task must NOT do (usually: the neighboring
   tasks' work).
10. **Working notes**: branch/PR conventions, and **provisional-vocabulary
    fallbacks** for soft dependencies — what to use if a dependency task
    hasn't merged yet, marked provisional (e.g., "if task-01 isn't merged,
    use the design-direction artifact IDs from its task file, flagged").

Then write the index (`tasks/README.md`) and state the dependency order and
which tasks can run in parallel.

## Concrete examples

**Example 1 (this session, task-01).** "Why": issue #22 + the owner's central
requirement quoted — "the WHAT is specified as much as possible in a generic
way, and the specification of the HOW is layered on top." Context-to-load:
`spec-completeness/README.md`, the four profiles, four raw spec URLs. Design
direction: 4 layers, 15 artifact IDs (A-VS … X-WE), Freedom Register as the
seam, 4 traceability rules — all marked hypothesis. Validation: all four gold
specs must decompose cleanly AND every audited defect must surface as a model
violation. Acceptance checklist: 8 items including "WHAT artifacts contain no
interface names, wire formats, defaults, or pseudocode."

**Example 2 (this session, dependency handling).** Task-03 depends softly on
task-01's vocabulary. Its working notes say: "If task-01 isn't done yet, read
`tasks/task-01-artifact-model.md` and write checks against the
design-direction artifact IDs, marked provisional." This let the owner run
02/03 in parallel after 01 — or even before it — without a coordination
session.

## Anti-patterns

- **Guessing the decomposition unit.** This session planned ~13 files
  (inline docs + 10 fine-grained hardening tasks) when the owner wanted
  exactly 3; a complete draft deliverable had already been written when the
  correction arrived. Granularity is an intent question — confirm it before
  authoring at volume.
- **Shipping finished work disguised as a task** (pasting your full draft
  into the file). The dedicated session becomes a rubber stamp and inherits
  your anchoring. Distill the draft into the design-direction section as a
  labeled hypothesis instead — that was the recovery move here, and it
  preserved the thinking while leaving the session room to disagree.
- **"As discussed" / "see the session".** The consumer has no session. Every
  reference must resolve to a repo file or an inline statement.
- **Omitting out-of-scope.** Adjacent tasks will overlap and two sessions
  will both build the same piece.
- **Hard dependencies where soft ones suffice.** Without provisional
  fallbacks, the work queue serializes needlessly.

## Acceptance criteria

- A reader given ONLY one task file (plus repo access) can state the
  deliverable, its paths, and its acceptance checklist without asking
  anything.
- Every task file contains the user's requirements in or near their own
  words, a hypothesis-labeled design direction, and a validation requirement
  grounded in existing repo evidence.
- The index's dependency graph is acyclic and marks hard vs. soft edges.
- No task file references conversation state that isn't in a file.

## Files this skill creates / modifies

- `<area>/tasks/task-NN-<slug>.md` — one per session-sized unit.
- `<area>/tasks/README.md` — index with dependency table and execution order.
