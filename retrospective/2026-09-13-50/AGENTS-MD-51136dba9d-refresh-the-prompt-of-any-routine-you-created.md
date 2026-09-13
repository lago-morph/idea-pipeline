# agent instruction

**Refresh the prompt of any routine you created.** "A scheduled routine only ever sees its own stored prompt, never the conversation. Whenever the situation it describes changes, update that prompt in place — never by deleting and recreating it — and delete the routine outright once its subject is finished."

*Grounded in: a check-in routine that kept re-raising a question the user had already answered, because its prompt still contained it.*

# justification

A check-in routine created in this session carried the text of an open question and a recommendation. The user answered it in chat. The routine's stored prompt did not change, so the next firing re-raised the settled question, and would have gone on doing so indefinitely. The same routine also carried standing context worth keeping — that the repository has no CI, so check runs are always empty — which is exactly why deleting and recreating it is the wrong repair: that discards the run history along with the stale text. Updating in place costs one call. Leaving it costs a recurring job that argues with decisions the user has already made.
