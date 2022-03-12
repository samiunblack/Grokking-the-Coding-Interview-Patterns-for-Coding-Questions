#Solution:
# follow the sliding window pattern
# keep a max variable
# when the window reached the Kth element update the max variable

def max_sum_subarray(arr, K):
    window_sum, window_start = 0, 0
    maximum = 0
    
    for window_end in range(len(arr)):
        window_sum += arr[window_end]
        
        if window_end >= K - 1:
            maximum = max(maximum, window_sum)
            window_sum -= arr[window_start]
            window_start += 1
    
    return maximum


def main():
    arr1 = [2, 1, 5, 1, 3, 2]
    print("Maximum Sum : %s" % str(max_sum_subarray(arr1, 3)))
    
    arr2 = [2, 3, 4, 1, 5]
    print("Maximum Sum: %s" % str(max_sum_subarray(arr2, 2)))

main()  