def threeSum(arr):
    #[-1,-1,0,1,2,4]
    arr.sort()
    n = len(arr)
    output = []
    for i, ele in enumerate(arr):
        if(i>0 and ele == arr[i-1]):
            continue
        start = i+1
        end = n-1
        while(start<=end):
            three_sum = ele + arr[start] + arr[end]
            if(three_sum == 0):
                output.append([ele, arr[start],arr[end]])
                start+=1
                while(arr[start] == arr[start-1] and left<right):
                    start+=1

            elif(three_sum>0):
                end-=1
            else:
                start+=1
    return output



arr = [-1,0,1,2,-1,4]
print(threeSum(arr))