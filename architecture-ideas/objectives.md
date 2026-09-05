# Objectives

Status: draft. Captured 2026-09-05 from discussion. This is Claude's understanding of the objectives, written for correction. Items marked *inferred* were not stated directly and should be confirmed or struck.

## What is being built

A framework that gives every decision and design involved in taking an idea to a running large system a defined place to live. The framework covers everything that is not application source code: requirements, architecture at every level, the development environment, the runtime platform, operations, and the standards that govern all of them.

The framework is a formalization of long experience in technical, application, and development architecture, plus more recent experience in the hybrid platform and DevOps engineer role. Part of the purpose is to get that experience out of one person's head and into a form that others, human or AI, can apply.

## Why

Architecture is traditionally left deliberately fuzzy. That works when humans hold the unmade decisions in their heads and fill them in consistently as they go. It fails when AI agents are asked to produce detailed specifications, development environments, monitoring dashboards, and similar artifacts from the architecture. An agent fills every gap on its own, and fills it differently on each session, model, and thinking-strength setting. The result is not repeatable.

So the framework has to make every decision explicit, or explicitly and deliberately open, so that work built on the architecture is repeatable across sessions, models, and settings.

## Who uses it

Some combination of AI agents and humans. Both must be able to read it, add to it, and check it for consistency.

## The three ways it will be used

1. **Extraction.** Take a system where decisions have already been made, find those decisions in code, configuration, and documents, and organize them into the framework.
2. **Guided new work.** Humans make new decisions and produce new designs. An AI helps with consistency and with cross-referencing each decision against the rest of the architecture.
3. **Checklist.** A list of everything that must be decided, documented, designed, and implemented for a system, other than the application source code, with status.

A fourth use follows from the second and third: an agent that has just finished an implementation run retrospects on the decisions it made along the way, so they can be formalized and made repeatable.

## Approach

- Start with a data model for the framework, before choosing a file layout or tooling.
- Seed the inventory of decision areas from the brainstorming notes in `reference/brainstorming.md`.
- Validate coverage using the current toy application. It is single user, has no authentication, has a data model of one array of text strings, and has very simple runtime and development environments. Every decision area can still be answered for it, often as "not applicable, because". Answering forces the question to be asked, which is what tests the inventory.
- Stress the framework by adding non-functional requirements to the toy application one at a time, and observing which decision areas change from not applicable to real.
- A separate project is experimentally producing specification artifacts by building something. This framework is meant to organize what that project discovers, and to cover the ground the toy application cannot reach on its own.

## Boundaries, from the brainstorming notes

- ADRs stand alone. They capture the intent behind decisions and are referenced from design and implementation artifacts. They are not the artifacts themselves.
- Code, compiled programs, images, and configuration files are all development output.
- Documentation is not development output, except where a standard mandates that something be documented.

## Success looks like (inferred)

- A specification produced under the framework yields substantially the same implementation from different models and settings.
- Every decision area for a system has an explicit status. Nothing is silent.
- A human or agent can answer "everything about X" for a component, interface, or environment without reading the whole corpus.
- The same framework works for a system being extracted, a system being newly designed, and a system being audited.

## Not yet decided

- The physical form the data model renders into: files, a graph, or both.
- Whether the top-level organizer is the traditional layer split from the notes, or something else. See the discussion in `ideas.md`.
- How much of the framework is a fixed inventory versus a method for discovering new decision areas.
