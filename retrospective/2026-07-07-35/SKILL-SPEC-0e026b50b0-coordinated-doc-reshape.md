# Spec: `coordinated-doc-reshape`

- **ID**: SKILL-SPEC-0e026b50b0
- **Source retrospective**: ../2026-07-07-35.md

## Intent

When a review produces a set of decisions that must be applied across a family of interdependent documents (a spec and its companions, a checklist and its executable checks), editing them ad hoc drifts them out of sync and forces the human reviewer to hold the whole cross-reference graph in their head. This skill runs the reshape as a disciplined, reviewable process: pin each decision as an ADR first so the edits have a checkable source of truth, reshape the documents in staged rounds each sized to one review sitting, carry explicit alignment notes on every not-yet-updated document during the in-between state, and verify cross-document consistency mechanically before each commit. Grounded in this session's two-round reshape of the four spec-completeness documents against five owner decisions.

## Trigger

**Direct:** the user asks to "reshape", "realign", "rework", or "propagate these decisions across" a set of two or more interdependent documents; or a review/design conversation closes with a batch of decisions that change something structural those documents share (a vocabulary, an artifact set, a rule numbering).

**Proactive — offer when:** a review has produced ≥3 binding decisions that each touch more than one document; or the documents cross-reference each other by shared IDs/section numbers/vocabulary that the decisions change; or one document's correctness is defined relative to another (a checklist that hardens a spec, a process that produces a model's artifacts).

**Negative — do not use for:** a change confined to one file; a purely additive change that touches no shared vocabulary; edits where the documents do not reference each other (no drift risk, so no coordination needed).

## Inputs

- The set of interdependent documents (paths), and how they reference each other (shared IDs, section numbers, a controlled vocabulary, "companion" relationships).
- The batch of decisions to apply — ideally already recorded as ADRs; if not, the first workflow step records them.
- The human reviewer's appetite for review granularity (one large diff vs. staged rounds) — ask if unstated.
- Repo conventions: the `adr` skill for decisions, `post-edit-reread-pass` for the final read, any link checker.

## Outputs

- One ADR per decision under `docs/adr/` (frozen IDs, adopted before edits begin).
- The reshaped documents, committed in one PR per review round, each round mergeable on its own.
- An **alignment note** at the top of every document, stating which documents are realigned, which are not, and which controls on conflict — present during the in-between state, removed when the last document is brought current.
- An **old→new mapping table** inside the reshaped documents wherever a renaming happened (old IDs/rules → new homes), so a reader and the next round can follow the change mechanically.
- A verification record (in the commit message or PR body): the cross-document consistency checks that passed.

## Workflow

1. **Pin decisions as ADRs first.** For each decision, author an ADR via the `adr` skill and get owner approval at the ADR stage. Do not begin editing the documents until the decisions are frozen. The ADRs are the source of truth every later edit is checked against.
2. **Choose the review granularity.** Present the reviewer a plain-language choice: one PR with all documents, or staged rounds (e.g. shape-defining documents first, then the documents downstream of them). Name the actual files and the trade-off; do not use coined shorthand. Default to staging when the downstream documents are defined *relative to* the upstream ones — staging lets the shape survive review before the dependent work is built on it.
3. **Order the rounds by dependency.** Reshape the documents that define the shared structure before the documents that consume it. Within a round, edit the upstream document before the ones that reference it.
4. **Carry alignment notes through the in-between state.** The moment round one changes shared structure, add a note to every not-yet-reshaped document: it is stale, and the reshaped documents + ADRs control on conflict. Remove each note only when that document is realigned in a later round.
5. **Preserve traceability across renames.** When the reshape renames a vocabulary or ID scheme, keep the old identifiers alive as a mapping table (old → new home) inside the reshaped document, and keep append-only historical records (changelogs, prior-decision appendices) verbatim rather than rewriting them.
6. **Verify cross-document consistency mechanically before each commit.** Run the checks the specific documents admit: set-diff of any dual-maintained lists (defined-set vs. referenced-set, both directions with `comm`), a sweep for the retired vocabulary the round obsoletes (excluding historical/mapping contexts), and grounding of every cross-reference the round moved. Then run `post-edit-reread-pass` for cross-section drift.
7. **Commit, push, PR per round.** One PR per round; each round's PR body states what changed, what is deliberately deferred to the next round, and the verification that passed. Restart the branch from the default branch after each round's PR merges.

## Concrete examples

### Example 1: the two-round spec-completeness reshape (this session)

Five owner decisions (use cases drive; DRY is a guideline; no freedom register; support rebuild and repair; documentation is default-on) had to land across `artifact-model.md`, `process.md`, `README.md`, and `hardening/` (a framework README + a 55-check definitions file).

- Step 1: recorded ADRs 0001–0005, merged as PR #33, before touching the four documents.
- Step 2: the owner chose two rounds ("first the shape of the thing... then the machinery details").
- Steps 3–4: round one (PR #34) rewrote `artifact-model.md` and `process.md`; both carried an alignment note — *"`README.md` §3 and `hardening/` are not yet realigned — that is review round two. Where they conflict, this document and the ADRs control."*
- Step 5: `artifact-model.md` §11 carried the old→new mapping table (sixteen artifacts → new homes) and §6 mapped the retired rules T1–T7 → the new C1–C10; the hardening appendix kept its historical A-1…A-7 entries verbatim.
- Step 6, round two (PR #35): verified the 55 checks with a defined-vs-referenced set-diff (`comm -13`/`comm -23`, zero orphans either direction) and a retired-vocabulary sweep (`R-FR`, `freeze`, `t1_orphans`, `T1`–`T7`) that returned only historical/mapping hits.

### Example 2: renaming a status enum across a spec and its test-plan

Suppose a decision renames a workflow's status enum (`ACTIVE/DONE/DEAD` → `RUNNING/COMPLETE/FAILED`) and this enum is referenced by a spec, a state-machine diagram, and an acceptance checklist that asserts "every status has a test."

- Pin the rename as one ADR; adopt it.
- Round one: edit the spec's enum definition and diagram; add an alignment note to the checklist ("status names not yet updated; spec controls").
- Preserve traceability: a two-column `old → new` table in the spec's changelog.
- Round two: update the checklist; remove its alignment note; verify with a set-diff that every new status name appears in both the spec enum and the checklist, and a sweep confirming zero live occurrences of the three old names outside the changelog table.

## Anti-patterns

- **Editing the documents before the decisions are frozen.** Then the edits *are* the decision record, spread across diffs, and the owner re-litigates each one inside four separate reviews. Pin ADRs first (this session did; the reshape went cleanly).
- **Leaving stale documents unmarked during a staged reshape.** A reader trusts the stale checklist as current. The alignment note is one paragraph; omitting it silently ships a contradiction (the round-one/round-two window would have been a trap without it).
- **Rewriting historical/append-only records to the new vocabulary.** The hardening appendix's A-1…A-7 entries were kept verbatim — they record what a prior task actually referenced. Migrating them would falsify history; the old→new mapping table is where the translation lives instead.
- **Trusting per-document review to catch cross-document drift.** Every individual list looked complete; the missing `shared/examples.md` surfaced only on a cross-enumeration join. Run the set-diff.
- **One giant diff when the documents are dependency-ordered.** If the checklist is defined relative to the spec, a single PR forces the reviewer to check both against each other at once and rebuilds the dependent work if the shape changes. Stage it.

## Acceptance criteria

- [ ] Every decision driving the reshape exists as an adopted ADR before any target document is edited.
- [ ] During any multi-round reshape, every not-yet-realigned document carries an alignment note naming what controls on conflict; the notes are all removed by the final round.
- [ ] Every renamed vocabulary/ID scheme has an old→new mapping table in the reshaped document, and append-only historical records are preserved verbatim.
- [ ] Before each commit, dual-maintained lists pass a bidirectional set-diff and the round's retired vocabulary returns zero live (non-historical) hits.
- [ ] Each review round is a self-contained, individually mergeable PR whose body states what is deferred to the next round.

## Files this skill creates / modifies

- `docs/adr/NNNN-*.md` — one ADR per decision (via the `adr` skill), adopted before edits begin.
- The target documents — reshaped in dependency order, with alignment notes added and later removed, and old→new mapping tables where renames occur.
- PR bodies — one per round, recording the deferred scope and the verification that passed.
