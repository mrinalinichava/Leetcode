def maxSumSubarrayOfSizek(arr,k):
    # [-1,2, 3,1,-3,2]
    #k = 2
    n = len(arr)
    if n<k:
        return 0 #or return the sum of entire array
    max_sum = sum(arr[:k])
    curr_sum = max_sum

    for i in range(1, n-k+1):
        curr_sum = curr_sum - arr[i-1] + arr[i+1]
        max_sum = max(curr_sum,max_sum)
    return max_sum


    # left,right= 0,1
    # max_sum = 0
    # while(right<n-1):
    #     if(right -left +1 <=k):
    #         summ = arr[left]+arr[right]
    #         max_sum = max(summ,max_sum)
    #     left+=1
    #     right+=1
    # return max_sum
arr = [-1,2,1,-3,2]
print(maxSumSubarrayOfSizek(arr,2))




