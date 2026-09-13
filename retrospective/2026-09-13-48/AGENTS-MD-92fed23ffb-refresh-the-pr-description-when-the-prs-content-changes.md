# agent instruction

**Refresh the PR description when the PR's content changes.** When a later push materially changes what a PR contains — a new section, a second document, a resolved ambiguity — update the PR title and body in the same turn as the push. A stale body misleads the reviewer now and the future reader mining the PR later.

*Grounded in: #44's body still described one file and an open ambiguity after the appendix landed.*

# justification

PR #44 opened as "one transcription, one uncertain word." By merge time it carried a resolved transcription, a 390-line appendix, and a correction about decisions — and its body had been refreshed twice, each time after the agent noticed the drift rather than as part of the push. The idea-pipeline treats merged PRs as a record (the retrospective skill mines them by number), so a stale body is a stale record. Updating the body is one tool call in the turn that already pushed.
