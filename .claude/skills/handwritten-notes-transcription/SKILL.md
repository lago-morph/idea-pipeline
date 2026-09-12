---
name: handwritten-notes-transcription
description: Transcribe a PDF (or photo/scan) of handwritten notes into verbatim markdown, shown chunk-by-chunk next to the rendered page images so the user can check the transcription against the original. Use whenever the user attaches or points at a PDF, photo, or scan of handwritten notes and asks to capture, transcribe, type up, digitize, "get the text", or "capture the raw text" from it — including when they also name a destination file. Covers rendering the PDF to images, splitting very tall single-page scans, zooming on ambiguous words, marking uncertainty inline rather than guessing, asking how the result should be saved when the user has not said, and always preserving the raw transcription alongside any later cleaned-up or reorganized product.
---

# Handwritten notes → markdown

Capture what is on the page, verbatim, and make it cheap for the user to
verify. Two rules carry most of the value:

1. **Never silently guess.** A word you cannot read gets marked, not invented.
2. **The raw transcription is preserved, always.** Every other product —
   an organized version, a summary, a spec — is *in addition to* it, never
   instead of it.

---

## When to use this skill

**Activate when:** the user attaches or references a PDF, photo, or scan of
handwritten notes and wants the text out of it — "transcribe this", "capture
the text", "type this up", "get the raw text into a markdown file", "here are
my notes on X".

**Do not activate for:** PDFs that already carry a real text layer (just read
them), printed-document OCR at volume, or transcribing audio.

---

## Workflow

### 1. Render the pages to images

`Read` on a PDF needs a page renderer. If `pdftoppm` is missing, install
PyMuPDF (`pip install pymupdf`) — that usually works where `apt-get
install poppler-utils` does not.

```bash
python3 .claude/skills/handwritten-notes-transcription/scripts/render_pages.py \
    <input.pdf> <scratchpad>/notes-render --dpi 300
```

The script prints one line per image with the page rectangle and the y-range
it covers — keep that output, it is what you use to aim zooms in step 3.

Handwriting scanning apps often emit **one very tall page** rather than many
normal ones. The script splits any page taller than `--max-height` into
overlapping chunks automatically. Chunks that are roughly 1500–1800 points
tall read reliably; a full 2300-point page in one image does not.

If the script reports an embedded text layer on a page, read that text
directly — it is more reliable than reading the rendering.

### 2. Read each chunk and transcribe it

Read the chunk images in order. Transcribe **verbatim**: keep the writer's
line breaks, indentation, bullet characters, abbreviations, underlines
(`_word_` or a note), boxed or circled emphasis, arrows, and margin notes.
Do not fix spelling, expand abbreviations, reorder, or "tidy" anything. If
the writer wrote `w/`, it stays `w/`.

Preserve the *shape* of the notes — indent levels are usually carrying
structure the writer intended.

### 3. Resolve ambiguities before presenting

For any word you are not confident about, re-render just that rectangle at
high DPI before you settle on a reading:

```bash
python3 .claude/skills/handwritten-notes-transcription/scripts/render_pages.py \
    <input.pdf> <scratchpad>/notes-render --clip 1,400,1090,514,1160 --dpi 900
```

`--clip` takes `PAGE,X0,Y0,X1,Y1` in PDF points, from the page rectangle and
y-ranges the default run printed.

Context resolves most of them: a list reading `Database / MCP / Git / Cloud`
settles whether an angular glyph is `MCP` or `MLP`. Use the surrounding
list, the writer's own letterforms elsewhere on the page, and the subject
matter.

**If zooming and context do not settle it, stop and mark it.** Do not pick
the most likely word and move on. Two things happen:

- Inline, at the spot: `statement none [word uncertain]`, or
  `[illegible: ~6 letters]`.
- In the presentation (step 5), call it out explicitly: which word, what
  your best reading is, and that you could not confirm it.

The user wrote the notes. They can read a word you cannot in one second.
A silent wrong guess can survive into every downstream product.

### 4. Decide the destination — ask if the user has not said

**If the user named a destination** (a filename, a section, an existing
document), use it.

**If they did not, ask before writing anything.** Offer these, and make sure
the display-only option is stated clearly — it is often what the user
actually wants, and it is easy to forget to offer:

- **Display only** — you print the transcription in the session as plain
  text formatted as markdown, in a fenced block, so the user can copy-paste
  it or save it themselves through the harness UI. No file is written.
- **A new file in the repo** — you propose a path and write it.
- **Into an existing document** — appended or as a new section.

State your default plan in the same breath so the user can just say "yes":
"I'll save the raw notes to `NN-name.md` unless you'd rather I just display
them." Let them override. Do not write a file over an explicit "just show
me".

### 5. Present the transcription next to the raw data

This is the check-my-work step, and it is not optional. The user needs to
compare what you typed against what they wrote **without** opening the PDF
and scrolling next to your output.

Go chunk by chunk. For each chunk, in this order:

1. Send the rendered chunk image (`SendUserFile` with `display: "render"`,
   or the equivalent inline image in whatever surface you are in).
2. Immediately follow it with the transcription of *that chunk only*, in a
   fenced plain-text block.

So the user reads: image, its text, next image, its text. Each chunk's text
sits directly under its own image. Do not dump all the images and then all
the text — that recreates the scrolling problem this step exists to solve.

After the last chunk, list the ambiguities from step 3 in one place, so
nothing is buried mid-scroll.

Then save (or don't) per step 4.

### 6. Ask what happens next

Once the transcription is saved or presented, ask — do not assume:

> Would you like to discuss the idea, or organize these notes into
> something structured?

Those are the two normal next moves. Discussing means exploring the content;
organizing means restructuring the raw text into sections, a spec, a
proposal. Wait for the answer. Transcribing is a complete deliverable on its
own.

---

## Preserving the raw transcription

The raw text is the artifact of record. It is the only thing in the session
that is a faithful copy of what is on the page.

- When saved to a file, the verbatim text lives under a clearly labelled
  heading — `## Raw transcription` — and everything else in that file goes
  in other sections.
- When any organized, cleaned-up, or summarized product is produced later,
  in this session or a later one, the raw transcription **stays**. It is
  never replaced, overwritten, or edited into the organized version.
- If the user chose display-only, the fenced block in the session *is* the
  preserved copy. Say so, and re-display it if the session produces a
  derived product later so the raw text does not scroll out of reach.
- The transcription is only ever edited to *correct* it against the
  original — for example when the user resolves an ambiguity you marked.

---

## Anti-patterns

- **Guessing an unreadable word.** The whole point of marking uncertainty is
  that the user can resolve it instantly. A confident wrong word is worse
  than a flagged one, because it does not look like it needs checking.
- **Reading a 2300-point page as one image.** The rendering is legible in
  the small; at full page height the letterforms blur. Split it.
- **Tidying while transcribing.** Fixing spelling, expanding `w/`, merging
  fragmentary lines into sentences, or reordering bullets all destroy
  information about how the writer was thinking. Transcribe; organize later
  and separately, if asked.
- **Dumping all images then all text.** Verification depends on adjacency.
- **Writing a file when the user has not said where things go.** Ask.
- **Forgetting to offer display-only.** It is the lightest option and often
  the right one.
- **Rolling straight from transcription into analysis.** The user asked for
  the text. Ask before going further.
- **Letting an organized version replace the raw one.** The raw transcription
  outlives every derived product.

---

## Acceptance criteria

1. Every page and chunk of the source has been read and transcribed.
2. The transcription is verbatim — structure, indentation, abbreviations and
   margin notes preserved; nothing corrected or reordered.
3. Every word not confidently read is marked inline **and** called out to
   the user; no silent guesses.
4. Each chunk's rendered image was shown immediately above its own
   transcription.
5. The destination was the user's choice — either one they named, or one
   they confirmed after being offered display-only as an option.
6. The raw transcription is preserved as its own labelled artifact.
7. The user was asked whether to discuss or organize, and the answer was
   waited for.

---

## Helper script

`scripts/render_pages.py` — renders a PDF to PNG chunks (default mode) or
re-renders one rectangle at high DPI (`--clip`). Requires PyMuPDF. It never
modifies the source PDF.
