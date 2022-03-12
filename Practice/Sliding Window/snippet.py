arr = [] #some elements

#core pattern
window_sum, window_start = 0

for window_end in range(arr):
    #do some logic
    
    #if window range greater than needed
    window_sum -= arr[window_start]
    window_start += 1
    

#snippet
current_window_length = window_end - window_start + 1

