# agent instruction

**Treat permission-stream failures as unanswered prompts.** "A tool error like 'Tool permission request failed / permission stream closed before response received' means a human approval prompt went unanswered — not a flaky API. Do not blind-retry: surface the approval need to the user, or pre-approve the tool family in .claude/settings.json permissions.allow (mcp__<Server>__<tool> entries)."

*Grounded in: two delete_trigger failures diagnosed as expired prompts; fixed by the settings allowlist.*

# justification

delete_trigger failed twice with "permission stream closed before response received," which pattern-matches a transient server error and invites retries. It was actually the permission dialog expiring unanswered — and those same dialogs were what the user later called "extremely annoying." Retrying would have generated more prompts; the durable fix was six lines in .claude/settings.json pre-approving the scheduling tool family, which also answered the user's ask directly. Misdiagnosis here has a double cost: wasted in-session retries, and a worsening prompt-fatigue loop for the human on the other end.
