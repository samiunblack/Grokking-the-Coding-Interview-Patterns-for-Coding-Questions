def triplet_sum_to_zero(arr):
    arr.sort()
    
    triplets = []
    
    for i in range(len(arr)):
        if i > 0 and arr[i] == arr[i - 1]:
            continue
        search_pair(arr, -arr[i], i + 1, triplets)

    return triplets
    
def search_pair(arr, target, left, triplets):
    right = len(arr) - 1
    
    while left < right:
        current_sum = arr[left] + arr[right]
    
        if current_sum == target:
            triplets.append([-target, arr[left], arr[right]])
            left += 1
            right -= 1
        
            while left < right and arr[left] == arr[left - 1]:
                left += 1
            while left < right and arr[right] == arr[right + 1]:
                right -= 1
        
        elif current_sum > target:
            right -= 1
        
        else:
            left += 1
            
print(triplet_sum_to_zero([-3, 0, 1, 2, -1, 1, -2]))