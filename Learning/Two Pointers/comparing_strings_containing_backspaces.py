def comparing_strings(str1, str2):
    stack1 = ""
    stack2 = ""
    
    for i in range(len(str1)):
        if str1[i] == "#":
            stack1 = stack1[:-1]
        else:
            stack1 += str1[i]

    for j in range(len(str2)):
        if str2[j] == "#":
            stack2 = stack2[:-1]
        else:
            stack2 += str2[j]

    return stack1 == stack2

def comparing_strings(str1, str2):
    index1 = len(str1) - 1
    index2 = len(str2) - 1
    
    while index1 >= 0 or index2 >= 0:
        i1 = get_next_valid_index(str1, index1)
        i2 = get_next_valid_index(str2, index2)
        
        if i1 < 0 and i2 < 0:
            return True
        if i1 < 0 or i2 < 0:
            return False
        
        if str1[i1] != str2[i2]:
            return False

        index1 = i1 + 1
        index2 = i2 + 1
        
    return True

def get_next_valid_index(str, index):
    backspace_count = 0
    
    while index >= 0:
        
        if str[index] == "#":
            backspace_count += 1
        elif backspace_count > 0:
            backspace_count -= 1
        else:
            break
        
        index -= 1
    
    return index

print(comparing_strings("xy#z", "xyz#"))