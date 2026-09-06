# agent instruction

**Stage files by name while background subagents are writing.** Do not run `git add` on a directory that a background subagent is writing into. Stage the specific files you own. A directory-level add captures a sibling's half-written file in your commit.

*Grounded in: commit a89a9b5, which captured the artifact type registry mid-draft.*

# justification

While three subagents were writing into `architecture-ideas/spine/`, a checkpoint commit ran `git add architecture-ideas/spine` to save six finished drafts. It also swept up the registry file that one subagent was still writing, so that commit carries a half-finished registry and the next commit carries its correction. Nothing broke, but the history now misrepresents when the registry was done, and the subagent had to report the capture in its summary. Naming the six files instead of the directory would have cost one longer command line. Checkpoint commits during fan-out are worth making; they just have to be scoped to what is actually finished.
