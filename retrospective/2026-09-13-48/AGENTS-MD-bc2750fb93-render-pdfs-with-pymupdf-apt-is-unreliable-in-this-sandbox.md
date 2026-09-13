# agent instruction

**Render PDFs with PyMuPDF; apt is unreliable in this sandbox.** When `Read` on a PDF fails because `pdftoppm` is missing, do not reach for `apt-get install poppler-utils` — the package mirror returns 404 here. Run `pip install pymupdf` and render pages with it. The `handwritten-notes-transcription` skill's `scripts/render_pages.py` already wraps this, including splitting very tall single-page scans and re-rendering one rectangle at high DPI.

*Grounded in: first attempt to read the scoped-sandbox notes PDF.*

# justification

The first PDF of the session could not be read by the `Read` tool (no `pdftoppm`), and the reflex fix — `apt-get install poppler-utils` — failed with a 404 from the Ubuntu mirror. `pip install pymupdf` succeeded in seconds and rendered every page at any DPI needed for the rest of the session, including 2000 dpi zooms on single words. Without this rule the next session repeats the two failed attempts before finding the one that works. Marginal cost of the rule: one pip command, already scripted.
