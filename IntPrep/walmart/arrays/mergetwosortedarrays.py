def mergesortedarrays(arr1,arr2):

    m = len(arr1)
    n = len(arr2)
    arr3 = [0]*(m+n)
    i = j = k = 0
    while(i<m and j<n):
        if(arr1[i]<arr2[j]):
            arr3[k] = arr1[i]
            i+=1
        else:
            arr3[k] = arr2[j]
            j+=1
        k+=1

    while(i<m):
        arr3[k] = arr1[i]
        i+=1
        k+=1

    while(j < n):
        arr3[k] = arr2[j]
        j+=1
        k += 1

    return arr3


def mergeSortedArrays1(arr1,arr2):

    total = len(arr1)
    n = len(arr2)
    m = total -n
    print(m,n)
    last = total -1
    while(m>0 and n>0):
        if(arr1[m-1]>arr2[n-1]):
            arr1[last] = arr1[m-1]
            m-=1
        else:
            arr1[last] = arr2[n-1]
            n-=1
        last-=1

    return arr1



arr1 = [1,3,5,7,11]
arr2= [2,4,6,8]
print(mergesortedarrays(arr1,arr2))

arr11 = [1,3,5,7,11,0,0,0,0]
arr22 = [2,4,6,8]
print(mergeSortedArrays1(arr11,arr22))
