from collections import deque

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

a = Node(3)
b = Node(11)
c = Node(4)
d = Node(4)
e = Node(2)
f = Node(1)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

    #     a
    #    / \
    #   b   c
    #  / \   \
    # d   e   f

def tree_min(root: Node):
    if root is None: return float("inf")
    return min(root.value, tree_min(root.left), tree_min(root.right))

print(tree_min(a))