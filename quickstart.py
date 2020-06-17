from linkedlist import LinkedList
from linkedlist import Element
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)

print(ll.get_position(3).value)
# Test insert
ll.insert(e4, 3)
# Should print 4 now
print(ll.get_position(3).value)
# Test delete
ll.delete(1)
# Should print 2 now
print(ll.get_position(1).value)
# Should print 4 now
print(ll.get_position(2).value)
# Should print 3 now
print(ll.get_position(3).value)

# for stack
from stack import Element, LinkedList, Stack

e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)
stack = Stack(e1)
#
# # Test stack functionality
stack.push(e2)
stack.push(e3)
print(stack.pop().value)

# For Queues
# Setup
from queue import Queue
q = Queue(1)
q.enqueue(2)
q.enqueue(3)

# Test peek
# Should be 1
print(q.peek())

# Test dequeue
# Should be 1
print(q.dequeue())

# Test enqueue
q.enqueue(4)
# Should be 2
print(q.dequeue())
# Should be 3
print(q.dequeue())
# Should be 4
print(q.dequeue())
q.enqueue(5)
# Should be 5
print(q.peek())