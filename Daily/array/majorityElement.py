from collections import defaultdict
def majorityElement(arr):
    n = len(arr)//2
    d = defaultdict(int)
    for i,ele in enumerate(arr):
        d[ele] = d[ele] + 1
    for key,val in d.items():
        if(d[key]>n):
            return key
    return -1




arr = [3,1,3]
arr1 = [2,2,1,1,1,2,2]
arr2 = [2,1,1,1,2,2]
print(majorityElement(arr))
print(majorityElement(arr1))
print(majorityElement(arr2))