# agent instruction

**No untested numeric claims in a skill.** Do not write a threshold, size, DPI, or limit into a skill that you have not measured in the session that produced it. If the number matters, test it once and say what was tested; if you can't, state the principle without the number.

*Grounded in: "1500–1800 points read reliably; a 2300-point page does not," written untested.*

# justification

The first `handwritten-notes-transcription` skill asserted that chunks of 1500–1800 points read reliably and a full 2300-point page does not. Neither had been tried — the page had simply been split into 384-point chunks and read. When the skill was applied to verify its own output, a 1173-point chunk read fine at a glance, and the full-page case was never tested at all. The numbers were cut in the revision. A wrong number in a skill is trusted by every future run; testing it costs one render.
