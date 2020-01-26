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
def has_child(node):
    return True if node.left or node.right else False
def has_both_child(node):
    return True if node.left and node.right else False
def height(root):
    parent = deque([root])
    length = 0
    visited = list()
    while len(parent) > 0:
        node = parent.popleft()
        print('parent', node.info)
        left_child = 0 if not node.left else node.left
        right_child = 0 if not node.right else node.right
        parent_set = [node, left_child, right_child]
        visited.append([node.info, left_child, right_child, length])
        print('parent_set', parent_set)
        print('visited', visited)
        if has_child(node):
            if has_both_child(node):
                # length += 1
                parent.append(node.left)
                parent.append(node.right)
            elif left_child:
                length += 1
                parent.append(node.left)
                # left_child = 0 if not node.left else node.left
                # right_child = 0 if not node.right else node.right
                # child_set = [node, left_child, right_child]
                # print('child_set', child_set)
                # diff = set(child_set).difference(set(parent_set))
                # if diff:
                #     diff.remove(0)
                #     parent.append(list(diff)[-1])

                # print('diff', diff)
            elif right_child:
                length += 1
                parent.append(node.right)
                # node = node.left
                # left_child = 0 if not node.left else node.left
                # right_child = 0 if not node.right else node.right
                # child_set = [node, left_child, right_child]
                # print('child_set', child_set)
                # diff = set(child_set).difference(set(parent_set))
                # if diff:
                #     diff.remove(0)
                #     parent.append(list(diff)[-1])
        else:
            # go back to mother set and pop out a new element
            print(parent)
            continue
    return length


tree = BinarySearchTree()
tree.create(5)
tree.create(2)
tree.create(7)
tree.create(9)
tree.create(1)

print('height', height(tree.root))