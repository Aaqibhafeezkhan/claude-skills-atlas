# Agents

This directory contains definitions for specialized AI agents: reusable role descriptions that establish an agent's purpose, responsibilities, scope, and operating boundaries.

## What belongs here

- Focused agent roles for research, engineering, analysis, or other repeatable work
- Agent instructions that are distinct from a single prompt or a multi-step workflow
- Clear tool and context requirements, including what the agent must not access or change

## Recommended structure

Use `agents/<category>/<agent-name>.md` and lowercase kebab-case names.

A useful agent definition normally covers:

1. **Role and purpose** — the problem the agent is intended to solve
2. **Scope** — responsibilities and explicit exclusions
3. **Inputs** — context or artifacts the agent needs
4. **Behavior** — expected steps, decision rules, and collaboration style
5. **Tools and permissions** — required capabilities and least-privilege boundaries
6. **Outputs** — deliverables and their expected format
7. **Limitations and safety** — uncertainty, escalation, and prohibited actions

Keep definitions self-contained and portable. Do not include credentials, private data, or assumptions tied to one contributor's environment.

## Examples

- [Research agent](research/) — category for research-oriented agent definitions
- [GitHub operator agent](../plugins/github-agent/agents/) — an agent distributed with the GitHub Agent plugin

## Suitable contributions

Add a narrowly scoped agent with a practical use case, improve an existing agent's boundaries or output contract, or add realistic examples that demonstrate how to use it safely. Check for overlapping roles before adding a new one.
