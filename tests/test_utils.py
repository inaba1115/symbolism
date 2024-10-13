import unittest

from symbolism.utils import sec_to_tick, tick_to_sec


class TestUtil(unittest.TestCase):
    def test_sec_to_tick(self):
        self.assertEqual(sec_to_tick(10.0), 9600)

    def test_tick_to_sec(self):
        self.assertAlmostEqual(tick_to_sec(9600), 10.0)
