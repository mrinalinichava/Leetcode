def threeSum(arr):
    n = len(arr)
    arr.sort()
    result = []

    for i,ele in enumerate(arr):
        if(i>0 and arr[i]==arr[i-1]):
            continue
        left = i+1
        right = n-1
        while(left<right):
            summ = arr[left]+arr[right]+ele
            if(summ==0):
                result.append([ele,arr[left],arr[right]])
                left+=1
                right-=1
                while(left<right and arr[left] == arr[left-1]):
                    left+=1
            elif(summ>0):
                right-=1
            else:
                left+=1
    return result



nums = [-1,0,1,2,-1,-4]
print(threeSum(nums))