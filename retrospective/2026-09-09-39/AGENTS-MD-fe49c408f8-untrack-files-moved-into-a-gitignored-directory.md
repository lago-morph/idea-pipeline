# agent instruction

**Untrack files moved into a gitignored directory.** "After moving a tracked file into a gitignored path (via `git mv` or `mv`), run `git rm --cached <path>` and confirm with `git status` that the index shows a deletion, not a rename — `.gitignore` never untracks a file that is already in the index."

*Grounded in: `every.mbox` staying staged as a rename into gitignored `.cache/` during the agent-patterns Phase 0 scaffold.*

# justification

During Phase 0 of the agent-patterns build (PR #39), SPEC §2 required moving the 11 MB `every.mbox` out of git into gitignored `.cache/`. The `git mv` succeeded — and `git status` quietly showed `R  agent-patterns/every.mbox -> agent-patterns/.cache/every.mbox`: the file was still fully tracked, headed into the next commit, because gitignore only filters *untracked* files. Had that commit landed, the repo would have carried the newsletter corpus the spec explicitly forbids committing, in a hard-to-notice location, requiring a history rewrite to purge. The fix was one command (`git rm --cached`) plus one glance at `git status`; the failure it prevents is a policy violation baked into history. The asymmetry is a few seconds against a permanent, license-relevant mistake.
