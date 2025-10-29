from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None


def tree(root: Node):

    arr = []
    q = deque([root])
    
    while q:
        node = q.popleft()
        arr.append(node.val)

        if node.left:
            q.append(node.left)

        if node.right:
            q.append(node.right)
    print(arr)


root = Node(1)
root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.left.right = Node(5)

root.right.left = Node(6)
root.right.right = Node(7)

tree(root)