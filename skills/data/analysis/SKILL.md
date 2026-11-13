---
name: data-analysis
description: Use when analyzing a dataset and producing reproducible findings, tables, visualizations, or statistical conclusions.
category: data
tags: [data, analysis]
---


# Data Analysis

## Workflow

1. Inspect schema, types, missingness, duplicates, and suspicious values.
2. Clarify the analytical question.
3. Define transformations explicitly.
4. Choose methods appropriate to the data and question.
5. Separate exploratory findings from confirmatory claims.
6. Quantify uncertainty where appropriate.
7. Produce clear tables or visualizations with labels.
8. Check for leakage, selection bias, confounding, and invalid assumptions when relevant.
9. Make the analysis reproducible.
10. State limitations.

Never invent observations or pretend a computation was performed when the data was not actually processed.

## Purpose

Support users who need to analyzing a dataset and producing reproducible findings, tables, visualizations, or statistical conclusions..

## When to use

Use this skill when the task involves data analysis and the user needs a structured, repeatable approach.

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

**Scenario:** A user requests help with data analysis and supplies the relevant context.

**Expected result:** Apply the guidance above, show the task-relevant result, and distinguish verified information from assumptions or open questions.

## Limitations

Do not invent missing facts, data, citations, or project-specific behavior. State uncertainty where the supplied evidence is insufficient, and seek qualified human review when the task has material safety, legal, scientific, or operational consequences.
