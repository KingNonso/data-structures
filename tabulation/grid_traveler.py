# the grid traveler problem in python
from itertools import repeat
import numpy

def grid_traveler(m, n):
    # initialize a non-identical list of lists
    # outer = numpy.empty((5,0)).tolist()
    # outer = [[0 for i in range(n + 2)] for i in range(m + 2)]
    outer = [[0 for x in repeat(None, n + 1)] for x in repeat(None, m + 1)]
    outer[1][1] = 1
    x, y = 0, 0
    while x <= m:
        while y <= n:
            current = outer[x][y]
            if (x + 1) <= m: outer[x+1][y] += current
            if (y + 1) <= n: outer[x][y+1] += current
            y = y + 1
        x, y = x + 1, 0  # there is need to reset y to 0
    return outer[m][n]


print(grid_traveler(3, 3))
print(grid_traveler(4, 5))
print(grid_traveler(6, 7))
print(grid_traveler(18, 18))


