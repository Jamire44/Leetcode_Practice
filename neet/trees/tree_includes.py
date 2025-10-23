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
    queue = deque([root])
    while(queue):
        curr = queue.popleft()
        if curr.value == target:
            return True
        if curr.left:
            queue.append(curr.left)
        if curr.right:
            queue.append(curr.right)
    return False


print(treeIncludes(a, "bc"))