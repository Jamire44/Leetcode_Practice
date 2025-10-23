from collections import deque

edges = [
    ['i', 'j'],
    ['k', 'i'],
    ['m', 'k'],
    ['k', 'l'],
    ['o', 'n']
]

def undirectedPath(edges, nodeA, nodeB):
    visited = set()
    graph = buildGraph(edges)
    return hasPath(graph, nodeA, nodeB, visited)


def buildGraph(edges):

    graph = {}

    for edge in edges:
        [ a, b ] = edge

        if a not in graph:
            graph[a] = []

        if b not in graph:
            graph[b] = []

        graph[a].append(b)  # add b as neighbor of a
        graph[b].append(a)


    return graph

def hasPath(graph, src, dst, visited):
    if src == dst:
        return True
    if src in visited:
        return False

    visited.add(src)

    for neighbour in graph[src]:
        if hasPath(graph, neighbour, dst, visited) == True:
            return True
    return False
        
    

print(undirectedPath(edges, 'j', 'z'))