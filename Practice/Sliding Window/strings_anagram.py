def strings_anagram(str, pattern):
    window_start, matched = 0, 0

    char_frequency = {}
    result = []

    for char in pattern:
        if char not in char_frequency:
            char_frequency[char] = 0
        
        char_frequency[char] += 1


    for window_end in range(len(str)):
        right_char = str[window_end]

        if right_char in char_frequency:
            char_frequency[right_char] -= 1
            if char_frequency[right_char] == 0:
                matched += 1
        
        if matched == len(char_frequency):
            result.append(window_start)


        if window_end >= len(char_frequency) - 1:
            left_char = str[window_start]
            window_start += 1

            if left_char in char_frequency:
                if char_frequency[left_char] == 0:
                    matched -= 1
                char_frequency[left_char] += 1

    return result


print(strings_anagram("ppqp", "pq"))