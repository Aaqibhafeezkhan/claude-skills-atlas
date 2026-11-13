---
name: debug-systematically
description: Diagnose software failures systematically instead of guessing. Use for bugs, failing tests, unexpected output, crashes, regressions, and inconsistent behavior.
category: coding
tags: [coding, debug-systematically]
---


# Debug Systematically

Treat debugging as evidence gathering and hypothesis elimination.

## Process

1. Reproduce the failure when possible.
2. Capture the exact error, input, environment, and expected behavior.
3. Minimize the failing case.
4. Trace backward from the observable failure to the earliest incorrect state.
5. Generate a small set of competing hypotheses.
6. Test the cheapest hypothesis that can distinguish them.
7. Apply the smallest correct fix.
8. Re-run the original reproduction and relevant regression tests.
9. Explain the root cause, not only the patch.

## Rules

- Never change multiple unrelated things before verifying the cause.
- Do not replace an error with silent fallback behavior unless intended.
- Preserve useful diagnostic information.
- Treat intermittent failures as evidence about timing, state, concurrency, caching, or environment.
- If the cause cannot be established, label it unresolved rather than guessing.

## Output

Return:

- Reproduction
- Observed vs expected behavior
- Root cause
- Minimal fix
- Verification
- Remaining uncertainty

## Purpose

Diagnose software failures systematically instead of guessing. Use for bugs, failing tests, unexpected output, crashes, regressions, and inconsistent behavior..

## When to use

Use this skill when the task involves debug systematically and the user needs a structured, repeatable approach.

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

**Scenario:** A user requests help with debug systematically and supplies the relevant context.

**Expected result:** Apply the guidance above, show the task-relevant result, and distinguish verified information from assumptions or open questions.

## Limitations

Do not invent missing facts, data, citations, or project-specific behavior. State uncertainty where the supplied evidence is insufficient, and seek qualified human review when the task has material safety, legal, scientific, or operational consequences.
