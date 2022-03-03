def find_smallest_missing_num(nums):
    length = len(nums)
    start = 0
    
    while start < length:
        correct_pos = nums[start] - 1
        
        if nums[start] <= len(nums) and nums[start] > 0 and nums[start] != nums[correct_pos]:
                nums[start], nums[correct_pos] = nums[correct_pos], nums[start]
            
        else:
            start += 1
    
    for i in range(length):
        if nums[i] != i + 1:
            return i + 1
    
    return nums.length + 1

print(find_smallest_missing_num([-3, 1, 5, 4, 2]))
print(find_smallest_missing_num([3, -2, 0, 1, 2]))
print(find_smallest_missing_num([3, 2, 5, 1]))