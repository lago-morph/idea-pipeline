---
id: refinement-stages
title: Application, technical, DevOps, and Ops are refinement stages of one concern
status: discussed
kind: rider
event: component and interface types
friction: The implementation-structure notes hold mechanism-stage decisions for components that have no logical-stage artifact yet, so the two stages have nowhere distinct to go.
agent-method-home: method/types/component.md and interface.md; possibly new types for the technical and operational stages
depends-on: [concern-tags]
---

## Idea

The brainstorming notes split architecture along the lines of where technical and application architects traditionally worked. The same concern appears at each layer: persistence is data ownership in application architecture, a mechanism in technical architecture, infrastructure in DevOps. The layers are refinement stages of one concern, not disjoint categories. Application is the logical answer, technical is the mechanism, DevOps is infrastructure and tooling, Ops is operating procedure.

## Why it matters for agents

Subject-primary organization, one artifact as the primary driver for implementing a component, needs the stages to hang off the subject. A component definition holds the logical stage. Its decisions note for an implementation holds the mechanism stage. The implementation record already separates these: "use cases and components included" is logical, "language, storage, build" is mechanism.

## What it would look like in agent-method

No new top-level split. The stage becomes a tag on guide questions and, later, a section order within a component's artifacts: what it promises, then how this implementation realizes it, then how it is deployed and operated. The "map components to" and "map interfaces to" lists in the brainstorming notes are the mechanism-stage question list, nearly verbatim.

## Open questions

- Whether the technical stage is a separate artifact type or a section of the component definition that varies per implementation.

## Source

Discussion 2026-09-05, taxonomy feedback. Brainstorming notes: all four architecture sections.
