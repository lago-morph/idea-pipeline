# agent instruction

**Deliverable-only PRs.** A task PR contains exactly the files the task's Deliverables section names. Analysis substrates (inventories, scratch evidence) stay out unless the task asks for them. Reproduce the task's acceptance checklist, ticked, in the PR body; reference the umbrella issue (#22) without closing it; leave task files unedited — completion is recorded by the merge, not by editing the queue.

*Grounded in: PR #26 shipping two files against a session that produced six-plus analysis artifacts, with the task-01 checklist ticked in the body.*

# justification

The work queue (`spec-completeness/tasks/`) is the owner's tracking surface and the umbrella issue spans three tasks; a PR that closes #22 or rewrites task files corrupts both. The ticked checklist in the body gives the reviewer the acceptance test without archaeology. (If you would rather keep evidence packages in the repo, invert the middle clause — but decide once, here; see the companion ADR draft on evidence retention.)
