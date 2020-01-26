from collections import deque

# Complete the isBalanced function below.
def isBalanced(s):
    stack = deque()
    for b in s:
        if b in ('{', '[', '('):
            stack.append(b)

        if b in ('}', ']', ')'):
            if len(stack) > 0:
                last = stack.pop()
                if last is '{' and b is '}':
                    continue
                elif last is '[' and b is ']':
                    continue
                elif last is '(' and b is ')':
                    continue
                else:
                    return 'NO'
            else:
                return 'NO'
    if len(stack) > 0:
        return 'NO'
    else:
        return 'YES'


sl = (
    "{(foo)(bar)}[hello](((this)is)a)test",
    "{(foo)(bar)}[hello](((this)is)atest",
    "{(foo)(bar)}[hello](((this)is)a)test))"
)
for s in sl:
    m = isBalanced(s)
    print("{}: {}".format(s, m))
