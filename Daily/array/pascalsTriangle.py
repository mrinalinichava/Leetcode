def pascalsTriangle(rows):

    triangle = []
    for i in range(rows):
        row = [1]*(i+1)
        for j in range(1,i):
            row[j] = triangle[i-1][j-1] + triangle[i-1][j]
        triangle.append(row)
    return triangle

def pascalsTri(rows):
    res = [[1]]

    for i in range(rows-1):
        temp = [0]+res[-1]+[0]
        row = []
        for j in range(len(res[-1])+1):
            row.append(temp[j]+temp[j+1])
        res.append(row)
    return res



rows = 5
print(pascalsTriangle(rows))
print(pascalsTri(rows))




