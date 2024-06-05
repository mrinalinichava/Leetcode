def containerWithMostWater(arr):

    #[1,8,6,2,5,4,8,3,7]
    n = len(arr)
    start , end = 0 , n-1
    max_area = 0
    while(start<=end):
        length = end-start
        width = min(arr[start],arr[end])
        area = length*width
        max_area = max(max_area,area)
        if(arr[start]>arr[end]):
            end = end-1
        else:
            start = start +1
    return max_area

nums = [1,8,6,2,5,4,8,3,7]
print(containerWithMostWater(nums))

