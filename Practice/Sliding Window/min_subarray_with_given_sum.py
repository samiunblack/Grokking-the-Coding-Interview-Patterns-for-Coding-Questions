import math

#Solution
# Take elements in the window until it reaches the given sum
# after reaching given sum update the min element
# shrink window until the sum becomes less than given sum
# again add element until it reaches given sum


def min_subarray_with_given_sum(arr, sum):
    window_sum, windowstart = 0, 0
    min_subarray = math.inf
    
    for window_end in range(len(arr)):
        window_sum += arr[window_end]
        
        subarray_length = window_end - windowstart + 1
        while window_sum >= sum:
            min_subarray = min(min_subarray, subarray_length)
            window_sum -= arr[windowstart]
            windowstart += 1
    
    return min_subarray

def main():
    arr1 = [2, 1, 5, 2, 3, 2];
    print("min subarray length: %s" % str(min_subarray_with_given_sum(arr1, 7)))
    
    arr2 = [2, 1, 5, 2, 8]
    print("min subarray length %s" % str(min_subarray_with_given_sum(arr2, 7)))
    
main()
            