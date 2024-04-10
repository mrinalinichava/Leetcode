def validAnagram(s,t):
    if len(s) != len(t):
        return False
    s = sorted(s)
    t = sorted(t)
    n = len(s)
    for i in range(n):
        if(s[i]!=t[i]):
            return False
    return True


def validAnagram1(s,t):
    if len(s) != len(t):
        return False
    d = set()
    for ele in s:
        d.add(ele)
    for ele in t:
        if(ele not in s):
            return False
    return True

s = "apple"
t = "leppa"
print(validAnagram(s,t))
print(validAnagram1(s,t))