"""Reference sheets cover the index and preserve observed resource status."""

from pathlib import Path
import unittest

import yaml

from scripts.character_sheets import HEADING
from scripts.validate import UniqueLoader, read_json

ROOT = Path(__file__).resolve().parents[1]


class CharacterSheetTests(unittest.TestCase):
    def setUp(self):
        self.sheets = {}
        for entry in read_json(ROOT / 'index.json')['entries']:
            if entry['type'] != 'characters':
                continue
            text = (ROOT / entry['path']).read_text()
            with self.subTest(character=entry['id']):
                self.assertEqual(text.count(HEADING), 1)
                block = text.partition(HEADING)[2].strip()
                self.assertTrue(block.startswith('```yaml\n') and block.endswith('\n```'))
                sheet = yaml.load(block[8:-4], Loader=UniqueLoader)['character_sheet']
                self.assertEqual(sheet['id'], entry['id'])
                self.sheets[entry['id']] = sheet

    def test_checkpoint_and_historical_pools_are_distinct(self):
        state = read_json(ROOT / 'state/checkpoint.json')
        for field, value in state['theron'].items():
            self.assertEqual(self.sheets['theron-ashvale'][field], value)
        for ident in ('garrick-vale', 'nyx-thorne', 'lyra-moonvale', 'lyanna-ashvale'):
            with self.subTest(character=ident):
                self.assertIsNone(self.sheets[ident]['hp'])
                self.assertIsNone(self.sheets[ident]['mp'])
                self.assertGreater(self.sheets[ident]['hp_max'], 0)
                self.assertGreater(self.sheets[ident]['mp_max'], 0)

    def test_zero_pools_and_unassessed_values_remain_distinct(self):
        for ident in ('gorren', 'talia-fen', 'rowan-hale'):
            self.assertEqual((self.sheets[ident]['mp'], self.sheets[ident]['mp_max']), (0, 0))
        for ident in ('dalen-reed', 'sera-willow', 'tobin-marsh', 'elowen-briar', 'perrin-oak', 'faye-linden'):
            for field in ('age', 'ancestry', 'hp', 'mp', 'defense'):
                with self.subTest(character=ident, field=field):
                    self.assertIsNone(self.sheets[ident][field])
            rank, level = ('F', 2) if ident in ('dalen-reed','sera-willow','tobin-marsh','elowen-briar') else (None, None)
            self.assertEqual((self.sheets[ident]['rank'], self.sheets[ident]['level']), (rank, level))

    def test_magic_evidence_and_assessment_proposals_preserve_resource_authority(self):
        lyra = self.sheets['lyra-moonvale']
        self.assertIsNone(lyra['mp'])
        self.assertEqual(lyra['mp_max'], 190)
        self.assertIn('Coordinated Barrier Casting', lyra['abilities'][0])

        for ident in ('aren-duskwell', 'lethara-mossveil'):
            with self.subTest(character=ident):
                sheet = self.sheets[ident]
                self.assertIsNone(sheet['mp'])
                self.assertIsNone(sheet['mp_max'])
                self.assertTrue(sheet['proposed_assessment']['status'].startswith('Proposed'))

        gorren = self.sheets['gorren']
        self.assertEqual((gorren['mp'], gorren['mp_max']), (0, 0))
        self.assertIn('Controlled Dragon Essence', gorren['abilities'][0])

    def test_each_indexed_character_has_a_distinct_portrait_prompt(self):
        prompts = set()
        for ident, sheet in self.sheets.items():
            with self.subTest(character=ident):
                prompt = sheet['image_generator_prompt']
                profile = sheet['character_design_profile']
                self.assertIn(sheet['name'], prompt)
                self.assertTrue(profile['appearance'])
                self.assertTrue(profile['wardrobe_and_props'])
                self.assertTrue(profile['practice_and_professional_skills'])
                self.assertNotIn(prompt, prompts)
                prompts.add(prompt)
                if 'portrait_reference' in profile:
                    self.assertTrue((ROOT / profile['portrait_reference']).is_file())
                    self.assertIn(profile['portrait_reference'], prompt)

    def test_designs_distinguish_nonmagical_casting_and_sacred_healing(self):
        profiles = {ident: sheet['character_design_profile'] for ident, sheet in self.sheets.items()}
        self.assertEqual(profiles['cedric-vale']['unassessed_stat_proposal']['mp_max'], 0)
        self.assertIn('mp_max', profiles['aren-duskwell']['unassessed_stat_proposal'])
        self.assertNotIn('mp_max', profiles['lethara-mossveil']['unassessed_stat_proposal'])
        self.assertIn('Rare sacred healing is established', profiles['therons-mother']['magic_and_healing'])
        self.assertIn('Personal MP remains 0', profiles['gorren']['magic_and_healing'])
