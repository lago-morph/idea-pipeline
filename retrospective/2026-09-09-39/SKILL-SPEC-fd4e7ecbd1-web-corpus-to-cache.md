# Spec: `web-corpus-to-cache`

- **ID**: SKILL-SPEC-fd4e7ecbd1
- **Source retrospective**: ../2026-09-09-39.md

## Intent

Fetch a heterogeneous list of web sources (blog posts, documentation pages, arXiv papers, GitHub READMEs, feeds, sitemaps) into a gitignored cache directory as clean markdown-ish text, one file per source with a SOURCE-URL header line, so downstream subagents can read them without network access and no copyrighted full text lands in git. Built from the agent-patterns Phase 1 acquire step, where 86 sources were fetched with a ~40-line urllib+html2text script after discovering the sandbox ships neither bs4 nor html2text and that RSS feeds truncate history.

## Trigger

- Direct: "fetch these sources into the cache", "acquire the bibliography", "download these URLs as text".
- Proactive: any research/ingest task where multiple subagents will later read the same web material — fetch once to disk instead of letting each subagent re-fetch.
- Negative: a single page needed once (just fetch it inline); material behind login or paywall (record `access: signup`/`paid` in the bibliography and skip — never scrape around access controls).

## Inputs

- A list of `name URL` pairs (name becomes the cache filename; choose names that double as bibliography ids).
- A cache directory that is confirmed gitignored **before** the first fetch.
- Optionally: a blog to enumerate with a date lower bound, and a topic filter for titles.

## Outputs

- `<cache>/web/<name>.txt` per source: first line `SOURCE-URL: <url>`, then markdown-converted text. PDFs saved as `<name>.pdf` unconverted.
- A fetch report: OK/FAIL per name with size, so dead URLs are caught at acquire time, not when a subagent reads an empty file.

## Workflow

1. Verify the cache directory is gitignored (`git check-ignore <dir>` must succeed). If not, stop and fix `.gitignore` first.
2. `pip install html2text` if missing (the sandbox does not ship it; nor bs4).
3. Write the fetch script once: urllib with a normal User-Agent, 60 s timeout, `html2text` with `body_width=0` and images ignored; write `SOURCE-URL:` header then the converted text; branch on `Content-Type` for PDFs. Read `name URL` pairs from stdin so batches are heredocs.
4. Run the fetches in batches; check the OK/FAIL lines. A "success" that is suspiciously small or starts with a cookie-banner/JS shell needs a spot-check with `sed -n '3,10p'`.
5. To enumerate a blog: fetch `sitemap.xml`, extract `<loc>`/`<lastmod>` pairs, filter by date bound and by plausibly-on-topic title slugs; only fall back to the RSS feed when there is no sitemap (feeds commonly carry only ~10 entries).
6. For arXiv: abstract page (`/abs/`) suffices for triage-depth work; use `/html/<id>` for full text when it exists. Say in the cached file's consumer notes when only an abstract was fetched.
7. Commit nothing from the cache; commit only the fetch log/bibliography updates.

## Concrete examples

### Example 1: the Willison guide (18 files)

The guide index was fetched first, chapter links extracted with one grep, and all 16 chapters fetched in one heredoc batch (`willison-aep-red-green-tdd https://simonwillison.net/guides/agentic-engineering-patterns/red-green-tdd/`, …). Result lines like `OK willison-aep-hoard: 13016 chars` confirmed real content; the whole guide landed in `.cache/web/` in one command.

### Example 2: enumerating addyosmani.com since 2025-03-01

`https://addyosmani.com/feed.xml` returned only 10 items. The sitemap (`432 urls, 274 blog posts`, with `<lastmod>` on 262) gave the full dated history; filtering by date and AI-relevant title slugs yielded 40 posts, all fetched in one generated batch. Spot-checks caught that `osmani-2026-gemini-cli` was 139 KB (fine) and that the Anthropic docs pages carried an llms.txt banner but real content below it.

## Anti-patterns

- **Fetching before the gitignore exists.** The session's mbox incident shows how easily raw material lands in the index; the cache must be ignored before it is populated.
- **Trusting the feed for history.** The Osmani feed silently hid 30 of 40 relevant posts.
- **Assuming converter libraries exist.** `import html2text` and `import bs4` both failed in the sandbox; probe and install first.
- **Treating HTTP 200 as content.** JS-shell pages and consent walls return 200; size and spot-check are the real signal.
- **Working around paywalls or signup gates.** Out of scope by policy; record the access level and move on.

## Acceptance criteria

- [ ] Every requested source has either a cache file with a SOURCE-URL header or an explicit FAIL in the report.
- [ ] `git status` shows nothing staged from the cache directory after the run.
- [ ] Blog enumerations state which mechanism (sitemap vs feed) produced the list and the date bound applied.
- [ ] Abstract-only fetches are distinguishable from full-text fetches by the consumer.

## Files this skill creates / modifies

- `<cache>/web/<name>.txt` (or `.pdf`) — one per source, gitignored.
- `<scratchpad>/fetch.py` — the fetch script (scratch).
- The project's bibliography/fetch log — access levels and dead-URL notes (committed).
