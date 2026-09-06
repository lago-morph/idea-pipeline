# Objectives

Status: draft. Captured 2026-09-05 from discussion, revised the same day after the spine took shape. This is Claude's understanding of the objectives, written for correction. Items marked *inferred* were not stated directly and should be confirmed or struck. `decisions-log.md` records which conclusions the owner has stated and which are proposed.

## What is being built

A framework that gives every decision and design involved in taking an idea to a running large system a defined place to live. The framework covers everything that is not application source code: requirements, architecture at every level, the development environment, the runtime platform, operations, and the standards that govern all of them.

The framework has two parts. The **nuggets** in `ideas/` are individual ideas that can be pulled into agent-method one at a time as that method needs them. The **spine** in `spine/` is the structure that holds a whole system's artifacts, subjects, and decisions together, so that pulling ideas in one at a time does not collapse under its own weight when applied to a real application.

The framework is a formalization of long experience in technical, application, and development architecture, plus more recent experience in the hybrid platform and DevOps engineer role. Part of the purpose is to get that experience out of one person's head and into a form that others, human or AI, can apply.

## Why

Architecture is traditionally left deliberately fuzzy. That works when humans hold the unmade decisions in their heads and fill them in consistently as they go. It fails when AI agents are asked to produce detailed specifications, development environments, monitoring dashboards, and similar artifacts from the architecture. An agent fills every gap on its own, and fills it differently on each session, model, and thinking-strength setting. The result is not repeatable.

So the framework has to make every decision explicit, or explicitly and deliberately open, so that work built on the architecture is repeatable across sessions, models, and settings.

Free-form notes work for a while and then collapse under their own weight. Structure designed in the abstract collapses before it starts. The framework has to be structured enough to stay navigable for a real application, and grounded enough to be validated against real content at every step.

## Who uses it

Some combination of AI agents and humans. Both must be able to read it, add to it, and check it for consistency. Humans decide and ratify. Agents propose, build, harvest, and check.

## What it must do

1. **Show what needs to be done to reach a level of maturity.** Given what a system is and how far along it is, list the artifacts and decisions still required.
2. **Give humans and agents a place to record decisions and application structure** as questions come up, so the record grows during the work rather than after it.
3. **Harvest the decisions an agent makes while building**, with provenance, so they are visible and reviewable rather than buried in code.
4. **Make an unsatisfactory prototype cheap to fix.** Every decision and structural choice behind it is explicit, so the owner can ratify what they like and revise what they do not at the root cause, and regenerate. Modifying is easier than building from scratch, but only when the decisions are explicit.
5. **Support three modes of entry.** Greenfield, where the system is authored outward from a vision. Capture, where an existing system's decisions are extracted and organized. Re-engineering, where a captured system is revised at the decision level and regenerated.
6. **Preserve testing and validation as first-class**, at three levels: is the artifact complete, does the implementation comply, does the method itself hold up.

## Approach

- The spine is the data model. It is six structures: system profile, maturity ladder, subject catalog, artifact type registry, decision records, derivation graph. See `spine/overview.md`. Anything new must prove it cannot be a field on one of the six.
- Seed the inventory of decision areas from the brainstorming notes in `reference/brainstorming.md` and from agent-method's existing and foreseen artifact types.
- Validate every structure against the idea-workbench application before proposing it anywhere. The workbench is single user, has no authentication, has a data model of one array of text strings, and has very simple runtime and development environments. Every decision area can still be answered for it, often as "not applicable, because". Answering forces the question to be asked.
- Stress the framework by changing the workbench's profile one characteristic at a time, and later by a second application with a different profile.
- Mature this in parallel with agent-method, building the pieces agent-method needs at the moment it needs them, and never ahead of that. See `plan.md`.

## Relationship to agent-method

Agent-method is about getting functional requirements and basic application architecture right. It grows its artifacts one at a time from real content, and its workbench is the first application specified with it. This work supplies the architecture beyond that, the structure that keeps a whole system navigable, and the pieces agent-method itself will need, such as the persistent-storage guide. Agent-method keeps its ground and its discipline. Nothing here overrides its rules.

## Boundaries, from the brainstorming notes

- ADRs stand alone. They capture the intent behind decisions and are referenced from design and implementation artifacts. They are not the artifacts themselves.
- Code, compiled programs, images, and configuration files are all development output.
- Documentation is not development output, except where a standard mandates that something be documented.

## Success looks like (inferred)

- A specification produced under the framework yields substantially the same implementation from different models and settings.
- Every decision area for a system has an explicit status. Nothing is silent.
- A human or agent can answer "everything about X" for a component, interface, or environment without reading the whole corpus.
- The owner can review a prototype by walking its decisions by subject, ratify most, revise a few, and regenerate without touching code.
- The same framework works for a system being extracted, a system being newly designed, and a system being re-engineered.
- The workbench needs a small number of artifacts. The count stays small as the method matures.

## Not yet decided

- The file shape of decision records. Two candidates in `spine/decision-record.md`; chosen in phase 2.
- Whether the spine moves to its own repository. Decided in phase 6.
- The remaining open questions at the end of each `spine/` file and in `decisions-log.md`.
