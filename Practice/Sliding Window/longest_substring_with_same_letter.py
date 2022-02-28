def longest_substring(str, K):
    window_start, max_len, max_count = 0, 0, 0

    char_frequency = {}

    for window_end in range(len(str)):
        right_char = str[window_end]

        if right_char not in char_frequency:
            char_frequency[right_char] = 0

        char_frequency[right_char] += 1

        max_count = max(max_count, char_frequency[right_char])

        while window_end - window_start + 1 - max_count > K:
            left_char = str[window_start]
            char_frequency[left_char] -=1
            if char_frequency[left_char] <= 0:
                del char_frequency[left_char]
            window_start += 1
        
        max_len = max(max_len, window_end - window_start + 1)
    
    return max_len

print(longest_substring("abbcb", 1))