from collections import defaultdict
def checkAnagram(s,t):
    return sorted(s)== sorted(t)


def groupAnagrams(arr):
    d = defaultdict(list)

    for ele in arr:
        sorted_ele = ''.join(sorted(ele))
        if(sorted_ele in d):
            d[sorted_ele].append(ele)
        else:
            d[sorted_ele]=[ele]
    return d.values()

arr = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(arr))



print(checkAnagram("tea","atee"))