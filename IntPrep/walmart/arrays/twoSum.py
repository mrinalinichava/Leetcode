from collections import defaultdict
def twosum(nums,target):
    d = defaultdict(int)
    res =[]
    for i,ele in enumerate(nums):
        rem = target-ele
        if(rem not in d):
            d[ele]=i
        else:
            res.append(d[ele])
            res.append(i)
    return res

nums = [2,7,11,15]
print(twosum(nums,9))
