def longest_substring(str, k):
    char_dict = {
        "a": "This is awesome"
    }

    window_start = 0
    max_length = 0


    for window_end in range(len(str)):
        right_char = str[window_end]

        if right_char not in char_dict:
            char_dict[right_char] = 0
        
        char_dict[right_char] += 1

        while len(char_dict) > k:
            left_char = str[window_start]
            char_dict[left_char] -= 1
            if char_dict[left_char] <= 0:
                del char_dict[left_char]
            window_start += 1

        max_length = max(max_length, window_end - window_start + 1)
    
    return max_length

print(longest_substring("araaci", 2))