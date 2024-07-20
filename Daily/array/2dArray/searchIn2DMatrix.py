def searchIn2DMatrix(matrix,target):
    m = len(matrix)
    n = len(matrix[0])
    for row in matrix:
        result = binarySearch(row,len(row),target)
        if(result != -1):
            return True
    return False


def binarySearch(arr,n,target):
    low = 0
    high = n-1
    while(low<=high):
        mid = (high + low) // 2
        if(arr[mid]>target):
            high = mid-1
        elif(arr[mid]<target):
            low = mid+1
        else:
            return mid
    return -1

arr  = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
print(searchIn2DMatrix(arr,77))