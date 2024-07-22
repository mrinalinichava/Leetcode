from collections import defaultdict

def twoSum0(arr, target):
    d = defaultdict(int)
    output = []
    for i,ele in enumerate(arr):
        l = []
        diff = target-ele
        if(diff in d):
            l.append(d[diff])
            l.append(i)
        if(l):
            output.append(l)
        d[ele]=i
    return output

def twosum(arr, target):
    seen = set()
    output = []
    for ele in arr:
        req = target - ele
        if req in seen:
            output.append((ele,req))
        seen.add(ele)
    return output

arr = [1,2,3,4,5]
print(twoSum0(arr,7))
print(twosum(arr,7))