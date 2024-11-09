def houseRobber(arr):

    n = len(arr)
    total = 0
    dp = [0]*(n)
    if(n==0):
        return 0
    if(n==1):
        return arr[0]
    if(n==2):
        return max(arr[0],arr[1])

    dp[0] = arr[0]
    dp[1] = arr[1]
    dp[2] = arr[0] +arr[2]

    for i in range(3,n):
        dp[i] = arr[i] +max(dp[i-2],dp[i-3])

    return max(dp[-1],dp[-2])


arr = [1,2,3,1]
arr1 = [1,0,3,9,0,4]
print(houseRobber(arr))
print(houseRobber(arr1))