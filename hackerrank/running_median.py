""" Find the Running Median"""
from collections import deque
def runningMedian(a):
    p = deque(a)
    run = list()
    new = []
    while len(p) > 0:
        t = p.popleft()
        print(t)
        new.append(t)
        s = sorted(new)
        lenght = len(s)
        q, r = divmod(lenght, 2)
        if r < 1:
            h = (s[q] + s[q - 1]) / 2
        else:
            h = s[q]
        run.append(h)
    return run



code = [1,8,10,2,9,3,4,5,6,7]
print(runningMedian(code))