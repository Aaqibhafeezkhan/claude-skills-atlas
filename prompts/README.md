# Prompts

This directory contains focused, reusable prompt templates for tasks that benefit from clear instructions but do not require a full skill package.

## What belongs here

- Copy-paste-ready prompts for a specific task
- Reusable prompt templates with clearly named input placeholders
- Prompts for coding, research, learning, mathematics, cybersecurity, and other supported domains

Use a skill when the task needs a fuller reusable procedure, multiple sections, or ongoing agent behavior. Use a workflow when the contribution is primarily a sequence of stages.

## Recommended structure

Use `prompts/<category>/<prompt-name>.md` with lowercase kebab-case names.

A prompt should normally include:

1. A clear title and intended outcome
2. The prompt text, ready to adapt or copy
3. Placeholders for variable inputs, such as `{{topic}}` or `{{constraints}}`
4. Optional usage notes, assumptions, and limitations
5. A concise example when it makes the prompt easier to apply

Avoid embedding personal information, secrets, or environment-specific values. Make the expected output explicit and keep instructions internally consistent.

## Examples

- [Debugging prompt](coding/debugging.md)
- [Paper-reading prompt](research/paper-reading.md)
- [Active-learning prompt](learning/active-learning.md)

## Suitable contributions

Add an original prompt that solves a repeatable problem, improve clarity or input handling in an existing prompt, or provide a useful example. Check for duplicates and explain meaningful differences between similar prompts.
