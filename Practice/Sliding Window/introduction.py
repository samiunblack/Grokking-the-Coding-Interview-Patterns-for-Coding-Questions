#Solution:
#Visualize each contagious array as a sliding window of 'K' elements. This means
#when we move to the next subarray we will slide the window by one element. So
#to reuse the previous subarray we will subtract the element going out from the
#window and add element now begin included in the sliding window.

#Time Complexity: O(n)

def find_averages_of_subarrays(arr, K):
    window_sum, window_start = 0.0, 0
    result = []
    
    for window_end in range(len(arr)):
        window_sum += arr[window_end]
        
        if window_end >= K - 1:
            result.append(window_sum / K)
            window_sum -= arr[window_start]
            window_start += 1
    
    return result

def main():
    array1 = [1, 3, 2, 6, -1, 4, 1, 8, 2]
    print("Average of all contiguous subarrays: %s" 
          % str(find_averages_of_subarrays(array1, 5)))
    
main()