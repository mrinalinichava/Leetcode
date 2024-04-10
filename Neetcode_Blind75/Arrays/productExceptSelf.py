
def productExceptSelf(arr):
    n = len(arr)
    output = [1]*n

    for i in range(1,n):
        output[i] = output[i-1]*arr[i-1]

    right = 1
    for i in range(n-1,-1,-1):
        output[i] = output[i]*right
        right = right*arr[i]
    return output

'''
Input: nums = [1,2,3,4]
Output: [24,12,8,6]
'''
nums = [1,2,3,4]

print(productExceptSelf(nums))