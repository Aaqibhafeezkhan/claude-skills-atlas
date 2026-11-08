# Plugins and integrations

This directory contains integrations that make Atlas resources available in AI-agent environments and developer tools.

## What belongs here

- Installable plugins and extensions
- API or protocol adapters for discovering and retrieving Atlas resources
- Agent tooling that connects a supported environment to repository content
- Integration-specific documentation, manifests, and tests

A plugin is an integration layer, not a replacement for the underlying reusable resource.

## Recommended structure

Use `plugins/<plugin-name>/`. Include a README that explains:

1. Purpose and supported host environment
2. Capabilities and explicit non-capabilities
3. Requirements and installation
4. Configuration and local development
5. Usage examples
6. Permissions, authentication, and security boundaries
7. License and attribution, where relevant

Keep secrets out of the repository. Prefer least-privilege access, document any network or write operations, and treat community resource content as untrusted input.

## Existing plugins

- [Atlas plugin](atlas/) — Claude Code marketplace plugin
- [ChatGPT Atlas integration](chatgpt-atlas/) — read-only API and OpenAPI scaffold
- [GitHub Agent plugin](github-agent/) — GitHub workflow plugin for Claude Code

## Suitable contributions

Add a useful integration with clear setup instructions, improve portability, document compatibility, or add tests for its documented behavior. Do not claim support for a host or capability that has not been implemented.
