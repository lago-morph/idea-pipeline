# agent instruction

**Read review batches in chunks under 25 KB.** When reading several files back for review in one call, keep the total under about 25 KB. Larger outputs are written to a file instead of returned, and reading them again costs a second pass.

*Grounded in: a 36 KB four-file read that was persisted to disk and re-read in halves.*

# justification

Reviewing four subagent drafts with one `cat` produced 36 KB, which the harness persisted to a file and returned as a 2 KB preview. The four files then had to be read again in two calls. The threshold is not documented, but 36 KB was over it and two calls of about 18 KB each were under it. The cost of the miss was one wasted call and the context of the preview. The rule costs nothing: split the read before running it.
