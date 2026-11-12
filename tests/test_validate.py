"""Regression tests mutate disposable copies; campaign files are never edited."""
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

import yaml

from scripts.validate import ValidationError, copper, frontmatter, validate

ROOT = Path(__file__).resolve().parents[1]
THERON = "entities/characters/theron-ashvale.md"
VAELTHARION = "entities/creatures/vaeltharion.md"
SOURCE = "archive/legacy-modules/codex/02-system-2-character-inventory-mechanics-ledger.md"


class RepositoryValidationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="vellorin-test-")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        for name in ("entities", "archive", "state"):
            shutil.copytree(ROOT / name, self.root / name)
        shutil.copy2(ROOT / "index.json", self.root / "index.json")

    def json_edit(self, path, change):
        p = self.root / path
        data = json.loads(p.read_text())
        change(data)
        p.write_text(json.dumps(data))

    def metadata_edit(self, path, change):
        p = self.root / path
        data = frontmatter(p)
        body = p.read_text().split("---", 2)[2]
        change(data)
        p.write_text("---\n" + yaml.safe_dump(data, sort_keys=False) + "---" + body)

    def fails(self, fragment):
        with self.assertRaisesRegex(ValidationError, fragment):
            validate(self.root)

    def test_repository_passes(self):
        self.assertIn("checkpoint valid", validate(self.root))

    def test_missing_indexed_entity(self):
        (self.root / THERON).unlink()
        self.fails("missing file")

    def test_unindexed_entity(self):
        shutil.copy2(self.root / THERON, self.root / "entities/characters/orphan.md")
        self.fails("unindexed=.*orphan")

    def test_duplicate_id(self):
        self.json_edit("index.json", lambda x: x["entries"].append(dict(x["entries"][0])))
        self.fails("duplicate entity ID")

    def test_duplicate_path(self):
        def change(x):
            entry = dict(x["entries"][0]); entry["id"] = "different-id"
            x["entries"].append(entry)
        self.json_edit("index.json", change)
        self.fails("duplicate entity path")

    def test_missing_archive_module_not_cited_by_entities(self):
        (self.root / "archive/legacy-modules/people/01-reading-key-and-canon-policy.md").unlink()
        self.fails("missing file")

    def test_missing_archive_source_original(self):
        (self.root / "archive/Shadows_Over_Vellorin_World_Bible_v1.md").unlink()
        self.fails("archive module.source: missing file")

    def test_unindexed_archive_module(self):
        (self.root / "archive/legacy-modules/orphan.md").write_text("Historical evidence")
        self.fails("archive/index coverage mismatch")

    def test_missing_archive_index(self):
        (self.root / "archive/legacy-index.json").unlink()
        self.fails("index.archive_index: missing file")

    def test_duplicate_archive_path(self):
        self.json_edit("archive/legacy-index.json", lambda x: x["modules"].append(x["modules"][0]))
        self.fails("duplicate module path")

    def test_wrong_currency_total(self):
        self.json_edit("state/checkpoint.json", lambda x: x["money"].update(total_gp_sp="0gp"))
        self.fails("currency total differs")

    def test_custody_funds_cannot_be_added_to_spendable_total(self):
        self.json_edit("state/checkpoint.json", lambda x: x["money"].update(total_gp_sp="593gp 2sp"))
        self.fails("currency total differs")

    def test_balanced_but_changed_central_money(self):
        self.json_edit("state/checkpoint.json", lambda x: x["money"].update(central_gp_sp="307gp", total_gp_sp="554gp"))
        self.fails("checkpoint/entity mismatch: party-finances money")

    def test_balanced_but_changed_reserve(self):
        self.json_edit("state/checkpoint.json", lambda x: x["money"].update(reserve_gp_sp="156gp 2sp", total_gp_sp="556gp"))
        self.fails("checkpoint/entity mismatch: party-finances money")

    def test_equivalent_integer_currency_forms_pass(self):
        self.json_edit("state/checkpoint.json", lambda x: x["money"].update(total_gp_sp="55500cp"))
        self.assertIn("checkpoint valid", validate(self.root))

    def test_every_theron_stat_must_match_entity(self):
        state = json.loads((self.root / "state/checkpoint.json").read_text())
        for field in state["theron"]:
            with self.subTest(field=field):
                value = "S" if field == "rank" else state["theron"][field] + (-1 if field in {"hp", "mp"} else 1)
                changed = json.loads(json.dumps(state)); changed["theron"][field] = value
                if field == "mp": changed["context"]["mp_before_recent_casts"] -= 1
                (self.root / "state/checkpoint.json").write_text(json.dumps(changed))
                self.fails("checkpoint/entity mismatch")
        (self.root / "state/checkpoint.json").write_text(json.dumps(state))

    def test_entity_stat_change_must_match_checkpoint(self):
        self.metadata_edit(THERON, lambda x: x["checkpoint_values"].update({"theron.hp": 99}))
        self.fails("checkpoint/entity mismatch")

    def test_chain_and_anchor_counts_must_match_entity(self):
        state = json.loads((self.root / "state/checkpoint.json").read_text())
        for field in state["world"]:
            with self.subTest(field=field):
                changed = json.loads(json.dumps(state)); changed["world"][field] += 1
                (self.root / "state/checkpoint.json").write_text(json.dumps(changed))
                self.fails("checkpoint/entity mismatch: vaeltharion")

    def test_entity_chain_change_must_match_checkpoint(self):
        self.metadata_edit(VAELTHARION, lambda x: x["checkpoint_values"].update({"world.vaeltharion_chains_attached": 1}))
        self.fails("checkpoint/entity mismatch")

    def test_date_time_location_must_match_entity(self):
        state = json.loads((self.root / "state/checkpoint.json").read_text())
        for field, value in (("date", "Year 847 Day 47"), ("time", "09:16"), ("location", "Elsewhere")):
            with self.subTest(field=field):
                changed = dict(state); changed[field] = value
                (self.root / "state/checkpoint.json").write_text(json.dumps(changed))
                self.fails("checkpoint/entity mismatch")

    def test_missing_checkpoint_fact_in_entity(self):
        self.metadata_edit(THERON, lambda x: x["checkpoint_values"].pop("theron.hp"))
        self.fails("checkpoint_values: expected keys")

    def test_deleting_authoritative_entity_and_its_index_entry(self):
        path = "entities/mechanics/party-finances.md"
        (self.root / path).unlink()
        self.json_edit("index.json", lambda x: x.update(entries=[e for e in x["entries"] if e["path"] != path]))
        self.fails("missing authoritative snapshot entity")

    def test_required_frontmatter_fields(self):
        original = (self.root / THERON).read_text()
        for field in ("id", "type", "status", "visibility", "source_refs"):
            with self.subTest(field=field):
                (self.root / THERON).write_text(original)
                self.metadata_edit(THERON, lambda x: x.pop(field))
                self.fails("required frontmatter fields")

    def test_metadata_wrong_types(self):
        original = (self.root / THERON).read_text()
        for field, value in (("id", 7), ("type", []), ("status", True), ("visibility", None), ("source_refs", SOURCE)):
            with self.subTest(field=field):
                (self.root / THERON).write_text(original)
                self.metadata_edit(THERON, lambda x: x.update({field: value}))
                self.fails("expected a nonempty string|source_refs must be")

    def test_metadata_invalid_values(self):
        original = (self.root / THERON).read_text()
        for field, value in (("type", "unknown"), ("status", "unknown"), ("visibility", "public"), ("id", "UPPER CASE")):
            with self.subTest(field=field):
                (self.root / THERON).write_text(original)
                self.metadata_edit(THERON, lambda x: x.update({field: value}))
                self.fails("invalid")

    def test_metadata_index_mismatch(self):
        self.metadata_edit(THERON, lambda x: x.update(status="last-verified"))
        self.fails("metadata mismatch status")

    def test_duplicate_yaml_keys(self):
        p = self.root / THERON
        p.write_text(p.read_text().replace("id: theron-ashvale", "id: theron-ashvale\nid: theron-ashvale"))
        self.fails("duplicate YAML key")

    def test_invalid_yaml(self):
        p = self.root / THERON; p.write_text("---\nid: [\n---\n")
        self.fails("invalid YAML")

    def test_unsafe_yaml_tag(self):
        p = self.root / THERON; p.write_text("---\n!!python/object:builtins.object {}\n---\n")
        self.fails("invalid YAML")

    def test_body_metadata_cannot_replace_frontmatter(self):
        p = self.root / THERON
        p.write_text(p.read_text().replace("id: theron-ashvale\n", "", 1) + "\nid: theron-ashvale\n")
        self.fails("required frontmatter fields")

    def test_both_yaml_quote_styles_pass(self):
        p = self.root / THERON; original = p.read_text()
        for quote in ("'", '"'):
            with self.subTest(quote=quote):
                p.write_text(original.replace(SOURCE, f"{quote}{SOURCE}{quote}"))
                self.assertIn("checkpoint valid", validate(self.root))

    def test_missing_source_with_both_yaml_quote_styles_fails(self):
        p = self.root / THERON; original = p.read_text()
        for quote in ("'", '"'):
            with self.subTest(quote=quote):
                p.write_text(original.replace(SOURCE, f"{quote}missing.md{quote}"))
                self.fails("missing file missing.md")

    def test_source_path_escape(self):
        self.metadata_edit(THERON, lambda x: x.update(source_refs=["../outside.md"]))
        self.fails("normalized repository-relative path")

    def test_absolute_source_path(self):
        self.metadata_edit(THERON, lambda x: x.update(source_refs=[str(ROOT / SOURCE)]))
        self.fails("normalized repository-relative path")

    def test_symlink_escape(self):
        (self.root / "escape.md").symlink_to(ROOT / SOURCE)
        self.metadata_edit(THERON, lambda x: x.update(source_refs=["escape.md"]))
        self.fails("path escapes repository")

    def test_empty_or_nonstring_sources(self):
        original = (self.root / THERON).read_text()
        for refs in ([], [1], [None], [""]):
            with self.subTest(refs=refs):
                (self.root / THERON).write_text(original)
                self.metadata_edit(THERON, lambda x: x.update(source_refs=refs))
                self.fails("source_refs")

    def test_duplicate_json_keys(self):
        p = self.root / "state/checkpoint.json"
        p.write_text(p.read_text().replace('"hp": 100', '"hp": 100, "hp": 99'))
        self.fails("duplicate JSON key")

    def test_boolean_is_not_an_integer_stat(self):
        self.json_edit("state/checkpoint.json", lambda x: x["theron"].update(hp=True))
        self.fails("expected an integer")

    def test_hp_and_mp_bounds(self):
        state = json.loads((self.root / "state/checkpoint.json").read_text())
        for field, value in (("hp", -1), ("hp", 101), ("mp", 401)):
            with self.subTest(field=field, value=value):
                changed = json.loads(json.dumps(state)); changed["theron"][field] = value
                (self.root / "state/checkpoint.json").write_text(json.dumps(changed))
                self.fails("integer|exceeds maximum")

    def test_optimized_python_still_rejects_bad_state(self):
        self.json_edit("state/checkpoint.json", lambda x: x["theron"].update(hp=-1))
        result = subprocess.run([sys.executable, "-O", str(ROOT / "scripts/validate.py"), "--root", str(self.root)], capture_output=True, text=True)
        self.assertEqual(result.returncode, 1)
        self.assertIn("ERROR:", result.stderr)
        self.assertNotIn("Traceback", result.stderr)


    def test_checkpoint_schema_rejects_unversioned_and_wrong_version(self):
        original = json.loads((self.root / "state/checkpoint.json").read_text())
        for value in (None, 1, True, 3):
            changed = dict(original)
            if value is None: changed.pop("schema_version")
            else: changed["schema_version"] = value
            (self.root / "state/checkpoint.json").write_text(json.dumps(changed))
            self.fails("expected keys|unsupported schema_version")

    def test_mana_cannot_restore_without_reconciled_expenditure(self):
        self.json_edit("state/checkpoint.json", lambda x: x["theron"].update(mp=400))
        self.fails("recent MP expenditure")

    def test_omitted_spell_cost_fails_mana_reconciliation(self):
        self.json_edit("state/checkpoint.json", lambda x: x["context"]["recent_mp_costs"].pop("Shadow Mantle"))
        self.fails("recent MP expenditure")

    def test_academy_cannot_be_marked_as_pooled(self):
        self.json_edit("state/checkpoint.json", lambda x: x["context"]["academy"].update(included_in_party_total=True))
        self.fails("academy funds must remain separate")

    def test_academy_cash_or_deposit_cannot_inflate_total(self):
        for extra in (34, 15, 49):
            self.json_edit("state/checkpoint.json", lambda x: x["money"].update(total_gp_sp=f"{555+extra}gp"))
            self.fails("currency total differs")

    def test_context_entity_references_must_resolve(self):
        self.json_edit("state/checkpoint.json", lambda x: x["context"]["companions_present"].append("invented-companion"))
        self.fails("unknown companion/role entity")

    def test_checkpoint_source_cannot_be_missing(self):
        self.json_edit("state/checkpoint.json", lambda x: x.update(source="missing.md"))
        self.fails("checkpoint.source: missing file")

    def test_old_personal_accounts_cannot_be_reintroduced(self):
        self.json_edit("state/checkpoint.json", lambda x: x["money"].update(garrick_gp_sp="95gp 8sp"))
        self.fails("checkpoint.money: expected keys")

    def test_current_snapshot_matches_handoff_totals(self):
        state = json.loads((self.root / "state/checkpoint.json").read_text())
        self.assertEqual((state["date"],state["time"]), ("Year 847 Day 153","22:05"))
        self.assertEqual(state["theron"]["mp"],337)
        self.assertEqual(sum(state["context"]["recent_mp_costs"].values()),63)
        self.assertEqual(copper(state["money"]["total_gp_sp"]),55500)
        self.assertEqual(state["world"], {"vaeltharion_chains_attached":0,"protective_anchors_retained":7})
        self.assertEqual(state["context"]["companions_present"], ["nyx-thorne","shade"])

    def test_core_and_new_spell_costs_are_preserved(self):
        text = (self.root / "entities/mechanics/theron-spells.md").read_text()
        costs = {}
        for line in text.splitlines():
            cells = [cell.strip() for cell in line.split("|")[1:-1]]
            for i in range(0, len(cells)-1, 2):
                if cells[i+1].isdigit(): costs[cells[i]] = int(cells[i+1])
        expected = {
            "Frost Lance":6,"Umbral Bolt":7,"Rune Barrier":9,"Minor Restoration":11,
            "Spatial Step":9,"Runic Edge":6,"Ward Sense":5,"Mental Probe":13,"Mental Link":9,
            "Controlled Memory Resonance":11,"Mirror Mind":6,"Vital Resonance":14,
            "Arcane Disruption":11,"Communication Spoof":7,"Extended Spatial Transfer":21,
            "Greater Rune Barrier":28,"Veiled Memory Trace":13,"Perceptual Interception":7,
            "Dreamfall Mastered":21,"Oath Sight":8,"Frost Veil":11,"Umbral Murmur":9,
            "Glacial Step":12,"Rime Snare":14,"Shadow Mantle":16,"Phantom Procession":18}
        self.assertEqual(costs,expected)
        self.assertEqual({k:costs[k] for k in json.loads((self.root / "state/checkpoint.json").read_text())["context"]["recent_mp_costs"]},
                         json.loads((self.root / "state/checkpoint.json").read_text())["context"]["recent_mp_costs"])


class CurrencyTests(unittest.TestCase):
    def test_exact_integer_conversion(self):
        self.assertEqual(copper("495gp 2sp"), 49520)
        self.assertEqual(copper("38 gp 2 sp"), 3820)
        self.assertEqual(copper("1gp 2sp 3cp"), 123)
        self.assertEqual(copper("0cp"), 0)
        self.assertEqual(copper("9007199254740993gp"), 900719925474099300)

    def test_invalid_currency_rejected(self):
        for value in ("", "1.5gp", "-1gp", "1gp garbage", "1gp 2gp", "gold", 1.5, True):
            with self.subTest(value=value), self.assertRaises(ValidationError):
                copper(value)


if __name__ == "__main__":
    unittest.main()
