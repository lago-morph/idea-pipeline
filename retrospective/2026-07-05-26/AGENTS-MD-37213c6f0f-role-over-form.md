# agent instruction

**Role over form.** When classifying spec content (this repo's artifact model, checklists, or checkers): the artifact is determined by what the content DOES, never by its notation (BNF, table, prose) or its document position (body vs. appendix). Expect abstract enums written in grammar notation and normative contracts living in appendices.

*Grounded in: attractor writing an abstract enum in BNF (L1141–47) and keeping a normative wire contract in Appendix C.*

# justification

Every future task in this repo (task-02 authoring, task-03 checkers) classifies spec content. Both obvious mechanical keys — notation and position — misfile real gold-spec content: BNF marks an abstract domain enum, appendices hold first-class failure models, and rationale sits in normative bodies. A checker keyed on surface form will systematically misfire; this rule is the one-line inoculation, and it was load-bearing in all four PR #26 decomposition tables.
