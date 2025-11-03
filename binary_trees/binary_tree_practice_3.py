from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def traverse_recursively(node: Node):
    if not node:
        return []

    return [node.val] + traverse_recursively(node.left) + traverse_recursively(node.right)

def traverse_preorder_iter(root: Node):
    if not root:
        return []
    stack = [root]
    values = []
    while stack:
        node = stack.pop()
        values.append(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return values

def traverse_BFS(root: Node):
    if not root:
        return []

    queue = deque([root])
    values = []

    while queue:
        node = queue.popleft()
        values.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return values
    


a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

print(traverse_BFS(a))

#       a
#     b   c
#   d  e    f

# Pre means before, val, left, right -> [1,2,4,5,3,10]