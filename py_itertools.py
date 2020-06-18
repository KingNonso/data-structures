import operator
from itertools import *

"""
Make an iterator that returns accumulated sums, or accumulated results of other binary functions (specified via the optional func argument).
If func is supplied, it should be a function of two arguments
There are a number of uses for the func argument. It can be set to min() for a running minimum, max() for a running maximum, or operator.mul() for a running product. 
Amortization tables can be built by accumulating interest and applying payment"""
def func(a,b):
    return a-b

print('Summation',list(accumulate([1,2,3,4,5,6,7])))
print('Custom function',list(accumulate([1,2,3,4,5,6,7], func)))
print('Running min',list(accumulate([1,2,3,4,5,6,7], min)))
print('Running max',list(accumulate([1,2,3,4,5,6,7], max)))
print('Running product',list(accumulate([1,2,3,4,5,6,7], operator.mul)))

# Amortize a 5% loan of 1000 with 4 annual payments of 90
cashflows = [1000, -90, -90, -90, -90]
print(list(accumulate(cashflows, lambda bal, pmt: bal*1.05 + pmt)))


