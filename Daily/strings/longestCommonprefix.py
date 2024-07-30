def longestCommonPrefix(strings):
    if(not strings):
        return ""
    prefix = strings[0]

    for string in strings:
        if(string.startswith(prefix)):
            continue
        while(not string.startswith(prefix)):
            prefix = prefix[:-1]
            if(not prefix):
                return ""
    return prefix



strings = ["abcdefg", "abcdef","abcde","abcd", "abc"]
print(longestCommonPrefix(strings))