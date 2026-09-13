# agent instruction

**Never invent a rating for material you could not fetch.** "If a source cannot be retrieved, do not give it a relevance rating, a summary, or a triage row inferred from its title or its citing document. Record the attempt, the exact URL, the failure, and the date where the next session will see it, and say plainly that it is unfetched."

*Grounded in: a catalogue cited by an ingested paper whose published path returned 404 and whose repository returned 403.*

# justification

A paper ingested in this session cited a companion catalogue by URL. The site was live; the cited path returned 404 and the repository returned 403. The corpus's triage table requires a relevance rating on every row, and a rating could have been inferred plausibly from the citing paper — which is exactly how a fabricated assessment enters a corpus whose entire value rests on traceability. The item went into the capture file instead, with the URL, both status codes, and the date. A future session can retry or ask the authors. The marginal cost is one line in a different file; the cost of the alternative is a corpus row asserting a judgement nobody made.
