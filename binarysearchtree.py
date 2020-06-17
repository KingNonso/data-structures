class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        new_val = Node(new_val)
        root = self.root
        if root.value > new_val.value:
            if root.left:
                self.fill_in(root.left, new_val, side='left')
            else:
                root.left = new_val
        else:
            if root.right:
                self.fill_in(root.right, new_val, side='right')
            else:
                root.right = new_val

    def fill_in(self, node, val, side='left'):
        if side == 'left':
            if node.left:
                if node.left.value > val.value:
                    self.fill_in(node.left, val, side)
                else:
                    self.fill_in(node.left, val, side='right')
            else:
                node.left = val
        else:
            if node.right:
                if node.right.value > val.value:
                    self.fill_in(node.right, val, side='left')
                else:
                    self.fill_in(node.right, val, side)
            else:
                node.right = val

    def search(self, find_val):
        current = self.root
        while current:
            if current.value == find_val:
                return True

            if current.value > find_val:
                current = current.right if current.right else False
            else:
                current = current.left if current.right else False
        return False


# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

# Check search
# Should be True
print(tree.search(4))
# Should be False
print(tree.search(6))