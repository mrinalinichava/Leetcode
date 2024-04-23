def nextGreatest(arr):

    # [2,7,4,3,5]

    s =[]
    n = len(arr)
    output = [0]*n
    s.append(0)
    for i in range(n-1,-1,-1):

        while(s and s[-1]<=arr[i]):
            s.pop(-1)
        if(s):
            output[i]=s[-1]
        else:
            output[i]=0
        s.append(arr[i])


    print(output)
    return output

arr = [2,7,4,3,5]
arr1 =[1,2,5,3,1,2,4,6]
nextGreatest(arr)

