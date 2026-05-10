# Spec: Browser History Intelligence

**Post-Phase 6 project (enters ideas pipeline queue)**
**Repo:** new — to be created

---

## What It Is

A pipeline that aggregates browser history from multiple devices (work computer, iPhone,
iPad), filters to IT/software/AI content only, analyzes for interest patterns, and
produces a categorized queue of topics and technologies worth pursuing further —
paired with smart bookmarks and top-level reference material for each.

This is one of the input feeds for the ideas pipeline. It surfaces latent interest
patterns that wouldn't make it into explicit idea capture.

---

## Current State

- Does not exist
- The most independent project in the portfolio — no hard dependencies on other new
  projects, can be built and run standalone
- The output (a structured interest queue) feeds into the ideas pipeline but doesn't
  require the pipeline to exist first

---

## Recommended Design

**Sources:**
- Chrome/Safari history export from work laptop
- iOS Safari history (iCloud sync or direct export)
- iPad history (same mechanism)
- Bookmarks and reading lists from the same sources

**Pipeline:**
1. Extraction: platform-specific history export scripts
2. Filter: keep only IT/software/AI domains (by URL pattern + content classification)
3. Deduplication and normalization
4. Pattern analysis: what topics appear frequently? what clusters emerge?
5. Categorization: group into themes (Kubernetes, AI agents, infrastructure, etc.)
6. Queue generation: produce a ranked list with links and brief context per topic
7. Smart bookmarks: for each high-interest topic, find the canonical reference page,
   best tutorial, and most relevant recent content

---

## Open Questions

- How is history extracted from iOS/iPad devices? iCloud sync to Mac first, or direct
  device export?
- How often does this run — one-time analysis or periodic refresh?
- What is the output format — a markdown doc, GitHub Issues, or an entry in the ideas
  pipeline database?
- How does it distinguish "I visited this for research" from "I visited this by accident"?

---

## What Needs to Happen Next

1. Research history export mechanisms for each platform/browser combination
2. Build the extraction and filter layer (can be simple Python scripts)
3. Run a one-time analysis to validate the pattern detection quality
4. Define the output format to match whatever the ideas pipeline expects

---

## Dependencies

**Depends on:** nothing (most independent project in the portfolio)
**Enables:** Ideas pipeline (one of its capture sources), personal tech radar
