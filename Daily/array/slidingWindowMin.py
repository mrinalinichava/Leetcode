from collections import  deque
def slidingWindowMin(arr,k):
    n = len(arr)
    dq = deque()
    res =[]
    for i in range(n):

        if (dq and dq[0] < i-k+1):
            dq.popleft()

        while(dq and arr[dq[-1]] > arr[i]):
            dq.pop()

        dq.append(i)
        if(i>=k-1):
            res.append(arr[dq[0]])
    return res

arr = [1,3,-1,-3,5,3,6,7]

print(slidingWindowMin(arr,3))