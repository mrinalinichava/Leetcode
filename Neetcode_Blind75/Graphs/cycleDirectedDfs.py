def detectCycleDirected(graph):

    visited = set()
    stack = set()
    for node in graph:
        if node not in visited:
            if(dfs(graph,node,visited,stack)):
                return True
    return False



def dfs(graph,node,visited,stack):
    if node in stack:
        return True
    if node in visited:
        return False
    stack.add(node)
    for neighbour in graph[node]:
        if(dfs(graph,neighbour,visited,stack)):
            return True
    stack.remove(node)
    visited.add(node)
    return False


graph = {
    0:[1],
    1:[2],
    2:[3],
    3:[0]
}

print("finding the cycle in a directed graph: ", detectCycleDirected(graph))