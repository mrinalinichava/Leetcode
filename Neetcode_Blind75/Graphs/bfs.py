def bfs(graph, start):
    queue = [start]
    visited = set()
    while(queue):
        node = queue.pop(0)
        visited.add(node)
        for neighbour in graph[node]:
            if(neighbour not in visited):
                queue.append(neighbour)
    return visited


graph = {
    "A": ["B", "C", "D"],
    "B": ["A","E"],
    "C": ["D", "E"],
    "D": [],
    "E": []
}

print("fThis is the final visited list in bfs {}", bfs(graph, "A"))