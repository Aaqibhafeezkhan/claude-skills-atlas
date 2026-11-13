# Workflows

This directory contains repeatable, multi-step procedures for completing a task with an AI assistant or agent.

## What belongs here

- End-to-end procedures with ordered stages
- Processes that define inputs, outputs, decision points, and failure handling
- Repeatable methods that coordinate multiple skills, prompts, tools, or human review

Use a prompt for a focused instruction and a skill for reusable task behavior. Use a workflow when the sequence and handoffs between stages are central to the contribution.

## Recommended structure

Use `workflows/<category>/<workflow-name>.md` with lowercase kebab-case names.

A useful workflow should describe:

1. **Goal and scope**
2. **Prerequisites and inputs**
3. **Steps and decision points**
4. **Expected outputs**
5. **Failure cases, recovery, and escalation**
6. **Verification or completion criteria**
7. **Safety and human approval requirements**, where relevant

Make dependencies explicit and avoid assuming access to tools, credentials, or services that users may not have.

## Examples

- [Coding workflows](coding/)
- [Research workflows](research/)

## Suitable contributions

Add a practical workflow that can be followed by someone unfamiliar with the author's environment, clarify a confusing handoff, or add verification and recovery guidance to an existing procedure.
