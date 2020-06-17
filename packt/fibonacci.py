"""The Fibonacci Function with an Iteration"""

def fibonacci_iterative(x):
    number = 1
    previous = 0
    for i in range(x-1):
        current_old = number
        number = number + previous
        previous = current_old
    return number


def fibonacci_recursive(x):
    number = 1
    previous = 0
    current = number + previous

if __name__  == '__main__':
    print(fibonacci_iterative(x))