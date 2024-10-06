import unittest

from symbolism.scale import Scale


class TestScale(unittest.TestCase):
    def test_map(self):
        s = Scale(0, [0, 5])
        self.assertEqual(s.map(-3), -19)
        self.assertEqual(s.map(-2), -12)
        self.assertEqual(s.map(-1), -7)
        self.assertEqual(s.map(0), 0)
        self.assertEqual(s.map(1), 5)
        self.assertEqual(s.map(2), 12)
        self.assertEqual(s.map(3), 17)

        s = Scale(2, [0, 5])
        self.assertEqual(s.map(-3), -17)
        self.assertEqual(s.map(-2), -10)
        self.assertEqual(s.map(-1), -5)
        self.assertEqual(s.map(0), 2)
        self.assertEqual(s.map(1), 7)
        self.assertEqual(s.map(2), 14)
        self.assertEqual(s.map(3), 19)
