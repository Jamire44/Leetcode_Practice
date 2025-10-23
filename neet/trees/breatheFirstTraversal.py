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

def breadFirstTrav(root: Node):
    if root is None:
        return []
    
    values = []
    queue = deque([root])

    while queue:
        curr = queue.popleft()
        values.append(curr.value)

        if curr.left:
            queue.append(curr.left)
        if curr.right:
            queue.append(curr.right)
    

    return values

print(breadFirstTrav(a))