graph = {
    0: [8,1,5],
    1: [0],
    5: [0,8],
    8: [0,5],
    2: [3,4],
    3: [2,4],
    4: [3,2]
}

def connected_comp(graph):
    visited = set()
    count = 0
    for node in graph:
        if explore(graph, node, visited) == True:
            count+=1
    return count
    


def explore(graph, curr, visited):
    if curr in visited:
        return False
    visited.add(curr)

    for nei in graph[curr]:
        explore(graph, nei, visited)
    return True

print(connected_comp(graph))