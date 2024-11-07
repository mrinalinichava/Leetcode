def findFirstAndLast(arr,target):
    n = len(arr)
    res = [-1,-1]
    for i,ele in enumerate(arr):
        print(ele,target)
        if(ele==target):
            print("i",i)
            j=i+1
            while(j<n and arr[j]==ele):
                j+=1
            print("j",j)
            res[0]=i
            res[1]=j-1
            break
    return res

def firstAndLastBinSearch(arr,target):
    n = len(arr)
    def binarySearch(arr,target,findLeft):
        result = -1
        n = len(arr)
        left = 0
        right = n-1
        while(left<=right):
            mid = (left+right)//2
            if(arr[mid]==target):
                result = mid
                if(findLeft):
                    right = mid-1
                else:
                    left = mid+1
            elif(arr[mid]>target):
                right = mid-1
            else:
                left=mid+1
        return result

    left = binarySearch(arr,target,findLeft=True)
    right = binarySearch(arr,target,findLeft=False)

    return [left,right]


arr = [1,1,2,2,2,2,3,4,4,4,4,5,6,7,8]
print(findFirstAndLast(arr,2))
print(firstAndLastBinSearch(arr,2))