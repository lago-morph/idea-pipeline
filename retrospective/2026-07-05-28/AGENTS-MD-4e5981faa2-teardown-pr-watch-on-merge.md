# agent instruction

**Tear down PR-watch machinery on merge.** The moment a watched PR merges or closes, in the same turn: unsubscribe from its activity and delete every send_later / self check-in trigger armed for it (use list_triggers if the trigger ID has scrolled out of context). An orphaned trigger fires into a finished task, wastes a turn re-deriving that nothing is left to do, and can ping the user about a PR that no longer exists.

*Grounded in: merging PR #28 and deleting its 60-minute check-in trigger alongside the unsubscribe, in the same turn.*

# justification

This session armed a 60-minute self check-in for PR #28 per the watch protocol, then merged the PR eleven minutes later on the user's instruction. Had the trigger survived the merge, it would have fired into a session that had already moved on to retrospective work, forcing a re-derivation of PR state mid-task purely to conclude "merged, nothing to do" — and the re-arm instruction embedded in the trigger prompt risks the loop persisting indefinitely. The teardown is two tool calls and only cheap while the trigger ID is still in context; afterwards it requires a list_triggers hunt. Watch machinery is easy to arm and invisible once armed — symmetry (arm on subscribe, tear down on merge) is the only reliable discipline.
