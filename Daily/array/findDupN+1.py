def findDuplicate(arr):
    arr.sort()
    n = len(arr)
    for i in range(1,n):
        if(arr[i]==arr[i-1]):
            return arr[i]
    return -1

def findDuplicateOptimized(arr):
    slow = arr[0]
    fast = arr[0]

    while(True):
        slow = arr[slow]
        fast = arr[arr[fast]]
        if(slow==fast):
            break
    slow = arr[0]
    while slow != fast:
        slow = arr[slow]
        fast = arr[fast]

    return slow


arr = [1,2,3,4,6,5,6]
print(findDuplicate(arr))
print(findDuplicate(arr))