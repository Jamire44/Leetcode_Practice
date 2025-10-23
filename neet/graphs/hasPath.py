from collections import deque
graph = {
    'f': ['g','i'],
    'g': ['h'],
    'h': [],
    'i': ['g','k'],
    'j': ['i'],
    'k': []
}

# def hasPath(graph, src, dst):
#     if src == dst:
#         return True
#     for neighbour in graph[src]:
#         if hasPath(graph, neighbour, dst) == True:
#             return True
#     return False
# print(hasPath(graph, 'f', 'e'))

def breadth_first_has_path(graph, src, dst):
    if src not in graph or dst not in graph:
        return False
    
    visited = set()
    q = deque([src])

    while q:
        curr = q.popleft()

        if curr == dst:
            return True
        if curr in visited:
            continue

        visited.add(curr)

        for nei in graph[curr]:
            q.append(nei)
    return False

print(breadth_first_has_path(graph, 'f', 'l'))  # False
print(breadth_first_has_path(graph, 'f', 'k'))  # True