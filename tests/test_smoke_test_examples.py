import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from smoke_test_examples import run_smoke_checks


FENCE = chr(96) * 3


class TestSmokeTestExamples(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = Path(self.temp_dir.name)

    def tearDown(self):
        self.temp_dir.cleanup()

    def write_markdown(self, content):
        path = self.root / "guide.md"
        path.write_text(content, encoding="utf-8")
        return path

    def test_valid_python_and_nested_json_examples_pass_without_execution(self):
        self.write_markdown(
            f"{FENCE}python\nvalue = 1 + 2\n{FENCE}\n\n"
            f"{FENCE}json\n{{\"ok\": true, \"nested\": {{\"count\": 2}}}}\n{FENCE}\n"
        )
        errors, skipped, checked, _ = run_smoke_checks(self.root)
        self.assertEqual(errors, [])
        self.assertEqual(skipped, [])
        self.assertEqual(checked, 2)

    def test_invalid_python_reports_source_and_example_number(self):
        self.write_markdown(
            f"{FENCE}text\nillustrative block\n{FENCE}\n\n"
            f"{FENCE}python\nif True print('broken')\n{FENCE}\n"
        )
        errors, _, _, _ = run_smoke_checks(self.root)
        self.assertTrue(any("guide.md:example 2" in error for error in errors))
        self.assertTrue(any("invalid Python syntax" in error for error in errors))

    def test_invalid_json_is_reported(self):
        self.write_markdown(f"{FENCE}json\n{{bad json}}\n{FENCE}\n")
        errors, _, _, _ = run_smoke_checks(self.root)
        self.assertTrue(any("invalid JSON" in error for error in errors))

    def test_external_shell_commands_are_skipped_not_executed(self):
        self.write_markdown(
            f"{FENCE}bash\necho before\n  curl https://example.com\n{FENCE}\n"
        )
        errors, skipped, checked, _ = run_smoke_checks(self.root)
        self.assertEqual(errors, [])
        self.assertEqual(checked, 0)
        self.assertTrue(any("manual verification required" in item for item in skipped))

    def test_external_python_service_is_marked_for_manual_verification(self):
        self.write_markdown(
            f"{FENCE}python\nimport requests\nrequests.get('https://example.com')\n{FENCE}\n"
        )
        errors, skipped, checked, _ = run_smoke_checks(self.root)
        self.assertEqual(errors, [])
        self.assertEqual(checked, 1)
        self.assertTrue(any("external service" in item for item in skipped))

    def test_safe_shell_syntax_is_checked(self):
        self.write_markdown(f"{FENCE}sh\nif true; then\n  echo ok\nfi\n{FENCE}\n")
        errors, skipped, checked, _ = run_smoke_checks(self.root)
        self.assertEqual(errors, [])
        self.assertEqual(skipped, [])
        self.assertEqual(checked, 1)

    def test_missing_local_link_identifies_source_file(self):
        self.write_markdown("See [missing guide](missing.md) for details.")
        errors, _, _, _ = run_smoke_checks(self.root)
        self.assertTrue(any("guide.md:link 1" in error for error in errors))
        self.assertTrue(any("missing local path" in error for error in errors))

    def test_placeholders_are_reported_for_manual_review(self):
        content = FENCE + "python\nprint({{value}})\n" + FENCE + "\n"
        self.write_markdown(content)
        errors, skipped, checked, _ = run_smoke_checks(self.root)
        self.assertEqual(errors, [])
        self.assertEqual(checked, 0)
        self.assertTrue(any("verify manually" in item for item in skipped))


if __name__ == "__main__":
    unittest.main()
