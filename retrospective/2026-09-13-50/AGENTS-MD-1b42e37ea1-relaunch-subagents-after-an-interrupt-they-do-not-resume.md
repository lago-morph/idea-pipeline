# agent instruction

**Relaunch subagents after an interrupt; they do not resume.** "Interrupting a turn stops every background subagent it started, and a stopped subagent cannot be resumed by messaging it. After any interrupt, list the running agents, assume the ones you started are gone, and relaunch with the corrected brief rather than trying to redirect them."

*Grounded in: a mid-flight scope change that found all four readers already stopped by the interrupt that delivered it.*

# justification

When the owner interrupted a turn to exclude one file from a source, the natural response was to message the affected reader with the scope change. The message failed: the agent had been stopped by the interrupt and would not be resumed. Listing the running agents showed all four were gone. The recovery — relaunching three readers with the exclusion written into the brief — was strictly better anyway, because the exclusion then appeared in the instructions rather than as a correction the reader had to apply to work already done. The cost of the rule is one listing call after an interrupt. The cost of not having it is a silent assumption that redirected agents are still working, and a wait for results that will never arrive.
