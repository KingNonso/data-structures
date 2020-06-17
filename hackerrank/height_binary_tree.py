"""Tree: Height of a Binary Tree
The height of a binary tree is the number of edges
 between the tree's root and its furthest leaf"""
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


def height(root):
    if root is None:
        return -1
    left_node = height(root.left)
    right_node = height(root.right)

    return 1 + max(left_node, right_node)


tree = BinarySearchTree()
tree.create(5)
tree.create(2)
tree.create(7)
tree.create(9)
tree.create(1)

print('height', height(tree.root))