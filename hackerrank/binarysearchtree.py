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

from collections import deque
def height(root):
    parent = root
    length = 0
    has_children = False if (not parent.left) or (not parent.right) else True
    visited = list()
    matrix = list()
    queue = deque([root])
    heights = []
    node = queue.popleft()
    while has_children:
        current = node
        print('current', current.info)
        verse = [node.info, node.left, node.right, length]
        matrix.append(verse)
        if node.left:
            length += 1
            current = node.left
            visited.append(current)
        elif node.right:
            length += 1
            current = node.right
            visited.append(current)
        has_children = False if (not current.left) or (not current.right) else True


tree = BinarySearchTree()
tree.create(5)
tree.create(2)
tree.create(7)
tree.create(9)
tree.create(1)
#
# print('root', tree.root)
# print(height(tree.root))