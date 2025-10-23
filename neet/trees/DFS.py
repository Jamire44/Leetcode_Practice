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


def depthFirstSearch(root: Node):

    if(root == None): return []

    result = []
    stack = [ root ]
    while (len(stack) > 0):
        curr = stack.pop()
        result.append(curr.value)

        if curr.right:
            stack.append(curr.right)
        if curr.left:
            stack.append(curr.left)

    return result
print(depthFirstSearch(a))