# agent instruction

**Self-contained briefs.** A subagent brief must inline every definition, list, and convention it depends on — never "the model above" or "as discussed". For large outputs, require the agent to write a file and return only a capped summary (path + findings).

*Grounded in: four spec-analyst briefs, each carrying the full 15-artifact definition block verbatim, returning ≤500-word summaries plus ~160-line inventory files.*

# justification

The four analysts of the task-01 session produced ~650 lines of line-cited classification without one round-trip clarification, because each brief was executable in isolation. The file+summary split kept four large evidence packages out of the dispatcher's context until each was needed. The marginal cost is duplicated definition text in briefs; the failure mode without it is agents classifying against a model they cannot see.
