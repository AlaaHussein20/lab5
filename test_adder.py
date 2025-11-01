import unittest
from adder import add

class TestAdder(unittest.TestCase):
    def test_add_integers(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_negatives(self):
        self.assertEqual(add(-1, -1), -2)

    def test_add_floats(self):
        self.assertAlmostEqual(add(1.5, 2.5), 4.0, places=1)

if __name__ == "__main__":
    unittest.main()
