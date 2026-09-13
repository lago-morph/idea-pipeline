# agent instruction

**Start follow-up work from a fresh branch off origin/main after a merge.** When a PR merges, do not reset or force-push the merged branch to reuse it. Run `git checkout -b <new-branch> origin/main` and work there. `git checkout -B`, `git reset --hard`, and `git push --force-with-lease` are classified as destructive in this environment and are denied, so the reset-in-place pattern stalls even when the branch holds only merged history.

*Grounded in: post-#44 branch reset denied twice.*

# justification

After PR #44 merged, two attempts to move the designated branch onto the new `main` were denied by the auto-mode classifier — first the combined `checkout -B` + `force-with-lease`, then `checkout -B` alone — and a plain fetch was then declined by the author. The session lost three tool calls and had to explain itself. The alternative, a fresh branch from `origin/main`, was accepted immediately for both the `preserve-context` skill and this retrospective and costs one command. Nothing about the old branch needs preserving after a squash merge; the content is on `main`.
