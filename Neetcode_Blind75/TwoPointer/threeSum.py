def threeSum(nums):
    nums.sort()
    n = len(nums)
    output = []

    for i, ele in enumerate(nums):
        if(i>0 and nums[i]==nums[i-1]):
            continue
        start,end = i+1, n-1
        while(start<end):
            summ = nums[start] + nums[end] + nums[i]
            if (summ == 0):
                output.append([nums[i], nums[start], nums[end]])
            while start< end and nums[start] == nums[start+1]:
                start = start+1
            if(summ<0):
                start +=1
            else:
                end -=1
    return output

nums = [-1,0,1,2,-1,-4]
print(threeSum(nums))

