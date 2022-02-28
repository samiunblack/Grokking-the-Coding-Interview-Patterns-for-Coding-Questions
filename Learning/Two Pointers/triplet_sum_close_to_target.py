import math

def triplet_sum_close_to_target(arr, target):
    arr.sort()
    
    smallest_diff = math.inf
    for i in range(len(arr)):
        left = i + 1
        right = len(arr) - 1
        
        while left < right:
            target_diff = target - arr[i] - arr[left] - arr[right]
            
            if target_diff == 0:
                return target - target_diff
            
            if abs(target_diff) < abs(smallest_diff):
                smallest_diff = target_diff
            
            if target_diff > 0:
                left += 1
            else:
                right -= 1
    
    return target - smallest_diff

print(triplet_sum_close_to_target([-3, -1, 1, 2], 1))