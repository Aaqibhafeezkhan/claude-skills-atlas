#!/usr/bin/env python3
"""Static smoke checks for executable examples in Markdown documentation.

This tool never executes code examples. Python and JSON blocks are parsed,
shell blocks are syntax-checked with sh -n, and local Markdown links are
checked for missing paths. External or destructive shell examples are reported
as requiring manual verification instead of being checked or run.
"""

import ast
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path
from urllib.parse import unquote, urlparse

ROOT = Path(__file__).resolve().parents[1]
FENCE = chr(96)
FENCE_START = re.compile(r"^\s{0,3}(" + re.escape(FENCE) + r"{3,}|~{3,})(.*)$")
LINK_RE = re.compile(r"\]\(([^)]+)\)")
EXTERNAL_SERVICE_PATTERN = re.compile(
    r"(?i)\b(?:requests|httpx|urllib\.request|socket|boto3|botocore|"
    r"openai|anthropic|google\.cloud|azure\.[a-z_]+|"
    r"psycopg2|sqlalchemy|pymongo|redis)\b|https?://"
)
KNOWN_MANUAL_LANGUAGES = {
    "javascript", "js", "typescript", "ts", "tsx", "jsx", "yaml", "yml",
    "sql", "html", "xml", "powershell", "pwsh", "ps1", "php", "java",
    "go", "rust", "ruby", "r", "c", "cpp", "c++",
}
MANUAL_SHELL_COMMAND = re.compile(
    r"(?im)(?:^|[;&|]\s*)[ \t]*"
    r"(?:sudo\b|rm\b|rmdir\b|mkfs\b|dd\b|shutdown\b|reboot\b|"
    r"curl\b|wget\b|ssh\b|scp\b|nc\b|ncat\b|"
    r"git\s+(?:clone|push)\b|git\s+reset\s+--hard\b|"
    r"npm\s+install\b|npx\b|pip\s+install\b|python\s+-m\s+pip\s+install\b|"
    r"apt(?:-get)?\s+install\b|brew\s+install\b|"
    r"docker\b|kubectl\s+(?:apply|delete|exec)\b|"
    r"terraform\s+apply\b|aws\b|az\b|gcloud\b|"
    r"psql\b|mysql\b|sqlite3\b)"
)


def markdown_files(root: Path):
    for path in sorted(root.rglob("*.md")):
        if any(part in {".git", ".venv", "node_modules"} for part in path.parts):
            continue
        yield path


def extract_code_blocks(text: str):
    """Yield (one-based block number, language, code) for Markdown fences."""
    lines = text.splitlines()
    index = 0
    block_number = 0
    while index < len(lines):
        match = FENCE_START.match(lines[index])
        if not match:
            index += 1
            continue

        marker = match.group(1)
        info = match.group(2).strip()
        language = info.split()[0].lower() if info else ""
        close_pattern = re.compile(
            r"^\s{0,3}" + re.escape(marker[0]) + r"{" + str(len(marker)) + r",}\s*$"
        )
        start = index + 1
        index = start
        while index < len(lines) and not close_pattern.match(lines[index]):
            index += 1
        if index >= len(lines):
            break

        block_number += 1
        yield block_number, language, "\n".join(lines[start:index])
        index += 1


def has_placeholder(code: str) -> bool:
    for line in code.splitlines():
        stripped = line.strip()
        if stripped in {"...", "…", "TODO", "# ...", "// ..."}:
            return True
    return bool(re.search(r"\{\{\s*[\w.-]+[^}\n]*\}\}", code))


def check_local_links(path: Path, root: Path, text: str):
    errors = []
    for link_number, match in enumerate(LINK_RE.finditer(text), start=1):
        link_text = match.group(1).strip()
        if not link_text:
            continue
        raw_target = link_text.split()[0].strip("<>")
        if not raw_target or raw_target.startswith("#"):
            continue
        parsed = urlparse(raw_target)
        if parsed.scheme or parsed.netloc:
            continue
        target_text = unquote(parsed.path)
        if not target_text:
            continue

        target = (path.parent / target_text).resolve()
        try:
            target.relative_to(root.resolve())
        except ValueError:
            continue
        if not target.exists():
            rel = path.relative_to(root).as_posix()
            errors.append(
                f"{rel}:link {link_number}: missing local path '{raw_target}'"
            )
    return errors


def check_code_block(rel: str, number: int, language: str, code: str):
    errors = []
    skipped = []
    label = f"{rel}:example {number}"

    if not language:
        return errors, skipped, 0

    if language in {"python", "py"}:
        if has_placeholder(code):
            skipped.append(f"{label}: Python snippet contains placeholders; verify manually")
            return errors, skipped, 0
        try:
            ast.parse(code, filename=rel)
        except SyntaxError as exc:
            errors.append(
                f"{label}: invalid Python syntax at line {exc.lineno}: {exc.msg}"
            )
            return errors, skipped, 1
        if EXTERNAL_SERVICE_PATTERN.search(code):
            skipped.append(
                f"{label}: Python example references a network API or external service; "
                "manual verification required (code was not executed)"
            )
        return errors, skipped, 1

    if language == "json":
        if has_placeholder(code):
            skipped.append(f"{label}: JSON example contains placeholders; verify manually")
            return errors, skipped, 0
        try:
            json.loads(code)
        except json.JSONDecodeError as exc:
            errors.append(
                f"{label}: invalid JSON at line {exc.lineno}, column {exc.colno}: {exc.msg}"
            )
            return errors, skipped, 1
        if EXTERNAL_SERVICE_PATTERN.search(code):
            skipped.append(
                f"{label}: JSON example references an external endpoint/service; "
                "manual verification required"
            )
        return errors, skipped, 1

    if language in {"sh", "bash", "shell"}:
        shell_text = "\n".join(
            re.sub(r"^\s*\$\s?", "", line) for line in code.splitlines()
        )
        if MANUAL_SHELL_COMMAND.search(shell_text):
            skipped.append(
                f"{label}: shell example includes external or destructive commands; "
                "manual verification required (never executed)"
            )
            return errors, skipped, 0
        shell = shutil.which("sh")
        if not shell:
            skipped.append(f"{label}: sh is unavailable; shell syntax needs manual verification")
            return errors, skipped, 0
        result = subprocess.run(
            [shell, "-n"],
            input=code,
            text=True,
            capture_output=True,
            check=False,
        )
        if result.returncode:
            detail = (result.stderr or "shell syntax check failed").strip().splitlines()[0]
            errors.append(f"{label}: invalid shell syntax: {detail}")
        return errors, skipped, 1

    if language in KNOWN_MANUAL_LANGUAGES:
        skipped.append(
            f"{label}: {language} example is not executed; manual verification required"
        )
    return errors, skipped, 0


def run_smoke_checks(root: Path):
    errors = []
    skipped = []
    checked = 0
    files = list(markdown_files(root))
    for path in files:
        text = path.read_text(encoding="utf-8-sig")
        rel = path.relative_to(root).as_posix()
        errors.extend(check_local_links(path, root, text))
        for number, language, code in extract_code_blocks(text):
            block_errors, block_skipped, block_checked = check_code_block(
                rel, number, language, code
            )
            errors.extend(block_errors)
            skipped.extend(block_skipped)
            checked += block_checked
    return errors, skipped, checked, len(files)


def main():
    root = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else ROOT
    errors, skipped, checked, file_count = run_smoke_checks(root)
    for error in errors:
        print(f"ERROR: {error}")
    for item in skipped:
        print(f"MANUAL: {item}")
    if errors:
        print(
            f"Smoke checks failed: {len(errors)} error(s), {checked} example(s) "
            f"checked, {len(skipped)} manual check(s), {file_count} Markdown file(s) scanned."
        )
        return 1
    print(
        f"Smoke checks passed: {checked} example(s) checked, {len(skipped)} "
        f"manual check(s), {file_count} Markdown file(s) scanned. "
        "No example code was executed."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
