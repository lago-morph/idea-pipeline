# agent instruction

**Write mermaid labels defensively and validate before commit.** In mermaid sources: no bare `&` in node labels (write "and"), no hyphens in state names (alias them: `state "PENDING-OWNER" as PO`), and validate every diagram before committing (Mermaid MCP validator; extract `.valid` from the saved result). A diagram that fails to render ships as a code block of noise — worse than no diagram.

*Grounded in: pre-emptive `&`-to-"and" and quoted-alias fixes in process.md's two diagrams, both validated true before commit.*

# justification

process.md's stage graph originally read `S6[S6 Assembly & lint]` and its question lifecycle needed a state literally named PENDING-OWNER — both constructs that mermaid variants mis-parse (`&` as an entity boundary, `-` as illegal in state identifiers). Caught in the re-read pass and fixed defensively ("and"; `state "PENDING-OWNER" as PO`), then both diagrams were validated true via the Mermaid MCP tool before commit. The failure mode is nasty precisely because it is invisible locally: the markdown looks fine, the PR diff looks fine, and only the rendered GitHub page shows a grey error block where the process's central diagram should be — in the merged, linked-from-README deliverable. Validation costs two tool calls per diagram; un-rendering costs a follow-up PR and a reader who bounced off the document's most load-bearing visual.
