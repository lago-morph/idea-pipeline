---
name: handwritten-notes-transcription
description: Transcribe a PDF (or photo/scan) of handwritten notes into markdown, shown chunk-by-chunk next to the rendered page images so the author can check it. Use whenever the user attaches or points at a PDF, photo, or scan of handwritten notes and asks to capture, transcribe, type up, digitize, "get the text", or "capture the raw text" from it — including when they also name a destination file. Covers rendering the PDF to images, splitting very tall single-page scans, zooming on ambiguous words, marking what can't be read instead of guessing, asking how the result should be saved when the user has not said, and keeping enhancement or reorganization fenced off until the transcription is captured.
---

# Handwritten notes → markdown

Capture what the author meant to write, and make it cheap for them to check.

---

## The line: author intent in, agent invention out

The transcription captures the author's intent. The author may correct a
reading, rearrange lines, or expand a shorthand note into a full sentence.
**Those are the transcription** — write them in clean, with no bracket and
no note about where they came from.

You add nothing. Your moves are mechanical only: read the marks, keep the
structure, mark what you cannot read. Never reword, interpret, infer a
meaning, complete a fragment, or fix what looks like a mistake.

Enhancement and reorganization — restructuring, sectioning, summarizing,
analysis — happen **only after** the transcription is captured, as a
separate product built on top of it. Never mixed into it.

---

## When to use this skill

**Use it when** the user attaches or references a PDF, photo, or scan of
handwritten notes and wants the text out of it.

**Skip it for** PDFs that already carry a real text layer (just read them),
printed-document OCR at volume, and audio.

---

## Workflow

### 1. Render the pages

`Read` on a PDF needs a page renderer. If `pdftoppm` is missing, install
PyMuPDF (`pip install pymupdf`) — that usually works where `apt-get install
poppler-utils` does not.

```bash
python3 .claude/skills/handwritten-notes-transcription/scripts/render_pages.py \
    <input.pdf> <scratchpad>/notes-render --dpi 300
```

Note-taking apps often emit **one very tall page** instead of many normal
ones. The script splits any page over `--max-height` into overlapping
chunks. Keep its output — the page rectangle and per-chunk y-ranges are how
you aim zooms in step 3.

If it reports an embedded text layer, read that text directly.

### 2. Transcribe each chunk

Read the chunks in order. Keep the author's line breaks, indentation,
bullets, abbreviations, underlines, boxed or circled emphasis, arrows, and
margin notes. Indent levels usually carry structure the author intended.

### 3. Zoom on anything unclear, then mark what's left

Re-render the rectangle at high DPI before settling on a reading:

```bash
python3 .claude/skills/handwritten-notes-transcription/scripts/render_pages.py \
    <input.pdf> <scratchpad>/notes-render --clip 1,400,1090,514,1160 --dpi 900
```

`--clip` takes `PAGE,X0,Y0,X1,Y1` in PDF points.

Letterforms settle most of it: compare the glyph against the same letter
elsewhere in the author's own hand.

**If it still won't resolve, mark it — never pick the likely word.** Inline
at the spot (`statement nove [not read]`), and again in the step-5
presentation. The author reads it in one second; a silent wrong guess
survives into everything downstream.

### 4. Decide the destination

If the user named one, use it. If not, **ask before writing anything**, and
make sure the lightest option is on the table:

- **Display only** — print the transcription in the session as plain text
  formatted as markdown, in a fenced block, for the user to copy-paste or
  save through the harness UI. No file written.
- **A new file** — propose a path.
- **Into an existing document** — appended or as a new section.

State your default in the same breath so they can just say yes: "I'll save
it to `NN-name.md` unless you'd rather I just display it."

### 5. Show the transcription next to the raw data

Go chunk by chunk. For each: send the rendered chunk image, then
immediately the transcription of **that chunk only** in a fenced block.
Image, its text, next image, its text.

Do not dump all images then all text — adjacency is the whole point.

After the last chunk, list any unresolved marks in one place.

### 6. Apply corrections, then ask what's next

Fold the author's corrections straight into the transcription per **The
line** above, and re-save.

Then ask — don't assume:

> Would you like to discuss the idea, or organize these notes into
> something structured?

Transcribing is a complete deliverable on its own.

---

## Keeping the transcription

- In a file, it lives under its own `## Raw transcription` heading;
  everything else goes in other sections.
- Derived products (organized versions, summaries, specs) are **additions**.
  The transcription is never replaced, overwritten, or edited into them.
- If the user chose display-only, the fenced block in the session is the
  copy of record. Say so, and re-display it if a derived product comes
  later.

---

## Anti-patterns

- **Guessing an unreadable word.** A confident wrong word doesn't look like
  it needs checking.
- **Interpreting while transcribing.** Expanding `w/`, merging fragments
  into sentences, fixing spelling, reordering bullets — all of it is the
  agent adding input. Only the author may do that.
- **Annotating the author's own corrections.** They aren't edits to the
  transcription; they are it.
- **Reading a 2300-point page as one image.** Split it.
- **Dumping all images then all text.**
- **Writing a file when the user hasn't said where things go.**
- **Rolling from transcription into analysis.** Ask first.

---

## Acceptance criteria

1. Every chunk of the source is transcribed.
2. Nothing in it came from you but mechanical reading; every author
   correction is folded in clean.
3. Anything not confidently read is marked inline and called out.
4. Each chunk's image was shown immediately above its own transcription.
5. The destination was the user's choice, with display-only offered.
6. The transcription is kept as its own artifact.
7. The user was asked whether to discuss or organize, and answered.

---

## Helper script

`scripts/render_pages.py` — renders a PDF to PNG chunks, or one rectangle
at high DPI (`--clip`). Requires PyMuPDF. Never modifies the source.
