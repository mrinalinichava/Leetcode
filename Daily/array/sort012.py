def sortAnArray012(arr):
    low = mid = 0
    high = len(arr)-1

    while(mid<=high):
        if(arr[mid]==1):
            mid = mid+1
        elif(arr[mid]==0):
            arr[mid],arr[low]=arr[low],arr[mid]
            mid = mid+1
            low=low+1
        else:
            arr[mid],arr[high]= arr[high],arr[mid]
            high = high-1
    return arr

arr = [2,0,2,1,1,0]
print(sortAnArray012(arr))