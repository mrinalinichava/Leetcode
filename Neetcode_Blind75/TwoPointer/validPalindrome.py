def validaPalindrome(s):
    s = s.lower()
    s.replace(" ","")
    s = "".join([ele for ele in s if ele.isalnum()])
    n = len(s)
    i,j = 0, n-1
    while(i<=j):
        if(s[i]!=s[j]):
            return False
        else:
            i = i+1
            j = j-1
    return True

s = "race a car"
s1 = "cakeekac"
print(validaPalindrome(s1))
