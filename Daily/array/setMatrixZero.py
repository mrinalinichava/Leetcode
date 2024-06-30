def setMatrixZero(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    rowFlag= [False]*rows
    colFlag = [False]*cols

    for row in range(rows):
        for col in range(cols):
            if(matrix[row][col]==0):
                rowFlag[row]=True
                colFlag[col]=True

    for row in range(rows):
        for col in range(cols):
            if(rowFlag[row] or colFlag[col]):
                matrix[row][col]=0

    return matrix

# optimal solution in o(1) space complexity.

def setMatrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    rowZero = False
    for row in range(rows):
        for col in range(cols):
            if(matrix[row][col]==0):
                matrix[0][col]=0
                if(row>0):
                    matrix[row][0]=0
                else:
                    rowZero = True

    for row in range(1,rows):
        for col in range(1,cols):
            if(matrix[row][0]==0 or matrix[0][col]==0):
                matrix[row][col] =0

    if(matrix[0][0]==0):
        for row in range(rows):
            matrix[row][0]=0

    if(rowZero):
        for col in range(cols):
            matrix[0][col]=0
    return matrix





matrix = [[1,1,1,0],[1,0,1,1],[1,1,1,1]]
print(setMatrixZero(matrix))
matrix1 = [[1,1,1,0],[1,0,1,1],[1,1,1,1]]
print(setMatrix(matrix1))