---
id: binding-level
title: Decisions are owned at a level and inherited below it
status: idea
kind: conditional
event: E7
friction: None yet. Nothing exists above the workbench's system level.
agent-method-home: method/CONVENTIONS.md or decision-guides.md; possibly a new link type
depends-on: [status-vocabulary]
---

## Idea

Decisions are owned at one of several levels: organization standard, platform, system, component. A lower level inherits a higher level's answer unless it explicitly overrides. "Inherited" is one of the five statuses. Together with binding time this answers "who decides this, when, and where is it written".

## Why it matters for agents

In any enterprise setting most decisions that are not application source code are made once at the platform level: logging mechanism, auth provider, CI tooling, persistence infrastructure. An agent implementing a component should find those answers, not re-decide them. This is where the platform and DevOps experience in the brainstorming notes lives.

## What it would look like in agent-method

Nothing until a level above the system exists. When it does, either a `standards` artifact at the higher level that decisions notes link to with `depends-on`, or an `inherits-from` link type. The existing implementation-standards note is already a system-level standard in this sense.

## Open questions

- Whether levels are a link type or a field.
- Whether the workbench will ever have a level above "system" or whether this only applies to a second, hosted application.

## Source

Discussion 2026-09-05. Brainstorming notes: the DevOps "Both" list is the platform level.
