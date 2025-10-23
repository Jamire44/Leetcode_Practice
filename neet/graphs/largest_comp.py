graph = {
    0: [8,1,5],
    1: [0],
    5: [0,8],
    8: [0,5],
    2: [3,4],
    3: [2,4],
    4: [3,2]
}

def largest(graph):

    longest = 0
    visited = set()
    for node in graph:
        size = explore(graph, node, visited)
        if size > longest:
            longest = size
    return longest

def explore(graph, curr, visited):
    if curr in visited:
        return 0
    visited.add(curr)
    size = 1

    for nei in graph[curr]:
        size += explore(graph, nei, visited)

    return size

print(largest(graph))