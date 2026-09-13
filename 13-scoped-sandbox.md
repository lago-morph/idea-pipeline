# Scoped Sandboxes

**Source:** handwritten notes, 2026-09-12

---

## Raw transcription

Scoped Sandboxes                                        2026-09-12

Idea:

  When working with AI agents, introduce a concept of scoped
  sandboxes.

  What this means is for every large task, during planning an
  explicit input/output interface is defined.

  This is not for security, it is to focus attention.   (!!)

  Each task has, as input, definition of the following:

  - Files
      - Git
      - Ephemeral working

  - AI files (skills, agents.md, harness config)

  - Resources + Credentials

      Database
      MCP
      Git
      Cloud

  - Network rules

  - Tools

      Programs able to use w/ knowledge

  Every item is tagged

    - CRUD permissions
    - If it is easily recreated (and how).  Must be explicit recipe or
      positive statement that it is not possible/intended to recreate
      exact state.
    - Expected concurrency
    - Expected use (with details in prompt)

  There is deterministic linting at end
      for information, to improve process,
      NOT for security or automated
      remediation.

  The driving use case is for organizing
  the work of AI agents, with some
  combination of the following attributes

  - Subagents for parallelization or to
    preserve orchestrator agent context

  - Repeatability for controlled experiments

      - How context affects tasks
      - Comparing models, harnesses, skills
      - experiments when 1 variable changes

  - Reducing accidental context
    pollution

  - As a clarification mechanism to
    define tasks well for both humans and
    agents

  - Explicit scope/change definition to
    reduce complexity for both humans and
    agents.

  Enabling technologies

    Dynamically scoped credentials

      - Create tightly scoped access tokens/keys
        as needed for specific tasks

    Beads
    Sparse GIT worktrees

---

## Appendix A — Session capture, 2026-09-12/13

**What this is.** A capture of the ideas exchanged in the session that
transcribed the notes above, grouped by topic rather than by time. It holds
what was said — including suggestions that were modified or dropped — so the
whole context can be picked up again later. Both voices are compressed; key
phrases are quoted.

**What this is not.** Not a design, not a prioritized list, not a set of
decisions. Where a decision *was* made explicitly in the conversation it is
marked as such. Everything else is still open. Summarizing and shaping a
solution out of this comes later.

Attribution: **J** is the author of the notes. **A** is the agent. Lines
marked **A (interpretation)** are the agent's read of intent, mood, or
values — offered as context for the words, not as words the author said.

---

### A.1 The author, as the agent read them

*A (interpretation), offered because it shaped how the agent responded.*

- The stated goal is encapsulation, but the felt problem is **attention**:
  losing the thread on a context switch, in an environment that is already
  distracting. J named ADHD and mild autism, and observed that agents show
  many of the same tendencies. This reframed the whole idea from a
  technical mechanism to an externalized executive function — a scaffold
  that answers "what am I doing, what may I touch, when am I done" so no
  one has to hold it in working memory.
- J's wife's comment — J overcomplicates, agents overcomplicate, and this
  project is an attempt to work with an agent to be *less* complicated —
  was offered with humor. J then took it up as the brief, "but with a
  little more nuance." The agent treated it as the governing constraint
  from that point on.
- J wants to **build something, not discuss endlessly**, and said so. At
  the same time J wants to keep "having fun talking about the ideas and
  capturing them for later." Both are real. The resolution J reached is a
  tightly scoped MVP plus a cheap place to park everything else.
- Frustration triggers J named: tedious ceremony ("I will quickly get
  frustrated and give up if it feels like tedious ceremony"), and
  credentials scattered everywhere so it is unclear what an agent needs.
- The beneficiary is **"future Jonathan."** The agent read this as the
  test for every proposed mechanism: does it pay off on re-entry, and is
  the cost invisible at the time of writing?
- J trusts agents to refactor well from solid specs and a clean
  architecture. This is why J was comfortable dropping speculative
  scaffolding — a lean thing can be extended later.

---

### A.2 The problem being solved

- **J:** Both the human and the agent get distracted, do several things at
  once, and lose track of where they are. The scoped sandbox is a set of
  conventions to make it easier to keep track of the scope of a task,
  especially for a human context-switching in a distracting environment.
- From the notes: "This is not for security, it is to focus attention"
  (marked `!!`). Both J and A returned to this line repeatedly.
- **A:** Attention-scoping is cheaper than enforcement-scoping and that is
  a feature. Enforcement has to make things impossible; an attention scope
  only has to make the boundary visible. "A contract you can read beats a
  wall you can't cross, when the goal is orientation." This also lets the
  end-of-task lint stay advisory.
- **A:** A context switch is expensive because you re-answer three
  questions: what was I doing, what am I allowed to touch, what does done
  look like. The scope declaration is those answers precomputed.
- **A:** The corpus already has the pieces separately —
  `define-done-first`, `front-load-context`, `intent-ledger`,
  `fresh-context-reset`. The scoped sandbox bundles them into one artifact
  both human and agent read on re-entry.
- **J:** Two things should always be part of the encapsulation: a
  **definition of done** and a **statement of the problem being solved.**

---

### A.3 What a scope declares

From the notes, each task has as input: files (git, ephemeral working), AI
files (skills, agents.md, harness config), resources and credentials
(database, MCP, git, cloud), network rules, tools. Every item tagged with
CRUD permissions, recreatability, expected concurrency, expected use.

What happened to that list in conversation:

- **A** proposed that the MVP encapsulation had converged to four fields:
  **Problem**, **Done**, **Scope** (directories, each with CRUD), **Later**.
  J did not object to the four; J added the requirement that the agent, not
  J, writes them (see A.4).
- **J:** Per-directory scope on a git repo plus explicit per-directory
  CRUD "is almost free — everything else can be added later."
- **Stubs — proposed, narrowed, then dropped.** J initially wanted "at
  least a stub of most of the mechanics" so later additions would be
  enhancements rather than re-architecture. **A** pushed back that stubs
  are speculative code, "the overcomplication trap wearing a disguise,"
  and offered a middle: a stub is a named field allowed to be empty, not a
  code path. **J** then went further than A's suggestion: no stubs at all.
  Implement the lean MVP and nothing else, "with a concession of an
  unstructured notes field if I just can't help myself." *Explicit
  decision.*
- **A** on the notes field: it is also where the agent puts "this didn't
  fit the four slots," which stops it inventing a fifth.
- **A:** The recreatability tag is the most valuable item in the notes'
  list and the least common — it answers "can I just blow this away and
  start over?", which is the scariest re-entry question. (See A.6 for
  where this landed.)
- **A:** The concurrency tag gives a checkable rule for parallel subagents
  for free: two scopes both declaring write on the same item can't run at
  once. Not taken up by J in this session.
- **A:** The margin note in the transcription — "explicit recipe or
  positive statement that it is not possible/intended to recreate exact
  state" — is the recreatability rule stated precisely.

---

### A.4 Declaration cost, and who does the work

This was the most emphatic theme from J.

- **J:** "I won't want to specify anything. I'll tell the agent to do it."
  The agent does most if not all of the writing, tracking, and preserving.
  "A human will get frustrated with the overhead immediately."
- **J:** If possible the machinery is invisible unless needed. Reviewing a
  plan is much easier if the agent has already drafted the structure, and
  a draft of the structure helps clarify boundaries and objective before
  handing a task to an agent.
- **J:** Turning a draft task into one ready to execute "should be a
  conversation with the human where the AI captures intent and fills in
  the blanks on its own."
- **J:** Clear algorithms to assemble the scope, "with as many
  deterministic scripted bits as possible," keep the cost to J's attention
  low. "This is essential."
- **A** named the one place the human must read: plan review before
  handoff. Everything else automatic.
- **Task size — A proposed a tripwire, J rejected it.** A worried that
  "anything worth specifying" would lead the ADHD half of J to specify
  everything, and proposed: "if you'd be sad to lose your place on it, it
  gets a scope." **J** pushed back: J will not be specifying; the agent
  decides what size warrants the machinery, and **adapts on its own by
  paying attention to J's behavior**, applying it more or less as J's
  reactions indicate. A withdrew the tripwire. *Explicit decision that the
  agent judges and adapts.*
- **A** then offered one observation to keep alongside it: adaptation
  needs a signal, and the cheapest is J overriding ("scope this" / "don't
  scope this") with the agent tracking the overrides. Offered as an
  observation, not a mechanism.
- **J** on which tasks qualify (before handing the judgment to the agent):
  epics certainly, probably refined stories or tasks; bugs or placeholder
  beads wait until enriching them adds more benefit than overhead.
- **A** suggested **profiles** — named starting scopes ("docs-only",
  "k8-platform change", "controlled experiment") with a task's scope as a
  diff from one — and that the end-of-task lint could feed the profiles by
  reporting where reality diverged. J did not respond to this directly;
  it is unaddressed, not rejected. A noted the notes for idea 14 say the
  same thing ("different profiles specified @ startup").

---

### A.5 Persistence, the carrier, and snapshots

- **J:** Declaration and tracking persist along with the work and the
  results. Not just a way to recreate inputs but outputs too, "so we can
  see start to finish and mine old tasks to use as a basis for new
  experiments, or to analyze what went right or wrong."
- **J:** **Beads** is the initial choice for carrying this information.
  "It has to be displaced to consider anything else." *Explicit.*
- **A** had suggested "the bead *is* the scope card" as the cleanest
  answer to where the declaration lives. Consistent with J's choice.
- **Snapshotting outputs.** **A** warned that snapshotting would "eat you"
  and suggested pointing instead: commit range, PR, lint delta, bead
  closing note. **J** stated the intended mechanism, which is a specific
  version of pointing: scope limited initially to objects in git; the
  snapshot is **a list of files and directories and a single commit hash,
  plus the bead**, which stays around after closure. The bead is "the
  place to put the breadcrumbs that allow one to reconstruct inputs and
  outputs. Then everything stays together." Anything else goes to Later.
  *Explicit.*
- **J:** "Later" is a **file, not a bead**, at this stage — J does not want
  to use beads to work out the idea itself. *Explicit.* (A had earlier
  suggested Later as a bead tagged `later`; superseded.)

---

### A.6 Files, recreatability, and what git gives for free

- **J:** Include in the MVP "the easiest mechanism that already gives 90%
  of the benefit": git files and directories and their commits.
- **J:** Scope should assume a PR. The input will already carry a commit —
  perhaps a single input commit for all git-tracked items.
- **J:** Anything not tracked in git is assumed **not recreatable**.
  *Explicit.*
- **A** had proposed a one-bit-per-directory "safe to blow away and
  regenerate" flag as cheap enough for v1. **A** reads J's
  git-tracked-or-not rule as subsuming it — tracked implies regenerable
  from the commit — but J did not say this.
- **J** flagged for the Later pile, **high priority**: track agent harness
  config, skills, and agents.md files that affect results but are not in
  the repo (e.g. in the user's home directory). **A** agreed this is the
  gap most likely to make an experiment silently non-repeatable.
- From the notes: sparse git worktrees as an enabling technology. **A**
  observed that every declared category in the notes has a physical
  realization already listed — files → sparse worktree, tools/network →
  devcontainer, credentials → secrets bundle, AI files → what is mounted —
  so the declaration and the environment can be the same document read
  two ways. Not pursued further in this session.

---

### A.7 Credentials

- From the notes: resources and credentials are one of the declared
  categories; dynamically scoped credentials are an enabling technology.
  The related notes are in `14-scoped-secrets.md` (by reference; not
  re-transcribed here).
- **J:** Start with **a single code that gives all-access to a secret
  store.** Initial credential bundling is **for convenience, not
  security** — the frustration is that credentials "live all over the
  place" and it is confusing to figure out which ones an agent needs.
  Limited lifetime and least privilege come later, "if I end up wanting
  it." *Explicit.*
- **J:** Will probably start as a skill wrapper around AWS Secrets Manager
  or an equivalent, focused on convenience. Anything more involved, like
  the vault-with-a-password idea in 14, is "for later or never if not
  needed."
- **A** raised the tension between "not for security" and credentials
  being plainly security, and proposed the resolution: security is a
  welcome side effect but every design decision is made for attention.
  "If minting a scoped credential is too annoying to do for focus alone,
  it's too annoying."
- **A** asked that "one key opens everything" be written into Later as a
  consciously accepted blast-radius risk, "so it was a choice and not a
  drift." J did not object.

---

### A.8 Re-entry

Open by J's own statement. What was said:

- **J:** Could be a one-sentence summary of objective and current status,
  expandable into more detail "in a way that doesn't require the agent
  context to be filled with summaries of current work." First cut is
  progressive disclosure: low fidelity first, deeper only when needed.
- **A** proposed a concrete shape to react to, three levels, with the
  agent reading only the top two by default:
  1. **Title** — the bead title, one sentence, the objective.
  2. **Status line** — one sentence in the bead body, agent-maintained
     at every checkpoint commit: where we are, what's next.
  3. **Full scope** — the fields, opened only when the status line isn't
     enough.
  "The human's re-entry is reading one sentence. The agent's re-entry is
  reading two." J has not yet responded to this shape.
- **A** earlier framed the "re-entry ritual" as the agent reading the
  scope card back to the human with the delta between declared and
  actually-touched. This predates the three-level proposal and is
  compatible with it.

---

### A.9 Linting, sub-scopes, and nesting

- From the notes: deterministic linting at the end, "for information, to
  improve process, NOT for security or automated remediation."
- **A:** The lint must stay informational — "the moment it blocks, people
  game it." A's suggested use: report declared-vs-touched deltas, and let
  the deltas improve profiles over time. (Profiles: see A.4, unaddressed.)
- **J:** Sub-scopes are **convention.** Not sure yet whether to do anything
  beyond implementation guidance. One cheap check: run the parent scope's
  linter over any sub-scope, advisory only — "that feels like a v2.0 idea
  though."
- **A** had asked whether nesting (subagent scope ⊆ orchestrator scope) is
  a rule, a lint, or a convention. J's answer: convention.

---

### A.10 Use cases carried from the notes

Named in the notes as the driving attributes, not elaborated further in
the session except as noted:

- Subagents for parallelization or to preserve orchestrator context.
  **A:** the scope declaration is exactly the brief you hand a subagent.
- Repeatability for controlled experiments — how context affects tasks;
  comparing models, harnesses, skills; one-variable changes. **A:** a
  declared scope plus recipes *is* the experiment fixture; hold the scope,
  swap the variable. J tied this to the persistence goal: mining old
  tasks as the basis for new experiments.
- Reducing accidental context pollution.
- A clarification mechanism to define tasks well for both humans and
  agents. J's "draft task → conversation → ready to execute" (A.4) is the
  operational form of this.
- Explicit scope/change definition to reduce complexity for both humans
  and agents.

---

### A.11 MVP versus Later — as discussed, not as decided

J was explicit that, except where stated, the MVP-versus-Later split has
**not** been decided. This section records what was *said* about the
split, in the words used, without ranking.

Things J explicitly placed in the first cut:
- Problem statement and definition of done in the encapsulation.
- Per-directory scope on a git repo with per-directory CRUD.
- Recreatability by git-tracked-or-not; scope assumes a PR.
- Snapshot as file/directory list plus one commit hash plus the bead.
- Beads as carrier.
- Agent writes it all; invisible unless needed; agent judges task size
  and adapts.
- Single all-access credential via a convenience skill.
- No stubs; an unstructured notes field as the pressure valve.

Things J explicitly placed in Later (or "later or never"):
- Tracking harness config / skills / agents.md outside the repo — J
  called this **high priority** within Later.
- Advisory parent-scope lint over sub-scopes ("v2.0").
- Limited-lifetime and least-privilege credentials.
- The vault / password / transient-secrets ideas from idea 14.
- Anything about outputs beyond the git-object snapshot.

Things A suggested that are neither accepted nor rejected:
- Profiles, and lint deltas feeding profiles (A.4, A.9).
- The three-level re-entry shape (A.8).
- Override-tracking as the adaptation signal (A.4).
- Writing the single-key blast radius into Later as an accepted risk
  (A.7).
- The "every category has a physical realization" observation (A.6).
- The concurrency-tag rule for parallel subagents (A.3).

Things A suggested that J rejected or superseded:
- The task-size tripwire (A.4).
- Stubs as empty named fields — J went further and dropped stubs
  entirely (A.3).
- Later as a bead — J: a file, for now (A.5).

---

### A.12 The parallel J asked to keep

**A** observed, and **J** asked to have shown, that the discipline used to
transcribe the handwritten notes at the top of this document is the same
discipline the scoped sandbox asks for on a task. The right column mixes
what J has said with A's proposals that are still open (see A.11); it is
the parallel as A sees it, not an agreed design.

| Transcribing the notes | Running a scoped task |
|---|---|
| Capture the page verbatim before anything else | Write Problem, Done, Scope before any work |
| Author's intent goes in; agent's invention stays out | Agent drafts; human's intent is what gets captured; no agent-invented scope |
| Unreadable words are marked, never guessed | Untracked or unknown items are declared not-recreatable, never assumed |
| Show the transcription next to the source so the author can check it | Show the plan to the human once, before handoff |
| Author corrects; corrections *are* the transcription | Human overrides; overrides *are* the signal the agent adapts to |
| Raw transcription is preserved; organizing happens after, separately | Declaration persists with the work; lint and analysis happen after, advisory |
| Enhancement is fenced off until capture is done | Enhancement is a Later item, not a change to the running scope |

The skill that encodes the left column was written and revised during
this same session, and its second revision was driven by exactly the
lesson the right column needs: the author's corrections are not
annotations on the record, they *are* the record.

---

### A.13 How this appendix was made

Recorded because J said this round of the conversation belongs in the
capture too.

- **J** asked for the ideas from the notes, the session's prompts, and A's
  reactions to be captured into a section of this document, labelled an
  appendix pre-emptively, doing "for this session what you earlier did
  with my handwritten notes." A was to say what it understood the request
  to be, give feedback, and wait.
- **A** proposed conversation order to preserve reversals, J's words
  verbatim with A's condensed, no separate Later file yet, and idea 14 by
  reference.
- **J** redirected: **theme, not time** — "transcription by theme." No
  conclusions past what was discussed. Include what was pursued and later
  modified or dropped, explicitly including A's rejected suggestions: "it
  all belongs so that the whole context can be understood later." Compress
  *both* voices as long as intent is preserved; quote key phrases. Later is
  part of the transcript, not a decision. Resist jumping to deliverables
  like a prioritized feature list. Inject A's read of intent, mood,
  objectives, and values, phrased as interpretation. Include this round.
  Idea 14 by reference. Show the parallel in A.12.
- What A did with that: the section structure above; A.1 for the
  interpretive read; A.11 as a record of what was said about the split
  rather than a ranking; A.12 as the parallel.

*End of Appendix A.*
