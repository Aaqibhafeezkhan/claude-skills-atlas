---
name: implementation-planner
description: Use when a coding task is large enough to require repository inspection, a plan, affected files, risks, and verification before implementation.
category: coding
tags: [coding, implementation-planner]
---


# Implementation Planner

## Goal

Turn a coding request into an implementation plan before changing code.

## Instructions

1. Inspect the repository structure and relevant configuration.
2. Identify the smallest set of files likely to change.
3. Trace existing patterns before proposing a new abstraction.
4. State assumptions instead of silently inventing requirements.
5. Produce:
   - objective
   - current architecture relevant to the task
   - files to inspect/change
   - implementation steps
   - risks and edge cases
   - verification plan
6. If important information is missing, ask focused questions before implementation.
7. Do not modify files unless the user explicitly asks for implementation.

## Output

Keep the plan concrete enough that another developer can execute it without rediscovering the repository.

## Source note

Inspired by recurring community recommendations to separate planning from implementation and keep work focused. See `docs/community-sources.md`.

## Purpose

Support users who need to a coding task is large enough to require repository inspection, a plan, affected files, risks, and verification before implementation..

## When to use

Use this skill when the task involves implementation planner and the user needs a structured, repeatable approach.

## Inputs

- The user's task, question, or objective.
- Relevant source material, data, constraints, and prior decisions.
- The required audience, depth, and output format, when specified.

## Outputs

- A result tailored to the stated task and audience.
- The key steps, evidence, or reasoning needed to make the result understandable.
- Assumptions, checks, and unresolved limitations where relevant.

## Example

**Scenario:** A user requests help with implementation planner and supplies the relevant context.

**Expected result:** Apply the guidance above, show the task-relevant result, and distinguish verified information from assumptions or open questions.

## Limitations

Do not invent missing facts, data, citations, or project-specific behavior. State uncertainty where the supplied evidence is insufficient, and seek qualified human review when the task has material safety, legal, scientific, or operational consequences.
