def longest_subarray_with_ones(arr, K):
    window_start, maxCount, max_length = 0, 0, 0
    
    for window_end in range(len(arr)):
        right_char = arr[window_end]
        
        if right_char == 1:
            maxCount += 1
        
        if window_end - window_start + 1 - maxCount > K:
            if arr[window_start] == 1:
                maxCount -= 1
            window_start += 1

        max_length = max(max_length, maxCount)
        
    return max_length
        
        