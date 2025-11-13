from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

three = Node(3)
nine = Node(9)
twenty = Node(20)
fifteen = Node(15)
seven = Node(7)

three.left = nine
three.right = twenty
twenty.left = fifteen
twenty.right = seven

def averageOfLevels(root: Node):
    if not root:
        return []

    values = []
    q = deque([root])

    while q:
        avg = 0
        length_of_level = len(q)
        for _ in range(length_of_level):
            node = q.popleft()
            avg += node.val

            if node.left:
                q.append(node.right)
            if node.left:
                q.append(node.left)

        values.append(avg/length_of_level)
    return values

print(averageOfLevels(three))