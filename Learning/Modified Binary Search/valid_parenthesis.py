def isValid(s):
    stack = []
    parentheseses = ["(", "{", "["]
    bracket_dict = {"}":"{", ")": "(", "]": "["}
    
    for parentheses in s:
        if parentheses in parentheseses:
            stack.append(parentheses)
        else:
            if parentheses in bracket_dict:
                if len(stack) > 0 and stack[-1] is bracket_dict[parentheses]:
                    stack.pop()
                else:
                    return False
    return len(stack) == 0

print(isValid("(])"))