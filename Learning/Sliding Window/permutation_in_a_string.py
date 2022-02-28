from collections import Counter

def permutation_in_string(str, pattern):
    counter = Counter(pattern)

    window_start, matched = 0, 0

    for window_end in range(len(str)):
        if str[window_end] in counter:
            counter[str[window_end]] -= 1
            if counter[str[window_end]] <= 0:
                matched += 1
        
        if matched == len(counter):
            return True
        
        if window_end > len(pattern):
            left_char = str[window_start]
            window_start += 1

            if left_char in counter:
                if counter[left_char] == 0:
                    matched -= 1
                counter[left_char] += 1
    return False

print(permutation_in_string("oidbcaf", "abc"))
        