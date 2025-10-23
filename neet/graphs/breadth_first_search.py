from collections import deque
graph = {
    'a': ['b', 'c'],
    'b': ['d'],
    'c': ["e"],
    'd': ['f'],
    'e': [],
    'f': []   
}
    
def breadth_first_traversal(graph: dict[str, list[str]], source: str) -> list[str]:
    values = []
    queue = deque([source])
    while queue:
        curr = queue.popleft()
        values.append(curr)
        for neighbours in reversed(graph[curr]):
            queue.append(neighbours)
    return values
    
print(breadth_first_traversal(graph, 'a'))