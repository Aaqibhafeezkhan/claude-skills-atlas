# Consumer Migration Guide

This guide explains how to consume Claude Skills Atlas resources in your own project and update them safely.

## Choose an integration method

### 1. Claude Code plugin

Use the official plugin to install Atlas into Claude Code:

```text
/plugin marketplace add cellrishi-code/claude-skills-atlas
/plugin install claude-skills-atlas@claude-skills-atlas
```

For local development:

```bash
claude --plugin-dir ./plugins/atlas
```

### 2. Direct repository consumption

Clone the repository when you want to review and copy individual resources:

```bash
git clone https://github.com/cellrishi-code/claude-skills-atlas.git
cd claude-skills-atlas
```

Resources are organized by type:

- `skills/` — reusable behavior and instructions
- `prompts/` — reusable prompt templates
- `workflows/` — repeatable multi-step procedures
- `agents/` — specialized agent definitions
- `templates/` — reusable starting points

Copy the complete resource, including any dependent files. Review its instructions and limitations before enabling it in your environment.

### 3. Read-only HTTP API

The reference integration under `plugins/chatgpt-atlas/` provides health checks, resource search, and resource retrieval.

Available endpoints:

- `GET /health`
- `GET /resources?q=code-review&type=skill&limit=10`
- `GET /resource?path=skills/coding/code-review/SKILL.md`

Deploy the service behind HTTPS and configure the server URL in `openapi.yaml`.

The API reads public resources from GitHub at runtime and does not provide a revision parameter. For reproducible content, use a pinned Git revision or retrieve files from a pinned GitHub URL.

## Pin a version for reproducible builds

The marketplace manifest documents plugin version `1.0.0`. This is a plugin version, not a version assigned to each individual resource.

For direct consumption, prefer a reviewed commit SHA over the moving `main` branch. Record the selected revision in your project's configuration or dependency documentation.

Example: retrieve a resource from a specific commit using Python.

```python
from urllib.request import urlopen

owner = "cellrishi-code"
repo = "claude-skills-atlas"
revision = "REPLACE_WITH_REVIEWED_COMMIT_SHA"
path = "skills/coding/code-review/SKILL.md"

url = f"https://raw.githubusercontent.com/{owner}/{repo}/{revision}/{path}"

with urlopen(url, timeout=15) as response:
    if response.status != 200:
        raise RuntimeError(f"Unable to retrieve resource: {response.status}")
    content = response.read().decode("utf-8")

print(content)
```

Replace the revision placeholder with a reviewed commit SHA before running the example. Review changes before updating the pinned revision.

## Check compatibility before updating

The current documented metadata schema includes `name`, `type`, `domain`, and `intended_use`, with resource paths derived from Git. Cross-agent compatibility metadata is listed as future work in the roadmap.

Before migrating to a newer revision:

1. Review the resource diff between the old and new revisions.
2. Check changed instructions, inputs, outputs, assumptions, and limitations.
3. Test the updated resource in your target agent and model environment.
4. Keep the previous revision available until the new version passes your checks.

Do not assume a resource is compatible with every agent or model simply because it is present in Atlas.

## Handle deprecations safely

The current resource metadata schema does not define standard resource-level version or deprecation fields. Do not assume an automatic deprecation flag or migration mapping is available.

If a resource is renamed, moved, or replaced:

1. Review repository history and relevant release or issue discussions.
2. Identify the replacement and compare its behavior with the resource you currently use.
3. Update your local path or integration configuration.
4. Re-run your checks before removing the old copy.

Document the Atlas commit SHA and resource paths your application depends on to make future migrations easier to review.

## Minimal integration example

For a project that vendors a skill, record its source revision and path explicitly:

```text
Atlas repository: cellrishi-code/claude-skills-atlas
Revision: <reviewed commit SHA>
Resource: skills/coding/code-review/SKILL.md
```

Copy the resource from that revision into the directory supported by your agent. Review its instructions, test it in a controlled environment, and update the recorded revision only after reviewing the changes.

## Related documentation

- [Installation guide](../INSTALL.md)
- [Resource metadata schema](resource-schema.md)
- [Testing prompts and skills](testing-prompts-and-skills.md)
- [Claude Skills Atlas repository](https://github.com/cellrishi-code/claude-skills-atlas)
