graph = {
    "A": ["B", "C", "D"],
    "B": ["A","E"],
    "C": ["D", "E"],
    "D": [],
    "E": []
}

# recursive vs iterative approach
visited = []


def dfs(graph, visited, node):
    if (node not in visited):
        visited.append(node)
    for neighbour in graph[node]:
        if (neighbour not in visited):
            visited.append(neighbour)
            dfs(graph, visited, neighbour)
    return visited


print("fThis is the final visited list in dfs {}", dfs(graph, visited, "A"))
