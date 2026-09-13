# agent instruction

**A retrospective rule that was never assembled binds nothing.** "Do not treat a rule proposed in a past retrospective as being in effect. Before relying on one, check whether it reached the agents file or a hook; if it did not, either assemble it or treat the behaviour as ungoverned."

*Grounded in: a prior retrospective's rule about checking generated files for empty fields, which was never assembled, while the artifact it described stayed broken.*

# justification

An earlier retrospective in this repository proposed a rule requiring generated files to be grepped for empty extracted fields, grounded in the exact artifact this session had to repair. The rule was written, committed, and never assembled into the agents file — so it governed nothing, and the truncated artifact it described survived untouched until a human noticed it months later. The corpus this session maintains now documents precisely this failure mode as its own pattern: prose that is not in force does not bind. The marginal cost of the rule is one check before citing a past retrospective as authority. The cost of skipping it is the belief that a problem is handled because somebody once wrote that it should be.
