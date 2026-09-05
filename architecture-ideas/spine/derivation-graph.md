# The derivation graph

Status: draft, 2026-09-05. Structure 6 of the spine.

## What it is

The links from a requirement to the decision record that answers it, from the record to the artifact field that carries the answer, and from the field to the generated thing derived from it. Generated things are code, configuration, check scripts, and documentation that a standard mandates. Documentation is otherwise not development output, so it is not a leaf of the graph.

The graph exists for one purpose: root-cause revision. The owner walks backward from a behavior to the record that caused it, revises the record, and walks forward to everything that must be regenerated. Nothing else is touched.

## Link kinds

| Kind | Direction | Drives | Agent-method link | Gap |
|---|---|---|---|---|
| must-exist-before | From the thing needed first to the thing that needs it | Authoring order; the guided walk over undecided records | `depends-on` / `depended-on-by` | None at artifact level |
| must-be-consistent-with | Symmetric | The consistency check of artifact review | `related-to` | `related-to` also carries "see also", so it may not be precise enough (to confirm) |
| derives-from | From the generated thing to the artifact or field it came from | Regeneration; the forward and reverse walks | None in front matter. The automated-checks note says "derived from this note" in prose, and each check's Source column names a sentence | Missing as a typed link. Generated things under `implementations/<N>/` have no front matter, so they cannot carry reciprocals |
| containment | From part to whole | Navigation by subject; the required artifact set | `is-part-of` / `includes` | Not a derivation kind. Kept for the subject catalog |

Two dependency kinds are kept apart because they drive different things. Conflating them makes the walk order wrong or the audit noisy.

## Granularity

Start at artifact level, which agent-method's conventions already support. Refine to field level only when a real case demands it. The first real case is already visible: a technical design depends on an interface's synchronous-or-asynchronous answer, not on the whole interface, and each check in `automated-checks-2.md` traces to one use-case sentence, not to the whole use case. Field-level targets would name a question number in a registry entry, or a record id, since questions are never renumbered (to confirm the anchor form).

## The reverse walk

From a behavior the owner dislikes in a prototype to the requirement.

1. Name the behavior as the owner saw it at the checkpoint.
2. Find the check that exercises it in the automated-checks note. If no check exercises it, that is a level 2 finding: a decided question with no verified-by.
3. Follow the check's Source column to the artifact field: a use-case sentence or a record decision.
4. Follow the field to the decision record that answers it, and read its provenance and ratification.
5. Follow the record to the requirement it satisfies, in the use case or the vision.
6. Revise at the record. If the fix cannot be expressed as a record revision, a question is missing from the registry, and it is harvested as such.

Worked example, from the workbench. Suppose the owner dislikes where a new idea appears in the list.

| Step | Node |
|---|---|
| Behavior | Pressing New puts the empty idea among the other placeholders at the top of the list |
| Check | `newGivesEmptySelectedInTopGroup`, sequence B step 2 of `automated-checks-2.md`: 58 rows, the selected row has class `empty`, every row before it is also `empty` |
| Artifact field | Source column: "Edit ideas, New ideas". The sentence is silent on position among existing empties, which is why the run reported it as a use-case ambiguity (to confirm the exact wording) |
| Decision record | The ordering decision in `implementation-structure-2.md`: empties first, then case-insensitive order, creation order among equals. Provenance agent-made-while-building, because the use case did not say |
| Requirement | Initial UI: placeholder sorted first; case-insensitive order. Edit ideas: New gives an empty, selected, editable idea |

The revision is a superseding record with provenance owner-stated. The forward walk from it lists the Edit ideas sentence as a proposed markup for the owner, `implementation-structure-N`, the check, and the implementation.

## The forward walk

From a revised record to everything that must be regenerated.

1. Start at the superseding record.
2. List every record linked to it by must-be-consistent-with. Each is revised or flagged.
3. List every artifact field that carries the record's answer.
4. List every generated thing with a derives-from link to those fields: code, configuration, checks, mandated documentation.
5. Regenerate the listed set from the artifacts, in must-exist-before order. Nothing outside the list is touched.
6. Run the checks derived from the revised fields.

## ADR 0007 and what the graph adds

ADR 0007 is the existing rule: every produced file is derived from an artifact; when file and artifact disagree the artifact is corrected first and the file regenerated; contracts between produced things are tables in artifacts, such as the hooks table; decisions made while producing are captured in the governing artifact. The regeneration test is applied at checkpoints by asking whether a fresh agent could rebuild this from the repository.

The graph adds what makes the rule traversable. The derivation is explicit and typed rather than stated in prose, so a script can walk it in either direction. The reverse direction exists at all, from behavior to requirement. The affected set of a revision is computed, not estimated. Field granularity is available where a real case demands it.

## Extending the link validator

Agent-method's link validator, third version, checks that every link in `workbench/` front matter has its reciprocal in the other file. The graph extends it in four ways, none of which needs new tooling beyond the validator itself.

| Extension | What it checks |
|---|---|
| A derives-from link kind, with a reciprocal name (to confirm) | Reciprocity, as for the existing kinds, wherever both ends are artifacts |
| Targets without front matter | Generated things under `implementations/<N>/` cannot carry a reciprocal. The artifact side holds a manifest instead: the record's Artifacts section and the checks note's hooks and Source tables. The validator checks that every file under `implementations/<N>/` is named by at least one derives-from link |
| Field-level targets | A link may name a question number or a record id. The validator checks the target exists and has not been renumbered |
| The silence rule at graph level | Every required question of every subject has a record, and every record with status decided has at least one derives-from link or a verified-by of review checklist item |

## Open questions

- Whether `related-to` is precise enough to mean must-be-consistent-with or a new link type is needed.
- The anchor form for field-level targets: question number, record id, or heading (to confirm).
- Whether generated things should gain a header comment naming their derives-from source, since they cannot carry front matter (to confirm).
- Whether the graph is links in files or edges in a real graph. The overview leaves this to the data model.
- Whether mandated documentation is a leaf, or an artifact with its own derives-from links.
