''' Recursion '''
def factorial(n):
    if n == 0:
        return 1
    f = n * factorial(n-1)
    print(f)
    return f

factorial(4)

''' Backtracking '''
def bitStr(n, s):
    var = []
    if n == 1: return s
    # return [ digit + bits for digit in bitStr(1,s) for bits in bitStr(n-1, s) ]
    for bits in bitStr(n - 1, s):
        print(bits, 'bits')
        for digit in bitStr(1, s):
            print(digit, ' dig')
            var += [digit + bits]


    return var

# print(bitStr(3, 'abc'))


''' Karatsuba (Multiplication Algo) '''
from math import log10, ceil
def karatsuba(x,y):
    if x < 10 or y < 10:
        return x*y

    # sets n, the no of digits in the highest input number
    n = max(int(log10(x)+1), int(log10(y)+1))
    print('n', n)

    # rounds up n/2
    n_2 = int(ceil(n/2.0))
    print('n_2', n_2)
    # adds 1 if n is uneven
    n = n if n % 2 == 0 else n + 1
    print('even', n)

    # splits the input numbers
    a, b = divmod(x, 10**n_2)
    c, d = divmod(y, 10**n_2)
    print(a,b,c,d)

    # applies the three recursive steps
    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    ad_bc = karatsuba((a+b), (c+d)) - ac - bd
    print(ac, bd, ad_bc)

    # performs the multiplication
    return (((10**n)*ac) + bd + ((10**n_2)*(ad_bc)))


import random
def test():
    for i in range(1):
        x = random.randint(1, 10 ** 5)
        y = random.randint(1, 10 ** 5)
        print('x', x)
        print('y', y)
        expected = x * y
        result = karatsuba(x, y)
        if result != expected:
            return ("failed")
    return ('ok')
print(test())

