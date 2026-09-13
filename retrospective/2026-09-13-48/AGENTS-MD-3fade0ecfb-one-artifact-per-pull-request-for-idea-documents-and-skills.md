# agent instruction

**One artifact per pull request for idea documents and skills.** Each idea document (`NN-name.md`) and each skill change goes in its own PR, branched from `origin/main`. If a file lands on a shared working branch by accident, carve it out: `git checkout -b <new> origin/main && git checkout <shared-branch> -- <file>`, commit, PR, merge; then merge `origin/main` back into the shared branch so its diff returns to one artifact.

*Grounded in: PR #47 carved out of the #44 branch on request.*

# justification

`14-scoped-secrets.md` was first committed onto the scoped-sandbox branch alongside `13-scoped-sandbox.md`. The author asked for "an isolated pr for this transcription." The carve-out took two commands, PR #47 merged with one call, and merging `main` back left #44's diff at exactly one file again. Four of the session's five PRs were isolated this way and every one merged cleanly — including when the author said the GitHub UI was "being strange" and just wanted one thing merged. A shared branch carrying two documents would have forced merging both or neither. Cost of the rule: one extra branch per artifact.
