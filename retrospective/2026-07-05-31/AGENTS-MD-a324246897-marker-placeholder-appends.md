# agent instruction

**Append to long documents with marker placeholders.** "When authoring a file too long for one Write, end each chunk with a unique placeholder comment (e.g. `<!-- SECTION3 -->`), append by Edit-replacing the marker with content plus the next marker, and grep for leftover markers before committing."

*Grounded in: hardening/checks.md (821 lines) written in five marker-appended chunks with zero mis-anchors.*

# justification

The two hardening documents (456 and 821 lines) were written in seven chunks across two files using marker replacement, with zero mis-anchored appends and zero duplicated sections; the exit grep for `<!--` confirmed no scaffolding survived into the commit. The alternative failure modes are all expensive: re-Writing a whole long file to append risks output-limit truncation halfway, and Edit-appending on "the last visible line" mis-anchors whenever that line is not unique. The marker is a guaranteed-unique anchor that costs one comment line; the exit grep costs one command.
