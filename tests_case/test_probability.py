import unittest
import math
from itertools import product


class TestProb(unittest.TestCase):
    def test_probability(self):
        n = 5
        sample_space = set(product(['P', 'A'], repeat=5))
        possible_ways = len(sample_space)
        no_of_ways = math.factorial(5 - 1)
        self.assertEqual((possible_ways - no_of_ways) / possible_ways, 0.25)


if __name__ == '__main__':
    unittest.main()
