import tempfile
import unittest
from pathlib import Path
import sys
from contextlib import redirect_stdout
from io import StringIO

sys.path.append(str(Path(__file__).resolve().parents[1] / "scripts"))
from validate_atlas import validate_catalog


class TestValidateAtlas(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = Path(self.temp_dir.name)
        (self.root / "CATALOG.md").touch()
        (self.root / "skills").mkdir()
        (self.root / "prompts").mkdir()

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_valid_links_and_anchors(self):
        (self.root / "doc1.md").write_text(
            "# Doc 1\n\nLink to [doc2](doc2.md#section-2) and [itself](#doc-1).",
            encoding="utf-8",
        )
        (self.root / "doc2.md").write_text("# Doc 2\n\n## Café", encoding="utf-8")
        self.assertEqual(validate_catalog(self.root), [])

    def test_missing_file(self):
        (self.root / "doc1.md").write_text("[broken](missing.md)", encoding="utf-8")
        errors = validate_catalog(self.root)
        self.assertTrue(any("Missing file" in e for e in errors))

    def test_missing_anchor(self):
        (self.root / "doc1.md").write_text(
            "[broken](doc2.md#missing-section)", encoding="utf-8"
        )
        (self.root / "doc2.md").write_text("# Doc 2", encoding="utf-8")
        errors = validate_catalog(self.root)
        self.assertTrue(any("Missing anchor" in e for e in errors))

    def test_percent_encoded_anchor(self):
        (self.root / "doc1.md").write_text(
            "[valid](doc2.md#caf%C3%A9)", encoding="utf-8"
        )
        (self.root / "doc2.md").write_text("## Café", encoding="utf-8")
        self.assertEqual(validate_catalog(self.root), [])

    def test_skill_required_metadata_and_sections(self):
        skill = self.root / "skills" / "example"
        skill.mkdir()
        (skill / "SKILL.md").write_text(
            "---\nname: example\ncategory: coding\ntags: [test]\n---\n\n"
            "# Example\n\n## Purpose\ntext\n## When to use\ntext\n"
            "## Instructions\ntext\n## Inputs\ntext\n## Outputs\ntext\n"
            "## Example\ntext\n## Limitations\ntext\n",
            encoding="utf-8",
        )
        self.assertEqual(validate_catalog(self.root), [])



    def test_skill_valid_recommendation_metadata(self):
        skill = self.root / "skills" / "example"
        skill.mkdir()
        (skill / "SKILL.md").write_text(
            "---\n"
            "name: example\n"
            "category: coding\n"
            "tags: [test]\n"
            "recommendation_use_cases: [review code, find bugs]\n"
            "recommendation_audience: [developers]\n"
            "recommendation_domain: software-engineering\n"
            "recommendation_prerequisites: [source code]\n"
            "recommendation_related_skills: [coding/debug-systematically]\n"
            "---\n\n"
            "# Example\n\n"
            "## Purpose\ntext\n"
            "## When to use\ntext\n"
            "## Instructions\ntext\n"
            "## Inputs\ntext\n"
            "## Outputs\ntext\n"
            "## Example\ntext\n"
            "## Limitations\ntext\n",
            encoding="utf-8",
        )
        self.assertEqual(validate_catalog(self.root), [])

    def test_skill_incomplete_recommendation_metadata(self):
        skill = self.root / "skills" / "example"
        skill.mkdir()
        (skill / "SKILL.md").write_text(
            "---\n"
            "name: example\n"
            "category: coding\n"
            "tags: [test]\n"
            "recommendation_use_cases: [review code]\n"
            "---\n\n"
            "# Example\n\n"
            "## Purpose\ntext\n"
            "## When to use\ntext\n"
            "## Instructions\ntext\n"
            "## Inputs\ntext\n"
            "## Outputs\ntext\n"
            "## Example\ntext\n"
            "## Limitations\ntext\n",
            encoding="utf-8",
        )
        errors = validate_catalog(self.root)
        self.assertTrue(
            any("recommendation metadata must define all fields" in e for e in errors)
        )


    def test_skill_missing_required_section(self):
        skill = self.root / "skills" / "example"
        skill.mkdir()
        (skill / "SKILL.md").write_text(
            "---\nname: example\ncategory: coding\ntags: [test]\n---\n\n"
            "# Example\n\n## Purpose\ntext\n",
            encoding="utf-8",
        )
        errors = validate_catalog(self.root)
        self.assertTrue(any("missing required section 'Instructions'" in e for e in errors))

    def test_duplicate_prompt_names(self):
        (self.root / "prompts" / "first.md").write_text(
            "# Duplicate Prompt\n\nPrompt body.", encoding="utf-8"
        )
        (self.root / "prompts" / "second.md").write_text(
            "# Duplicate Prompt\n\nAnother body.", encoding="utf-8"
        )
        errors = validate_catalog(self.root)
        self.assertTrue(any("Duplicate prompt name" in e for e in errors))

    def test_duplicate_skill_names(self):
        for folder in ("first", "second"):
            skill = self.root / "skills" / folder
            skill.mkdir()
            (skill / "SKILL.md").write_text(
                "---\nname: code-review\ncategory: coding\ntags: [test]\n---\n\n"
                "# Code Review\n\n"
                "## Purpose\ntext\n"
                "## When to use\ntext\n"
                "## Instructions\ntext\n"
                "## Inputs\ntext\n"
                "## Outputs\ntext\n"
                "## Example\ntext\n"
                "## Limitations\ntext\n",
                encoding="utf-8",
            )

        output = StringIO()
        with redirect_stdout(output):
            errors = validate_catalog(self.root)
        self.assertTrue(any("Duplicate skill name" in e for e in errors))

    def test_similar_skill_descriptions_are_flagged(self):
        skills = {
            "code-review": (
                "Code Review",
                "Review source code to identify bugs, security issues, "
                "and maintainability problems.",
            ),
            "review-source-code": (
                "Review Source Code",
                "Review source code to identify bugs, security issues, "
                "and maintainability problems.",
            ),
        }

        for folder, (name, description) in skills.items():
            skill = self.root / "skills" / folder
            skill.mkdir()
            (skill / "SKILL.md").write_text(
                f"---\nname: {folder}\ncategory: coding\ntags: [test]\n---\n\n"
                f"# {name}\n\n"
                f"## Purpose\n{description}\n"
                "## When to use\ntext\n"
                "## Instructions\ntext\n"
                "## Inputs\ntext\n"
                "## Outputs\ntext\n"
                "## Example\ntext\n"
                "## Limitations\ntext\n",
                encoding="utf-8",
            )

        output = StringIO()
        with redirect_stdout(output):
            validate_catalog(self.root)

        self.assertIn("WARNING: Similar skills", output.getvalue())


    def test_similar_but_not_identical_skill_descriptions_are_flagged(self):
        descriptions = {
            "code-review": (
                "Code Review",
                "Review source code to identify bugs, security issues, "
                "and maintainability problems.",
            ),
            "review-source-code": (
                "Review Source Code",
                "Review source code to identify bugs, security issues, "
                "and maintainability problems in software.",
            ),
        }

        for folder, (name, description) in descriptions.items():
            skill = self.root / "skills" / folder
            skill.mkdir()
            (skill / "SKILL.md").write_text(
                f"---\nname: {folder}\ncategory: coding\ntags: [test]\n---\n\n"
                f"# {name}\n\n"
                f"## Purpose\n{description}\n"
                "## When to use\ntext\n"
                "## Instructions\ntext\n"
                "## Inputs\ntext\n"
                "## Outputs\ntext\n"
                "## Example\ntext\n"
                "## Limitations\ntext\n",
                encoding="utf-8",
            )

        output = StringIO()
        with redirect_stdout(output):
            validate_catalog(self.root)
        self.assertIn("WARNING: Similar skills", output.getvalue())
if __name__ == "__main__":
    unittest.main()
