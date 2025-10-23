from collections import deque

edges = [
    ['w','x'],
    ['x','y'],
    ['z','y'],
    ['z','v'],
    ['w','v']
]

def shortest_path(edges, a, b):

    visited = set()
    graph = makeGraph(edges)
    queue = deque([a, 0])

    while queue:
        [node, dist] = queue.popleft()
        if node == b:
            return dist
        for nei in graph:
            if nei not in visited:
                visited.add(nei)
                queue.append([nei, dist + 1])

    return -1

def makeGraph(edges):

    graph = {}

    for edge in edges:
        graph[x,y] = edge
    
    if not graph[x]: []
    if not graph[y]: []

    graph[a].append(b)
    graph[b].append(a)

    return graph

