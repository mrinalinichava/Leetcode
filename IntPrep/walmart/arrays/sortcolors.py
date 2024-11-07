def sortcolors(arr):
    n = len(arr)
    low = mid = 0
    high = n-1
    while(mid<=high):
        if(arr[mid]==1):
            mid+=1
        elif(arr[mid]==0):
            arr[mid],arr[low] = arr[low],arr[mid]
            mid+=1
            low+=1
        else:
            arr[mid],arr[high] = arr[high],arr[mid]
            high-=1

    return arr

arr = [2,0,2,1,1,0]
arr1= [0,0,0,1,1,1,2,2,0,0,1,1]
print(sortcolors(arr1))