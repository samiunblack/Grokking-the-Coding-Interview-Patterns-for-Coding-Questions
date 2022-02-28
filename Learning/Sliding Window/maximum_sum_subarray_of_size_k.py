def max_subarray_of_size_k(k, arr):
    #take the first k elements and add them
    #keep the result in a variable called largest
    #slide the window- remove the first element and a last element
    #sum it and see if it's larger than the previous one
    
    #note it's contagious subarray

    largest = 0

    windowStart, windowSum = 0, 0

    for windowEnd in range(len(arr)):
        windowSum += arr[windowEnd]

        if windowEnd >= k - 1:
            largest = max(largest, windowSum)
            windowSum -= arr[windowStart]
            windowStart += 1
    
    return largest

print(max_subarray_of_size_k(2, [2, 3, 4, 1, 5]))