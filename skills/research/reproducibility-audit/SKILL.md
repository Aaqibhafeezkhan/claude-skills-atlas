---
name: reproducibility-audit
category: research
tags: [reproducibility, research-methods, experiments, audit]
recommendation_use_cases: [audit whether a study or experiment can be reproduced, identify missing methodological details, prepare a reproducibility checklist]
recommendation_audience: [researchers, students, data scientists]
recommendation_domain: research-methods
recommendation_prerequisites: [a paper, experiment description, or analysis workflow]
recommendation_related_skills: [research/experimental-planning, research/evidence-checker, machine-learning/experiment-analysis]
---

# Reproducibility Audit

## Purpose

Assess whether another person could independently reproduce a reported study, experiment, or computational analysis from the available description and artifacts. Identify missing information without treating missing documentation as proof that the result is false.

## When to use

Use this skill when reviewing a paper, laboratory protocol, computational experiment, data analysis, or project report for reproducibility before publication, handoff, or replication.

## Instructions

1. **Define the target.** Clarify whether the goal is conceptual replication, exact computational reproduction, or repetition of a physical experiment. These require different evidence.
2. **Inventory the artifacts.** Record which paper, protocol, datasets, code, configuration files, environment details, and supplementary materials are actually available. Do not imply that inaccessible artifacts were inspected.
3. **Extract the procedure.** Summarize the sequence of steps, inputs, transformations, parameters, controls, and outcome measurements needed to recreate the result.
4. **Check data provenance.** Look for dataset versions, collection dates, inclusion/exclusion rules, preprocessing, labeling, licensing, and any restrictions on access. Never request or expose private or sensitive records unnecessarily.
5. **Check computational details when relevant.** Look for code revision or release, dependency versions, hardware or runtime assumptions, random seeds, initialization, train/validation/test splits, configuration values, and nondeterministic operations.
6. **Check experimental details when relevant.** Look for materials, equipment, calibration, sample sizes, control groups, repetitions, environmental conditions, measurement units, and stopping criteria.
7. **Trace claims to evidence.** Map each important reported result to the procedure and artifact that would allow it to be checked. Distinguish reported facts from inferred requirements.
8. **Classify gaps.** Use the labels Documented, Partially documented, Missing, Not applicable, or Unable to verify. Give a short reason for each classification.
9. **Prioritize blockers.** Separate gaps that prevent reproduction from details that merely make it slower or less convenient. Suggest the smallest concrete addition that would resolve each blocker.
10. **Report uncertainty fairly.** Do not claim a result is reproducible merely because code or data exists. Do not label a study irreproducible solely because an artifact was unavailable during this review.

## Inputs

- Paper, report, protocol, or experiment description
- Available code, data, supplementary files, and environment specifications
- The intended reproduction target, if known
- Any constraints on data access, equipment, runtime, or permissions

## Outputs

- A brief statement of the reproduction target and review scope
- An artifact inventory with availability and provenance
- A checklist of required methodological details and their status
- A prioritized list of blockers, risks, and concrete remediation steps
- A clear statement of what was inspected and what remains unverified

## Example

A paper reports a model's test accuracy but does not identify the dataset version, split strategy, preprocessing, or random seed.

A useful audit records these items as missing or partially documented, explains which ones could materially change the result, and asks the authors to provide the dataset identifier, split-generation procedure, preprocessing steps, and training configuration. It does not conclude that the reported accuracy is incorrect.

## Limitations

A documentation audit cannot establish that a result will reproduce in practice. Reproduction may depend on unavailable data, proprietary equipment, hidden implementation details, stochastic variation, or changes in external dependencies. Validate the original artifacts and run an independent reproduction when feasible.
