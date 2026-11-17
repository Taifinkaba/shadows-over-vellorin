"""Mutation tests for graph integrity, evidence preservation and proposal boundaries."""
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import unittest

from scripts.validate import ValidationError, validate

ROOT = Path(__file__).resolve().parents[1]


class TravelTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='vellorin-travel-')
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        for name in ('entities', 'archive', 'state', 'changes'):
            shutil.copytree(ROOT / name, self.root / name)
        shutil.copy2(ROOT / 'index.json', self.root / 'index.json')

    def path(self, ident):
        kind = 'mechanics' if ident in ('world-geography', 'travel-routes') else 'locations'
        return self.root / f'entities/{kind}/{ident}.md'

    def data(self, ident):
        return json.loads(re.search(r'```json\n(.*?)\n```', self.path(ident).read_text(), re.S)[1])

    def edit(self, ident, change):
        p = self.path(ident)
        source = p.read_text()
        m = re.search(r'```json\n(.*?)\n```', source, re.S)
        value = json.loads(m[1])
        change(value)
        p.write_text(source[:m.start(1)] + json.dumps(value, indent=2) + source[m.end(1):])

    def reject(self, ident, change, pattern):
        self.edit(ident, change)
        with self.assertRaisesRegex(ValidationError, pattern):
            validate(self.root)

    def test_repository_preserves_supported_reports(self):
        self.assertIn('checkpoint valid', validate(self.root))
        for ident, minutes, mode in (
            ('route-ashvale-eastrun', 120, 'unknown'),
            ('route-eastrun-briarfall', 180, 'walking'),
            ('route-waystation-brackenford', 35, 'wagon'),
            ('route-brackenford-cottage', 8, 'walking'),
        ):
            d = self.data(ident)['durations'][0]
            self.assertEqual((d['minimum'], d['mode']), (minutes, mode))
        self.assertIsNone(self.data('route-ashvale-eastrun')['durations'][0]['maximum'])

    def test_duplicate_registry_id(self):
        self.reject('travel-routes', lambda d: d['route_ids'].append(d['route_ids'][0]), 'duplicate route ID')

    def test_missing_registry_entry(self):
        self.reject('travel-routes', lambda d: d['route_ids'].pop(), 'coverage mismatch')

    def test_route_must_be_indexed(self):
        p = self.root / 'index.json'
        idx = json.loads(p.read_text())
        idx['entries'] = [e for e in idx['entries'] if e['id'] != 'route-ashvale-eastrun']
        p.write_text(json.dumps(idx))
        with self.assertRaisesRegex(ValidationError, 'coverage mismatch'):
            validate(self.root)

    def test_character_cannot_be_endpoint(self):
        self.reject('route-ashvale-eastrun', lambda d: d.update(start='theron-ashvale'), 'invalid route endpoint')

    def test_missing_endpoint(self):
        self.reject('route-ashvale-eastrun', lambda d: d.update(destination='missing-town'), 'invalid route endpoint')

    def test_self_loop(self):
        self.reject('route-ashvale-eastrun', lambda d: d.update(destination=d['start']), 'identical route endpoints')

    def test_continent_is_not_road_endpoint(self):
        self.reject('route-caelthorne-elyndor', lambda d: d.update(destination='aethoria'), 'continent road endpoint')

    def test_no_canon_route_through_proposal(self):
        self.reject('route-ashvale-eastrun', lambda d: d.update(destination='elyndor'), 'canonical route through proposed')

    def test_no_silent_route_promotion(self):
        self.reject('route-caelthorne-rivermere', lambda d: d.update(classification='CONFIRMED CANON'), 'metadata mismatch')

    def test_no_silent_node_promotion(self):
        self.reject('world-geography', lambda d: next(n for n in d['nodes'] if n['id']=='elyndor').update(classification='CONFIRMED CANON'), 'metadata mismatch')

    def test_cannot_promote_parent_continent(self):
        self.reject('world-geography', lambda d: next(n for n in d['nodes'] if n['id']=='vellorin')['parents'][0].update(classification='CONFIRMED CANON'), 'canonical containment through proposed')

    def test_containment_cycles(self):
        def change(d):
            next(n for n in d['nodes'] if n['id']=='aethoria')['parents'].append(dict(id='vellorin', classification='PROPOSED', source_refs=['changes/chronicles/world-geography-travel-design.md']))
        self.reject('world-geography', change, 'containment cycle')

    def test_duplicate_location_node(self):
        self.reject('world-geography', lambda d: d['nodes'].append(d['nodes'][0]), 'duplicate canonical location/node')

    def test_duplicate_canonical_title(self):
        p = self.root / 'index.json'
        idx = json.loads(p.read_text())
        title = next(e['title'] for e in idx['entries'] if e['id']=='blackthorn-watch')
        next(e for e in idx['entries'] if e['id']=='blackthorn-north-waystation')['title'] = title
        p.write_text(json.dumps(idx))
        with self.assertRaisesRegex(ValidationError, 'duplicate canonical location title'):
            validate(self.root)

    def test_intermediate_must_be_real_settlement(self):
        self.reject('route-caelthorne-rivermere', lambda d: d.update(intermediate_settlements=['sovereign-nexus']), 'invalid intermediate location')

    def test_duration_range_and_boolean_rejected(self):
        for value in (-1, True, 2.5):
            with self.subTest(value=value):
                self.edit('route-caelthorne-rivermere', lambda d: d['durations'][0].update(minimum=value))
                with self.assertRaisesRegex(ValidationError, 'invalid duration range'):
                    validate(self.root)

    def test_reversed_duration_range(self):
        self.reject('route-caelthorne-rivermere', lambda d: d['durations'][0].update(maximum=1), 'invalid duration range')

    def test_historical_duration_cannot_change(self):
        self.reject('route-waystation-brackenford', lambda d: d['durations'][0].update(minimum=30), 'contradicts historical source')

    def test_historical_mode_cannot_change(self):
        self.reject('route-eastrun-briarfall', lambda d: d['durations'][0].update(mode='wagon'), 'contradicts historical source')

    def test_false_evidence_quote(self):
        self.reject('route-eastrun-briarfall', lambda d: d['durations'][0].update(source_quote='~four hours'), 'quote not found')

    def test_proposed_duration_cannot_claim_history(self):
        self.reject('route-caelthorne-rivermere', lambda d: d['durations'][0].update(basis='historical-report'), 'basis mismatch')

    def test_unsupported_exact_historical_mileage(self):
        self.reject('route-ashvale-eastrun', lambda d: d.update(distance=dict(value=12,unit='miles',basis='verified')), 'unsupported historical distance')

    def test_inaccessible_mode_has_no_duration(self):
        self.reject('route-eastrun-briarfall', lambda d: d['accessibility'].update(walking=False), 'inaccessible mode')

    def test_broken_integration_reference(self):
        self.reject('route-waystation-brackenford', lambda d: d['integration_points'][0].update(target_id='invented-prison'), 'broken integration reference')

    def test_endpoint_service_not_wayside_claim(self):
        self.reject('route-waystation-brackenford', lambda d: d['integration_points'][0].update(at_location='ashvale-estate'), 'outside endpoints')

    def test_unknown_data_is_valid_and_not_filled(self):
        route = self.data('route-eastrun-greyhaven-mill')
        self.assertIsNone(route['distance'])
        self.assertEqual(route['durations'], [])
        self.assertIsNone(route['intermediate_settlements'])
        self.assertIsNone(route['toll_requirements'])
        self.assertIn('checkpoint valid', validate(self.root))

    def test_unknown_mode_is_not_retroactive_riding(self):
        self.reject('route-ashvale-eastrun', lambda d: d['durations'][0].update(mode='riding'), 'contradicts historical source')

    def test_optimized_validator_rejects_bad_graph(self):
        self.edit('route-ashvale-eastrun', lambda d: d.update(destination='missing-town'))
        result = subprocess.run([sys.executable, '-O', str(ROOT/'scripts/validate.py'), '--root', str(self.root)], capture_output=True, text=True)
        self.assertEqual(result.returncode, 1)
        self.assertIn('invalid route endpoint', result.stderr)

    def test_validation_does_not_mutate_campaign_files(self):
        files = [p for folder in ('state','entities/characters','entities/creatures','entities/items','entities/quests') for p in (self.root/folder).rglob('*') if p.is_file()]
        before = {p: p.read_bytes() for p in files}
        validate(self.root)
        self.assertEqual(before, {p: p.read_bytes() for p in files})

    def test_historical_endpoints_cannot_be_reassigned(self):
        self.reject('route-ashvale-eastrun', lambda d: d.update(destination='blackthorn-watch'), 'endpoints not supported')

    def test_invalid_duration_unit(self):
        self.reject('route-caelthorne-rivermere', lambda d: d['durations'][0].update(unit='turnips'), 'invalid duration unit')

    def test_invalid_classification(self):
        self.reject('route-caelthorne-rivermere', lambda d: d.update(classification='APPROVED'), 'invalid classification')

    def test_unknown_distance_not_zero(self):
        self.reject('route-caelthorne-rivermere', lambda d: d.update(distance=dict(value=0,unit='miles',basis='proposed-estimate')), 'invalid distance')

    def test_partial_framework_rejected(self):
        p = self.root/'index.json'
        idx = json.loads(p.read_text())
        idx['entries'] = [e for e in idx['entries'] if e['id'] != 'travel-procedure']
        p.write_text(json.dumps(idx))
        (self.root/'entities/rules/travel-procedure.md').unlink()
        with self.assertRaisesRegex(ValidationError, 'missing directory, registry or procedure'):
            validate(self.root)
