# Spec: Session Analyzer

**Post-Phase 6 project (enters ideas pipeline queue)**
**Repo:** new — to be created

---

## What It Is

A pipeline that mines AI agent session histories across all platforms and accounts —
Claude (web, desktop, iOS), ChatGPT, Codex CLI, Claude Code CLI — to find patterns in
how the user works with agents: what they correct, what approaches they prefer, what
clarifications they consistently make, what patterns appear in successful vs unsuccessful
sessions. The output is a personal `agent-style.md` file that can be dropped into any
repo's AGENTS.md to give agents a head start on working the way the user expects.

---

## Current State

- Does not exist
- Personal (Lagomorph Labs) and work accounts are separate; their outputs stay separate
- Multiple export mechanisms exist per platform but are inconsistent — this is a
  significant data collection challenge before any analysis can happen

---

## Session Sources to Cover

| Platform | Access Method | Account |
|---|---|---|
| Claude web | Session export / this conversation history tool | Personal |
| Claude iOS/iPad app | Export if available; manual transcript | Personal |
| Claude Code CLI | Local `~/.claude/` session files | Personal |
| ChatGPT web | Data export (JSON) | Personal / Work |
| OpenAI Codex CLI | Local session logs | Personal / Work |
| Claude Code at work | Separate account; similar mechanism | Work |

---

## Recommended Design

**What to mine for:**
- Correction patterns: when the agent does X, the user says "don't do that, do Y instead"
- Preference signals: formats the user accepts vs asks to change, levels of verbosity
- Working style: does the user prefer asking questions upfront or diving in?
- Typical clarifications: things the user always specifies that an agent shouldn't have
  to be told explicitly
- Session structure: how the user tends to start and end sessions, how they hand off work

**Output format:**
- `agent-style.md` — a markdown file with sections: communication style, output
  preferences, working patterns, things to never do, things to always do
- Structured for dropping into `AGENTS.md` in any repo

---

## Open Questions

- How are sessions exported from each platform, especially mobile? Some may require
  manual copy-paste initially.
- How does the analyzer distinguish user-specific patterns from task-specific patterns
  (the user formats code differently when doing infra vs writing)?
- How often is the style file refreshed — one-time or periodic?
- Should work patterns and personal patterns be completely separate files, or one file
  with context tags?

---

## Recommended Additions

- **Style evolution tracking**: compare old sessions to new ones — are preferences
  changing? Does the user want to know?
- **Cross-project consistency**: flag when AGENTS.md files across repos have
  contradictory style guidance

---

## What Needs to Happen Next

1. Inventory what session data is actually accessible per platform (do this manually first)
2. Prioritize by richness: Claude web likely has the most; start there
3. Build the extraction pipeline for one source before expanding
4. Define the agent-style.md format (this can be done independently of data collection)

---

## Dependencies

**Depends on:** nothing structural (can be started now), Phase 3 (style file format
aligns with SKILL.md conventions)
**Enables:** Ideas pipeline (personal patterns are a capture source), all future agent
work (agents aligned to user's style from the start)
