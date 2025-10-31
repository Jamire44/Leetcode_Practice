class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.val)
    
A = Node(1)
B = Node(2)
C = Node(3)
D = Node(4)
E = Node(5)
F = Node(10)

A.left = B
A.right = C
B.left = D
B.right = E
C.left = F


def pre_order(node: Node):
    if not node:
        return
    
    print(node)
    pre_order(node.left)
    pre_order(node.right)


def inorder(node: Node):
    if not node:
        return
    
    inorder(node.left)
    print(node)
    inorder(node.right)


def post_order(node: Node):
    if not node:
        return

    inorder(node.left)
    inorder(node.right)
    print(node)
    

def pre_order_iterative(root: Node):
    stack = [root]

    while stack:
        node = stack.pop()
        print(node.val)
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)

def inorder_iter(root: Node):
    stack = []
    result = []
    curr = root

    while curr or stack:

        # Going left
        while curr:
            stack.append(curr)
            curr = curr.left
        
        # Add stacks most recent
        curr = stack.pop()
        result.append(curr)

        curr = curr.right
    
    


pre_order_iterative(A)