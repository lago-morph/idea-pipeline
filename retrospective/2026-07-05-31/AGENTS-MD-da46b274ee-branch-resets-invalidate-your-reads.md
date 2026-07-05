# agent instruction

**Branch resets invalidate your reads.** "After any `git checkout -B`, reset, or merge that rewrites files on disk, treat every earlier Read as void: Grep or Read the exact target region again before the next Edit. Expect edits based on pre-reset reads to be rejected — or, worse, to anchor on stale text."

*Grounded in: artifact-model.md edits rejected with "File has not been read yet" after the post-merge branch restart.*

# justification

Right after PR #30 merged and the working branch was restarted from origin/main, two artifact-model.md edits were rejected with "File has not been read yet" — the file had been read at length earlier in the session, but the checkout invalidated that state. A third edit in the same pass failed on remembered line wrapping in README.md. Each failure costs a full round trip, and the dangerous variant is the edit that succeeds against stale text. One targeted Read or Grep after every reset is strictly cheaper than one failed Edit; this extends the existing grep-before-re-edit rule to the git operation that silently voids reads.
