def moveZeros(arr):
    n = len(arr)
    nonzero = 0
    for zero in range(n):
        if(arr[zero]!=0):
            if(nonzero!=zero):
                arr[nonzero],arr[zero]=arr[zero],arr[nonzero]
            nonzero+=1

    return arr

def moveZeros1(arr):
    n = len(arr)
    nonzero = 0  # Track where the next non-zero element should be placed

    # Iterate over the entire array
    for i in range(n):
        if arr[i] != 0:

            arr[nonzero] = arr[i]
            nonzero += 1


    # Fill the rest of the array with zeros
    for i in range(nonzero, n):
        arr[i] = 0

    return arr

# Example usage
arr = [2, 0, 4, 0, 9]
moveZeros(arr)
print(arr)  # Output: [2, 4, 9, 0, 0]

arr1 = [2, 0, 4, 0, 9]
moveZeros1(arr1)
print(arr1)  # Output: [2, 4, 9, 0, 0]


arr = [2,0,4,0,9]
print(moveZeros(arr))