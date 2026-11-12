---
name: skill-author
description: Design or improve a reusable Claude Agent Skill with precise activation criteria, focused instructions, examples, verification, and safe boundaries. Use when creating or refactoring a SKILL.md.
category: claude
tags: [claude, skill-author]
---


# Skill Author

Create skills that are reusable, testable, and easy for another contributor to understand.

## Process

1. Define one clear job for the skill.
2. Write an activation description that states when it should be used.
3. Keep instructions focused on behavior, not background exposition.
4. Separate required steps from optional guidance.
5. Include failure conditions and safety boundaries.
6. Add examples when they clarify invocation or expected output.
7. Define verification that can expose common failures.
8. Move large reference material outside the main skill.
9. Test against representative tasks.
10. Revise based on observed failures.

## Quality checklist

- Is the purpose specific?
- Is the trigger description useful?
- Are assumptions explicit?
- Is the output format clear?
- Can the skill be tested?
- Does it avoid unnecessary permissions or destructive actions?
- Does it duplicate an existing Atlas resource?

## Output

Return:

- Skill purpose
- Activation description
- Instructions
- Examples
- Verification plan
- Known limitations

## Purpose

Design or improve a reusable Claude Agent Skill with precise activation criteria, focused instructions, examples, verification, and safe boundaries. Use when creating or refactoring a SKILL.md..

## When to use

Use this skill when the task involves skill author and the user needs a structured, repeatable approach.

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

**Scenario:** A user requests help with skill author and supplies the relevant context.

**Expected result:** Apply the guidance above, show the task-relevant result, and distinguish verified information from assumptions or open questions.

## Limitations

Do not invent missing facts, data, citations, or project-specific behavior. State uncertainty where the supplied evidence is insufficient, and seek qualified human review when the task has material safety, legal, scientific, or operational consequences.
