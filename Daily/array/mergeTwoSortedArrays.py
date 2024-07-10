def mergeSortedArrays(arr1,arr2,m,n):
    last = m+n-1
    while(m>0 and n>0):
        if(arr1[m-1] > arr2[n-1]):
            arr1[last] = arr1[m-1]
            m-=1
        else:
            arr1[last] = arr2[n-1]
            n-=1
        last-=1
    while(n>0):
        arr1[last]=arr2[n-1]
        n-=1
        last-=1
    return arr1

arr1 = [1,4,6,0,0,0]
arr2 = [2,3,5]
print(mergeSortedArrays(arr1,arr2,3,3))