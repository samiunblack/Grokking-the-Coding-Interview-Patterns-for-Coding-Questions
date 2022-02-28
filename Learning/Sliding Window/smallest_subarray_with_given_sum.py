import math

def smallest_subarray(s, arr):
    #take the first element and see if it's greater or equal to s
    #if not expand the window
    #see if next two elements is greater or equal to s
    #if not expand the window
    #when found such subarray make it's len smallest
    #expand the window removing first element
    #and adding last element
    #if the window sum is greater than s
    #remove the last element and see if it still satisfies
    #keep doing this until the end

    window_start, window_sum = 0, 0
    min_len = math.inf

    for window_end in range(len(arr)):
        window_sum += arr[window_end]

        while window_sum >= s:
            min_len = min(min_len, window_end - window_start + 1)
            window_sum -= arr[window_start]
            window_start += 1
        
    if min_len == math.inf: 
        return 0
    else: return min_len


print(smallest_subarray(7, [2, 1, 5, 2, 3, 2]))
print(smallest_subarray(8, [2, 1, 5, 2, 8]))
print(smallest_subarray(8, [3, 4, 1, 1, 6]))