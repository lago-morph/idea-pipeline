---
id: artifact-count-test
title: The number of artifacts the toy app needs is a health metric
status: discussed
kind: rule
event: any regeneration run recorded
friction: The metrics table already has a "repo docs opened" column, 25 for run 1. This rule reads it as a health metric and adds a by-type breakdown.
agent-method-home: ai/procedures/implement-by-subagent.md metrics table
depends-on: [system-profile]
---

## Idea

Count the artifacts a small system requires under the method. If the workbench needs around five, the method scales down. If it needs twenty, the applicability rules are not working, whatever the enterprise case looks like. The count is a standing test that the method has not collapsed under its own weight, which is how the two archived attempts ended.

## Why it matters for agents

It is cheap, objective, and catches the failure mode early. It is also a proxy for how much a regeneration subagent must read.

## What it would look like in agent-method

One column in the metrics table: artifacts the subagent was given, by type. Watch the trend across implementations.

## Open questions

- Whether per-area decisions notes count individually or as part of their implementation record.

## Source

Discussion 2026-09-05.
