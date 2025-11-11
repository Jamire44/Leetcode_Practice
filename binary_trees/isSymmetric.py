from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

one = Node("1")
two = Node("2")
twor = Node("2")
three = Node("3")
four = Node("4")
fourr = Node("4")
threer = Node("3")

one.left = two
one.right = twor
two.left = None
two.right = three
twor.left = None
twor.right = threer

def sort(root: Node):
    if not root:
        return None
    
    left_counter = 0
    right_counter = 0
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

def isSym(root: Node):
    q = deque([(root.left, root.right)])
    while q:
        l,r = q.popleft()
        if not l and not r:
            continue
        if not l or not r:
            return False
        if l.val != r.val:
            return False
        q.append((l.left, r.right))
        q.append((l.right, r.left))
    return True