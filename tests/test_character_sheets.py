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
            for field in ('age', 'ancestry', 'rank', 'level', 'hp', 'mp', 'defense'):
                with self.subTest(character=ident, field=field):
                    self.assertIsNone(self.sheets[ident][field])
