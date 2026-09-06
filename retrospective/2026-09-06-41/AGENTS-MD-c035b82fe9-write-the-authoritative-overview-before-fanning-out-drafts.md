# agent instruction

**Write the authoritative overview before fanning out drafts.** When splitting a document set across parallel subagents, write the overview that fixes vocabulary and structure first, commit it, and make every subagent read it before drafting. Order dependent drafts so a subagent never has to assume a sibling document that does not exist yet. Ask each subagent to end with a five-line list of the judgment calls it made.

*Grounded in: the registry draft that had to be realigned after the maturity ladder landed mid-flight.*

# justification

Three general-purpose subagents drafted eight spine documents in parallel. All three read `spine/overview.md` and `spine/decision-record.md` first, and the drafts came back using one vocabulary, which is why the consistency pass found only one contradiction across nine files. The one problem was a dependency: the registry's "first required at" column needed the maturity ladder, which another subagent was writing at the same time. The registry subagent used an assumed ladder, then re-read the real one when it appeared and moved eleven values. That worked, but only because the subagent noticed. Sequencing the ladder before the registry would have cost a few minutes of wall clock. The five-line judgment-call summary from each subagent was what made review cheap: every deviation was named, and four of them went straight into the decisions log.
