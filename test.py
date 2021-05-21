import math
from itertools import product

n = int(input("Enter N number of days"))

# Total number of possibility
sample_space = set(product(['P', 'A'], repeat=n))
possible_ways = len(sample_space)
print(sample_space)

# Total number of possibility eliminating the last day [graduation day]
no_of_ways = math.factorial(n-1)
print(no_of_ways)

# probability of missing the graduation ceremony
missing_probability = (possible_ways - no_of_ways) / possible_ways
perfect = missing_probability * 100
print(str(round(perfect, 0)) + '%')
