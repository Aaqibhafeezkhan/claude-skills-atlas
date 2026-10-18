# Contributing

Welcome to Claude Skills Atlas.

The goal is simple: collect useful, reusable Claude instructions from people across the world and make them easy to discover.

## Contribution types

### Skills

Put reusable instruction packages under:

```text
skills/<category>/<name>/SKILL.md
```

A skill should normally contain:

- front matter with a name, category, and tags
- Purpose
- When to use
- Instructions
- Inputs
- Outputs
- Example
- Limitations

Starting from scratch? Copy [the skill contributor starter template](templates/skill-starter/SKILL.md), replace its placeholders, and adapt the sections to your use case.

### Prompts

Put copy-paste prompt templates under:

```text
prompts/<category>/<name>.md
```

Use placeholders such as `{{topic}}`, `{{language}}`, `{{level}}`, or `{{constraints}}` rather than private information.

### Workflows

Put repeatable multi-step procedures under:

```text
workflows/<category>/<name>.md
```

Explain the stages, inputs, outputs, and failure cases.

### Agents

Put specialized agent definitions under:

```text
agents/<category>/<name>.md
```

Describe the role, scope, expected inputs, behavior, tools/context, and boundaries.

### Templates

Put reusable checklists, schemas, report structures, or document templates under:

```text
templates/<category>/<name>.md
```

## Naming

Use lowercase kebab-case for directories and files.

Good:

```text
skills/coding/code-review/SKILL.md
prompts/mathematics/proof-explainer.md
workflows/research/literature-review.md
```

Avoid personal names, dates, random numbers, and vague names such as `prompt1.md`.

## Quality checklist

Before opening a PR:

- The contribution is useful to people other than the author.
- The intended task and expected output are clear.
- Variables are used for information that changes between users.
- Examples are realistic and safe.
- No passwords, API keys, tokens, session cookies, private documents, or personal data are included.
- External claims and adapted material are attributed where appropriate.
- Check existing skills for duplicate names and overlapping purposes before creating a new skill.
- Run `python scripts/validate_atlas.py` to check for duplicate resource names and flag highly similar skill Purpose descriptions for review.
- If an existing skill covers the same task, extend it instead of creating a duplicate.
- Keep intentional variants only when they serve meaningfully different use cases, audiences, inputs, or outputs. Explain the distinction in the skill's Purpose and When to use sections.
- Treat overlap warnings as review prompts, not automatic proof that two skills are duplicates.
- The contribution does not intentionally contain prompt injection designed to compromise unrelated users, tools, or systems.
- The contribution follows the folder structure and naming rules.

## Pull requests

Maintainers can use the [Maintainer Merge Checklist](docs/maintainer-merge-checklist.md) for a consistent final review before merging resource PRs.

Keep PRs focused. One coherent contribution is easier to review than a large mixed change.

### First-time contributor workflow

For a typical contribution:

1. Fork the repository and clone your fork locally.
2. Create a focused branch for your change.
3. Make the contribution and review the changes locally.
4. Test the contribution where practical.
5. Commit the changes with a clear commit message.
6. Push the branch to your fork.
7. Open a Pull Request from your fork to the main repository.
8. Respond to maintainer feedback and update the PR if revisions are requested.

Maintainers may:

- ask for revisions
- move a contribution into another category
- combine duplicates
- reject unsafe, misleading, low-quality, or improperly licensed material

## Attribution and licensing

Only submit content you are allowed to redistribute.

When adapting an existing work, include the original source and relevant license/attribution information.

## Common Development Commands

### Regenerate the resource catalog

`CATALOG.md` is generated from the repository resources. After adding or removing resources, regenerate the catalog with:

```bash
python scripts/generate_catalog.py
```

The script updates `CATALOG.md` automatically. Do not edit `CATALOG.md` manually.


## Testing

Where practical, test prompts or skills with Claude and describe what was tested.

Do not claim a result is "verified" or "works" unless you actually evaluated it.

See [Testing Prompts and Skills](docs/testing-prompts-and-skills.md) for a step-by-step guide and a template for recording the model, version, and setup you tested with. For a more structured evaluation plan, use the [Guide to Maintainable Skill Tests](docs/maintainable-skill-tests.md), which covers deterministic checks, model-based evaluation, and reusable test cases.

## Security

Never publish secrets or private data.

For repository security issues, see [SECURITY.md](SECURITY.md).
