# agent instruction

**Use absolute paths in parallel Bash calls.** The shell's working directory persists between calls, and a `cd` in one call changes where a parallel call's relative paths resolve. Every file path in a Bash call that may run alongside another must be absolute.

*Grounded in: idea files written with relative paths that landed correctly only because a parallel `cd` had already run.*

# justification

Two Bash calls ran in parallel to write fourteen nugget files. The first began with `cd .../architecture-ideas/ideas`. The second used `mkdir -p` with an absolute path and then wrote files with bare relative names. The files landed in the right place only because the first call's `cd` had already changed the persistent working directory. Had the calls interleaved differently, eight files would have been written to the repository root, and the `ls` that followed would have caught it only by luck. The environment notes confirm the working directory persists and that `cd` in a compound command is discouraged. Absolute paths cost nothing and remove the race.
