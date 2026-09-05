# Decision records

Status: draft, 2026-09-05. Structure 5 of the spine.

## What a decision record is

The answer to one question, from one artifact type, for one subject. A record is the smallest unit a human can ratify or revise. It is where an agent's choices during a build become visible, attributable, and reversible. Agent-method holds these today as lines in a per-implementation decisions note, with "repeated unchanged" and "new in implementation N" markers. The record makes the fields of that line explicit.

## Fields

| Field | Values or form | Purpose |
|---|---|---|
| subject | a subject catalog id | What this decision is about |
| artifact type, question | registry entry id, question number | Which question is being answered. Questions are numbered and never renumbered, so records stay comparable across implementations |
| status | undecided, decided, deliberately open with bounds, inherited, not applicable with reason | Silence is never a valid state. "Deliberately open" states the bounds. "Inherited" names the source record. "Not applicable" states the reason, usually a profile value |
| answer | free text, or a value from the question's option space | The decision |
| provenance | owner-stated, owner-ratified, agent-proposed, agent-made-while-building, extracted-with-evidence | Who made it and how. This field is what makes review possible |
| ratification | unratified, ratified, rejected, superseded | Whether the owner has accepted it. Only the owner's word in conversation ratifies. A merge never does |
| rationale | link to an ADR, or short text | Why. ADRs stand alone and are referenced, never inlined |
| evidence | links | For extracted records: where in the existing system the answer was found. For decided records: where it is implemented |
| binding time | design, build, deploy, runtime | Inherited from the question's tag; may be overridden with a reason |
| implementation | implementation number, or "all" | Which implementation this record applies to. Records that hold across implementations are standards |
| history | prior record ids | When superseded, the chain back |

## Status rules

- A registry question that is required for this subject at this maturity level, and has no record, is a defect. Artifact review catches it.
- A record with status undecided and provenance agent-proposed is a question the agent is asking the owner. It appears in the owner's work queue.
- A record with provenance agent-made-while-building and ratification unratified is harvested debt. Every such record must be ratified, revised, or rejected before the next implementation starts. This is the rule that keeps prototypes from silently becoming the specification.
- A record with status not-applicable carries the profile value or maturity level that makes it so, and flips to undecided automatically when that value changes.

## The review workflow

This is the workflow the whole spine exists to enable.

1. An implementation is produced. Its run yields records with provenance agent-made-while-building, plus an ambiguity list.
2. The owner walks the unratified records by subject. Grouping by subject means the owner reviews one component's choices together, which is how a human evaluates a design.
3. Each record is ratified, revised, or rejected. A revision creates a superseding record with provenance owner-stated and a link to the one it replaces.
4. The derivation graph lists what depends on each revised record: artifacts, other records, generated code, checks. Those are regenerated. Nothing else is touched.
5. Rejected records with no replacement become undecided, and the next run must ask before choosing.

The owner never edits generated code to fix a decision. The record is the root cause. If a fix cannot be expressed as a record revision, that is a missing question in the registry, and it is harvested as such.

## Standards

A record that holds for every implementation, or for every subject of a kind, is a standard. Agent-method's implementation-standards note is a set of these. In the spine a standard is a record with implementation "all" and a binding level. Records at a lower level inherit it unless they override, and an override carries a reason. This is how platform-level decisions reach components without being re-decided.

## What this looks like as files

Not decided. Two candidates, to be chosen when the workbench's existing decisions notes are rewritten as records in phase 2 of `../plan.md`:

- One decisions note per subject per implementation, as agent-method does today, with each line carrying the fields above as a table row. Cheapest to adopt. Comparison across implementations is by reading two files side by side.
- One file per record. Most precise, most files. Comparison is a query over front matter.

Either way, the fields are the same, and the link validator that already exists in agent-method extends to check them.
