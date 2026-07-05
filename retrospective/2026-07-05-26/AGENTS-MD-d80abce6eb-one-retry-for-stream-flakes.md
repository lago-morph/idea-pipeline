# agent instruction

**One retry for stream flakes.** On MCP errors like "permission stream closed before response received", retry the identical call once before investigating. Expect MCP servers to disconnect and reconnect mid-session; deferred tools need a ToolSearch load before first call and after a server flap.

*Grounded in: the Mermaid validator failing with a stream-closed error and succeeding verbatim on retry; the GitHub MCP server flapping twice mid-session.*

# justification

Both failure signatures look alarming and both were self-healing in the task-01 session. The rule converts a would-be debugging detour into a single retry, and the flap expectation prevents the worse move: declaring a capability unavailable and re-planning around a tool that returns thirty seconds later.
