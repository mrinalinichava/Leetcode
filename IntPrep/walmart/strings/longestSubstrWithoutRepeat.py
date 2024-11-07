def longestWithoutRepeat(str):
    n = len(str)
    s = set()

    left = 0
    maxLen = 0
    for right in range(n):
        # if(str[right] not in s):
        #     s.add(str[right])
        #
        # else:
        while(str[right] in s):
            s.remove(str[left])
            left+=1
        s.add(str[right])
        maxLen = max(maxLen,right-left+1)


    return maxLen

s = "abcadcefg"
s1 = "abcabcabc"
s2 = "abcdefghpqrs"
print(longestWithoutRepeat(s))
print(longestWithoutRepeat(s1))
print(longestWithoutRepeat(s2))