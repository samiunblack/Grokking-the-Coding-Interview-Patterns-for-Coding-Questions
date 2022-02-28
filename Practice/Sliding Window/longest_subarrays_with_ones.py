def longest_subarray(arr, K):
    window_start, max_count, max_len = 0, 0, 0

    for window_end in range(len(arr)):
        right_char = arr[window_end]

        if right_char == 1: max_count += 1

        if window_end - window_start + 1 - max_count > K:
            if arr[window_start] == 1: max_count -= 1
            window_start+= 1
        
        max_len = max(max_len, window_end - window_start + 1)
    
    return max_len

print(longest_subarray([0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], 3))