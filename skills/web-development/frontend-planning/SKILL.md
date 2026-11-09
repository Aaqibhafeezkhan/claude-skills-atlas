---
name: frontend-planning
category: web-development
tags: [frontend, architecture, accessibility, planning]
---

# Frontend Planning

## Purpose

Create an implementation-ready plan for a frontend feature that fits the existing application architecture and accounts for user flows, interface states, accessibility, and verification.

## When to use

Use this skill before implementing a new frontend feature, a significant UI change, or a cross-component interaction. It is also useful when requirements need to be translated into a component and state plan. Do not use it for a small, isolated code change that already has clear requirements.

## Instructions

1. Summarize the user problem and identify the primary user flows.
2. Inspect the existing project structure, framework, routing, component patterns, styling conventions, and available design system.
3. Identify the pages, components, hooks, services, and state boundaries likely to change. Reuse existing abstractions where appropriate.
4. Map data requirements and API dependencies. Record unknown contracts as questions rather than inventing endpoints or response fields.
5. Define the important UI states, including loading, success, empty, validation, error, disabled, and retry states where relevant.
6. Account for responsive layouts, keyboard interaction, focus behavior, semantic structure, and accessible names.
7. Identify performance, security, and privacy considerations relevant to the feature, such as large lists, untrusted content, and sensitive data.
8. Define implementation steps in a practical order and list the acceptance checks needed to verify the behavior.
9. Separate confirmed project conventions from assumptions and unresolved decisions.

## Inputs

- Required: feature description, user goals, and any known acceptance criteria.
- Optional: repository or relevant source files, design references, API documentation, supported browsers, device requirements, and accessibility constraints.

## Outputs

Return an implementation plan containing:

- User flows and acceptance criteria.
- Affected files and proposed component responsibilities.
- Data flow, API dependencies, and state model.
- Loading, empty, success, and error-state behavior.
- Responsive and accessibility requirements.
- Ordered implementation steps.
- Verification checks, assumptions, and open questions.

## Example

**Input:** Plan a searchable product list with category filters and pagination for an existing React application.

**Expected behavior:** Inspect the existing routing, component, and data-fetching patterns; identify the list, search and filter controls, pagination state, loading and empty states, and keyboard-accessible interactions. Record the API contract as an open question if it is not present in the supplied project.

**Expected output:** A concise plan naming the likely components and files, describing state and data flow, and listing functional, responsive, and accessibility checks.

## Limitations

A planning document cannot confirm that a proposed design fits code that has not been inspected. Do not invent framework conventions, API contracts, design-system components, or browser support. Mark assumptions clearly and ask for missing requirements when they materially affect the plan.
