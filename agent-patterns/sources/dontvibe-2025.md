---
id: dontvibe-2025
title: "Professional Software Developers Don't Vibe, They Control: AI Agent Use for Coding in 2025"
author: Ruanqianqian Huang, Avery Reyna, Sorin Lerner, Haijun Xia, Brian Hempel
date: 2025-12-16
url: https://arxiv.org/abs/2512.14012
access: direct
accessed: 2026-09-13
scope: interactive
relevance: high
pass: distilled
patterns: [calibrate-autonomy, cognitive-surrender, plan-before-code, small-reviewable-steps, front-load-context, review-agent-diffs, tier-review-by-risk, agentic-manual-testing, give-a-runnable-check, checkpoint-commits, agents-md-hygiene, comprehension-debt]
---

## Summary

Two-part 2025 study of developers with three or more years of professional
experience: 13 field observations (45-minute think-aloud on their own real task,
plus interview) and a 99-respondent qualitative survey of GitHub users active in
agentic-coding repos. The headline is that professionals do not vibe code. All 13
observed participants controlled implementation at some level, and 11 of 13
controlled design — writing plans themselves, revising an agent's draft, or having
the agent polish their own. Survey respondents reported modifying agent output
about half the time, and 50 of 99 drove architecture themselves. Agents were rated
suitable for small, repetitive, scaffolding, test, documentation and simple-debugging
work; unsuitable for complex tasks, business logic, legacy integration, and
security-critical or high-stakes work. High-level planning was the most divided
question. No respondent endorsed fully autonomous operation, yet enjoyment was
high (mean 5.1/6).

## Takeaways for our use case

- Control is exercised at two distinct points — who decides the design, and who
  checks the implementation — and the study found practitioners holding both, even
  when the agent writes every line.
- Plans were kept human-owned far more often than they were delegated: agents were
  rated strongly suitable for *following* a well-defined plan (28 suitable vs 2 not)
  but were the most contested for *producing* high-level design (13 vs 23).
- Big plans were fine; big executions were not. The largest observed plans ran past
  70 steps but were run in chunks of at most six, with a median of 1.8 steps actually
  executed per prompt.
- Prompt detail was the main lever people reported: name files, variables, error
  messages, libraries and the specific step to do now. Respondents repeatedly said
  long prompts beat short ones and that vague prompts are what send agents off the rails.
- Review depth tracked familiarity, not policy: the nine participants working inside
  their expertise read every agentic change, while the three working outside it
  skipped line-by-line review but policed the agent's decisions and outputs instead
  (for example rejecting dependencies it tried to install).
- Verification was overwhelmingly concrete — running the CLI, reading diffs, clicking
  the UI, attaching a debugger — and UI, database and remote-app checks stayed manual.
- The unsuitable list is worth treating as a checklist before delegating: complex
  logic, big multi-file coordinated changes, business logic needing domain context,
  integrating with legacy code, performance-critical code, CI/deployment, and
  anything security-critical or privacy-sensitive.
- Agents were reported doing more than asked — extra files, rewritten sections,
  unrequested packages — by 8 of 13 observed participants, which is an argument for
  small units and cheap rollback rather than for better prompts alone.
- The authors' own caveat: tooling has improved since the study, so the task-suitability
  table may shift; they expect the control-and-supervision finding to persist.

## Candidate patterns / evidence

- → `calibrate-autonomy`: task suitability was coded across 89 task types; agents were
  judged fit for small, repetitive, scaffolding work and unfit as complexity, domain
  knowledge or stakes rise — and no respondent said agents could replace human
  decision making (0 suitable vs 12 not).
- → `cognitive-surrender`: every observed participant and every survey theme kept a
  human in the loop; one respondent summed the norm up as "never let the agent be
  completely autonomous", and enjoyment was conditional on staying in control.
- → `plan-before-code`: 11 of 13 observed participants owned the plan before
  implementation, and following a well-defined plan was the second-highest-rated
  agent strength in the survey.
- → `small-reviewable-steps`: 70-plus-step plans were executed at most six steps at a
  time; the median across participants was 1.8 executed steps per prompt, explicitly
  to maintain control.
- → `front-load-context`: prompts were coded into 43 context types (top ten tabulated);
  clear context and explicit instructions were the most-cited strategy (12 of 13
  observations, 43 of 99 surveys), and respondents reported longer prompts working better.
- → `review-agent-diffs`: the nine in-expertise participants reviewed every agentic
  change, and one-shotting code without modification or verification was among the
  most rejected uses (5 suitable vs 23 not).
- → `tier-review-by-risk`: review depth varied with domain familiarity and stakes —
  line-by-line review inside one's expertise, decision-and-output monitoring outside
  it, and avoidance entirely for high-stakes/privacy (0:8) and security-critical (2:5) work.
- → `agentic-manual-testing`: verification tactics were manual exercise as often as
  suites — clicking the UI, browser dev tools, debuggers — and testing stayed manual
  for UI interactions, databases and remote applications.
- → `give-a-runnable-check`: agents were reported highly effective at a bug when
  pointed at a specific failing test, and one participant had the agent generate tests
  for every change to reinforce TDD.
- → `checkpoint-commits`: participants leaned on version control specifically to make
  rollback cheap after bad agent runs.
- → `agents-md-hygiene`: persistent user rules were used by 3 of 13 observed and 18 of
  99 surveyed to encode project specs, general guidelines and corrections; one
  respondent maintained a project context file alongside descriptive commit messages.
- → `comprehension-debt`: participants objected to the agent changing code they did not
  understand, and one warned that agent output lets people ship something that works
  but is a nightmare to maintain; legacy-code integration was one of the worst-rated
  uses (3:17).
- → `form-your-own-take-first`: respondents described deliberately taking time over the
  implications of an agent's proposal before approving it, and one participant asked
  the agent to challenge his own proposal rather than confirm it.

## Other-use-case material

- Multi-agent parallelism was common (4 of 13 observations, 31 of 99 surveys) but
  manually configured, used to parallelize tasks or combine model strengths, with git
  and worktrees to merge the results — a long-running/multi-session concern rather
  than a single-session practice.
- The paper's future-work section is builder-facing: better interfaces for the planning
  step, for automated testing in realistic environments, and for understanding why an
  agent fails or hangs.
- The authors note there is no rigorously developed set of agent best practices yet and
  call for studying the most productive developers specifically — relevant framing for
  how much weight any practitioner corpus, including this wiki, should carry.
