import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EXPECTED_VERSION = "0.4.0"
EXPECTED_SKILLS = {
    "brainstorming",
    "chunk",
    "code-audit",
    "code-review",
    "commit",
    "copywriting",
    "inchstone",
    "milestone",
    "pipeline",
    "pr",
    "roadmap",
    "summary",
    "systematic-debugging",
    "test-driven-development",
    "verification-before-completion",
}


class PackageCompatibilityTest(unittest.TestCase):
    def load_json(self, relative_path: str) -> dict:
        with (ROOT / relative_path).open(encoding="utf-8") as file:
            return json.load(file)

    def test_portable_and_claude_manifests_agree(self):
        portable = self.load_json("plugin.json")
        claude = self.load_json(".claude-plugin/plugin.json")
        marketplace = self.load_json(".claude-plugin/marketplace.json")
        listing = marketplace["plugins"][0]

        self.assertEqual(
            portable["$schema"],
            "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json",
        )
        for manifest in (portable, claude, listing):
            self.assertEqual(manifest["name"], "bender")
            self.assertEqual(manifest["version"], EXPECTED_VERSION)

    def test_all_canonical_skills_are_packaged(self):
        actual = {
            path.parent.name for path in (ROOT / "skills").glob("*/SKILL.md")
        }
        self.assertEqual(actual, EXPECTED_SKILLS)

    def test_each_skill_has_codex_metadata(self):
        for name in EXPECTED_SKILLS:
            skill_dir = ROOT / "skills" / name
            with self.subTest(skill=name):
                skill = (skill_dir / "SKILL.md").read_text(encoding="utf-8")
                metadata = (skill_dir / "agents" / "openai.yaml").read_text(
                    encoding="utf-8"
                )
                self.assertTrue(skill.startswith(f"---\nname: {name}\ndescription: "))
                self.assertIn(f"${name}", metadata)

    def test_copywriting_supporting_reference_is_packaged(self):
        self.assertTrue(
            (ROOT / "skills/copywriting/references/brand-setup.md").is_file()
        )


if __name__ == "__main__":
    unittest.main()
