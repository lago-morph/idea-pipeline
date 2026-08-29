---
id: hoard-working-code
title: Hoard working code and point at it
type: pattern
status: candidate
durability: structural
scope: interactive
tools: both
category: session-setup
verified: 2026-08-29
models: [claude-5, gpt-5.6]
confidence: medium
sources: [willison-2026-aep]
related: [front-load-context]
aliases: []
---
# Hoard working code and point at it

**Use when:** the task resembles something you or someone else has already solved, and you
would otherwise describe the behaviour in prose.

**Do:**
- Keep a personal collection of small proven solutions — a tools repo, TILs, scratch
  experiments — and treat it as an asset, not clutter.
- Point the agent at working code rather than describing what you want: an analogous
  feature in this repo, a sibling project, or a reference repo cloned to `/tmp` so it can
  never land in your commit.
- Name well-known software explicitly when it exists; the name does the work of a
  specification.
- When you get a trick working once, save it where you can point at it again.

**Why:** an agent recombines two working examples into a third thing far more reliably than
it invents from scratch, and a trick only has to be figured out once.

**Don't / when not:** don't point at code you haven't verified works — a broken reference
propagates.

**Evidence:**
- [willison-2026-aep] a personal hoard of proven working examples is the key asset, since an agent needs a trick figured out once to reuse it forever.
- [willison-2026-aep] the newsletter-tool prompt clones a reference repo to `/tmp` and says "similar to how the Atom feed works" in place of a detailed spec.
- [willison-2026-aep] "compile gifsicle to WASM" does enormous work because the software is old and widely known.
