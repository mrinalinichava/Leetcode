def maximumSumSubarrary(nums):
    max_sum = nums[0]
    curr_sum = nums[0]
    start = end = temp = 0

    for i in range(1,len(nums)):
        if(nums[i]>curr_sum+nums[i]):
            curr_sum = nums[i]
            temp = i
        else:
            curr_sum = curr_sum+nums[i]
        if(curr_sum>max_sum):
            max_sum = curr_sum
            start = temp
            end = i
    return max_sum, nums[start:end+1]

nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
maxsum,subarray  = maximumSumSubarrary(nums)
print(f"Max sum: {maxsum}, Subarray: {subarray}")