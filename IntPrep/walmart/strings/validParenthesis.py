def validaParentesis(s):
    #((}}
    stack = []
    for char in s:
        if char in ['{','[','(']:
            stack.append(char)
        else:
            ele = stack.pop()
            if((char == '}' and ele!='{') or (char ==')' and ele!='(') or
                (char == ']' and ele!='[')):
                return False
    return True


s = "{{(())}}"
s1 = "{{))"
print(validaParentesis(s))
print(validaParentesis(s1))