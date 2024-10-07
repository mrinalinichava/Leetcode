from collections import deque
def slidingWindowMax(arr,k):

    # n = len(arr)
    # res =[]
    # for i in range(n):
    #     maxi = max(arr[i:i+k])
    #     res.append(maxi)
    #
    # return res
    n = len(arr)
    res = []
    left = right = 0
    dq = deque()
    if n == 0 or k == 0:
        return []
    for i in range(n):

        if(dq and dq[0] <i-k+1):
            dq.popleft()
        while(dq and arr[dq[-1]]<arr[i]):
            dq.pop()

        dq.append(i)

        if(i>=k-1):
            res.append(arr[dq[0]])
    return res

arr = [1,3,-1,-3,5,3,6,7]

print(slidingWindowMax(arr,3))