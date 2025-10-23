# Qs (double ended queue)
from collections import deque

queue = deque()

# Add right side
queue.append(1)
queue.append(2)
print(queue)

# O(1), unlike a stack, pop left
queue.popleft()
print(queue)

# Add left
queue.appendleft(2)
print(queue)

# Pop right
queue.pop()
print(queue)