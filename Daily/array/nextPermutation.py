def nextPermutation(arr):
    #[1,3,4,9,8,7]
    n = len(arr)
    k = -1
    for i in range(n-2,-1,-1):
        if(arr[i]<arr[i+1]):
            k = i
            break
    if(k==-1):
        arr.reverse()

    for j in range(n-1,k,-1):
        if(arr[j]>arr[k]):
            arr[j],arr[k] = arr[k],arr[j]
            break
    arr[k+1:] = arr[k+1:][::-1]
    print(arr)

arr = [1,3,4,9,8,7]
nextPermutation(arr)
arr2 =[1,2,3]
nextPermutation(arr2)