# agent instruction

**Use the sitemap, not the feed, to enumerate a blog.** "When enumerating a site's posts for a date-bounded harvest, do not trust the RSS/Atom feed — feeds commonly carry only the latest ~10 entries. Fetch `sitemap.xml` and filter on `<lastmod>` dates; fall back to the feed only when no sitemap exists."

*Grounded in: addyosmani.com's feed listing 10 posts where the sitemap yielded all 40 relevant posts since 2025-03-01.*

# justification

The agent-patterns Phase 1 acquire step had to enumerate Addy Osmani's AI-development posts since 2025-03-01. The natural first move — fetch the RSS feed — returned exactly 10 items, all from the previous six weeks. Stopping there would have silently dropped 30 of the 40 relevant posts, including the highest-value ones (`good-spec`, `intent-debt`, `agents-md`) that ended up cited across a dozen pattern pages, and nothing in the feed says it is truncated. The sitemap fetch was one extra request and a five-line parse of `<loc>`/`<lastmod>` pairs, giving the complete dated history. The asymmetry: one HTTP request versus an invisible 75% hole in the corpus that no later phase would have flagged, because triage can't rate what acquire never fetched.
