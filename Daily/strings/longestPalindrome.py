def longestPalindromicSubstring(s):
    n = len(s)
    res = ""
    max_len = 0
    for i in range(n):
        #odd length palindrome
        left = right = i
        while(left>=0 and right<n and s[left]==s[right]):
            length = right-left+1
            if(length>max_len):
                res = s[left:right+1]
                max_len = length
            left -= 1
            right += 1

        #even length palindromes
        left,right = i,i+1
        while(left>=0 and right<n and s[left]==s[right]):
            length = right-left+1
            if(length>max_len):
                res = s[left:right+1]
                max_len = length
            left -=1
            right +=1

    return res

s = "bababd"
s1 = "bbbbbbd"
s2 = "b"
print(longestPalindromicSubstring(s))
print(longestPalindromicSubstring(s2))