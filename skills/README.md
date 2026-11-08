# Skills

This directory contains reusable instruction packages for tasks an AI assistant or agent may need to perform consistently.

## What belongs here

- Task-focused instructions with a defined purpose and expected output
- Reusable procedures that benefit from context, constraints, and quality checks
- Domain-specific guidance that can be applied across projects

A skill is more structured than a single prompt. It should explain when to use it, what information it needs, how to perform the task, and how to assess the result.

## Recommended structure

Use `skills/<category>/<skill-name>/SKILL.md` with lowercase kebab-case directory names.

Follow the repository's skill conventions and include the required front matter. A strong `SKILL.md` normally covers:

1. **Purpose**
2. **When to use**
3. **Instructions** — clear, ordered steps
4. **Inputs**
5. **Outputs**
6. **Example**
7. **Limitations** and relevant safety boundaries

Add supporting files only when they materially improve the skill. Keep examples realistic, avoid private context, and state when a task requires human judgment or external verification.

## Examples

- [Code review](coding/code-review/SKILL.md)
- [Systematic debugging](coding/debug-systematically/SKILL.md)
- [Evidence checker](research/evidence-checker/SKILL.md)
- [Mathematics problem solver](mathematics/problem-solver/SKILL.md)

## Suitable contributions

Contribute an original, reusable skill, improve an existing skill's procedure or quality checks, or add focused supporting examples. Search for similar skills first; extend an existing resource when the purpose substantially overlaps.
