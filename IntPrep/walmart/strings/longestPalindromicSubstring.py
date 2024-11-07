def longestPalindromicSubstring(s):
    #caabaac
    n = len(s)

    def expandAroundCentre(left,right):
        while(left>=0 and right < len(s) and s[left]==s[right]):
            left-=1
            right+=1
        return s[left+1:right]

    longest = ""
    for i in range(n):
        odd = expandAroundCentre(i,i)
        even = expandAroundCentre(i,i+1)
        # print("odd",odd)
        # print("even",even)
        if len(odd) > len(longest):
            longest = odd
        if len(even) > len(longest):
            longest = even
    print("longest",longest)
    return longest

s="babad"
s1 = "caabaacdcaab"
print(longestPalindromicSubstring(s1))