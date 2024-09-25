def maxProdOfThreeElements(arr):
    arr.sort()
    print(arr)
    case1 = arr[0]*arr[1]*arr[-1]
    case2 = arr[-1]*arr[-2]*arr[-3]
    return max(case1,case2)



arr1 = [-6,7,8,1,-9,0,1,2,3]
arr2 = [-1,-2,0,1,2]
arr3 = [-1,0,1,2]
print(maxProdOfThreeElements(arr1))
print(maxProdOfThreeElements(arr3))