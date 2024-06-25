from collections import deque

def detectACycle(graph):
    visited = set()
    for key in graph.keys():
        if key not in visited:
            if(dfs(graph,key,-1,visited)):
                return True
    return False


def dfs(graph,source,parent,visited):
    visited.add(source)
    for neighbour in graph[source]:
        if neighbour not in visited:
            if(dfs(graph,neighbour,source,visited)):
                return True
        elif neighbour != parent:
            return True
    return False




graph = {
    0: [1, 2],
    1: [0, 2, 3],
    2: [0,1],
    3: [1]
}

print("The given graph has a cycle using dfs :",detectACycle(graph))