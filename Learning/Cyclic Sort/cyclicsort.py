def cyclic_sort(nums):
    start = 0
    
    while start < len(nums):
        swap = nums[start] - 1
        if nums[start] != nums[swap]:
            nums[start], nums[swap] = nums[swap], nums[start]

        else:
            start += 1
    
    return nums

print(cyclic_sort([1, 5, 6, 4, 3, 2]))