def rotate90clockwise(matrix):
    row = len(matrix)
    for i in range(row):
        for j in range(i):
            matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]

    for r in range(row):
        matrix[r].reverse()
    return matrix


matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(rotate90clockwise(matrix))