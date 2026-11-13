---
name: model-evaluation
title: Machine Learning Model Evaluation
type: skill
domain: machine-learning
tags: [evaluation, metrics, experiments]
intended_use: Evaluate an ML model without relying on a single metric.
category: machine-learning
---


# Model Evaluation

1. Identify task type and target population.
2. Establish a baseline.
3. Select metrics that match the task and decision costs.
4. Separate train, validation, and test evidence.
5. Inspect subgroup and error patterns where relevant.
6. Check calibration when probabilities are used.
7. Report uncertainty and limitations.
8. Prevent leakage and test-set overuse.

## Output

Metrics, baseline comparison, error analysis, validation design, and limitations.

Never fabricate performance numbers.

## Purpose

Evaluate an ML model without relying on a single metric..

## When to use

Use this skill when the task involves model evaluation and the user needs a structured, repeatable approach.

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

**Scenario:** A user requests help with model evaluation and supplies the relevant context.

**Expected result:** Apply the guidance above, show the task-relevant result, and distinguish verified information from assumptions or open questions.

## Limitations

Do not invent missing facts, data, citations, or project-specific behavior. State uncertainty where the supplied evidence is insufficient, and seek qualified human review when the task has material safety, legal, scientific, or operational consequences.
