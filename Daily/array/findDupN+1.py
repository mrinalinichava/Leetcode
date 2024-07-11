def findDuplicate(arr):
    arr.sort()
    n = len(arr)
    for i in range(1,n):
        if(arr[i]==arr[i-1]):
            return arr[i]
    return -1

arr = [1,2,3,4,5,5]
print(findDuplicate(arr))