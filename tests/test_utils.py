import unittest

from symbolism.utils import sec_to_tick


class TestUtil(unittest.TestCase):
    def test_sec_to_tick(self):
        self.assertEqual(sec_to_tick(10.0), 9600)
