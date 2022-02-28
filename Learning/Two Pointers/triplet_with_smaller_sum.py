def triplet_with_smaller_sum(arr, target):
    arr.sort()
    count = 0
    
    for i in range(len(arr)):
        count += search_pair(arr, target - arr[i], i)
    
    return count

def search_pair(arr, target, first):
    count = 0
    left = first + 1
    right = len(arr) - 1
    
    while left < right:
        if arr[left] + arr[right] < target:
            count += right - left
            left += 1
        else:
            right -= 1
    
    return count
        
        
print(triplet_with_smaller_sum([-1, 4, 2, 1, 3], 5))