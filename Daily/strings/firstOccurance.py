def firstOccurance(haystack, needle):
    if not needle:
        return 0

    n = len(haystack)
    m = len(needle)

    for i in range(n-m+1):
        if(haystack[i:i+m] == needle):
            return i
    return -1

a = "butsad"
b = "sad"
print(firstOccurance(a,b))