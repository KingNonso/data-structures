from collections import deque

""" binary tree node"""
class Node:
    def __init__(self, data):
        self.data = data
        self.right_child = None
        self.left_child = None


class Tree:
    def __init__(self):
        self.root_node = None

    def find_min(self):
        current = self.root_node
        while current.left_child:
            current = current.left_child
        return current

    def find_max(self):
        current = self.root_node
        while current.right_child:
            current = current.right_child
        return current

    def insert(self, data):
        node = Node(data)
        if self.root_node is None:
            self.root_node = node
        else:
            current = self.root_node
            parent = None
            while True:
                parent = current
                if node.data < current.data:
                    current = current.left_child
                    if current is None:
                        parent.left_child = node
                        return
                else:
                    current = current.right_child
                    if current is None:
                        parent.right_child = node
                        return

    def get_node_with_parent(self, data):
        parent = None
        current = self.root_node
        if current is None:
            return (parent, None)
        while True:
            if current.data == data:
                return (parent, current)
            elif current.data > data:
                parent = current
                current = current.left_child
            else:
                parent = current
                current = current.right_child
        return parent, current

    def remove(self, data):
        parent, node = self.get_node_with_parent(data)

        if parent is None and node is None:
            return False

        # Get children count
        children_count = 0

        if node.left_child and node.right_child:
            children_count = 2
        elif (node.left_child is None) and (node.right_child is None):
            children_count = 0
        else:
            children_count = 1

        if children_count == 0:
            if parent:
                if parent.right_child is node:
                    parent.right_child = None
                else:
                    parent.left_child = None
            else:
                self.root_node = None
        elif children_count == 1:
            next_node = None
            if node.left_child:
                next_node = node.left_child
            else:
                next_node = node.right_child

            if parent:
                if parent.left_child is node:
                    parent.left_child = next_node
                else:
                    parent.right_child = next_node
            else:
                self.root_node = next_node
        else:
            parent_of_leftmost_node = node
            leftmost_node = node.right_child
            while leftmost_node.left_child:
                parent_of_leftmost_node = leftmost_node
                leftmost_node = leftmost_node.left_child
            node.data = leftmost_node.data
            if parent_of_leftmost_node.left_child == leftmost_node:
                parent_of_leftmost_node.left_child = leftmost_node.right_child
            else:
                parent_of_leftmost_node.right_child = leftmost_node.right_child

    def search(self, data):
        current = self.root_node
        while True:
            if current is None:
                return None
            elif current.data is data:
                return data
            elif current.data > data:
                current = current.left_child
            else:
                current = current.right_child
        return current

    def inorder(self, root_node):  # depth-first tree traversal
        current = root_node
        if current is None:
            return
        self.inorder(current.left_child)
        print(current.data)
        self.inorder(current.right_child)

    def preorder(self, root_node):  # depth-first tree traversal
        current = root_node
        if current is None:
            return
        print(current.data)
        self.preorder(current.left_child)
        self.preorder(current.right_child)

    def postorder(self, root_node):  # depth-first tree traversal
        current = root_node
        if current is None:
            return
        self.postorder(current.left_child)
        self.postorder(current.right_child)
        print(current.data)

    def breadth_first_traversal(self):
        list_of_nodes = []
        traversal_queue = deque([self.root_node])
        while len(traversal_queue) > 0:
            node = traversal_queue.popleft()
            print('dq', node.data)
            list_of_nodes.append(node.data)

            if node.left_child:
                traversal_queue.append(node.left_child)

            if node.right_child:
                traversal_queue.append(node.right_child)
        return list_of_nodes


""" build up a tree for an expression written in postfix notation """


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

def calc(node):  #evaluate the expression
    if node.data is "+":
        return calc(node.left) + calc(node.right)
    elif node.data is "-":
        return calc(node.left) - calc(node.right)
    elif node.data is "*":
        return calc(node.left) * calc(node.right)
    elif node.data is "/":
        return calc(node.left) / calc(node.right)
    else:
        return node.data

""" Balancing braces in a sentence
"""
from pybook.stack import Stack

expr = "4 5 + 5 3 - *".split()
stack = Stack()
for term in expr:
    if term in "+-*/":
        node = TreeNode(term)
        node.right = stack.pop()
        node.left = stack.pop()
    else:
        node = TreeNode(int(term))
    stack.push(node)

# root = stack.pop()
# result = calc(root)
# print(result)
# n1 = Node("root node")
# n2 = Node("left child node")
# n3 = Node("right child node")
# n4 = Node("left grandchild node")
# n1.left_child = n2
# n1.right_child = n3
# n2.left_child = n4
#
# current = n1
# while current:
#     print(current.data)
tree = Tree()
tree.insert(5)
tree.insert(2)
tree.insert(7)
tree.insert(9)
tree.insert(1)
print('bfs', tree.breadth_first_traversal())
print(tree.root_node.data)
# for i in range(1, 10):
#     found = tree.search(i)
#     print("{}: {}".format(i, found))