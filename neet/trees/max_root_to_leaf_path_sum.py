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

def max_root_sum(root: Node):
    if root.left == None and root.right == None:
        return root.value
    maxchild = max(max_root_sum(root.left), max_root_sum(root.right))
    return root.value + maxchild
    
print(max_root_sum(a))