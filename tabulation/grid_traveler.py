# the grid traveler problem in python
from itertools import repeat
import numpy

def grid_traveler(m, n):
    # initialize a non-identical list of lists
    # outer = numpy.empty((5,0)).tolist()
    # outer = [[0 for i in range(n + 2)] for i in range(m + 2)]
    outer = [[0 for x in repeat(None, n + 1)] for x in repeat(None, m + 1)]
    outer[1][1] = 1

    print(outer)
    pass

print(grid_traveler(2, 3))
# print(grid_traveler(4, 5))
# print(grid_traveler(6, 7))
# print(grid_traveler(18, 18))


