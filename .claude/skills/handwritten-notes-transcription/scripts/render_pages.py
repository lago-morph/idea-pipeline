#!/usr/bin/env python3
"""Render a PDF of handwritten notes into PNG chunks sized for visual reading.

Usage:
    render_pages.py <pdf> <outdir> [--dpi 300] [--max-height 1800] [--overlap 20]
    render_pages.py <pdf> <outdir> --clip PAGE,X0,Y0,X1,Y1 [--dpi 900]

Default mode renders every page, splitting any page taller than --max-height
points into overlapping vertical chunks (scanning apps often emit one very
tall page). Chunk mode (--clip) re-renders a single rectangle at high DPI so
an ambiguous word can be examined closely.

Requires PyMuPDF:  pip install pymupdf
"""

import argparse
import sys
from pathlib import Path


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("pdf")
    ap.add_argument("outdir")
    ap.add_argument("--dpi", type=int, default=300)
    ap.add_argument("--max-height", type=float, default=1800,
                    help="max page height in points before splitting into chunks")
    ap.add_argument("--overlap", type=float, default=20,
                    help="points of vertical overlap between chunks")
    ap.add_argument("--clip", help="PAGE,X0,Y0,X1,Y1 in PDF points; renders only that rect")
    args = ap.parse_args()

    try:
        import pymupdf
    except ImportError:
        print("PyMuPDF not installed. Run: pip install pymupdf", file=sys.stderr)
        return 1

    doc = pymupdf.open(args.pdf)
    out = Path(args.outdir)
    out.mkdir(parents=True, exist_ok=True)

    if args.clip:
        page_no, x0, y0, x1, y1 = (float(v) for v in args.clip.split(","))
        page = doc[int(page_no) - 1]
        rect = pymupdf.Rect(x0, y0, x1, y1)
        path = out / f"zoom-p{int(page_no):02d}-{int(x0)}_{int(y0)}.png"
        page.get_pixmap(dpi=args.dpi, clip=rect).save(path)
        print(path)
        return 0

    for i, page in enumerate(doc, start=1):
        r = page.rect
        # Report embedded text: if a page already has a text layer, the PDF is
        # not purely handwritten and that text is worth reading directly.
        text = page.get_text().strip()
        if text:
            print(f"# page {i}: embedded text layer present ({len(text)} chars)",
                  file=sys.stderr)
        n = max(1, int(-(-r.height // args.max_height)))
        h = r.height / n
        for c in range(n):
            top = max(r.y0, r.y0 + c * h - (args.overlap if c else 0))
            bottom = min(r.y1, r.y0 + (c + 1) * h + args.overlap)
            clip = pymupdf.Rect(r.x0, top, r.x1, bottom)
            name = f"page-{i:02d}.png" if n == 1 else f"page-{i:02d}-chunk-{c + 1}.png"
            path = out / name
            page.get_pixmap(dpi=args.dpi, clip=clip).save(path)
            # y-range is printed so --clip coordinates can be derived for zooms.
            print(f"{path}\ty={top:.0f}..{bottom:.0f}\tpage_rect={r.width:.0f}x{r.height:.0f}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
