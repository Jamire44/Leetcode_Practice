graph = {
    'a': ['b', 'c'],
    'b': ['d'],
    'c': ["e"],
    'd': ['f'],
    'e': [],
    'f': []   
}

def depth_first_traversal(graph: dict[str, list[str]], source: str):
    elems = []
    stack = [source]
    while(stack):
        curr = stack.pop()
        elems.append(curr)
        for neighbour in reversed(graph[curr]):
            stack.append(neighbour)
    return elems

print(depth_first_traversal(graph, 'a')) # abdfce

def depth_first_recursively(graph: dict[str, list[str]], source: str):
    arr = []
    arr.append(source)
    for neighbour in graph[source]:
        depth_first_recursively(graph, neighbour)
    return arr

print(depth_first_recursively(graph, 'a')) # abdfce
# print(depth_first_traversal(graph, 'a')) # abdfce