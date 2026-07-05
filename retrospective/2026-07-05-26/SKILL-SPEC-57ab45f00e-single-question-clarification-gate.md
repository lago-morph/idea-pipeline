# Spec: `single-question-clarification-gate`

- **ID**: SKILL-SPEC-57ab45f00e
- **Source retrospective**: ../2026-07-05-26.md

## Intent

When a user delegates a long-running task and invites questions before going away, the naive move is to ask everything that comes to mind; the expensive failure is asking questions the material already answers (burning the user's last minutes at the keyboard) or asking nothing and guessing wrong on a real fork. This skill inserts a triage gate: survey every referenced document first, strike every question the material answers or explicitly delegates, ask only the genuine forks (with a recommended default first), and convert the near-miss questions into a stated-defaults veto list. In the source session, a task file plus its siblings eliminated all but one candidate question; the single `AskUserQuestion` (artifact-ID stability) was answered in one click, the stated defaults (diagram format, classification position, PR conventions) drew no veto, and every default held through merge.

## Trigger

- Direct: "ask any questions before you start", "I'll be away after you
  get going", "treat this file as a prompt — clarify first".
- Proactive: any session-sized delegation whose prompt names context files
  the agent has not yet read.
- Negative: the user is staying interactive (ask as you go instead); the
  task is small enough that a wrong guess costs less than a question.

## Inputs

- The task prompt/file and everything it references (specs, READMEs,
  sibling task files, prior PRs).
- The repository state (branch conventions, existing vocabulary the
  task's output must fit into).

## Outputs

- Zero to three `AskUserQuestion` calls, each a genuine fork with a
  recommended option listed first.
- A short stated-defaults list in chat ("veto now, otherwise I'm off"),
  covering the judgment calls the agent will make itself.
- Immediate task start after the answer — no second round.

## Workflow

1. Read the task file end-to-end, then every document it lists as
   context, then any sibling files that consume the task's output (in the
   source session, tasks 02/03 hard-coded the artifact IDs — the decisive
   fact for the one real question).
2. Draft the candidate-question list privately. For each, attempt to
   answer it from the material. Strike it if: the task text answers it or
   explicitly delegates it ("your model must take a position" means do
   not ask for the position); it has a conventional default (diagram
   format, PR etiquette); or it is a fact checkable in the repo (check it
   instead).
3. Verify feasibility blockers *before* asking anything — network
   fetches, tool access, upstream drift. A blocker discovered after the
   user leaves is the thing this gate exists to prevent. (Source session:
   fetched all four external specs and line-count-verified them before
   the question.)
4. Ask what survives — at most three questions, each with the recommended
   option first and consequences in the descriptions. If nothing
   survives, say so and present only the defaults list.
5. Present the stated-defaults list for everything struck in step 2 that
   a reasonable owner might still care about. Frame it as a veto window,
   not a request for confirmation.
6. Start immediately after the answers. Do not return with a second
   round of questions unless a genuine new fork emerges from the work
   itself.

## Concrete examples

### Example 1: The source session (task-01 delegation)

Prompt: "Read `spec-completeness/tasks/task-01-artifact-model.md` and
treat it like a prompt. Ask any questions/clarifications you need before
you start, as I will be away." Candidate questions after the survey:
ID-stability freedom (survived — tasks 02/03 embed the IDs, so the answer
changes the deliverable and downstream files); Mermaid vs ASCII (struck —
task says "ASCII or Mermaid", GitHub renders Mermaid); the concrete-syntax
classification (struck — task text: "Your model must take a position");
doc length (struck — content requirements determine it). Asked one
question with three options ("Stable IDs, additive OK" recommended and
chosen); stated four defaults; user vetoed none; all four held through
the merge of PR #26.

### Example 2: Counterfactual misuse (asking a delegated question)

Same prompt, but the agent asks "Should concrete grammars go in R-IS or
C-DM?" — a question the task file answers two paragraphs below its
objective ("the planning session leaned toward R-IS … Your model must
take a position and apply it consistently"). The user must retype what
they already wrote, from their phone. The gate exists to make this class
of question impossible: it is struck at step 2 because the task text
explicitly delegates it.

## Anti-patterns

- **Asking before reading**. Every question must survive contact with the
  full referenced context first.
- **Re-asking decisions the task text already made or delegated** — the
  concrete-syntax position in the source session.
- **Burying the recommendation**. The recommended option goes first,
  labeled.
- **Converting the defaults list into questions**. Defaults are stated,
  not asked; the user's silence is consent.
- **A second question round after the user leaves** for anything that was
  knowable during the gate.
- **Skipping the feasibility probe** and discovering a blocked fetch or
  missing tool an hour into autonomous work.

## Acceptance criteria

- [ ] Every asked question is unanswerable from the task file and its
      referenced context (spot-checkable by a reviewer).
- [ ] Questions number ≤3 and each carries a recommended option first.
- [ ] A stated-defaults list accompanies the questions (or stands alone
      when zero questions survive).
- [ ] Feasibility blockers (fetches, tools, upstream drift) were probed
      before the user disengaged.
- [ ] Work starts immediately after the answers, with no follow-up
      question round about gate-knowable facts.

## Files this skill creates / modifies

- None on disk — the skill's output is the question set, the defaults
  list, and an earlier, better-informed task start.
