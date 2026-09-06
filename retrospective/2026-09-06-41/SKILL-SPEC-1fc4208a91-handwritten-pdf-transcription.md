# Spec: `handwritten-pdf-transcription`

- **ID**: SKILL-SPEC-1fc4208a91
- **Source retrospective**: ../2026-09-06-41.md

## Intent

Transcribe a handwritten or hand-drawn PDF, typically a tablet export with no text layer, into markdown that is verbatim in wording, normalized in spelling and formatting, and faithful to the page's structure, while honoring marker glyphs the author used to tag items. The skill earns its place because the built-in PDF reader could not render pages in this environment, the page turned out to be one vector canvas over eight thousand pixels tall, and getting a legible, checkable transcription took a specific sequence: install a renderer, render overlapping strips, read them in order, and re-render ambiguous regions at higher resolution before committing a reading.

## Trigger

Direct: the user attaches or names a PDF and asks to transcribe, type up, convert, or "make a markdown version" of it, especially with words like handwritten, notes, brainstorming, tablet, reMarkable, or verbatim.

Proactive: a PDF read returns no extractable text and no embedded images but has hundreds of vector drawings, which is the signature of a tablet export. Offer the skill before guessing at content.

Negative: do not use for PDFs with a text layer, where `pymupdf`'s `get_text()` returns content; use plain extraction. Do not use for scanned bitmaps where an OCR path is available and the user wants searchable text rather than a human-checked transcription.

## Inputs

- The PDF path.
- The user's formatting instructions: verbatim or edited, which spelling to normalize, whether headings and nesting should mirror the page.
- Any marker convention the user names, such as boxed glyphs meaning "definition of done", and what to do with them: transcribe, omit, or collect into a section.
- The destination path in the repository.

## Outputs

- One markdown file at the destination, with a short provenance note at the top stating the source and the normalization applied.
- Any marker-driven section the user asked for, such as a table of tagged items with the heading each sits under.
- A commit and pull request per the repository's conventions.

## Workflow

1. Try the built-in PDF reader with a page range. If it fails for lack of `pdftoppm`, install `pymupdf` with pip and continue with it. Do not attempt to install system packages.
2. Open the PDF with `pymupdf`. Print page count, each page's rectangle, `len(page.get_text())`, `len(page.get_images())`, and `len(page.get_drawings())`. A page with zero text, zero images, and many drawings is a vector canvas of handwriting.
3. If a page is taller than about 900 points, render it in strips. Use a clip height of 450 points with a 30-point overlap and 200 dpi. Save `stripNN.png` in the scratchpad directory. Print each strip's clip rectangle so ambiguous regions can be located later.
4. Read the strips in order with the image reader, at most five per call. Transcribe as you go into a working draft, preserving heading levels and list nesting as they appear on the page.
5. For every region where a word is unclear, a gap might hide faint content, or a line is cut at a strip boundary, re-render that region alone at 250 dpi from its y-range and read it. Do not guess. Record any remaining ambiguity as a note to the user, not as a silent choice.
6. Apply the user's normalization: fix spelling, expand obvious abbreviations only when the user asked for spelling updates, keep the author's wording otherwise. Preserve underlines and emphasis the author drew.
7. Handle markers as instructed. If the user wants tagged items collected, build a table with the item text and the heading path it sits under, and do not reproduce the marker glyphs inline.
8. Write the file with a provenance line. Commit, push, and open the pull request.
9. In the reply, list every reading that was ambiguous and how it was resolved, so the user can check those spots first.

## Concrete examples

### Example 1: a tall tablet export with definition-of-done markers

Input: `Architecture_ideas.pdf`, one page, rectangle 514 by 4189 points, zero text, zero images, 2060 drawings. The user asks for a verbatim transcription with spelling and formatting updates, says boxed "DoD" glyphs mark definition-of-done candidates, wants those collected in a table at the end with the architecture type each falls under, and wants the glyphs themselves omitted.

Steps: the built-in reader fails on `pdftoppm`; `pip install pymupdf` succeeds. Ten strips of 450 points at 200 dpi are rendered and read in two batches of five. Two regions are re-rendered at 250 dpi: an empty-looking gap under "Logical model of system", which proves to be blank, and the boundary between strips eight and nine under "Ops architecture", which proves to lose nothing. Four DoD glyphs are found: one under functional requirements, three under application architecture.

Output: `architecture-ideas/reference/brainstorming.md` with the page's five top-level sections as headings, nested bullets, the one underlined word kept underlined, and a closing "DoD candidates" table of four rows. The reply flags two readings for the user to check: "(Database messageQ)" expanded to "(database, message queue)", and "validation rules" squeezed under "input/output data structures" treated as part of that bullet.

### Example 2: a multi-page scan with a partial text layer

Input: a twelve-page PDF where pages one to three have a text layer and pages four to twelve are handwritten.

Steps: `get_text()` is non-empty for the first three pages; those are extracted directly and normalized. Pages four to twelve report zero text and are rendered whole at 200 dpi, since each is a normal page height, then read three at a time. One page has a diagram; it is described in a fenced block as "diagram: three boxes labeled A, B, C with arrows A to B and B to C" rather than transcribed as prose.

Output: one markdown file with a heading per page, a provenance note saying pages one to three were extracted and four to twelve transcribed from renders, and a list of two unclear words with the readings chosen.

## Anti-patterns

- **Reporting a page as empty because the text layer is empty.** The first read of the PDF returned nothing; the content was all vector strokes. Check drawings before concluding.
- **Rendering the whole tall page at once.** A 4189-point page at 200 dpi is over eleven thousand pixels tall and unreadable as one image. Strips with overlap are what made it legible.
- **Guessing at an unclear word to keep moving.** Two spots in the session needed a 250 dpi crop to settle; both would have been wrong guesses. Re-render, then read.
- **Transcribing marker glyphs inline when the user asked to omit them.** The DoD boxes were markers for a section, not content.
- **Installing system packages.** `apt-get` is not available here; `pip install pymupdf` is enough.

## Acceptance criteria

- [ ] Every line of handwriting on the page appears in the output, in the page's order and nesting, with no silent omissions.
- [ ] Every ambiguous reading is either resolved by a higher-resolution re-render or listed for the user in the reply.
- [ ] Marker glyphs are handled exactly as instructed, and any collected section names the heading path for each item.
- [ ] The output file states its provenance and the normalization applied.
- [ ] The scratchpad holds the strip renders so a reviewer can check any reading against the source.

## Files this skill creates / modifies

- `<destination>.md`: the transcription.
- `<scratchpad>/stripNN.png` and `<scratchpad>/<region>.png`: renders kept for review, never committed.
