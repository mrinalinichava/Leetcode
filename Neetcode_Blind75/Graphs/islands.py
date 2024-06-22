def noOfislands(graph):
    rows = len(graph)
    cols = len(graph[0])
    count = 0
    for i in range(rows):
        for j in range(cols):
            if(graph[i][j]== "1"):
                dfs(graph,i,j)
                count = count + 1

    return count


def dfs(graph,i,j):
    if( i< 0 or i>=len(graph) or j< 0 or j>=len(graph[0]) or graph[i][j]== "0"):
        return
    graph[i][j] = "0"
    dfs(graph, i + 1,j )
    dfs(graph, i - 1, j)
    dfs(graph, i , j + 1)
    dfs(graph, i, j - 1)


graph = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

print("fnumber of islands in the graph are {} ", noOfislands(graph))

