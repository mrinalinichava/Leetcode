def longestConsecSeq(arr):
    n = len(arr)
    s = set()

    for ele in arr:
        s.add(ele)
    max_count = 0
    for ele in arr:
        if (ele -1 in s):
            continue
        else:
            count = 0
            while(count+ele in s):
                count+=1
            max_count = max(count,max_count)
    return max_count


nums = [100,4,200,1,3,2]
print(longestConsecSeq(nums))