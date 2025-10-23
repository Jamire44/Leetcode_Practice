from collections import deque

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')

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

def treeIncludes(root: Node, target: str) -> bool:
    if root is None: return False
    if root.value is target: return True

    return treeIncludes(root.left, target) or treeIncludes(root.right, target)
    


print(treeIncludes(a, "b"))