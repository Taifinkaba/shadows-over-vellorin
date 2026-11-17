"""The consolidated suite must preserve independent subcase state and failures."""
from pathlib import Path
from types import SimpleNamespace
import tempfile
import unittest
from case_support import isolated_case


class IsolationTests(unittest.TestCase):
    def test_files_attributes_and_failed_cases_restore(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);(root/'one').write_text('original');case=SimpleNamespace(root=root,state={'cp':1})
            with self.assertRaisesRegex(AssertionError,'synthetic failure'):
                with isolated_case(case):
                    (root/'one').unlink();(root/'extra').write_text('extra');case.state['cp']=2
                    raise AssertionError('synthetic failure')
            self.assertEqual((root/'one').read_text(),'original');self.assertFalse((root/'extra').exists());self.assertEqual(case.state,{'cp':1})

    def test_symlink_cannot_write_through_to_external_target(self):
        with tempfile.TemporaryDirectory() as tmp, tempfile.TemporaryDirectory() as outer:
            root=Path(tmp);target=Path(outer)/'outside';target.write_text('external');(root/'one').write_text('original')
            with isolated_case(SimpleNamespace(root=root)):
                (root/'one').unlink();(root/'one').symlink_to(target);(root/'broken').symlink_to(root/'missing')
            self.assertEqual(target.read_text(),'external');self.assertFalse((root/'one').is_symlink())
            self.assertEqual((root/'one').read_text(),'original');self.assertFalse((root/'broken').is_symlink())

    def test_real_checkout_cannot_be_used_as_disposable_fixture(self):
        with self.assertRaisesRegex(ValueError,'disposable'):
            with isolated_case(SimpleNamespace(root=Path(__file__).resolve().parents[1])):pass
