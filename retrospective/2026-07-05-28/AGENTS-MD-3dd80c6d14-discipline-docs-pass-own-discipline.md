# agent instruction

**Discipline docs must pass their own discipline.** Before shipping a document that prescribes rules (complete enums, mechanical exit criteria, change control), audit the document against its own prescriptions: every enum it defines is complete, every criterion it states is evaluable over its own schemas, and every general rule it declares either holds internally or carries a declared exception. The document's own prescriptions are its review checklist.

*Grounded in: three process.md defects found by self-application — an "all fields filled" criterion contradicting an optional field, a status (APPLIED) that was neither open nor terminal under the hygiene rule, and a change-control rule its own A-GL artifact could not obey.*

# justification

Three of the twelve defects caught in process.md's re-read passes were self-application failures: exit criterion S0-X1 demanded "all fields filled" over a schema with an optional field; the S6 question-hygiene rule enumerated the open statuses but left APPLIED (neither open nor terminal) in limbo; and the change-control rule "artifacts go CONTROLLED at producing-stage exit" was violated by the document's own A-GL design. None of these is visible to a reader checking prose flow — each is visible instantly to a reader asking "does this document obey the rule it just stated?". The audit costs one targeted pass; shipping a process spec that contradicts itself costs credibility exactly where the document demands rigor from others, and every such contradiction becomes a process-defect record the first time someone executes it.
