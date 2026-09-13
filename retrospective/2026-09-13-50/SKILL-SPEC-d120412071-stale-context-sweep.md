# Spec: `stale-context-sweep`

- **ID**: SKILL-SPEC-d120412071
- **Source retrospective**: ../2026-09-13-50.md

## Intent

Sweep the artifacts that *describe* work for staleness after the work itself moves on. In this session a pull request body went stale four separate times as commits landed, and a scheduled check-in routine kept re-raising a question the user had already answered — because its own prompt text still contained it. These artifacts fail silently: nothing errors, the description simply stops matching the branch, and a recurring job keeps asking a settled question until someone notices.

## Trigger

**Direct**: "update the PR", "is the description still right?", "why does it keep asking me that?"

**Proactive**: run automatically at three moments — after any push that adds a commit to a branch with an open pull request; when a scheduled check-in fires; and before reporting a task complete.

**Negative**: skip for a branch with no open pull request and no scheduled job attached to it.

## Inputs

- The open pull request for the current branch, if any: its body and the commits it now contains.
- Any scheduled routine or recurring reminder this session created, and the literal prompt text each one carries.
- The set of questions the session has put to the user, and which of them have been answered.

## Outputs

- An updated pull request body covering every commit on the branch.
- Updated (or deleted) routine prompts, carrying only questions that are still open.
- No output at all when nothing has drifted — silence is the correct result of a clean sweep.

## Workflow

1. List the commits on the branch and compare them against the sections of the pull request body. Any commit whose substance is not described is drift.
2. Rewrite the body to cover them. Keep the structure; extend it rather than replacing it, so a reviewer's sense of the document survives.
3. Re-derive the body's "still open" section from current reality, not from its previous contents. Every item the user has since decided must come out.
4. For each scheduled routine this session created, read the prompt text it will actually deliver. Check it against what is still true: resolved questions removed, new ones added, and any standing context (for example, "this repo has no CI") preserved so the next firing does not re-derive it.
5. Update the routine in place rather than deleting and recreating it, so its run history survives.
6. When the underlying work is finished — a pull request merged, a task closed — delete the routine and drop any subscription, rather than leaving them to fire against finished work.
7. If nothing has drifted, say nothing and end the turn.

## Concrete examples

**Example 1 — the pull request body.** PR #50 in this session accumulated seven commits across several hours. Its body was rewritten three times: after the evidence-line commit, after the orphan-slug commit, and after the deprecation and ingest commits. Each rewrite extended the section list and re-derived the "still open" list, which shrank from four items to three to one as the user answered questions.

**Example 2 — the routine that kept asking.** A check-in routine was created carrying the text "options A re-rate only, B rewrite the cluster, C deprecate; my recommendation was B". The user answered "C" in chat. The routine's own prompt still said the question was open, so the next firing re-raised it. The fix was to rewrite the routine's prompt to say the question was resolved and to name the questions that had replaced it — and, when the work finished, to delete the routine outright.

## Anti-patterns

- **Treating the pull request body as write-once.** It is the reviewer's entry point; a body describing three of seven commits is worse than no body, because it implies completeness.
- **Leaving a routine's prompt untouched while updating everything else.** The prompt is the only thing the next firing sees. Chat context does not reach it.
- **Deleting and recreating a routine to change its text.** That discards its run history; update it in place.
- **Reporting the sweep when it found nothing.** A clean sweep is silence. Announcing "nothing changed" every hour is the same noise the sweep exists to prevent.
- **Letting a subscription outlive its subject.** A merged pull request with a live subscription and a live routine will keep waking the session against finished work.

## Acceptance criteria

1. Every commit on the branch is represented in the pull request body.
2. The body's open-questions list contains only questions the user has not answered.
3. Every routine's prompt text matches current reality, including which questions are settled.
4. When the work completes, routines are deleted and subscriptions dropped in the same turn.
5. A sweep that finds no drift produces no user-facing output.

## Files this skill creates / modifies

- No repository files. It modifies the pull request body, scheduled routine prompts, and subscription state.
