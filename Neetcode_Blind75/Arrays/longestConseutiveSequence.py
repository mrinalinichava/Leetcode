

def longestConsecutiveSequence(arr):

    n = len(arr)
    s = set()
    maxcount = 0
    for ele in arr:
        s.add(ele)

    for i,ele in enumerate(arr):
        count = 0
        if(ele-1 in s):
            continue
        while(count+ele in s):
            count+=1
            maxcount = max(maxcount,count)
    return maxcount


'''
Input: nums = [100,4,200,1,3,2,5]
Output: 4
'''
nums = [100,4,200,1,3,2,5]
print(longestConsecutiveSequence(nums))