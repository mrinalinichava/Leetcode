def reverseString(s):
    s.strip()
    # print("\"" + s + "\"")
    print(s)
    words = s.split()
    print(words)
    rev_words = words[::-1]

    return " ".join(rev_words)


s = "     world     hello     "
print(reverseString(s))