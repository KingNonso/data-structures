""" Tree: Level Order Traversal
In level order traversal, we visit the nodes
 level by level from left to right."""
class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""
from collections import deque


def levelOrder(root):
    r = deque([root])
    string = ''
    if root is not None:
        string = str(root.info) + ' '
    while len(r) > 0:
        q = r.popleft()
        if q.left is not None:
            r.append(q.left)
            string += str(q.left.info) + ' '
        if q.right is not None:
            r.append(q.right)
            string += str(q.right.info) + ' '
    print(string)
