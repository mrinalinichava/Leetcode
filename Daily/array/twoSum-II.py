def two_sum_ii(arr,target):
    n = len(arr)
    left, right = 0, n-1

    while(left<=right):
        summ = arr[left] + arr[right]
        if(summ<target):
            left+=1
        elif(summ>target):
            right-=1
        else:
            return (arr[left],arr[right])

nums = [2,3,5,7,11,15]
target = 8
print(two_sum_ii(nums,target))