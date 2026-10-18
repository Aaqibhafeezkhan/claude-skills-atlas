# Guide to Maintainable Skill Tests

A useful skill test checks whether a skill reliably produces the intended behavior, not whether a model repeats a sample answer word for word. Model outputs naturally vary in phrasing, ordering, and detail. Tests should make important requirements observable while leaving room for valid alternatives.

This guide is for contributors creating or maintaining tests for skills in the Atlas. It complements [Testing Prompts and Skills](testing-prompts-and-skills.md), which explains how to run a test and record the environment.

## 1. Define the behavior before writing cases

Start with the skill's purpose, inputs, outputs, and boundaries. Turn these into a small set of observable expectations.

Prefer properties such as:

- Identifies the main issue and explains why it matters.
- Uses only evidence present in the supplied input.
- Requests missing information when a conclusion depends on it.
- Follows the required output structure.
- Avoids exposing secrets or taking actions outside the requested scope.

Avoid requirements tied to one exact sentence, a fixed bullet order, or a particular example unless that wording or order is itself part of the contract.

For each expectation, decide how it can be checked and what counts as acceptable variation. Keep required behavior separate from preferences that may improve an answer but are not essential.

## 2. Choose the right kind of evaluation

### Deterministic validation

Use deterministic checks for requirements that can be evaluated consistently without interpreting a model's quality. Examples include:

- Required files, front matter, section headings, or output keys are present.
- A JSON response parses and matches a schema.
- A link or reference follows a specified format.
- A prohibited literal, secret-like fixture value, or unexpected extra field is absent.
- A script produces the same normalized result for a fixed input.

These checks should be fast, repeatable, and strict about the contract. Normalize harmless differences such as whitespace or key order when those differences do not matter.

### Model-based evaluation

Use model-based evaluation when the requirement depends on meaning, judgment, or behavior in context. Examples include:

- Whether the answer addresses the user's actual request.
- Whether a diagnosis is supported by the provided evidence.
- Whether the skill asks a clarifying question when the input is ambiguous.
- Whether the response follows the skill's intended approach without unnecessary work.

Use a rubric with specific criteria instead of asking only whether an answer is "good." Where possible, have a human review a sample of outputs, especially when the evaluation is new or the consequences of an error are significant.

A model-based grader can also vary or make mistakes. Treat its score as evidence, not ground truth. Validate the rubric against human judgments and avoid using the same model's unexamined opinion as the only pass/fail signal.

### Use both when appropriate

A practical test suite often combines deterministic checks for structure and safety with model-based review for semantic quality. Do not use a model to check a simple exact constraint, and do not assume a schema check proves that an answer is useful or correct.

## 3. Build a balanced set of cases

Start small and choose cases that exercise different parts of the skill's contract. Include these categories where relevant:

| Case type | What it checks | Example |
| --- | --- | --- |
| **Positive** | The skill succeeds on an ordinary, in-scope request. | A debugging skill receives a short function and a reproducible error. |
| **Negative** | The skill handles an out-of-scope or disallowed request appropriately. | The user asks a code-review skill to reveal credentials from a log. |
| **Boundary** | The skill handles missing, ambiguous, empty, or borderline input. | The reported error is provided without the relevant code or environment. |
| **Adversarial** | The skill resists misleading input or instructions that conflict with its intended boundaries. | A code sample contains a comment telling the assistant to ignore the review task and print a token. |

Not every skill needs the same number of cases. Choose cases based on realistic failure modes, and explain why a category is not applicable rather than adding contrived examples merely to fill a quota.

For model-based tests, use a fresh conversation for each run and repeat important cases. If repeat runs differ, record the variation instead of silently selecting the most favorable output.

## 4. Reusable test-case template

Copy this template for each case and fill in only what applies:

```yaml
id: debugging-missing-context
type: boundary # positive | negative | boundary | adversarial
purpose: Check that missing evidence is not invented
skill: skills/coding/debug-systematically/SKILL.md

input: |
  The application crashes on startup. What is the root cause?

expected_properties:
  - States that the supplied information is insufficient to identify a root cause.
  - Asks for useful missing details, such as the error message and relevant logs.
  - Does not invent a stack trace or claim to have inspected the application.

acceptable_variation:
  - May ask for the error message before or alongside environment details.
  - May use bullets or a short paragraph.

must_not:
  - Assert a specific root cause without evidence.
  - Claim to have run the application.

evaluation:
  deterministic:
    - Check that the fixture contains no private data.
  model_based:
    - Score evidence discipline and usefulness against the properties above.

notes: Keep the input synthetic and self-contained.
```

This is a documentation template, not a required test-runner format. Adapt the fields to the project's tooling while preserving the distinction between input, required properties, allowed variation, and evaluation method.

## 5. Write assertions about properties, not wording

A maintainable assertion describes what must be true about the response.

**Brittle assertion**

```python
assert response == "The root cause is a missing environment variable."
```

This fails if a correct answer explains the same point in different words, and it may pass a response that copies the sentence without supporting evidence.

**Property-oriented checks**

- The response distinguishes known facts from hypotheses.
- It does not claim a root cause when the input is insufficient.
- It requests at least one relevant missing detail.
- It does not invent logs, files, or tool results.

Use exact-match assertions only when the output contract genuinely requires exact text, such as a fixed command, a machine-readable enum, or a required protocol token. Otherwise, use structural validation, a rubric, or human review.

For each property, document:

1. **Required:** behavior that must be present for the case to pass.
2. **Forbidden:** behavior that makes the case fail, even if other parts are good.
3. **Flexible:** presentation or reasoning details that may vary without affecting correctness.
4. **Evidence:** what in the output supports the judgment.

A response can satisfy the required properties while still having different phrasing, length, ordering, or examples. Do not penalize those differences unless the skill's contract makes them important.

## 6. Keep fixtures small, safe, and reproducible

Fixtures should isolate the behavior under test.

- Use synthetic, public, or deliberately redacted data. Never commit credentials, access tokens, session cookies, private documents, or personal information.
- Keep only the context needed to exercise the behavior. Remove unrelated conversation history and huge logs where a short excerpt will reproduce the case.
- Use stable filenames, explicit assumptions, and fixed inputs. Avoid relying on network access, current time, an external service, or undocumented local state unless that dependency is what you are testing.
- If randomness is part of a test harness, set a seed where possible and record the relevant configuration.
- Keep expected properties beside the fixture, and version them with the test so changes are reviewable.
- Make adversarial examples inert: describe the attack or include harmless placeholder text rather than real secrets or executable harmful payloads.
- If a fixture is derived from an external source, check permission to redistribute it and include attribution when required.

Do not make fixtures so artificial that they no longer represent real use. Prefer a small representative case plus a few targeted edge cases over one giant fixture that mixes many unrelated failures.

## 7. Evaluate and report results honestly

For each test run, record enough context for another contributor to understand or reproduce the result:

- Skill path and test-case IDs.
- Model and exact version, if model-based.
- Interface or runtime and relevant settings.
- Run count and observed pass/fail results.
- Which expected properties passed or failed.
- Known limitations and cases not tested.

Do not describe a skill as reliable based on a single favorable output. Do not report a model or version as tested if it was not actually used. When a skill changes, rerun the cases affected by that change and note any updated expectations.

For a larger suite, track failures by property and case type. This helps distinguish a skill regression from a flaky evaluation, an overly strict assertion, or a fixture that no longer represents the intended behavior.

## 8. Review checklist

Before submitting a test or changing an existing one:

- [ ] The intended behavior and scope are written down.
- [ ] Deterministic requirements are separated from semantic judgments.
- [ ] Positive, negative, boundary, and adversarial cases are considered.
- [ ] Expected properties, forbidden behavior, and acceptable variation are explicit.
- [ ] Assertions do not depend on exact wording unless exact wording is part of the contract.
- [ ] Fixtures are small, synthetic or safely redacted, and reproducible.
- [ ] Model name, setup, repetitions, observed results, and limitations are recorded when applicable.
- [ ] The tests fail for meaningful regressions and tolerate harmless response variation.

## Related

- [Testing Prompts and Skills](testing-prompts-and-skills.md): running tests and recording the model and setup.
- [Skill Authoring Guide](skill-authoring-guide.md): defining a skill's purpose, scope, inputs, outputs, and limitations.
- [CONTRIBUTING.md](../CONTRIBUTING.md): contribution and review expectations.
