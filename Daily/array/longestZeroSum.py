def longestSubarrayZeroSum(arr):
    d = {}
    max_len = 0
    summ = 0

    for i,ele in enumerate(arr):
        summ = summ+ele
        if(summ==0):
            max_len = i+1
        if(summ in d):
            max_len = max(max_len,i-d[summ])
        else:
            d[summ]=i
    return max_len


arr =[9, -3, 3, -1, 6, -5]
print(longestSubarrayZeroSum(arr))

arr1 = [6, -2, 2, -8, 1, 7, 4, -10]
print(longestSubarrayZeroSum(arr1))
