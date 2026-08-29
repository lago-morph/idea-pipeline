---
id: every-2026-07-13-polish-agent-built
title: How I Polish Software That Agents Built
author: Kieran Klaassen
date: 2026-07-13
url: (Gmail export, local mbox)
access: gmail
accessed: 2026-08-29
scope: interactive
relevance: high
pass: distilled
patterns: [polish-pass, run-app-beside-the-agent, dictate-what-feels-wrong]
---
## Summary

The author argues that with planning and agents doing the coding, the remaining
human work is deciding whether the result is any good and pushing it past what
the agent could reach alone. He calls this final step "polish." The worked
example: a pull request had passed every automated check and the review agents
had nothing left to flag, yet an email card animated in from the top of the
screen instead of opening from where he clicked. A command in their compound
engineering plugin checks out the branch, starts the dev server in the
background, and opens the running app inside the editor next to the agent. He
uses the feature, dictates what feels wrong — the animation, then too much
whitespace and cards that need to be more compact — and the app hot-reloads
until it looks right. Note: this email is truncated at a paywall; only the
setup and one example are in the text.

## Takeaways for our use case

- Treat "all checks green and review agents silent" as the start of your own review, not the end of review — automated checks say nothing about whether the result is good.
- Make the running artifact visible next to the agent in the same window, so the loop is use-it, say what's wrong, watch it hot-reload, look again.
- Script the setup of that loop (check out the branch, start the dev server, open the app) so the friction of looking at the real thing is near zero.
- Feed back subjective, sensory complaints in plain language — density, spacing, animation direction, timing — rather than trying to specify them in advance.
- Dictating the complaint out loud is fast enough to keep the loop tight; the point is low-latency reaction while looking at the thing.
- Accept that a plan cannot carry this: a plan can ask for a magazine feel, but only a human looking at the page can say when the density is right.
- Judgement about qualities the model has no access to (taste for this product, these users) is the part of the work that stays yours.

## Candidate patterns / evidence

- → polish-pass: a deliberate final step after automated checks pass, where the human uses the software and tells the agent what feels off until it doesn't.
- → run-app-beside-the-agent: their `/ce-polish` command checks out the branch, starts the dev server in the background, and opens the running app inside the editor next to the agent, then gets out of the way.
- → dictate-what-feels-wrong: the animation and whitespace fixes came from speaking the complaint aloud and looking again after hot-reload, not from a written spec.
- → supervise-first-run (supporting): the agent's PR passed every automated check and still shipped a visibly wrong animation, so a human first look was what caught it.

## Other-use-case material

- The overnight-agent framing (waking to a stack of green pull requests to review before the first meeting) is a long-running-agent workflow; flag as `scope: long-running`.
- Paywalled and therefore not distilled: how polish changed the author's planning and reviewing, and when a muttered complaint becomes a standing rule the agent follows on future features. The second of those looks directly relevant and is worth chasing in a fetchable source.
