def trappingRainwater(arr):
    #height = [0,1,0,2,1,0,1,3,2,1,2,1]
    n = len(arr)
    left =[0]*n
    right=[0]*n
    left[0]= arr[0]

    for i in range(n):
        left[i] = max(left[i-1],arr[i])

    right[n-1]=arr[n-1]
    for i in range(n-2,-1,-1):
        right[i] = max(arr[i],right[i+1])

    total = 0
    for i in range(n):
        total += min(left[i],right[i]) -arr[i]

    return total

height = [0,1,0,2,1,0,1,3,2,1,2,1]
height1= [4,2,0,3,2,5]
print(trappingRainwater(height))
print(trappingRainwater(height1))