---
id: concern-tags
title: Concern is a tag for auditing, not an organizer
status: discussed
kind: conditional
event: E6
friction: None yet. Five guides exist and cross-guide consistency is still done by reading.
agent-method-home: front matter or a column on guide questions; later the link validator
depends-on: []
---

## Idea

Subject (a component, an interface, an environment) is the primary organizer because it gives implementation its boundaries and one artifact as the driver. Concern (persistence, identity and access, observability, concurrency and failure, configuration, external dependencies, security, lifecycle, runtime environment, communication) is a tag on each guide question. The concern view is for completeness review: "show me every persistence decision across all subjects".

## Why it matters for agents

The consistency check in guided work is a concern-view query: a synchronous interface on a component whose concurrency answer is a background worker. Without the tag, that check requires reading everything.

## What it would look like in agent-method

A `concern` value on each guide question. The ten concerns above fell out of the brainstorming notes by noticing which topics recurred across layers. The link validator could later produce the concern view as a generated index.

## Open questions

- Whether ten concerns is the right granularity for the workbench, which today exercises perhaps three.

## Source

Discussion 2026-09-05, subject versus concern.
