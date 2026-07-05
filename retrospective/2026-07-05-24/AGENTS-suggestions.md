# AGENTS.md suggestions — 2026-07-05-24

These are proposed additions to the project's agents file (typically
`AGENTS.md` at the repo root). Each section contains:

1. **Proposed addition** — the exact text to paste.
2. **Why this earns its place in your agents file** — the argument for doing
   it, grounded in something that happened (or nearly happened).

Decide each on its own merits. Skip ones that don't apply to your operating
posture; copy-paste the ones that do.

---

## Suggestion 1: Prune before pushing a restarted branch

### Proposed addition

> **Prune before pushing a restarted branch.** After a PR merges, GitHub may
> delete the remote branch. Before pushing new work on a branch restarted
> from main, run `git fetch --prune origin` first; a `--force-with-lease`
> push against a stale remote-tracking ref fails with "stale info" even when
> the push is safe.
>
> *Grounded in: PR #24 push rejected until `--prune` cleared the deleted
> `origin/claude/...` ref.*

### Why this earns its place in your agents file

This failure is misleading by design: "stale info" reads like a conflict with
someone else's work, inviting a dangerous plain `--force` as the "fix." The
actual cause — remote branch auto-deleted on merge — is invisible from the
error. This repo's workflow (one long-lived agent branch name, restarted from
main after every merge) hits this on *every* multi-PR session. Cost of the
rule: one fetch. Cost without it: a confusing error at best, a reflexive
force-push habit at worst.

---

## Suggestion 2: Blind, identical-rubric fan-out for comparative analysis

### Proposed addition

> **Comparative analysis is blind and rubric-first.** When comparing ≥3
> artifacts (specs, docs, designs), write one rubric, dispatch one subagent
> per artifact in parallel, and give no agent sight of the others' outputs or
> of your hypothesis. Convergence across independent profiles is evidence;
> shared context is anchoring. Always include one adversarial rubric
> dimension ("where is this artifact weakest?").
>
> *Grounded in: the four-spec profiling for issue #22.*

### Why this earns its place in your agents file

The issue #22 analysis rested on the claim "these attributes appear in all
four specs." That claim is only meaningful because the four profiles couldn't
see each other — otherwise attribute lists bleed from the first profile into
the rest and the intersection is an artifact of ordering. The adversarial
dimension clause pays for itself separately: the gold specs' *defects*
(undefined helpers, dangling references) became the checklist's lint section
and task-03's regression corpus — the single most reused output of the
session. Praise-shaped analysis of good examples produces nothing actionable.

---

## Suggestion 3: Subagent deliverable contract

### Proposed addition

> **Subagent briefs end with a deliverable contract.** Every analysis
> subagent brief ends with: "Your final message IS the deliverable — return
> <exact format> as markdown, no preamble," and requires evidence pointers
> (file:line) for every claim. Save returned deliverables verbatim as files;
> don't paraphrase them into oblivion.
>
> *Grounded in: four spec profiles published nearly verbatim from subagent
> final messages.*

### Why this earns its place in your agents file

Without the contract, subagents return chatty summaries addressed to you
("I found several interesting things! First…") that need a rewrite pass
before they're usable — doubling the cost of every fan-out. With it, all
four profiles in this session went from tool result to committed evidence
file with only a preamble line trimmed. The evidence-pointer requirement is
what made the downstream synthesis auditable: every "all four specs do X"
claim in the published README can be checked against line numbers without
re-reading 8,000 lines.

---

## Suggestion 4: Distill, don't discard

### Proposed addition

> **Distill, don't discard.** When a scope correction invalidates finished
> draft work, don't paste the draft into the successor artifact as finished
> content and don't delete the thinking. Compress it into the successor as
> an explicitly-labeled hypothesis ("starting design direction — refine or
> restructure with stated reasons"), so the value transfers without
> pre-anchoring whoever does the real work.
>
> *Grounded in: the artifact-model draft deleted and distilled into
> task-01's design-direction section after the "one task file per idea"
> correction.*

### Why this earns its place in your agents file

The two default reactions to "that's not what I wanted" are both wrong:
shipping the draft anyway (ignores the correction; the dedicated session
becomes a rubber stamp) or deleting it wholesale (throws away a complete,
correct design). The distillation took ~10 minutes and produced a better
task file than a cold start would have — the future session gets the layer
structure, IDs, and traceability rules as a starting point it's explicitly
licensed to overturn. The "labeled hypothesis" phrasing is the load-bearing
part; without it, design direction reads as settled and anchors anyway.

---

## Suggestion 5: Full reread before committing multi-section documents

### Proposed addition

> **Reread long docs top-to-bottom before commit.** Any document with 5+
> sections gets one full top-to-bottom reread before committing, hunting
> specifically for cross-section factual drift — and treat every universal
> quantifier ("all four…", "every…") as a claim to re-verify against its
> sources, not prose to skim.
>
> *Grounded in: "all four specify backoff as an equation" — false for one
> spec, caught only in the reread.*

### Why this earns its place in your agents file

The error wasn't visible from inside any single edit: each section was
locally correct, and the false universal was only checkable against the four
profile files. In a repo whose entire product is analysis documents, one
published false claim quietly poisons everything derived from it (the
checklist item, the task-file validation requirements). Cost: minutes per
document. The caught-it-once record here is exactly one for one — the base
rate of this error class is high enough that the pass will keep paying.

---

## Suggestion 6: Task granularity is an intent question

### Proposed addition

> **Confirm the decomposition unit before authoring at volume.** When asked
> to produce task definitions, work queues, or split work into sessions,
> confirm how many units and where the cuts fall BEFORE writing them. If the
> session is non-interactive, state the assumed granularity explicitly at the
> start of the deliverable and keep the first unit cheap to restructure.
>
> *Grounded in: a ~13-file plan (inline docs + 10 fine-grained tasks) vs. the
> owner's intended 3; a full draft was already written when the correction
> arrived.*

### Why this earns its place in your agents file

"Write task definitions for each of these items" had two readings — per
checklist item or per idea — and the wrong one was chosen with high
confidence. The correction arrived one file into a thirteen-file plan; the
recovery cost was modest only because the correction came early. Granularity
determines everything downstream (file count, session count, dependency
structure), making it one of the highest-leverage single questions available.
One AskUserQuestion or one explicit stated-assumption sentence is the entire
cost.

---

## Suggestion 7: Don't promise scheduled self check-ins

### Proposed addition

> **Scheduled wakeups may need approval you can't get.** In non-interactive
> sessions, `send_later` / trigger-creation MCP calls can fail with "requires
> approval." Don't promise timed check-ins; rely on webhook-driven events
> (which auto-wake the session and auto-unsubscribe on PR merge), and tell
> the user explicitly when a timed check-in could not be armed.
>
> *Grounded in: two failed `send_later` attempts for PR #23/#24 watching.*

### Why this earns its place in your agents file

The failure mode is a silent broken promise: the session says "I'll check on
the PR in an hour," the approval-gated call fails, and nobody is watching.
This session caught it and disclosed it, but only because the error surfaced
in-turn. The rule converts a reliability hole into a known limitation with a
stated fallback — webhooks covered both PRs fine, including delivering the
merge notifications that made check-ins unnecessary. Zero cost; it's purely
a don't-claim-what-you-can't-arm rule.

---

## Suggestion 8: Raw-URL fetch for user-cited external repos

### Proposed addition

> **User-cited public files: fetch raw, don't fight repo scope.** GitHub MCP
> tools are scoped to this repo. When the user explicitly links files in
> other public repos, fetch them via
> `curl https://raw.githubusercontent.com/<owner>/<repo>/<ref>/<path>` (the
> proxy allows it) into the scratchpad, and record byte/line counts so
> subagent briefs can plan chunked reads.
>
> *Grounded in: four external specs (~360 KB) fetched for the issue #22
> analysis.*

### Why this earns its place in your agents file

The wrong paths here are tempting: trying GitHub MCP tools against
out-of-scope repos (denied), or `add_repo`-ing repos that only need to be
*read once* (heavyweight, and unavailable for repos outside the account).
The raw fetch worked immediately, made the artifacts local and stable for
four parallel subagents to read identical bytes, and the recorded `wc -lc`
output drove the "read in two chunks" instructions in the briefs. This repo's
core loop — analyzing other projects' specs — will do this constantly.
