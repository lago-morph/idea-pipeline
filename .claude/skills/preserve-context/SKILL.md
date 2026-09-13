---
name: preserve-context
description: Capture the ideas in a conversation — the current session or a supplied transcript of a past one — into a markdown record grouped by topic, not by time, with the human's and the agent's statements treated alike, changes and reversals kept, the agent's read of the human's intent and values labelled as interpretation, and nothing processed into conclusions, priorities, or decisions. Trigger only on an explicit ask such as "preserve the context", "preserve this conversation", "summarize the ideas", "capture the ideas from this session", "transcribe this conversation by topic", or "do what you did for the scoped sandbox appendix". Not a summary — a transcription by theme that keeps the losers, the hedges, and the meta-conversation so the whole context can be picked up later.
---

# Preserve context

Capture what was said and meant in a conversation, grouped by topic, so
someone can come back to any part of it later without holding the whole
thing in their head. Transcription by theme. Not a summary, not a design.

---

## The line: capture the conversation, do not process it

A summary keeps the winners. This keeps everything: ideas that were
proposed and dropped, suggestions the human rejected, hedges, reversals,
and the conversation about how to do the capture itself. The value is the
**whole context** — a future reader, human or agent, should be able to
understand not just where the ideas landed but how they moved.

You do not rank, prioritize, decide, conclude, or design. You do not add
implementation detail that was not discussed. The only decisions a
capture records as decisions are ones the human explicitly called
decisions; everything else the human said firmly is a **stated position**
at a point in time.

You *do* record your own read of the human's intent, mood, values, and
unstated objectives — because a conversational partner tracks those and
they are context for the words — but always labelled as your
interpretation, never as something the human said.

---

## When to use this skill

**Use it only on an explicit ask.** The human names the act: preserve,
capture, transcribe by topic, "summarize the ideas" (they mean this, not
a summary). A session ending, or a conversation that seems rich, is not a
trigger.

**Sources it works on:** the current session's context; a pasted or
attached transcript of a past session (markdown, JSONL export, plain
text); a range within either ("from when we started talking about X").

**Skip it for:** status reports, decision logs, retrospectives, specs.
Those process the material; this preserves it. `self-retrospective`
harvests lessons; this keeps the conversation.

---

## Workflow

### 1. Confirm scope and destination

Scope: which conversation, and from where to where. Default is the whole
of what was pointed at.

Destination: if the human named one, use it. If not, **ask before
writing**, and put the lightest option on the table:

- **Display only** — the capture printed in the session as markdown in a
  fenced block, for the human to copy or save through the harness UI.
- **An appendix** to an existing document the conversation was about —
  labelled as an appendix so organized content can go above it later.
- **A new file** — propose a path.

State your default so the human can just say yes.

### 2. Read the whole source before writing anything

End to end, once, for the shape. Do not start writing sections on the
first pass — topics cluster only when you have seen where the
conversation went. On the pass, note for each idea: who raised it, who
responded, what changed, whether it was resolved, and any phrase either
party used that carries the idea better than a paraphrase would.

For a supplied transcript, read it as a file. For the current session,
your context is the source; if it has been compacted, say so in the
capture's "how this was made" section.

### 3. Write the interpretive read of the human first

One section, labelled as interpretation, before the topics. What the
human is trying to do, what they value, what frustrates them, who the
work is for, what they said about themselves that changed how you
responded. Quote the phrases that anchored your read. This section is
where you are allowed to think; the rest is where you are not.

### 4. Write the topic sections

One section per thread. Within a section, the order is whatever makes the
thread easiest to follow — usually the idea, then the responses, then
what moved. Not chronological across sections.

For every statement: **attribute it** (`J:` / `A:` or the names used),
**compress it** to the idea, **quote** the key phrase if there is one.
Compress both voices the same way; the agent's words are not privileged
and not discounted.

Mark movement explicitly. Patterns that recur:

- *proposed → narrowed → dropped*
- *proposed by A, rejected by J*
- *proposed by A, unaddressed* (not rejected — say which)
- *J's initial position → J's later position*
- *withdrawn by the proposer*

Keep hedges. If the human said "probably," "for now," "if I end up
wanting it," "with a little more nuance," those words stay. Dropping a
hedge is putting words in their mouth.

Anything either party asked to have kept as-is — a parallel, an insight,
a table — gets its own section, kept as-is.

### 5. Write the positions section

A record of where things stood, in three lists and no ranking:

- what the human placed firmly, marked *stated position*
- what the agent proposed that is still open
- what the agent proposed that the human rejected or superseded

Title it "as discussed, not as decided." If the human later says the
positions are opinions at a point in time, that is the default reading;
say so in the intro and here.

### 6. Write "how this capture was made"

The conversation about the capture belongs in the capture: what was
asked, what you proposed, how the human redirected you, what you did
with that. If the source was compacted or partial, say so here.

### 7. Re-read for overstatement

One full pass, specifically hunting for:

- your inference presented as the human's words
- a hedge the human used that you dropped
- "decided" or "agreed" where the human only stated a position
- a rejected or unaddressed idea that quietly vanished
- anything that reads as a recommendation

Fix each. Note in the commit message what the pass caught.

### 8. Save, show, fold in corrections

Save per step 1. Show the human. Their corrections *are* the record —
fold them in clean, no brackets, and record the correction itself in the
"how this was made" section if it changed the framing.

---

## Anti-patterns

- **Summarizing.** Dropping the ideas that lost. The losers are context.
- **Ordering by time.** A timeline is a different document. Theme.
- **Ranking.** Any list that reads as priorities has processed the ideas.
- **Upgrading a position to a decision.** Only the human can do that, and
  only by saying so.
- **Dropping hedges.** "Probably" is data.
- **Presenting your interpretation as their statement.** Label it.
- **Adding implementation detail.** If it wasn't discussed, it isn't in.
- **Forgetting the meta-conversation.** How the capture was asked for and
  shaped is part of the context.
- **Privileging one voice.** Compress the agent and the human alike.

---

## Acceptance criteria

1. Every thread in the source has a section; nothing raised was dropped.
2. Every statement is attributed and compressed; key phrases are quoted.
3. Every proposal that moved — narrowed, dropped, rejected, withdrawn,
   unaddressed — is marked with how it moved.
4. The human's hedges are preserved.
5. Interpretation is in its own labelled section and nowhere else
   unlabelled.
6. No section ranks, prioritizes, recommends, or records a decision the
   human did not call a decision.
7. "How this capture was made" is present.
8. The overstatement re-read ran and its findings were fixed.
9. Destination was the human's choice, with display-only offered.

---

## Template

`templates/capture-template.md` — the skeleton, with the intro block and
attribution key. Copy it; rename the sections to the actual threads.
