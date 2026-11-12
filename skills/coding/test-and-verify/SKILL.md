---
name: test-and-verify
description: Use after implementing code to systematically verify behavior, tests, regressions, and important edge cases.
category: coding
tags: [coding, test-and-verify]
---


# Test and Verify

## Goal

Verify a completed coding change instead of assuming that a successful edit means the task is complete.

## Workflow

1. Inspect the diff.
2. Identify the behavior changed.
3. Find existing tests that cover it.
4. Add focused tests when coverage is missing and the task warrants them.
5. Run the narrowest useful test first.
6. Run broader checks when appropriate.
7. Inspect failures rather than hiding or weakening tests.
8. Check formatting, linting, types, and build status when relevant.
9. Report exactly what was run and what was not run.
10. Never claim a test passed unless it actually ran successfully.

## Final report

- Changed behavior
- Tests/checks executed
- Results
- Remaining risks

## Purpose

Use after implementing code to systematically verify behavior, tests, regressions, and important edge cases..

## When to use

Use this skill when the task involves test and verify and the user needs a structured, repeatable approach.

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

**Scenario:** A user requests help with test and verify and supplies the relevant context.

**Expected result:** Apply the guidance above, show the task-relevant result, and distinguish verified information from assumptions or open questions.

## Limitations

Do not invent missing facts, data, citations, or project-specific behavior. State uncertainty where the supplied evidence is insufficient, and seek qualified human review when the task has material safety, legal, scientific, or operational consequences.
