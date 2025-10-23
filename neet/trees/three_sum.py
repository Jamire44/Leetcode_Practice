from collections import deque

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

a = Node(3)
b = Node(11)
c = Node(4)
d = Node(4)
e = Node(2)
f = Node(1)

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

# def three_sum(root: Node) -> int:
#     if root is None:
#         return 0
#     return root.value + three_sum(root.left) + three_sum(root.right)

# print(three_sum(a))
def threeSum(root: Node) -> int:
    if root is None: return 0
    total = 0
    queue = deque([root])
    while(queue):
        curr = queue.popleft()
        total += curr.value
        if curr.left:
            queue.append(curr.left)
        if curr.right:
            queue.append(curr.right)
        
    return total

print(threeSum(a))