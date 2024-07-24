def fourSum(nums,target):
    n = len(nums)
    nums.sort()
    output = []
    for i in range(n):
        if(i>0 and nums[i]==nums[i-1]):
            continue
        for j in range(i+1,n):
            if(j>i+1 and nums[j]==nums[j-1]):
                continue
            start = j+1
            end = n-1
            while(start<end):
                summ = nums[i] + nums[j] + nums[start] +nums[end]
                if(summ>target):
                    end-=1
                elif(summ<target):
                    start+=1
                else:
                    output.append([nums[i],nums[j],nums[start],nums[end]])
                    start+=1
                    end-=1

                    while(nums[start]==nums[start-1] and start<end):
                        start+=1
                    while(nums[end]==nums[end+1] and start<end):
                        end-=1
    return output

nums = [4, 3, 3, 4, 4, 2, 1, 2, 1, 1]
target = 9

print(fourSum(nums,target))