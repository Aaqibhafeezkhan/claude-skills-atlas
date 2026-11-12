---
name: codebase-understanding
description: Build a reliable mental model of an unfamiliar repository before making changes. Use when entering a new codebase, investigating architecture, or when the user asks where a feature belongs.
category: coding
tags: [coding, codebase-understanding]
---


# Codebase Understanding

Build understanding before proposing edits. Prefer evidence from the repository over assumptions.

## Process

1. Identify entry points, package/build files, configuration, tests, and documentation.
2. Map the relevant directory structure.
3. Trace the execution path for the requested feature or bug.
4. Identify important data models, interfaces, dependencies, and integration boundaries.
5. Search for existing implementations before proposing new ones.
6. Record constraints, conventions, and likely regression points.
7. Summarize the model in a compact form before changing code.

## Rules

- Read targeted files before broad exploration.
- Do not invent architecture that is not supported by repository evidence.
- Prefer existing abstractions over introducing parallel ones.
- Distinguish observed facts from hypotheses.
- If the change crosses multiple layers, state the dependency order.

## Output

Return:

- Repository map
- Relevant execution/data flow
- Existing patterns to reuse
- Constraints and risks
- Proposed change locations
- Verification plan

## Purpose

Build a reliable mental model of an unfamiliar repository before making changes. Use when entering a new codebase, investigating architecture, or when the user asks where a feature belongs..

## When to use

Use this skill when the task involves codebase understanding and the user needs a structured, repeatable approach.

## Instructions

Apply the guidance and checks above in sequence. Use the supplied context as the source of truth, make assumptions explicit, and verify important conclusions before presenting them.

## Inputs

- The user's task, question, or objective.
- Relevant source material, data, constraints, and prior decisions.
- The required audience, depth, and output format, when specified.

## Outputs

- A result tailored to the stated task and audience.
- The key steps, evidence, or reasoning needed to make the result understandable.
- Assumptions, checks, and unresolved limitations where relevant.

## Example

**Scenario:** A user requests help with codebase understanding and supplies the relevant context.

**Expected result:** Apply the guidance above, show the task-relevant result, and distinguish verified information from assumptions or open questions.

## Limitations

Do not invent missing facts, data, citations, or project-specific behavior. State uncertainty where the supplied evidence is insufficient, and seek qualified human review when the task has material safety, legal, scientific, or operational consequences.
