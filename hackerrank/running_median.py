""" Find the Running Median"""

def runningMedian(a):
    run = []
    new = []
    for i in a:
        new.append(i)
        s = sorted(new)
        lenght = len(s)
        q, r = divmod(lenght, 2)
        if r < 1:
            h = (s[q] + s[q - 1])/2
        else:
            h = s[q]
        run.append(h)
    return run





code = [1,8,10,2,9,3,4,5,6,7]
print(runningMedian(code))