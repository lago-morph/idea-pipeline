# Spec: `repo-orientation-report`

- **ID**: SKILL-SPEC-6c79deb0a5
- **Source retrospective**: ../2026-09-06-41.md

## Intent

Produce a bounded, cited orientation on another repository, its objectives, artifact types, decisions, procedures, status, scope boundaries, and vocabulary, using Explore subagents so the main context absorbs a few thousand words instead of the whole tree. The skill earns its place because the session had to understand agent-method well enough to design something that slots into it, the repository was about 500 KB across 109 files, and two subagent reports of about 1500 words each, with a file path on every claim and a twenty-term vocabulary list, were enough to do that without loading the notes into the main context.

## Trigger

Direct: the user asks to "take a look at" or "understand" another repository, its objectives, its status, or "where this will slot in", and names the repository or a directory of it.

Proactive: a task depends on conventions defined in another repository, such as file layouts, link types, or vocabulary that the output must mirror.

Negative: do not use when the user wants a critique or review of the other repository; the report is descriptive by instruction. Do not use for a single known file, which should be read directly.

## Inputs

- The repository owner and name, or a path to an existing clone.
- Directories to exclude, such as archives the owner has quarantined.
- The question the orientation must answer, usually one of: what it is trying to achieve, what it produces, what its status is, and where new work would attach.
- Any shape you must mirror exactly, which you will read yourself rather than delegate.

## Outputs

- Two or three subagent reports in the conversation, each under about 1500 words, with a fixed outline, file paths on every claim, and a vocabulary list.
- A short synthesis in the reply: what the repository is, what it already has that overlaps the task, and what the task must respect.
- No files in the repository unless the user asks for the orientation to be captured.

## Workflow

1. Clone the repository into `/tmp/<name>` with `--depth 1`. Use the session's read access to public repositories; if the repository is private, attach it through the session's repository tool first.
2. List the top-level directories with file counts and byte totals, excluding the directories the owner quarantined. Do not read inside quarantined directories for any reason.
3. Split the tree into two or three reading assignments of roughly equal size along the repository's own concern boundaries, for example method versus workbench versus working documents.
4. Write one brief per assignment with these fixed sections: what it is, in the repository's own words with quotes and paths; the artifact types it defines with fields and dependencies; decisions already made; procedures and lessons; status, concrete; scope boundaries, quoted; and a vocabulary of ten to twenty terms. State the word cap, forbid critique and proposals, require a file path on every claim, and name the excluded directories.
5. Launch the subagents in the background in one message, as Explore type.
6. While they run, read directly only the few files whose exact shape the task must mirror, such as a conventions file, one type description, and the current handoff. Keep this under about 20 KB.
7. When the reports arrive, write the synthesis: three to five sentences on what the repository is, a table of what it already has that the task discussed under other names, and the seam where new work attaches.
8. Use the vocabulary list from the reports in every later document so coined terms do not creep in.

## Concrete examples

### Example 1: orienting on agent-method before designing a companion structure

Input: `lago-morph/agent-method`, exclude any directory starting with `archive`, question: objectives and status, so a new framework can be designed to slot in over time.

Steps: clone to `/tmp/agent-method`; sizes show `method/` 30 KB, `ai/` 158 KB, `workbench/` 192 KB. Two briefs: one for `method/` and `ai/`, one for `workbench/`. Four files read directly: `method/README.md`, `method/CONVENTIONS.md`, `method/types/vision.md`, `ai/HANDOFF.md`. Reports return in about two and four minutes.

Output synthesis: agent-method grows a specification as a graph of typed artifacts, adds process only on observed friction, and already has a guide / decisions / standard pattern with six foreseen guides; the seam for new work is that pattern, one guide at a time. A table maps eight discussed ideas to the names agent-method already uses for them. Every later document uses "guide", "decisions note", "regeneration run", "ambiguity", and "ratified" rather than new coinages.

### Example 2: orienting on a service repository before writing an integration

Input: a private service repository, question: what interfaces it exposes and how it is deployed.

Steps: attach with push access disabled, clone to `/tmp`. Sizes show most bytes in generated client code, which is excluded from the assignments. Two briefs: one for the API definitions and their versioning conventions, one for deployment manifests and runbooks. Two files read directly: the API style guide and the release checklist, because the integration must follow both.

Output synthesis: a table of interfaces with their version policy and the file that defines each, a paragraph on the deployment topology, and the two conventions the integration must follow, with paths.

## Anti-patterns

- **Reading the whole repository into the main context.** The alternative in the session would have cost roughly sixty times the context the reports did.
- **Letting the subagents critique.** The user said explicitly that no critique was wanted; a critical report is also longer and less quotable.
- **Skipping the vocabulary section.** It is the cheapest defense against inventing terms the other repository already has names for.
- **Reading quarantined directories because they look useful.** The owner's `CLAUDE.md` forbade it; the archived attempts were kept only as source material to mine later on request.
- **Duplicating the subagents' reading yourself while they run.** Read only what must be mirrored exactly; otherwise wait.

## Acceptance criteria

- [ ] Every claim in each report carries a file path, and spot-checking three claims against the clone finds them accurate.
- [ ] Each report is under about 1500 words and follows the fixed outline.
- [ ] The synthesis names the seam where new work attaches, in the repository's own vocabulary.
- [ ] No file inside an excluded directory was opened.
- [ ] The main context spent under about 10 KB on direct reads.

## Files this skill creates / modifies

- `/tmp/<name>/`: the shallow clone, disposable.
- Nothing in the working repository unless the user asks for the orientation to be captured, in which case one markdown file at the path they name.
