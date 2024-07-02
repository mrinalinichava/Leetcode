# Leetcode : https://leetcode.com/problems/degree-of-an-array/description/

from collections import defaultdict
def degreeOfArray(arr):
    freq = defaultdict(int)
    first = defaultdict(int)
    last = defaultdict(int)

    for i,ele in enumerate(arr):
        if(ele not in freq):
            first[ele]=i
        freq[ele] = freq[ele]+1
        last[ele]=i
    min_degree = max(freq.values())
    minlen = len(arr)
    for ele in freq:
        if(freq[ele] == min_degree):
            curr_len = last[ele] - first[ele] + 1
            minlen = min(minlen,curr_len)
    return minlen

arr = [1,2,2,3,1]
print(degreeOfArray(arr))