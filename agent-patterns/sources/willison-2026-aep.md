---
id: willison-2026-aep
title: Agentic Engineering Patterns (guide)
author: Simon Willison
date: 2026-02-23 (ongoing)
url: https://simonwillison.net/guides/agentic-engineering-patterns/
access: direct
accessed: 2026-08-29
scope: interactive
relevance: high
pass: distilled
patterns: [red-green-tdd, run-tests-first, agentic-manual-testing, give-self-verification-tools, show-your-work-artifacts, subagents-for-context, git-with-agents, seed-context-from-recent-commits, hoard-working-code, reference-code-as-spec, name-known-software, linear-walkthroughs, interactive-explanations, small-reviewable-steps, review-agent-diffs, no-unreviewed-code, compound-engineering, prototype-to-decide]
---
## Summary

A living, book-shaped guide (14 chapters as of this reading, chapters explicitly updated over time rather than frozen) collecting practices for building software with coding agents — tools that both write and run code. Willison defines "agentic engineering" as professional engineers amplifying their own expertise with these tools, and deliberately reserves "vibe coding" for its original meaning: unreviewed, prototype-quality output nobody looked at. His organising premise is that typing code has become cheap while *good* code — working, verified, minimal, tested, documented, handling errors — has not, so most of our inherited habits about which trade-offs are worth it need re-deriving. The Principles chapters argue agents should raise quality rather than lower it: technical debt that is conceptually simple but tedious is now cheap to pay down, prototypes are cheap enough to settle design arguments empirically, and each project should end by feeding what was learned back into the instructions. The remaining chapters are concrete: how the agent loop actually works, Git as an agent-operated tool, subagents as context management, three testing chapters (red/green TDD, "first run the tests", agentic manual testing with browser automation), two chapters on recovering understanding of code you did not write, plus two line-by-line dissections of real prompts and an appendix of reusable prompts.

## Takeaways for our use case

- Short canonical phrases carry a lot of engineering discipline that models already know: "use red/green TDD" and "first run the tests" each unlock a whole practice from four words.
- Open a session against an existing repo by making the agent run the test suite — it forces it to learn the test command, gives it a size estimate of the project, and biases it toward testing its own later changes.
- Automated tests passing is not evidence the thing works; ask the agent to exercise the code the way a human would (`python -c`, `curl` against a dev server, a throwaway file in `/tmp`, a real browser) and then convert anything it finds into a permanent test.
- The single highest-leverage thing you can hand an agent is a way to check its own work; a CLI whose `--help` output is written to teach an agent is a better investment than a longer prompt.
- Make the agent record its manual testing as a document built from executed commands and their real output, so the record cannot drift into what it hoped had happened.
- Keep everything in Git and treat history as an editable narrative — agents are fluent enough at rebase, reflog, bisect and history surgery that "sort out this git mess" is a viable prompt.
- Starting a session with "review changes made today" cheaply loads recent code and commit messages into context and gives you something to build the next request on.
- Reach for a subagent to protect the top-level context window, not to build an org chart; the root agent can usually review or debug its own work if it has tokens to spare.
- Point the agent at working code rather than describing behaviour: an existing analogous feature, a sibling project, or a repo cloned to `/tmp` (so the reference never lands in your commit).
- Keep your own hoard of small proven solutions, because an agent can recombine two working examples into a third thing far more reliably than it can invent from scratch.
- Naming well-known software in a prompt ("compile gifsicle to WASM") substitutes for paragraphs of specification, and agents are unusually good at brute-forcing toolchains you would give up on.
- Treat not understanding your own codebase as cognitive debt with the same drag as technical debt, and pay it down with a generated walkthrough or an interactive/animated explanation of the specific mechanism you cannot picture.
- Never file a PR you have not reviewed yourself, including the agent-written description; ship several small commits or PRs and include evidence of your own testing.
- End work by writing down what you learned into the instructions the agent reads next time — quality compounds, and the cost of small improvements has collapsed.

## Candidate patterns / evidence

- → `red-green-tdd`: dedicated chapter — test-first suits agents because it guards against both non-working and never-used code, and watching the tests fail first is what stops a test that passes vacuously.
- → `run-tests-first`: "First run the tests" chapter — a four-word opener that makes the agent discover the test command, reveals project size, and puts it in a testing mindset for the rest of the session.
- → `agentic-manual-testing`: chapter arguing passing tests routinely coexist with obviously broken software, and that agent-driven manual exercise (`python -c`, `curl`, Playwright/Rodney) surfaces bugs the suite missed.
- → `give-self-verification-tools`: repeated across the manual-testing and both annotated-prompt chapters — agents do markedly better when handed a validation mechanism; `uvx <tool> --help` with agent-oriented help text is the delivery trick.
- → `show-your-work-artifacts`: the Showboat pattern — `note`/`exec`/`image` build a document where `exec` records the real command and real output, deliberately making it hard for the agent to write down what it wished had happened.
- → `subagents-for-context`: chapter frames subagents primarily as context-limit management (Claude Code's Explore subagent), with parallelism and specialist roles as secondary; warns against over-fragmenting into many specialists.
- → `git-with-agents`: chapter of prompts showing agents handle merge conflicts, reflog recovery, bisect, squashing and history rewriting well enough that Git's advanced features become routine rather than occasional.
- → `seed-context-from-recent-commits`: "review changes made today" is recommended as a session opener because the resulting `git log` loads both the modified code and the intent behind it.
- → `hoard-working-code`: chapter argues a personal collection of proven working examples (TILs, tools repo, research repo) is the key asset, since an agent only needs a trick figured out once to reuse it forever.
- → `reference-code-as-spec`: the newsletter-tool prompt clones a reference repo to `/tmp` and says "similar to how the Atom feed works", replacing a detailed spec; `/tmp` is chosen so the reference cannot be committed.
- → `name-known-software`: the gif-optimizer dissection notes that "compile gifsicle to WASM" does enormous work because the software is old and widely known, and that agents will brute-force an Emscripten toolchain past errors that would stop a human.
- → `linear-walkthroughs`: chapter where a vibe-coded SwiftUI app is made comprehensible by asking for a walkthrough that pulls code snippets via `sed`/`grep`/`cat` rather than retyping them, to avoid hallucinated code.
- → `interactive-explanations`: chapter naming "cognitive debt" and paying it down by commissioning an animated explanation of the one algorithm (spiral word-cloud placement) the prose walkthrough failed to make intuitive.
- → `small-reviewable-steps`: anti-patterns chapter — several small PRs beat one big one, and splitting work into separate commits is now easy because the agent does the Git work.
- → `review-agent-diffs`: same chapter — the first review pass is your job, and agent-written PR descriptions are convincing enough that they must be read and validated too.
- → `no-unreviewed-code` (anti-pattern): "Don't file pull requests with code you haven't reviewed yourself" — doing so delegates the real work to reviewers who could have prompted an agent themselves; attach manual-testing notes or screenshots as evidence.
- → `compound-engineering`: better-code chapter endorses Every's loop of ending each project with a retrospective whose lessons are written into the instructions future agent runs read.
- → `prototype-to-decide`: better-code chapter — agents make throwaway simulations and load tests cheap enough to run several at once, so technology choices can be settled by evidence instead of argument.

## Other-use-case material

- **`scope: long-running`** — the better-code chapter's recommended workflow for tedious tech-debt refactors is to hand them to *asynchronous* agents (Jules, Codex web, Claude Code on the web) working in a branch or worktree, then judge the resulting PR: land it, re-prompt it, or throw it away. The judgement criterion transfers to interactive work; the fire-and-forget mechanics do not.
- **`scope: long-running`** — code-is-cheap advises overriding the instinct that something is not worth the time by firing off an async session anyway, on the grounds that the downside is only wasted tokens. This depends on having somewhere to run work you are not watching.
- **`scope: meta`** — the "How coding agents work" chapter is background (tokens, chat templates, prefix caching, the tool loop, reasoning effort). The one operationally relevant detail is that agents avoid rewriting earlier conversation content to preserve the prefix cache.
- **`scope: meta`** — the Appendix collects non-coding prompts (artifact house style, proofreading, alt text, podcast highlights); useful as prompt craft, out of scope for coding patterns.
