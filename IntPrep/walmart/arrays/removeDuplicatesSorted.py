def removeDuplictatesFromSorted(arr):
    # 1,1,1,2,2,3,3,4,5,6

    stack  = []
    for ele in arr:
        if(not stack or stack[-1]!=ele):
            stack.append(ele)

    return stack


def removeDuplicatesInPlace(arr):
    # 1,1,1,2,2,3,4,5,6
    n = len(arr)
    left = 0
    for right in range(1,n):
        if(arr[right]!=arr[left]):
            left+=1
            arr[left]=arr[right]
            print(arr)
    # return left+1
    return arr[:left+1]


arr = [1,1,2,2,3,3,4,5,6,6]
print(removeDuplictatesFromSorted(arr))
print(removeDuplicatesInPlace(arr))