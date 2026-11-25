"""One whole-campaign fingerprint check instead of repeated copies per subsystem."""
import hashlib
import json
from pathlib import Path
import re
import unittest
from snapshot_helpers import YEAR853_REVISIONS, YEAR852_CLOSE_REVISIONS, TWIN_SWORD_REVISIONS, DRAGON_REFERENCE_REVISIONS, YEAR852_REVISED_AUTHORITIES, CHARACTER_SHEET_REVISIONS, DAY196_REVISED_AUTHORITIES, SUNCREST262_REVISED_AUTHORITIES, YEAR851_REVISED_AUTHORITIES

ROOT=Path(__file__).resolve().parents[1]


class PreservationTests(unittest.TestCase):
    def test_all_current_owner_fingerprints(self):
        expected={}
        for fixture in sorted((ROOT/'tests/fixtures').glob('*.json')):
            d=json.loads(fixture.read_text())
            def collect(value):
                if not isinstance(value,dict):return
                for key,row in value.items():
                    if key in ('sha256','protected_sha256','historical_sha256','unchanged_sha256') and isinstance(row,dict):
                        for path,digest in row.items():
                            if isinstance(digest,str) and re.fullmatch('[0-9a-f]{64}',digest):
                                self.assertTrue(path not in expected or expected[path]==digest, path+' inconsistent fixture fingerprints')
                                expected[path]=digest
                    elif fixture.name.startswith('phase2-') and isinstance(row,dict) and 'after_sha256' in row and '/' in key:
                        self.assertTrue(key not in expected or expected[key]==row['after_sha256'],key)
                        expected[key]=row['after_sha256']
                    else:collect(row)
            collect(d)
        self.assertGreater(len(expected),300)
        for revisions in (DAY196_REVISED_AUTHORITIES, SUNCREST262_REVISED_AUTHORITIES, CHARACTER_SHEET_REVISIONS, YEAR851_REVISED_AUTHORITIES, YEAR852_REVISED_AUTHORITIES, DRAGON_REFERENCE_REVISIONS, TWIN_SWORD_REVISIONS, YEAR852_CLOSE_REVISIONS, YEAR853_REVISIONS):
            for path, revision in revisions.items():
                if path in expected:
                    self.assertEqual(expected[path], revision['before_sha256'], path)
                expected[path] = revision['after_sha256']
        for path,digest in expected.items():
            with self.subTest(path=path):self.assertEqual(hashlib.sha256((ROOT/path).read_bytes()).hexdigest(),digest)

    def test_original_autonomy_payloads_and_revision_evidence(self):
        f=json.loads((ROOT/'tests/fixtures/phase2-07-preservation.json').read_text())
        for path,old in f['legacy_autonomy_payloads'].items():
            with self.subTest(path=path):
                d=json.loads(re.search(r'```json\n(.*?)\n```',(ROOT/path).read_text(),re.S)[1])
                d.pop('autonomy_design',None);d.pop('approved_autonomy_design',None);self.assertEqual(d,old)
                r=f['authorized_owner_revisions'][path];self.assertNotEqual(r['before_sha256'],r['after_sha256'])

    def test_no_historical_evidence_removed(self):
        f=json.loads((ROOT/'tests/fixtures/phase2-07-preservation.json').read_text())
        for path in f['unchanged_sha256']:
            with self.subTest(path=path):self.assertTrue((ROOT/path).is_file())
        self.assertEqual(len(f['authorized_owner_revisions']),6)
        self.assertTrue(any(p.startswith('archive/') for p in f['unchanged_sha256']))
