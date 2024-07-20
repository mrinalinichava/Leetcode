from collections import defaultdict
def findRepeatMissing(arr):
    n = len(arr)
    d = [0]*(n)
    repeated = missing = None
    for i in range(n):
        d[arr[i]-1] = d[arr[i]-1]+1
    for i in range(n):
        if(d[i]==2):
            repeated = i+1
        if(d[i]==0):
            missing = i+1
    return (repeated,missing)


arr = [3,1,2,5,3]
arr2 = [1,3,4,3,2]
print(findRepeatMissing(arr))
print(findRepeatMissing(arr2))