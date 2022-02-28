def longest_subarray(arr, k):
    window_start, max_length, max_count = 0, 0, 0

    for window_end in range(len(arr)):
        if arr[window_end] == 1:
            max_count += 1

        if (window_end - window_start + 1 - max_count) > k:
            if arr[window_start] == 1:
                max_count -= 1
            window_start += 1
        max_length = max(max_length, window_end - window_start + 1)

    return max_length

print(longest_subarray([0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], 2))