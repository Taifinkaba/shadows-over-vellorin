from case_support import isolated_case
"""Approved fictional topology must not become historical or operational evidence."""
import hashlib
import json
from pathlib import Path
import re
import shutil
import tempfile
import unittest

from snapshot_helpers import YEAR852_CLOSE_REVISIONS, TWIN_SWORD_REVISIONS, DRAGON_REFERENCE_REVISIONS, YEAR852_REVISED_AUTHORITIES, YEAR851_REVISED_AUTHORITIES, SUNCREST262_REVISED_AUTHORITIES
from scripts.validate import ValidationError, validate

ROOT = Path(__file__).resolve().parents[1]


class Phase2GeographyTests(unittest.TestCase):

    def data(self, root, kind, ident):
        return json.loads(re.search(r'```json\n(.*?)\n```', (root/f'entities/{kind}/{ident}.md').read_text(), re.S)[1])


    def mutate(self, ident, change, pattern, kind='mechanics'):
        with tempfile.TemporaryDirectory() as name:
            root = Path(name)
            for folder in ('entities', 'state', 'archive', 'changes', 'docs', 'governance'):
                shutil.copytree(ROOT/folder, root/folder)
            shutil.copy2(ROOT/'index.json', root/'index.json')
            p = root/f'entities/{kind}/{ident}.md'
            s = p.read_text(); m = re.search(r'```json\n(.*?)\n```', s, re.S)
            d = json.loads(m[1]); change(d)
            p.write_text(s[:m.start(1)] + json.dumps(d, indent=2) + s[m.end(1):])
            with self.assertRaisesRegex(ValidationError, pattern):
                validate(root)


    def test_continuity_and_contracts_and_schema_1(self):
        with self.subTest(case='test_approved_realm_cannot_become_historical_node'), isolated_case(self):
            self.mutate('world-geography', lambda d: next(n for n in d['nodes'] if n['id']=='valedorn').update(classification='CONFIRMED CANON'), 'classification/metadata mismatch')
        with self.subTest(case='test_design_node_cannot_parent_historical_membership'), isolated_case(self):
            self.mutate('world-geography', lambda d: next(n for n in d['nodes'] if n['id']=='caelthorne')['parents'][0].update(classification='CONFIRMED CANON'), 'canonical containment through proposed')
        with self.subTest(case='test_untouched_canon_and_authorized_revision_provenance'), isolated_case(self):
            manifest = json.loads((ROOT/'tests/fixtures/phase2-01-preservation.json').read_text())
            pass  # Whole-file fingerprints are centralized in test_preservation.
            for path, revision in manifest['authorized_geography_revisions'].items():
                self.assertEqual(hashlib.sha256((ROOT/path).read_bytes()).hexdigest(), (SUNCREST262_REVISED_AUTHORITIES | YEAR851_REVISED_AUTHORITIES | YEAR852_REVISED_AUTHORITIES | DRAGON_REFERENCE_REVISIONS | TWIN_SWORD_REVISIONS | YEAR852_CLOSE_REVISIONS).get(path, {}).get('after_sha256', revision['after_sha256']), path)
                self.assertNotEqual(revision['before_sha256'], (SUNCREST262_REVISED_AUTHORITIES | YEAR851_REVISED_AUTHORITIES | YEAR852_REVISED_AUTHORITIES | DRAGON_REFERENCE_REVISIONS | TWIN_SWORD_REVISIONS | YEAR852_CLOSE_REVISIONS).get(path, {}).get('after_sha256', revision['after_sha256']))
        with self.subTest(case='test_approved_relationships_and_unplaced_marches'), isolated_case(self):
            nodes = {n['id']: n for n in self.data(ROOT, 'mechanics', 'world-geography')['nodes']}
            for ident in ('valedorn', 'elyndor', 'ironhollow-holds', 'rivermere-league', 'frostmarch'):
                self.assertEqual(nodes[ident]['classification'], 'APPROVED DESIGN')
                self.assertEqual(nodes[ident]['parents'][0]['id'], 'vellorin')
            self.assertEqual(nodes['northern-marches']['parents'][0]['id'], 'vellorin')
            self.assertEqual(nodes['caelthorne']['parents'][0]['id'], 'valedorn')
            self.assertEqual(nodes['vellorin']['parents'][0]['classification'], 'PROPOSED')
        with self.subTest(case='test_region_corridors_have_no_survey_or_duration'), isolated_case(self):
            for ident in ('route-northern-marches-frostmarch', 'route-elyndor-woodland-passage'):
                d = self.data(ROOT, 'locations', ident)
                self.assertEqual(d['classification'], 'PROPOSED')
                self.assertIsNone(d['distance'])
                self.assertEqual(d['durations'], [])
                self.assertTrue(all(v is None for v in d['accessibility'].values()))
                self.assertIsNone(d['patrol_jurisdiction'])
                self.assertIsNone(d['toll_requirements'])

    def test_contracts_and_schema_2(self):
        with self.subTest(case='test_approved_parent_requires_approval_evidence'), isolated_case(self):
            self.mutate('world-geography', lambda d: next(n for n in d['nodes'] if n['id']=='valedorn')['parents'][0].update(source_refs=['entities/locations/brackenford.md']), 'approved containment/provenance')
        with self.subTest(case='test_road_cannot_use_geographic_approval_classification'), isolated_case(self):
            self.mutate('route-northern-marches-frostmarch', lambda d: d.update(classification='APPROVED DESIGN'), 'invalid classification', 'locations')
