from case_support import isolated_case, validate_scope
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
        for name in ('entities', 'archive', 'state', 'changes', 'docs', 'governance'):
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
            validate_scope(self.root, 'travel')


    def test_causality_and_continuity_1(self):
        with self.subTest(case='test_no_canon_route_through_proposal'), isolated_case(self):
            self.reject('route-ashvale-eastrun', lambda d: d.update(destination='elyndor'), 'canonical route through proposed')
        with self.subTest(case='test_no_silent_route_promotion'), isolated_case(self):
            self.reject('route-caelthorne-rivermere', lambda d: d.update(classification='CONFIRMED CANON'), 'metadata mismatch')
        with self.subTest(case='test_repository_preserves_supported_reports'), isolated_case(self):
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
        with self.subTest(case='test_historical_duration_cannot_change'), isolated_case(self):
            self.reject('route-waystation-brackenford', lambda d: d['durations'][0].update(minimum=30), 'contradicts historical source')
        with self.subTest(case='test_historical_mode_cannot_change'), isolated_case(self):
            self.reject('route-eastrun-briarfall', lambda d: d['durations'][0].update(mode='wagon'), 'contradicts historical source')

    def test_continuity_and_contracts_and_schema_2(self):
        cases = [
            ('test_proposed_duration_cannot_claim_history', 'route-caelthorne-rivermere', lambda d: d['durations'][0].update(basis='historical-report'), 'basis mismatch'),
            ('test_unsupported_exact_historical_mileage', 'route-ashvale-eastrun', lambda d: d.update(distance=dict(value=12, unit='miles', basis='verified')), 'unsupported historical distance'),
            ('test_historical_endpoints_cannot_be_reassigned', 'route-ashvale-eastrun', lambda d: d.update(destination='blackthorn-watch'), 'endpoints not supported'),
            ('test_missing_registry_entry', 'travel-routes', lambda d: d['route_ids'].pop(), 'coverage mismatch'),
            ('test_character_cannot_be_endpoint', 'route-ashvale-eastrun', lambda d: d.update(start='theron-ashvale'), 'invalid route endpoint'),
        ]
        for case, arg0, arg1, arg2 in cases:
            with self.subTest(case=case), isolated_case(self):
                self.reject(arg0, arg1, arg2)

    def test_contracts_and_schema_3(self):
        cases = [
            ('test_missing_endpoint', 'route-ashvale-eastrun', lambda d: d.update(destination='missing-town'), 'invalid route endpoint'),
            ('test_self_loop', 'route-ashvale-eastrun', lambda d: d.update(destination=d['start']), 'identical route endpoints'),
            ('test_continent_is_not_road_endpoint', 'route-caelthorne-elyndor', lambda d: d.update(destination='aethoria'), 'continent road endpoint'),
            ('test_no_silent_node_promotion', 'world-geography', lambda d: next((n for n in d['nodes'] if n['id'] == 'elyndor')).update(classification='CONFIRMED CANON'), 'metadata mismatch'),
            ('test_cannot_promote_parent_continent', 'world-geography', lambda d: next((n for n in d['nodes'] if n['id'] == 'vellorin'))['parents'][0].update(classification='CONFIRMED CANON'), 'canonical containment through proposed'),
        ]
        for case, arg0, arg1, arg2 in cases:
            with self.subTest(case=case), isolated_case(self):
                self.reject(arg0, arg1, arg2)

    def test_contracts_and_schema_4(self):
        with self.subTest(case='test_containment_cycles'), isolated_case(self):
            def change(d):
                next(n for n in d['nodes'] if n['id']=='aethoria')['parents'].append(dict(id='vellorin', classification='PROPOSED', source_refs=['changes/chronicles/world-geography-travel-design.md']))
            self.reject('world-geography', change, 'containment cycle')
        with self.subTest(case='test_intermediate_must_be_real_settlement'), isolated_case(self):
            self.reject('route-caelthorne-rivermere', lambda d: d.update(intermediate_settlements=['sovereign-nexus']), 'invalid intermediate location')
        with self.subTest(case='test_duration_range_and_boolean_rejected'), isolated_case(self):
            for value in (-1, True, 2.5):
                with self.subTest(value=value):
                    self.edit('route-caelthorne-rivermere', lambda d: d['durations'][0].update(minimum=value))
                    with self.assertRaisesRegex(ValidationError, 'invalid duration range'):
                        validate(self.root)
        with self.subTest(case='test_reversed_duration_range'), isolated_case(self):
            self.reject('route-caelthorne-rivermere', lambda d: d['durations'][0].update(maximum=1), 'invalid duration range')
        with self.subTest(case='test_inaccessible_mode_has_no_duration'), isolated_case(self):
            self.reject('route-eastrun-briarfall', lambda d: d['accessibility'].update(walking=False), 'inaccessible mode')

    def test_contracts_and_schema_5(self):
        with self.subTest(case='test_endpoint_service_not_wayside_claim'), isolated_case(self):
            self.reject('route-waystation-brackenford', lambda d: d['integration_points'][0].update(at_location='ashvale-estate'), 'outside endpoints')
        with self.subTest(case='test_unknown_data_is_valid_and_not_filled'), isolated_case(self):
            route = self.data('route-eastrun-greyhaven-mill')
            self.assertIsNone(route['distance'])
            self.assertEqual(route['durations'], [])
            self.assertIsNone(route['intermediate_settlements'])
            self.assertIsNone(route['toll_requirements'])
            self.assertIn('checkpoint valid', validate(self.root))
        with self.subTest(case='test_unknown_mode_is_not_retroactive_riding'), isolated_case(self):
            self.reject('route-ashvale-eastrun', lambda d: d['durations'][0].update(mode='riding'), 'contradicts historical source')
        with self.subTest(case='test_optimized_validator_rejects_bad_graph'), isolated_case(self):
            self.edit('route-ashvale-eastrun', lambda d: d.update(destination='missing-town'))
            result = subprocess.run([sys.executable, '-O', str(ROOT/'scripts/validate.py'), '--root', str(self.root)], capture_output=True, text=True)
            self.assertEqual(result.returncode, 1)
            self.assertIn('invalid route endpoint', result.stderr)
        with self.subTest(case='test_invalid_duration_unit'), isolated_case(self):
            self.reject('route-caelthorne-rivermere', lambda d: d['durations'][0].update(unit='turnips'), 'invalid duration unit')

    def test_contracts_and_schema_and_identity_6(self):
        with self.subTest(case='test_invalid_classification'), isolated_case(self):
            self.reject('route-caelthorne-rivermere', lambda d: d.update(classification='APPROVED'), 'invalid classification')
        with self.subTest(case='test_unknown_distance_not_zero'), isolated_case(self):
            self.reject('route-caelthorne-rivermere', lambda d: d.update(distance=dict(value=0,unit='miles',basis='proposed-estimate')), 'invalid distance')
        with self.subTest(case='test_partial_framework_rejected'), isolated_case(self):
            p = self.root/'index.json'
            idx = json.loads(p.read_text())
            idx['entries'] = [e for e in idx['entries'] if e['id'] != 'travel-procedure']
            p.write_text(json.dumps(idx))
            (self.root/'entities/rules/travel-procedure.md').unlink()
            with self.assertRaisesRegex(ValidationError, 'missing directory, registry or procedure'):
                validate(self.root)
        with self.subTest(case='test_duplicate_registry_id'), isolated_case(self):
            self.reject('travel-routes', lambda d: d['route_ids'].append(d['route_ids'][0]), 'duplicate route ID')
        with self.subTest(case='test_route_must_be_indexed'), isolated_case(self):
            p = self.root / 'index.json'
            idx = json.loads(p.read_text())
            idx['entries'] = [e for e in idx['entries'] if e['id'] != 'route-ashvale-eastrun']
            p.write_text(json.dumps(idx))
            with self.assertRaisesRegex(ValidationError, 'coverage mismatch'):
                validate(self.root)

    def test_identity_and_resources_7(self):
        with self.subTest(case='test_duplicate_location_node'), isolated_case(self):
            self.reject('world-geography', lambda d: d['nodes'].append(d['nodes'][0]), 'duplicate canonical location/node')
        with self.subTest(case='test_duplicate_canonical_title'), isolated_case(self):
            p = self.root / 'index.json'
            idx = json.loads(p.read_text())
            title = next(e['title'] for e in idx['entries'] if e['id']=='blackthorn-watch')
            next(e for e in idx['entries'] if e['id']=='blackthorn-north-waystation')['title'] = title
            p.write_text(json.dumps(idx))
            with self.assertRaisesRegex(ValidationError, 'duplicate canonical location title'):
                validate(self.root)
        with self.subTest(case='test_false_evidence_quote'), isolated_case(self):
            self.reject('route-eastrun-briarfall', lambda d: d['durations'][0].update(source_quote='~four hours'), 'quote not found')
        with self.subTest(case='test_broken_integration_reference'), isolated_case(self):
            self.reject('route-waystation-brackenford', lambda d: d['integration_points'][0].update(target_id='invented-prison'), 'broken integration reference')
        with self.subTest(case='test_validation_does_not_mutate_campaign_files'), isolated_case(self):
            files = [p for folder in ('state','entities/characters','entities/creatures','entities/items','entities/quests') for p in (self.root/folder).rglob('*') if p.is_file()]
            before = {p: p.read_bytes() for p in files}
            validate(self.root)
            self.assertEqual(before, {p: p.read_bytes() for p in files})
