from collections import deque

def detectACycle(graph):
    visited = set()
    for key in graph.keys():
        if key not in visited:
            if(bfs(graph,key,visited)):
                return True
    return False


def bfs(graph,source,visited):
    queue = deque([(source,-1)])
    visited.add(source)
    while queue:
        node,parent = queue.popleft()
        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append((neighbour,node))
            elif neighbour != parent:
                return True
    return False




graph = {
    0: [1, 2],
    1: [0, 2, 3],
    2: [0, 1],
    3: [1]
}

print("The given graph has a cycle :",detectACycle(graph))