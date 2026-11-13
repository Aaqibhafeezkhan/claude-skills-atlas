---
name: codebase-explorer
description: Use when entering an unfamiliar codebase and you need to understand architecture, entry points, dependencies, conventions, and data flow before editing.
category: coding
tags: [coding, codebase-explorer]
---


# Codebase Explorer

## Instructions

Build a concise mental model from evidence in the repository.

Inspect, as relevant:

- README and project documentation
- package/build configuration
- application entry points
- directory structure
- important modules
- tests
- configuration and environment handling

Then report:

1. Project purpose
2. Main entry points
3. Major components
4. Data/control flow
5. Important conventions
6. Relevant files for the requested task
7. Unknowns that require further inspection

Do not invent architecture that is not supported by the repository.

## Purpose

Support users who need to entering an unfamiliar codebase and you need to understand architecture, entry points, dependencies, conventions, and data flow before editing..

## When to use

Use this skill when the task involves codebase explorer and the user needs a structured, repeatable approach.

## Inputs

- The user's task, question, or objective.
- Relevant source material, data, constraints, and prior decisions.
- The required audience, depth, and output format, when specified.

## Outputs

- A result tailored to the stated task and audience.
- The key steps, evidence, or reasoning needed to make the result understandable.
- Assumptions, checks, and unresolved limitations where relevant.

## Example

**Scenario:** A user requests help with codebase explorer and supplies the relevant context.

**Expected result:** Apply the guidance above, show the task-relevant result, and distinguish verified information from assumptions or open questions.

## Limitations

Do not invent missing facts, data, citations, or project-specific behavior. State uncertainty where the supplied evidence is insufficient, and seek qualified human review when the task has material safety, legal, scientific, or operational consequences.
