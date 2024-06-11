def longestSubsring(s):
    n = len(s)
    left = 0
    sett = set()
    maxSub = 0
    for right in range(n):
        while(s[right] in sett):
            sett.remove(s[left])
            left=left+1
        sett.add(s[right])
        maxSub = max(maxSub,right-left+1)
    return maxSub

s1= "abcabcbb"
s2 = "abcdbcpa"
print(longestSubsring(s1))
print(longestSubsring(s2))


