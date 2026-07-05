# agent instruction

**Declare the exception at the rule.** When a general rule meets a case that genuinely cannot comply, write the exception into the rule's definition site and into every place the rule binds — never leave it implicit for readers to reconcile. An undeclared exception is a latent contradiction; a declared one is a design decision.

*Grounded in: A-GL's glossary half violating "artifacts go CONTROLLED at producing-stage exit" until the exception was declared at the rule (§3.3), the producing stage card (S2), and the production map (§7).*

# justification

process.md's change-control rule is one sentence; the A-GL glossary genuinely cannot obey it (terms accrue with every artifact that introduces them, long after A-GL's producing stage exits). The first draft left that tension implicit, and the re-read flagged it as a contradiction a pressure-test executor would have had to improvise around — the exact failure mode (SCHEMA_MISFIT, ruling required) the pressure test exists to count. The fix cost three sentences, one at each site where the rule binds. The asymmetry: declaring an exception is a few lines at authoring time; an undeclared one becomes a judgment call made independently — and differently — by every future executor, which is the definition of the ambiguity this whole repo is trying to eliminate.
