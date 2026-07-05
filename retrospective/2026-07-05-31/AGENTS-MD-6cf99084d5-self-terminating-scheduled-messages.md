# agent instruction

**Scheduled messages carry their own stop condition.** "Every send_later/trigger message must state its termination rule inside the message text ('if the PR is merged or closed, stop — do not re-arm') so a stale firing is a clean no-op even when the trigger outlives its purpose or cannot be deleted."

*Grounded in: the PR #30 check-in trigger firing after the merge and terminating itself.*

# justification

The hourly PR #30 check-in trigger could not be deleted — its delete calls died on unanswered permission prompts — so it fired after the PR was already merged. Because the message itself said "if merged or closed, stop — do not re-arm," the stale firing cost one short turn and ended the loop cleanly instead of re-arming a zombie hourly poll. Writing the stop condition costs one sentence at scheduling time; a trigger without one keeps waking the session indefinitely on a dead task, burning attention and tokens every hour until someone notices.
