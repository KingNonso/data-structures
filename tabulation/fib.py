# Fibonnacci number implementation in Python

def fib(n):
    numbers = [0] * (n + 3)
    start = 0
    numbers[1] = 1
    while start <= n:
        current = numbers[start]
        numbers[start + 1] += current
        numbers[start + 2] += current
        start += 1
    # print(numbers)
    return numbers[n]


print(fib(6)) # 8
print(fib(7)) # 13
print(fib(8)) # 21
print(fib(50)) # 12586269025


