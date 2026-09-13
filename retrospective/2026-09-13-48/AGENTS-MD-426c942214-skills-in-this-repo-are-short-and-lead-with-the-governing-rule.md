# agent instruction

**Skills in this repo are short and lead with the governing rule.** Structure a skill as: the one rule that governs it first (a section called "The line"), then when to use it, a numbered workflow, one-line anti-patterns, acceptance criteria. Cut worked examples that only restate a rule already given. Aim under ~200 lines. The author's standard, verbatim: "Skills should be helpful and unambiguous and short."

*Grounded in: handwritten-notes-transcription cut from 212 to 166 lines on request.*

# justification

The first version of `handwritten-notes-transcription` said each rule three times — in prose, in a worked example, and in an anti-pattern — and ran 212 lines. The author asked for the key rule "in a more direct concise way" and added that skills should be helpful, unambiguous, and short. The revision lost 46 lines and no behaviour. The second skill of the session, `preserve-context`, was written to this shape from the start and needed no revision. Cost of ignoring the rule: a revision PR per skill. Cost of following it: writing the governing sentence first.
