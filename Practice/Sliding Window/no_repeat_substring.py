def no_repeat_substring(str):
    window_start = 0
    max_len = 0

    char_frequency = {}

    for window_end in range(len(str)):
        right_char = str[window_end]

        if right_char in char_frequency:
            window_start = max(window_start, char_frequency[right_char] + 1)
        
        char_frequency[right_char] = window_end


        max_len = max(max_len, window_end - window_start + 1)
    return max_len

print(no_repeat_substring("aabccbb"))
print(no_repeat_substring("abbbb"))
print(no_repeat_substring("abccde")) 