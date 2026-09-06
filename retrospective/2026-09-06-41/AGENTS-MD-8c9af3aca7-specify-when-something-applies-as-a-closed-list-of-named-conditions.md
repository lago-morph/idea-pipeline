# agent instruction

**Specify when something applies as a closed list of named conditions.** When a document says when an item is needed, pulled in, or triggered, define a short fixed list of named conditions once, give every item exactly one condition and one relationship to it, and do not join conditions with "or". Do not mix work items, thresholds, symptoms, and external events in the same free-text field.

*Grounded in: the fourteen nugget triggers the owner called confusing and ambiguous.*

# justification

The first version of the fourteen nugget files each carried a free-text `trigger:` line. Some named a work item already on agent-method's plan, some named a threshold such as more than about five guides, some named a symptom of a run, and some named an external event that might never happen. Several joined two conditions with "or". The plan's sync table described the same events in different words. The owner's verdict was that the conditions and trigger points were confusing and ambiguous. The fix was a nine-row table of named events, three relationship kinds, and one of each per nugget, and it took one pass. Defining the closed list first would have cost the same pass and avoided the round-trip. Free-text conditions read fine one at a time and fail as a set.
