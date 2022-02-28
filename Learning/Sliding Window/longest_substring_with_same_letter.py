def longest_substring(str, k):
    window_start, max_length, max_repeat = 0, 0, 0

    char_dict = {}

    for window_end in range(len(str)):
        right_char = str[window_end]

        if right_char not in char_dict:
            char_dict[right_char] = 0
        char_dict[right_char] += 1

        max_repeat = max(max_repeat, char_dict[right_char])

        if window_end - window_start + 1 - max_repeat > k:
            left_char = str[window_start]
            char_dict[left_char] -= 1
            window_start += 1
        
        max_length = max(max_length, window_end - window_start + 1)
    return max_length

print(longest_substring("aabcbb", 2))