import heapq
from collections import defaultdict
def kMostFrequentElements(arr,k):
    d= defaultdict(int)
    for ele in arr:
        d[ele]+=1
    max_heap = []
    output =[]
    for k,v in d.items():
        max_heap.append((-v,k))
    heapq.heapify(max_heap)


def kMostFrequentElements1(arr,k):
    d= defaultdict(int)
    for ele in arr:
        d[ele]+=1
    sorted_dict= dict(sorted(d.items(), key = lambda x : x[1], reverse = True))
    return list(sorted_dict.keys())[:k]


'''
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
'''
nums = [1,1,1,2,2,3]
k = 2
print(kMostFrequentElements1(nums,k))







