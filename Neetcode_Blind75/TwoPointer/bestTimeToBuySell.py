

def bestTimeToBuyAndSell(arr):
    #[7,1,5,3,6,4]
    n = len(arr)
    left = 0
    right = left+1
    maxcount  = 0
    while(right<n):

        if(arr[left]>arr[right]):
            left = right
            right = right+1
        else:
            count = arr[right] - arr[left]
            maxcount = max(maxcount, count)
            right = right+1
    return maxcount
arr  = [7,6,4,3,1]
print(bestTimeToBuyAndSell(arr))
