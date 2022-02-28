def pair_with_targetsum(arr, target):
    nums = {}
    
    for i, num in enumerate(arr):
        if target - num  in nums:
            return [nums[target - num], i]
        else:
            nums[arr[i]] = i
    
    return [-1, -1]

print(pair_with_targetsum([1, 2, 3, 4, 6], 6))
print(pair_with_targetsum([2, 5, 9, 11], 11))