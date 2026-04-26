import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from solver import find_minimum_beers

class TestBeerSolver(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(find_minimum_beers(2, 2, "YN NY"), 2)

    def test_example_2(self):
        self.assertEqual(find_minimum_beers(6, 3, "YNN YNY YNY NYY NYY NYN"), 2)

    def test_simple_case(self):
        self.assertEqual(find_minimum_beers(3, 2, "YN YN YN"), 1)

if __name__ == "__main__":
    unittest.main()