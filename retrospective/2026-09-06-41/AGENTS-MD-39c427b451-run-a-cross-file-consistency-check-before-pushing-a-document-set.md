# agent instruction

**Run a cross-file consistency check before pushing a document set.** After multi-file edits, check that every file another file references exists, that no em or en dashes crept in, that headings stay within the agreed depth, and that any fact stated in two files agrees. Fix contradictions at the source and record them in the decisions log.

*Grounded in: the end-user management criterion that the maturity ladder placed at two different levels.*

# justification

The maturity ladder's entry criteria put end-user management at the Enterprise level while its own criteria matrix put it at the Operated level. The registry subagent noticed the disagreement and flagged it in a table cell rather than resolving it. A single grep-and-read pass over the finished set found it, along with a stale sentence in `ideas.md` that still said the data model came first. The pass took one command: a dash check, a heading-depth check, an existence check on every `spine/*.md` path referenced from the index files, and targeted greps on the two facts the subagent summaries had flagged. Without it, the contradiction would have shipped in the owner's review copy. The `post-edit-reread-pass` skill describes the principle; this rule names the four concrete checks that caught real errors.
