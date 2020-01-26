"""Make a Queue class using a list!
Hint: You can use any Python list method
you'd like! Try to write each one in as
few lines as possible.
Make sure you pass the test cases too!"""


class Queue(object):
    def __init__(self, head=None):
        self.storage = [head]

    def enqueue(self, new_element):
        if self.storage:
            self.storage += [new_element]
        else:
            self.storage = [new_element]
        return self.storage

    def peek(self):
        return self.storage[0]

    def dequeue(self):
        peek = self.peek()
        del self.storage[0]
        return peek



