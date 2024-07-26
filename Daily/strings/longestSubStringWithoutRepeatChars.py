def lengthOfLongestSubStr(s):
    n = len(s)
    sett = set()
    max_len = 0
    left = 0
    for right in range(n):
        while(s[right] in sett):
            sett.remove(s[left])
            left+=1
        sett.add(s[right])
        max_len = max(max_len, right-left+1)
    return max_len

s = "abcabcdbb"
print(lengthOfLongestSubStr(s))



