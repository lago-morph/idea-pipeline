# agent instruction

**Pin the corpus.** Before citing line numbers into external documents (the four gold specs or any future corpus), fetch fresh copies and verify line counts match the versions the prior analysis measured (`wc -l` equality). On mismatch, stop and re-anchor before citing.

*Grounded in: the four gold specs matching the profiles' measurements exactly (2,090 / 1,467 / 2,169 / 2,185), which made hundreds of prior line citations safely reusable.*

# justification

This repo's analysis chain (profiles → artifact model → future checkers) is welded together by line numbers into documents this repo does not control. The check is one `wc -l` per document; skipping it and citing into a drifted upstream would silently corrupt every downstream table. In the task-01 session the check passed and unlocked confident reuse; the day it fails is the day it pays for itself.
