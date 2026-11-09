---
name: api-design
category: web-development
tags: [api, backend, http, rest]
---

# API Design

## Purpose

Plan a consistent, maintainable HTTP API that exposes application capabilities through clear resources, operations, and contracts.

## When to use

Use this skill when designing a new HTTP API, extending an existing endpoint, reviewing an API contract, or documenting request and response behavior. Use an implementation or code-review skill when the API contract is already settled and the task is primarily code changes.

## Instructions

1. Identify the consumers, use cases, and resources the API must support.
2. Define resource paths and HTTP methods around the intended operations. Prefer predictable, resource-oriented naming.
3. Specify request parameters, headers, request bodies, response schemas, status codes, and error formats.
4. Define validation rules, authentication, authorization, and data-exposure boundaries.
5. Consider pagination, filtering, sorting, idempotency, concurrency, and versioning where the use case requires them.
6. Check consistency with existing API conventions and avoid introducing a new pattern without a reason.
7. Document representative success and error cases, including relevant edge cases.
8. Identify unresolved decisions and assumptions instead of inventing external behavior.

## Inputs

- Required: API use cases, intended consumers, and the relevant resource or domain model.
- Optional: existing API specifications, framework conventions, authentication requirements, compatibility constraints, and sample payloads.

## Outputs

Provide an API design that includes:

- Endpoint paths and HTTP methods.
- Request and response schemas.
- Validation and error behavior.
- Authentication and authorization considerations.
- Pagination, idempotency, and versioning decisions where applicable.
- Open questions, assumptions, and representative examples.

## Example

**Input:** Design an endpoint for retrieving a customer's invoices with optional status filtering and pagination.

**Expected behavior:** Define a collection endpoint, query parameters, response envelope, validation rules, authorization boundary, and error responses. Follow the project's existing naming and pagination conventions when they are available.

**Illustrative endpoint:** `GET /customers/{customerId}/invoices?status=overdue&limit=20&cursor={cursor}`.

## Limitations

This skill produces a design proposal, not proof that an API is secure, performant, or compatible. Validate decisions against the actual application, API framework, consumers, and applicable security requirements. Do not assume a particular standard, framework, or external service behavior unless the supplied context supports it.
