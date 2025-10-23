from collections import deque
    
def has_path(graph: dict[str, list[str]], src: str, dst: str, visted = None):
    if visted is None:
        visited = set()

    if src == dst:
        return True
    if src in visted:
        return False
    
    visited.add(src)

    for neighbours in graph[src]:
        if(has_path(graph, neighbours, dst, visited) == True):
            return True
    return False

# print(has_path(graph, 'a', 'l'))

def breadth_has_path(graph: dict[str, list[str]], src: str, dst: str, visited=None):
    queue = deque([src])
    visited = set()
    while(queue):
        curr = queue.popleft()
        if curr in visited:
            continue
        visited.add(curr)
        if curr == dst:
            return True
        for neighbours in graph[curr]:
            queue.append(neighbours)
    return False

graph = {
    'a': ['b', 'c'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': []
}

print(breadth_has_path(graph, 'a', 'b'))  # True
print(breadth_has_path(graph, 'a', 'f'))  # True
print(breadth_has_path(graph, 'c', 'b'))  # False
