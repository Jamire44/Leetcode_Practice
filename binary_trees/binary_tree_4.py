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

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f


def preorder(root: Node):
    if not root: 
        return []
    return [root.val] + preorder(root.left) + preorder(root.right)


def inorder(root: Node):
    if not root:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)


def postorder(root: Node):
    if not root:
        return []
    
    return postorder(root.left) + postorder(root.right) + [root.val]

def preorder_iter(root: Node):
    if not root:
        return []
    
    stack = [root]
    inorder = []
    while stack:
        node = stack.pop()
        inorder.append(node.val)
        if node.left:
            inorder.append(node.left)
        if node.right:
            inorder.append(node.right)

    return inorder


def inorder_iter(root: Node):
    inorder = []
    stack = []
    node = root

    while stack or node:
        while node:
            stack.append(node)
            node = node.left
        
        node = stack.pop()
        inorder.append(node.val)

        node = node.right

    return inorder

#       A
#     B   C
#   D  E    F

def post_two_stacks(root: Node):
    if not root:
        return []
    
    stack1 = [root]
    stack2 = []
    result = []

    while stack1:
        node = stack1.pop()
        stack2.append(node)

        if node.left:
            stack1.append(node.left)

        if node.right:
            stack1.append(node.right)

    
    while stack2:
        result.append(stack2.pop().val)
    
    return result

def BFS(root: Node):
    q = deque([root])
    bfs = []

    while q:
        node = q.popleft()
        bfs.append(node.val)

        if node.left:
            q.append(node.left)

        if node.right:
            q.append(node.right)
    return bfs

#       A
#     B   C
#   D  E    F

print(BFS(a))
print(preorder(a))
print(inorder_iter(a))
print(post_two_stacks(a))
# print()
# print()
# print()
# print()