# agent instruction

**Merge mechanics.** This repo has no CI — do not wait for checks before declaring a PR ready. Merge via merge commit (repo convention). After a designated branch's PR merges, follow-up work restarts the same branch name from origin/main and opens a new PR — never stack commits on merged history.

*Grounded in: PR #26 showing zero check runs; the merge-commit history of PRs #1–#26; the task-01 retrospective riding a restarted branch.*

# justification

Each fact was discovered by probing during the task-01 session (an empty check-runs call, a scan of merge history). Three lines in the agents file convert those probes into zero-cost knowledge for every future session, and the branch-restart rule prevents the one git state that is genuinely painful to unwind — new commits stacked on already-merged history.
