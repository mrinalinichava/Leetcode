from collections import defaultdict

def groupAnagrams(arr):
    d = defaultdict(list)
    output = []
    for i,ele in enumerate(arr):
        sorted_ele = ''.join(sorted(ele))
        if(sorted_ele in d):
            d[sorted_ele].append(ele)
        else:
            d[sorted_ele] = [ele]

    for key,values in d.items():
        output.append(values)
    print(output)


strs = ["eat","tea","tan","ate","nat","bat"]
# Expected Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
print(groupAnagrams(strs))