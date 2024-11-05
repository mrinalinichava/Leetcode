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


def threeSumHash(nums):
    n = len(nums)
    nums.sort()
    result = set()
    for i, ele in enumerate(nums):
        left, right = i + 1, n - 1
        while (left < right):
            summ = ele + nums[left] + nums[right]
            if (summ == 0):
                result.add((ele, nums[left], nums[right]))
                left += 1
                right -= 1
            elif (summ > 0):
                right -= 1
            else:
                left += 1
    return [list(triplet) for triplet in result]


nums = [-1,0,1,2,-1,-4]
print(threeSum(nums))

nums = [-1,0,1,2,-1,-4]
print(threeSumHash(nums))

