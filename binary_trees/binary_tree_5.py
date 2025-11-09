from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")
g = Node("g")

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
d.right = g

def preorder_iter(root: Node):
    if not root:
        return []

    values = []
    stack = [root]

    while stack:
        node = stack.pop()
        values.append(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return values

def inorder_iter(root: Node):
    if not root:
        []

    values = []
    stack = []
    node = root

    while node or stack:
        while node:
            stack.append(node)
            node = node.left
        
        node = stack.pop()
        values.append(node.val)

        node = node.right

    return values


def BFS(root: Node):
    q = deque([root])
    values = []
    while q:
        node = q.popleft()
        values.append(node.val)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
    return values        


def postorder_iter(root: Node):
    if not root:
        return []
    
    stack = []
    values = []
    last_visited = None
    node = root

    while node or stack:
        if node:
            stack.append(node)
            node = node.left
        else:
            peek = stack[-1]
            if peek.right and peek.right != last_visited:
                node = peek.right
            else:
                values.append(peek.val)
                last_visited = stack.pop()
                node = None
    return values

print(postorder_iter(a))

#        a
#     b     c
#   d  e   |  f
#  | g | |   | |