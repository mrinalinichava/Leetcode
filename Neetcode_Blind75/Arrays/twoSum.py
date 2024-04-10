from collections import defaultdict
def twoSum(arr,target):
    d = defaultdict(int)
    output = []
    for i,ele in enumerate(arr):
        req_ele = target - ele
        if(req_ele in d.keys()):
            output.append(d[req_ele])
            output.append(i)
        d[ele] = i
    return output


def twoSum1(arr,target):
    arr.sort()
    n = len(arr)
    left,right = 0,n-1
    output=[]
    while(left<=right):
        if(arr[left]+arr[right]==target):
            output.append(left)
            output.append(right)
            break
        elif(arr[left]+arr[right]>target):
            right = right-1
        else:
            left=left+1
    return output


arr = [2,7,11,15]
arr1 = [3,2,4]
target = 9
target1 = 7
print(twoSum1(arr,target))
print(twoSum1(arr1,target1))

