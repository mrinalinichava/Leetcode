def validParenthesis(s):
    n = len(s)
    stack = []

    if(n%2!=0):
        return False

    for i in range(n):
        if(s[i] in ['{','(','[']):
            stack.append(s[i])
        else:
            top = stack.pop()
            if(s[i]=='}' and top!='{'):
                return False
            if (s[i] == ')' and top != '('):
                return False
            if (s[i] == ']' and top != '['):
                return False
    if(stack):
        return False
    else:
        return True


s = "[{{}}]]"
print(validParenthesis(s))