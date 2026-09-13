# agent instruction

**Create the PR and offer to merge; merge only on the word.** Open the PR, say it is ready, and stop. Merge only when the author says so, with squash, and confirm the merged SHA. When they ask because the GitHub interface is misbehaving, that is the instruction — merge, don't investigate the interface.

*Grounded in: five PRs, each merged only on explicit instruction.*

# justification

Every PR in the session (#44–#48) was merged only after the author said "merge" — once with "merge just the skill edits," once with "the GitHub interface is being strange." Twice the agent created a PR and explicitly did not merge because it had only been asked to create; the author then asked, and the merge was one call. The author's stated preference is that the agent do exactly what was asked and confirm before doing more. Cost of the rule: one round-trip per merge. Cost of breaking it: a merge the author did not want on `main`.
