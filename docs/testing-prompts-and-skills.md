# Testing Prompts and Skills

Claude's answers can change from one run to the next, and between models and versions. So "I tried it once and it looked fine" doesn't tell the next person very much. This guide shows a simple, repeatable way to test a prompt or skill before you open a PR, and how to write down what you found so a reviewer can trust it.

You don't need special tools for any of this. A fresh chat and a few minutes of note taking is enough.

## 1. Decide what "good" looks like first

Before you run anything, write one or two sentences about what a good output should contain. For example: "Lists the bug, explains the cause in plain words, and suggests the smallest fix without rewriting other code."

If you skip this step, it is very easy to look at whatever Claude produced and decide it was what you wanted all along.

## 2. Pick a few realistic test inputs

Two or three inputs is usually enough for a small resource. Try to cover:

- **A normal case:** the everyday situation the resource was written for.
- **An edge case:** messy, incomplete, or unusually long input.
- **A boundary case:** something the resource should refuse, push back on, or ask a clarifying question about.

Use made-up or public data only. Never test with passwords, API keys, private documents, or anyone's personal information.

## 3. Run the test

- Start a **new conversation** for every run, so earlier messages don't influence the result.
- Fill in every `{{variable}}` with your test input. Leftover placeholders change how Claude responds.
- Run each input **at least twice**. If the two outputs are very different, mention that in your notes.
- For skills, also check that the skill gets used when it should, and that it stays out of the way when the task is unrelated.
- If you can, try the same input on a second model. This is optional, but it helps when you want to describe where the resource works well.

## 4. Record what you used

Models and apps change over time, so a result only makes sense alongside the setup that produced it. Copy this block into your PR description and fill it in. The values below are a made-up example to show the format, not real results:

```text
Resource:        prompts/coding/debugging.md
Model:           Claude Sonnet 4.6 (claude-sonnet-4-6)
Where:           claude.ai web app
Date tested:     2026-10-05
Settings:        defaults (no extended thinking, no custom instructions)
Inputs tried:    3 (normal, edge, boundary)
Runs per input:  2
What went well:  Found the bug in both normal-case runs and kept the fix small.
What didn't:     On the edge case it rewrote an unrelated function in one of the two runs.
Not tested:      Claude Code, API, other models.
```

A few tips:

- Copy the model name exactly as the app or API shows it. Don't guess the version.
- Note anything you changed from the defaults, such as extended thinking, a system prompt, project instructions, or API parameters like temperature.
- If the resource was edited during review, test again and update the record.

## 5. Describe results honestly

Write down what you actually observed, not what you hope is true.

| Avoid | Write instead |
|---|---|
| "Verified." | "Tested with 3 inputs on Claude Sonnet 4.6 in claude.ai. 3 of 3 normal-case runs matched the expected output." |
| "Works perfectly." | "Worked well for short code snippets. Less reliable on files over ~300 lines." |
| "Works with all Claude models." | "Tested on Claude Sonnet 4.6 only." |
| "Tested." (no details) | "Tested on 2 inputs, 2 runs each. Notes below." |
| "Tested" when you only read it | "Reviewed, but not run with Claude yet." |

Being clear about what you didn't test is just as useful as listing what worked. A reviewer can decide what to try next, and users know where to be careful.

Don't paste full conversation logs into the PR unless they help. If you do include output, remove any personal or private details first.

## 6. Where your notes go

- **PR description:** put your test record under the **Testing** section of the [pull request template](../.github/PULL_REQUEST_TEMPLATE.md).
- **The resource itself:** if you found a limitation that future users should know about, add a short line to its **Limitations** or **Notes** section.

## Quick checklist

Before opening your PR:

- [ ] I wrote down what a good output looks like before testing.
- [ ] I tried at least one normal case and one edge or boundary case.
- [ ] I used a fresh conversation for each run.
- [ ] I recorded the model name, where I ran it, the date, and any non-default settings.
- [ ] My PR says what I tested **and** what I didn't.
- [ ] I didn't use words like "verified" or "works" without describing what I actually checked.
- [ ] My test inputs and outputs don't contain secrets or personal data.

## Related

- [Guide to Maintainable Skill Tests](maintainable-skill-tests.md): design robust positive, negative, boundary, and adversarial cases without overfitting to one response.
- [CONTRIBUTING.md](../CONTRIBUTING.md): contribution rules, including the testing section.
- [Skill Quality Audit prompt](../prompts/claude-code/skill-quality-audit.md): a prompt for reviewing a skill's clarity and safety before you test it.
