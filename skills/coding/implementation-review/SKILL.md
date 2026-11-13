---
name: implementation-review
description: Review an implementation against its requirements, repository conventions, correctness risks, tests, and maintainability. Use before opening a pull request or when reviewing completed work.
category: coding
tags: [coding, implementation-review]
---


# Implementation Review

Review completed work as if another engineer must maintain it.

## Process

1. Read the task or acceptance criteria.
2. Inspect the diff and changed files.
3. Trace changed behavior through callers and dependencies.
4. Check correctness, edge cases, error handling, and compatibility.
5. Compare the implementation with nearby repository conventions.
6. Inspect or add focused tests where practical.
7. Check documentation and user-facing behavior.
8. Separate blocking issues from suggestions.

## Review order

Prioritize:

1. Functional correctness
2. Security and data safety
3. Regression risk
4. Test coverage
5. Maintainability
6. Performance
7. Style

## Rules

- Do not praise code merely because it looks clean.
- Every finding should identify evidence, impact, and a concrete fix.
- Do not request speculative abstractions without a demonstrated need.
- If no blocking issue exists, explicitly say so.

## Output

Use:

- Verdict: ready / needs changes
- Blocking findings
- Non-blocking findings
- Missing tests
- Documentation gaps
- Suggested verification commands

## Purpose

Review an implementation against its requirements, repository conventions, correctness risks, tests, and maintainability. Use before opening a pull request or when reviewing completed work..

## When to use

Use this skill when the task involves implementation review and the user needs a structured, repeatable approach.

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

**Scenario:** A user requests help with implementation review and supplies the relevant context.

**Expected result:** Apply the guidance above, show the task-relevant result, and distinguish verified information from assumptions or open questions.

## Limitations

Do not invent missing facts, data, citations, or project-specific behavior. State uncertainty where the supplied evidence is insufficient, and seek qualified human review when the task has material safety, legal, scientific, or operational consequences.
