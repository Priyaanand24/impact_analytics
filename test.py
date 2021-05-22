import math
from itertools import product


def probability():
    """
    probability function
    :return: n
    """
    n = int(input("Enter N number of days"))

    # Total number of possibility
    sample_space = set(product(['P', 'A'], repeat=n))
    possible_ways = len(sample_space)
    # Total number of possibility eliminating the last day [graduation day]
    no_of_ways = math.factorial(n - 1)
    print("Total Number of possibilities ",no_of_ways)

    # probability of missing the graduation ceremony
    missing_probability = (possible_ways - no_of_ways) / possible_ways
    print("probability missing the graduation ceremony",missing_probability)


probability()
