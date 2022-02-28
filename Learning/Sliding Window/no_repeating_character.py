def no_repeating_character(str):
    window_start = 0
    max_length = 0

    char_dict = {}

    for window_end in range(len(str)):
        right_char = str[window_end]

        if right_char in char_dict:
            window_start = max(window_start, char_dict[right_char] + 1)
        
        char_dict[right_char] = window_end
        
        max_length = max(max_length, window_end - window_start + 1)
    
    return max_length

print(no_repeating_character("aabccbb"))